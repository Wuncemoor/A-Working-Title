import tcod as libtcod
from fov_function import initialize_fov, recompute_fov
from ECS.entity import get_blocking_entities_at_location
from death_functions import kill_monster, kill_player
from enums.game_states import GameStates, EncounterStates, LootStates
from game_messages import Message
from input_handlers import handle_keys, handle_mouse, handle_main_menu
from render_functions import render_all
from loader_functions.initialize_new_game import get_game_variables
from loader_functions.data_loaders import load_game, save_game
from loader_functions.constants import get_constants
from loader_functions.image_objects import get_image_objects
from menus import main_menu, message_box
from random_utils import encounter_check
import sys
import pygame


# Main Loop
def main():
    constants = get_constants()
    images = get_image_objects()
    pygame.init()

    screen = pygame.display.set_mode((constants['screen_width'], constants['screen_height']))
    resource_surface = pygame.Surface((constants['rscreen_width'], constants['rscreen_height']))
    message_surface = pygame.Surface((constants['mscreen_width'], constants['mscreen_height']))
    camera_surface = pygame.Surface((constants['cscreen_width'], constants['cscreen_height']))

    pygame.display.set_caption('Wuncemoor')

    player = None
    dungeons = {}
    entities = []
    game_map = None
    message_log = None
    game_state = None
    key = None

    show_main_menu = True
    show_load_error_message = False

    main_menu_background_image = images.get('backgrounds').get('mm_bg')
    mm_gui_img = images.get('gui').get('main_menu')

    clock = pygame.time.Clock()
    clock.tick(constants['fps'])

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = event.key

        # Game Logic Here
        if show_main_menu:
            main_menu(screen, constants['screen_width'], constants['screen_height'], main_menu_background_image,
                      mm_gui_img, fontsize=40)

            if show_load_error_message:
                message_box(screen, 50, constants['screen_width'],
                            constants['screen_height'])

            pygame.display.flip()

            action = handle_main_menu(key)

            new_game = action.get('new_game')
            load_saved_game = action.get('load_game')
            exit = action.get('exit')

            if show_load_error_message and (new_game or load_saved_game or exit):
                show_load_error_message = False
            elif new_game:

                player, dungeons, entities, structures, transitions, noncombatants, game_map, world_map, camera, \
                message_log, game_state = get_game_variables(constants, images)
                camera.refocus(player.x, player.y, game_map, constants)
                game_state = GameStates.PLAYERS_TURN

                show_main_menu = False
            elif load_saved_game:
                try:
                    player, dungeons, entities, structures, transitions, noncombatants, game_map, world_map, camera, \
                    message_log, game_state = load_game()
                    show_main_menu = False
                except FileNotFoundError:
                    show_load_error_message = True
            elif exit:
                pygame.quit()
                sys.exit()

        else:
            screen.fill((0, 0, 0))
            show_main_menu = False
            play_game(player, dungeons, entities, structures, transitions, noncombatants, game_map, world_map, camera, message_log,
                      game_state, screen, camera_surface, resource_surface, message_surface, constants, images)


def play_game(player, dungeons, entities, structures, transitions, noncombatants, game_map, world_map, camera, message_log, game_state,
              screen, camera_surface, resource_surface, message_surface, constants, images):
    fov_recompute = True
    fov_map = initialize_fov(game_map)
    game_state = game_state
    previous_game_state = game_state
    targeting_item = None
    dialogue_partner = None
    encounter = None
    loot = None

    while True:
        for event in pygame.event.get():
            player_turn_results = []
            encounter_results = []
            loot_results = []
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:

                action = handle_keys(event.key, game_state)


                move = action.get('move')
                interact = action.get('interact')
                show_inventory = action.get('show_inventory')
                drop_inventory = action.get('drop_inventory')
                show_map = action.get('show_map')
                show_competence = action.get('show_competence')
                inventory_index = action.get('inventory_index')
                show_stats_menu = action.get('show_stats_menu')
                show_primary_stats = action.get('show_primary_stats')
                show_combat_stats = action.get('show_combat_stats')
                show_noncombat_stats = action.get('show_noncombat_stats')
                show_journal = action.get('show_journal')
                show_strength_feats = action.get('show_strength_feats')
                show_instinct_feats = action.get('show_instinct_feats')
                show_coordination_feats = action.get('show_coordination_feats')
                show_vitality_feats = action.get('show_vitality_feats')
                show_arcana_feats = action.get('show_arcana_feats')
                show_improvisation_feats = action.get('show_improvisation_feats')
                show_wisdom_feats = action.get('show_wisdom_feats')
                show_finesse_feats = action.get('show_finesse_feats')
                show_charisma_feats = action.get('show_charisma_feats')
                show_devotion_feats = action.get('show_devotion_feats')
                gain_competence = action.get('gain_competence')
                exit = action.get('exit')
                level_up = action.get('level_up')
                show_character_sheet = action.get('show_character_sheet')
                converse = action.get('converse')
                traverse_menu = action.get('traverse_menu')
                choose_menu_option = action.get('choose_menu_option')
                toggle = action.get('toggle')

                if move and game_state == GameStates.PLAYERS_TURN:
                    dx, dy = move
                    destination_x = player.x + dx
                    destination_y = player.y + dy

                    if not game_map.is_blocked(destination_x, destination_y):
                        target = get_blocking_entities_at_location(entities, destination_x, destination_y)

                        if target:
                            if target.combatant:
                                attack_results = player.combatant.attack(target)
                                player_turn_results.extend(attack_results)
                                game_state = GameStates.ENEMY_TURN
                        else:
                            player.move(dx, dy)
                            camera.refocus(player.x, player.y, game_map, constants)

                            fov_recompute = True

                            game_state = GameStates.ENEMY_TURN

                            if game_map.dangerous:
                                encountering = encounter_check()
                                if encountering:
                                    tile = game_map.tiles[destination_x][destination_y]

                                    options = ['FIGHT', 'ITEM', 'RUN']
                                    encounter = game_map.current_map.get_encounter(images, tile, options)

                                    previous_game_state = game_state
                                    game_state = GameStates.ENCOUNTER


                if interact and game_state == GameStates.PLAYERS_TURN:
                    nothing = True
                    for entity in entities:
                        if entity.x == player.x and entity.y == player.y:
                            if entity.item:
                                game_map.current_map.map_entities.remove(entity)
                                pickup_results = player.combatant.inventory.add_item(entity)
                                player_turn_results.extend(pickup_results)
                                nothing = False
                                break
                    for transition in transitions:
                        if transition.x == player.x and transition.y == player.y:
                            new_dungeon = dungeons[transition.transition.go_to_dungeon]
                            new_map = new_dungeon.maps[transition.transition.go_to_floor]
                            game_map.set_current_map(new_map)
                            player.x, player.y = transition.transition.go_to_xy[0], transition.transition.go_to_xy[1]
                            camera.refocus(player.x, player.y, game_map, constants)
                            entities = [player]
                            entities.extend(game_map.current_map.map_entities)
                            transitions = []
                            transitions.extend(game_map.current_map.transitions)
                            structures = []
                            structures.extend(game_map.current_map.structures)
                            noncombatants = []
                            noncombatants.extend(game_map.current_map.noncombatants)
                            fov_map = initialize_fov(game_map)
                            fov_recompute = True
                            nothing = False
                            break
                    for noncom in noncombatants:
                        if noncom.x == player.x and noncom.y == player.y:
                            dialogue_partner = noncom
                            previous_game_state = game_state
                            game_state = GameStates.DIALOGUE
                            nothing = False
                    if nothing:
                        message_log.add_message(Message('Nothing to see here, move along...', libtcod.dark_blue))

                if show_inventory:
                    previous_game_state = game_state
                    game_state = GameStates.SHOW_INVENTORY

                if drop_inventory:
                    previous_game_state = game_state
                    game_state = GameStates.DROP_INVENTORY

                if show_character_sheet:
                    previous_game_state = game_state
                    game_state = GameStates.CHARACTER_SHEET

                if show_competence:
                    previous_game_state = game_state
                    game_state = GameStates.COMPETENCE_MENU

                if show_map:
                    previous_game_state = game_state
                    game_state = GameStates.SHOW_MAP

                if show_journal:
                    previous_game_state = game_state
                    game_state = GameStates.SHOW_JOURNAL

                if inventory_index is not None and previous_game_state != GameStates.PLAYER_DEAD and inventory_index < \
                        len(player.combatant.inventory.items):
                    item = player.combatant.inventory.items[inventory_index]

                    if game_state == GameStates.SHOW_INVENTORY:
                        player_turn_results.extend(
                            player.combatant.inventory.use(item, entities=entities, fov_map=fov_map))
                    elif game_state == GameStates.DROP_INVENTORY:
                        player_turn_results.extend(player.combatant.inventory.drop_item(item))

                if gain_competence:
                    attribute, competence = gain_competence

                    player_turn_results.extend(player.competencies.comp_setter(attribute, competence))

                if show_stats_menu:
                    previous_game_state = game_state
                    game_state = GameStates.CHARACTER_MENU
                if show_primary_stats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.PRIMARY_STATS_SCREEN
                if show_combat_stats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.COMBAT_STATS_SCREEN
                if show_noncombat_stats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.NONCOMBAT_STATS_SCREEN
                if show_competence:
                    previous_game_state = game_state
                    game_state = GameStates.COMPETENCE_MENU
                if show_strength_feats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.STRENGTH_FEATS
                if show_instinct_feats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.INSTINCT_FEATS
                if show_coordination_feats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.COORDINATION_FEATS
                if show_vitality_feats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.VITALITY_FEATS
                if show_arcana_feats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.ARCANA_FEATS
                if show_improvisation_feats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.IMPROVISATION_FEATS
                if show_wisdom_feats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.WISDOM_FEATS
                if show_finesse_feats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.FINESSE_FEATS
                if show_charisma_feats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.CHARISMA_FEATS
                if show_devotion_feats:
                    older_game_state = previous_game_state
                    previous_game_state = game_state
                    game_state = GameStates.DEVOTION_FEATS

                if level_up:

                    if level_up == 'Strength':
                        player.combatant.attributes.strength += 1
                    elif level_up == 'Instinct':
                        player.combatant.attributes.instinct += 1
                    elif level_up == 'Coordination':
                        player.combatant.attributes.coordination += 1
                    elif level_up == 'Vitality':
                        player.combatant.attributes.vitality += 1
                    elif level_up == 'Arcana':
                        player.combatant.attributes.arcana += 1
                    elif level_up == 'Improvisation':
                        player.combatant.attributes.improvisation += 1
                    elif level_up == 'Wisdom':
                        player.combatant.attributes.wisdom += 1
                    elif level_up == 'Finesse':
                        player.combatant.attributes.finesse += 1
                    elif level_up == 'Charisma':
                        player.combatant.attributes.charisma += 1
                    elif level_up == 'Devotion':
                        player.combatant.attributes.devotion += 1

                    game_state = previous_game_state
                if converse:
                    key = chr(converse)
                    dialogue = dialogue_partner.noncombatant.dialogue
                    try:
                        current_node = dialogue.graph_dict.get(dialogue.current_convo)

                        dialogue.current_convo = current_node.results.get(key)
                        current_node = dialogue.graph_dict.get(dialogue.current_convo)
                        current_node.visited = True

                        if dialogue.current_convo == 'exit':
                            dialogue.current_convo = 'root'
                            game_state = previous_game_state
                    except KeyError:
                        pass

                if traverse_menu:
                    if game_state == GameStates.ENCOUNTER:
                        if (traverse_menu < 0 and encounter.current_option == 0) or \
                                (traverse_menu > 0 and encounter.current_option == len(encounter.options) - 1):
                            pass
                        else:
                            encounter.current_option += traverse_menu
                    elif game_state == GameStates.LOOTING:
                        if loot.state == LootStates.THINKING:
                            if (traverse_menu < 0 and loot.current_option == 0) or (traverse_menu > 0 and loot.current_option == (len(loot.options) - 1)):
                                pass
                            else:
                                loot.current_option += traverse_menu
                        elif loot.state == LootStates.SIFTING:
                            if (traverse_menu < 0 and loot.current_option == 0) or (traverse_menu > 0 and loot.current_option == (len(loot.items) - 1)):
                                pass
                            else:
                                loot.current_option += traverse_menu
                        elif loot.state == LootStates.DEPOSITING:
                            if (traverse_menu < 0 and loot.current_option == 0) or (traverse_menu > 0 and loot.current_option == (len(loot.claimed) - 1)):
                                pass
                            else:
                                loot.current_option += traverse_menu

                if toggle:
                    if game_state == GameStates.LOOTING:
                        if loot.state == LootStates.SIFTING and toggle == 'right' and len(loot.claimed) > 0:
                            loot_results.append({'toggle': 'right'})
                        elif loot.state == LootStates.DEPOSITING and toggle == 'left' and len(loot.items) > 0:
                            loot_results.append({'toggle': 'left'})






                if choose_menu_option:
                    if game_state == GameStates.ENCOUNTER:
                        if encounter.state == EncounterStates.THINKING:
                            encounter_results.append({encounter.options[encounter.current_option]: True})
                        elif encounter.state == EncounterStates.FIGHT_TARGETING:
                            attack_results = player.combatant.attack(encounter.event)
                            encounter_results.extend(attack_results)
                        elif encounter.state == EncounterStates.VICTORY:
                            loot = encounter.loot

                            encounter = None
                            game_state = GameStates.LOOTING
                    elif game_state == GameStates.LOOTING:
                        if loot.state == LootStates.THINKING:
                            loot_results.append({loot.options[loot.current_option]: True})
                        elif loot.state == LootStates.SIFTING:
                            loot.claimed.append(loot.items[loot.current_option])
                            del loot.items[loot.current_option]
                            if len(loot.items) == 0:
                                loot.current_option = 2
                                loot.state = LootStates.THINKING
                            elif loot.current_option > len(loot.items) - 1:
                                loot.current_option -= 1
                        elif loot.state == LootStates.DEPOSITING:
                            loot.items.append(loot.claimed[loot.current_option])
                            del loot.claimed[loot.current_option]
                            if len(loot.claimed) == 0:
                                loot.current_option = 0
                                loot.state = LootStates.SIFTING
                            elif loot.current_option > len(loot.claimed) - 1:
                                loot.current_option -= 1

                if exit:
                    if game_state == GameStates.ENCOUNTER:
                        if encounter.state == EncounterStates.FIGHT_TARGETING:
                            encounter_results.append({'UNFIGHT': True})
                    elif game_state == GameStates.LOOTING:
                        if loot.state in (LootStates.SIFTING, LootStates.DEPOSITING):
                            loot.state = LootStates.THINKING
                        elif loot.state == LootStates.THINKING and loot.current_option == 2:
                            loot_results.append({'LEAVE': True})
                        elif loot.state == LootStates.THINKING:
                            loot.current_option = 2
                    elif game_state == GameStates.CHARACTER_SHEET:
                        game_state = GameStates.PLAYERS_TURN

                    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY, GameStates.CHARACTER_MENU,
                                      GameStates.SHOW_MAP):
                        game_state = previous_game_state
                    elif game_state in (
                            GameStates.PRIMARY_STATS_SCREEN, GameStates.COMBAT_STATS_SCREEN,
                            GameStates.NONCOMBAT_STATS_SCREEN):
                        game_state = previous_game_state
                        previous_game_state = older_game_state
                    elif game_state in (
                            GameStates.STRENGTH_FEATS, GameStates.INSTINCT_FEATS, GameStates.COORDINATION_FEATS,
                            GameStates.VITALITY_FEATS, GameStates.ARCANA_FEATS, GameStates.IMPROVISATION_FEATS,
                            GameStates.WISDOM_FEATS, GameStates.FINESSE_FEATS, GameStates.CHARISMA_FEATS,
                            GameStates.DEVOTION_FEATS):
                        game_state = previous_game_state
                        previous_game_state = older_game_state
                    elif game_state == GameStates.COMPETENCE_MENU:
                        game_state = GameStates.PLAYERS_TURN
                    elif game_state == GameStates.TARGETING:
                        player_turn_results.append({'targeting_cancelled': True})
                    else:
                        save_game(player, dungeons, entities, game_map, message_log, game_state)

                        pygame.quit()
                        sys.exit()

                for player_turn_result in player_turn_results:
                    message = player_turn_result.get('message')
                    dead_entity = player_turn_result.get('dead')
                    item_added = player_turn_result.get('item_added')
                    item_consumed = player_turn_result.get('consumed')
                    item_dropped = player_turn_result.get('item_dropped')
                    equip = player_turn_result.get('equip')
                    targeting = player_turn_result.get('targeting')
                    targeting_cancelled = player_turn_result.get('targeting_cancelled')
                    xp = player_turn_result.get('xp')

                    if message:
                        message_log.add_message(message)

                    if dead_entity:
                        corpse = images.get('entities').get('combatants').get('corpse')
                        if dead_entity == player:
                            message, game_state = kill_player(dead_entity, corpse)
                        else:
                            message = kill_monster(dead_entity, corpse)

                        message_log.add_message(message)

                    if item_added:
                        entities.remove(item_added)

                        game_state = GameStates.ENEMY_TURN

                    if item_consumed:
                        game_state = GameStates.ENEMY_TURN

                    if item_dropped:
                        game_map.current_map.map_entities.append(item_dropped)
                        entities = [player]
                        entities.extend(game_map.current_map.map_entities)

                        game_state = GameStates.ENEMY_TURN

                    if equip:
                        equip_results = player.combatant.equipment.toggle_equip(equip)

                        for equip_result in equip_results:
                            equipped = equip_result.get('equipped')
                            dequipped = equip_result.get('dequipped')

                            if equipped:
                                message_log.add_message(Message('You equip the {0}!'.format(equipped.name)))
                            if dequipped:
                                message_log.add_message(Message('You dequipped the {0}!'.format(dequipped.name)))

                        game_state = GameStates.ENEMY_TURN

                    if targeting:
                        previous_game_state = GameStates.PLAYERS_TURN
                        game_state = GameStates.TARGETING

                        targeting_item = targeting

                        message_log.add_message(targeting_item.item.useable.targeting_message)

                    if targeting_cancelled:
                        game_state = previous_game_state

                        message_log.add_message(Message('Targeting cancelled.'))

                    if xp:
                        leveled_up = player.combatant.level.add_xp(xp)
                        message_log.add_message(Message('You gain {0} experience points!'.format(xp), libtcod.dark_orange))

                        if leveled_up:
                            message_log.add_message(Message(
                                'Your skills grow once more! Level {0}!'.format(
                                    player.combatant.level.current_level) + '!',
                                libtcod.dark_orange))
                            if not GameStates.TARGETING:
                                previous_game_state = game_state
                                game_state = GameStates.LEVEL_UP
                            else:
                                previous_game_state = GameStates.PLAYERS_TURN
                                game_state = GameStates.LEVEL_UP
                for encounter_result in encounter_results:

                    fight = encounter_result.get('FIGHT')
                    unfight = encounter_result.get('UNFIGHT')

                    run = encounter_result.get('RUN')
                    end_turn = encounter_result.get('end_turn')

                    xp = encounter_result.get('xp')
                    message = encounter_result.get('message')
                    dead_entity = encounter_result.get('dead')
                    if fight:
                        encounter.state = EncounterStates.FIGHT_TARGETING
                    elif unfight:
                        encounter.state = EncounterStates.THINKING
                    elif run:
                        game_state = previous_game_state
                        player.combatant.level.add_xp(encounter.loot.xp)
                        if xp is None:
                            xp_text = Message("You didn't learn much there...", libtcod.dark_orange)
                        else:
                            xp_text = Message('You gain {0} experience points!'.format(xp), libtcod.dark_orange)
                        message_log.add_message(xp_text)
                        encounter = None
                    elif message:
                        message_log.add_message(message)
                    elif xp:
                        encounter.loot.xp += xp
                    elif dead_entity:
                        corpse = images.get('entities').get('combatants').get('corpse')
                        if dead_entity == player:
                            message, game_state = kill_player(dead_entity, corpse)
                        else:
                            encounter.loot.add_loot(dead_entity)
                            message = kill_monster(dead_entity, corpse)
                            message_log.add_message(message)
                    elif end_turn:
                        if encounter.event.combatant:
                            encounter.state = EncounterStates.ENEMY_TURN
                        else:
                            message_log.add_message(Message('YOU WIN THE FIGHT!', libtcod.black))
                            message_log.add_message(Message('Press [Enter] to loot.', libtcod.black))
                            encounter.state = EncounterStates.VICTORY

                for loot_result in loot_results:

                    take_all = loot_result.get('AUTO')
                    take_some = loot_result.get('MANUAL')
                    leave = loot_result.get('LEAVE')
                    toggle = loot_result.get('toggle')


                    if take_all:
                        loot.claimed.extend(loot.items)
                        loot.items = []
                        loot.current_option = 2
                    if take_some and (len(loot.items) + len(loot.claimed)) > 0:
                        loot.current_option = 0

                        if len(loot.items) > 0:
                            loot.state = LootStates.SIFTING
                        else:
                            loot.state = LootStates.DEPOSITING
                    if leave:
                        player.combatant.level.add_xp(loot.xp)
                        player.combatant.inventory.items.extend(loot.claimed)

                        loot = None
                        game_state = GameStates.PLAYERS_TURN
                    if toggle == 'right':
                        loot.state = LootStates.DEPOSITING
                    elif toggle == 'left':
                        loot.state = LootStates.SIFTING








            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_action = handle_mouse((event.pos, event.button))

                left_click = mouse_action.get('left_click')
                right_click = mouse_action.get('right_click')

                if game_state == GameStates.TARGETING:
                    if left_click:
                        target_x, target_y = left_click

                        item_use_results = player.combatant.inventory.use(targeting_item, entities=entities,
                                                                          fov_map=fov_map, target_x=target_x,
                                                                          target_y=target_y)

                        player_turn_results.extend(item_use_results)
                    elif right_click:
                        player_turn_results.append({'targeting_cancelled': True})

        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, constants['fov_radius'], constants['fov_light_walls'],
                          constants['fov_algorithm'])

        render_all(screen, camera_surface, resource_surface, message_surface, entities, player, structures, transitions,
                   noncombatants, game_map, world_map, images, camera, fov_map, fov_recompute, message_log,
                   constants['cscreen_width'], constants['cscreen_height'], constants['map_width'],
                   constants['map_height'], game_state, encounter, loot)

        fov_recompute = False

        pygame.display.flip()

        if encounter:
            if encounter.state == EncounterStates.ENEMY_TURN:
                if encounter.event.combatant:
                    enemy_turn_results = encounter.event.combatant.ai.take_turn_e(player)
                    for enemy_turn_result in enemy_turn_results:
                        message = enemy_turn_result.get('message')
                        dead_entity = enemy_turn_result.get('dead')

                        if message:
                            message_log.add_message(message)

                        if dead_entity:
                            corpse = images.get('entities').get('combatants').get('corpse')
                            if dead_entity == player:
                                message, game_state = kill_player(dead_entity, corpse)
                            else:
                                message = kill_monster(dead_entity, corpse)

                            message_log.add_message(message)

                        if game_state == GameStates.PLAYER_DEAD:
                            break
                    encounter.state = EncounterStates.THINKING

        if game_state == GameStates.ENEMY_TURN:
            for entity in entities:
                if entity.combatant:
                    if entity.combatant.ai:
                        enemy_turn_results = entity.combatant.ai.take_turn(player, fov_map, game_map, entities)

                        for enemy_turn_result in enemy_turn_results:
                            message = enemy_turn_result.get('message')
                            dead_entity = enemy_turn_result.get('dead')

                            if message:
                                message_log.add_message(message)

                            if dead_entity:
                                corpse = images.get('entities').get('combatants').get('corpse')
                                if dead_entity == player:
                                    message, game_state = kill_player(dead_entity, corpse)
                                else:
                                    message = kill_monster(dead_entity, corpse)

                                message_log.add_message(message)

                                if game_state == GameStates.PLAYER_DEAD:
                                    break
                if game_state == GameStates.PLAYER_DEAD:
                    break
            else:
                game_state = GameStates.PLAYERS_TURN


if __name__ == '__main__':
    main()
