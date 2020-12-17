from abstracts.abstract_logic import AbstractLogic
from config.constants import DARK_BLUE, DARK_ORANGE, BLACK, WHITE, SCREEN_SIZE
from enums.game_states import EncounterStates, RewardStates, GameStates, ShopStates
from handlers.views.messages import Message
from loader_functions.data_loaders import load_game
from loader_functions.initialize_new_game import get_game_variables
import pygame as py


class NewGame(AbstractLogic):

    def logic(self):
        world, party = get_game_variables()
        self.game.preplay(world, party)


class LoadGame(AbstractLogic):

    def logic(self):
        world, party = load_game()
        self.game.preplay(world, party)


class TitleSettings(AbstractLogic):

    def logic(self):
        self.game.quit()


class TitleAcknowledgements(AbstractLogic):

    def logic(self):
        self.game.quit()


class QuitGame(AbstractLogic):

    def logic(self):
        self.game.quit()


class Move(AbstractLogic):

    def logic(self, output):
        dx, dy = output
        destination_x = self.game.party.x + dx
        destination_y = self.game.party.y + dy

        tile = self.game.world.current_map.tiles[destination_y][destination_x]

        self.game.party.change_direction(output)

        if not tile.blocker:

            self.game.party.move(dx, dy)
            self.handler.camera.refocus(self.game.party.x, self.game.party.y)

            self.handler.fov.needs_recompute = True

            if tile.floor.has_transition():
                transition = tile.floor.transition
                world = self.game.world
                new_dungeon = world.dungeons[transition.go_to_dungeon]
                if world.current_dungeon.name != transition.go_to_dungeon:
                    world.current_dungeon.time_dilation = self.game.time.stamp()
                    self.game.time.apply_dilation(new_dungeon)
                    world.current_dungeon = new_dungeon

                new_map = new_dungeon.maps[transition.go_to_floor]
                world.current_map = new_map
                self.game.party.x = transition.go_to_xy[0]
                self.game.party.y = transition.go_to_xy[1]
                self.handler.camera.refocus(self.game.party.x, self.game.party.y)

                self.handler.fov.map = self.handler.fov.initialize(world)
                self.handler.fov.needs_recompute = True

            elif self.game.world.dangerous:
                self.game.time.goes_on()
                self.game.encounter.check(tile)


class Interact(AbstractLogic):

    def logic(self):
        nothing = True
        changes = []
        world = self.game.world
        for entity in world.current_map.entities:
            if entity.x == self.game.party.x and entity.y == self.game.party.y:
                if entity.item:
                    pickup_results = self.game.party.inventory.add_item(entity)
                    changes.extend(pickup_results)
                    nothing = False
                    break

        for noncom in world.current_map.noncombatants:
            if noncom.x == self.game.party.x and noncom.y == self.game.party.y:
                self.game.dialogue.partner = noncom
                self.game.dialogue.set_real_talk()
                self.game.state_handler = self.game.dialogue
                self.game.options.current = noncom.noncombatant.dialogue
                nothing = False
        if nothing:
            self.game.log.messages.add_message(Message('Nothing to see here, move along...', DARK_BLUE))
        return changes


class MenusToggle(AbstractLogic):

    def logic(self, output):

        if self.handler.menu_type is output:
            return MenusSubToLife.logic(self)
        else:
            return MenusToMenus.logic(self, output)


class LifeToMenus(AbstractLogic):

    def logic(self, obj):
        return [{'state': 'menus'}, {'substate': obj}]


class MenusToMenus(AbstractLogic):

    def logic(self, obj):
        return [{'substate': obj}]


class MenusSubToLife(AbstractLogic):

    def logic(self):
        self.handler.menu_type.sub = None
        return [{'state': 'life'}]


class MenusExit(AbstractLogic):

    def logic(self):
        if self.handler.menu_type.sub is None:
            self.game.state_handler = self.game.life
        else:
            self.handler.menu_type.sub = None
            self.game.options.current = self.handler.menu_type.options


class MenuGoToSub(AbstractLogic):

    def logic(self):
        sub = self.handler.menu_type.get_sub()
        if len(sub) > 0:
            self.handler.menu_type.sub = sub
            self.game.options.wrap_and_set(sub)


class ShopBaseGoToSub(AbstractLogic):

    def logic(self):
        player_sub, shop_sub = self.handler.get_subinventories(self.game.options.current.choice)
        if len(shop_sub) > 0:
            changes = [{'substate': ShopStates.BUYING}]
            self.handler.sub_index = self.game.options.current.choice
            self.game.options.wrap_and_set(shop_sub)
        elif len(player_sub) > 0:
            changes = [{'substate': ShopStates.SELLING}]
            self.handler.sub_index = self.game.options.current.choice
            self.game.options.wrap_and_set(player_sub)
        elif len(self.handler.transaction_details) > 0:
            changes = [{'substate': ShopStates.TRANSACTING}]
            self.handler.sub_index = self.game.options.current.choice
            self.game.options.wrap_and_set(self.handler.transaction_details)
        else:
            changes = []
        print(self.handler.sub_index)
        return changes


class FightTargeting(AbstractLogic):

    def logic(self):
        changes = [{'substate': EncounterStates.FIGHT_TARGETING}]
        return changes


class EncounterExit(AbstractLogic):

    def logic(self):
        if self.handler.state is EncounterStates.FIGHT_TARGETING:
            changes = [{'substate': EncounterStates.THINKING}]
        else:
            changes = []
        return changes


class UseSatchel(AbstractLogic):

    def logic(self):
        pass


class RunAway(AbstractLogic):

    def logic(self):
        changes = [{'state': 'life'}]
        xp = self.handler.loot.xp
        if xp > 0:
            changes.append({'xp': xp})
            message = Message('You gain {0} experience points!'.format(xp), DARK_ORANGE)
        else:
            message = Message("You didn't learn much there...", DARK_ORANGE)
        changes.append({'message': message})

        return changes


class AttackMob(AbstractLogic):

    def logic(self):
        changes = []
        combat = self.handler.combat
        x, y = combat.grid.x, combat.grid.y
        attack_results = combat.party.p1.combatant.attack(combat.grid.rows[x][y])
        changes.extend(attack_results)
        return changes


class EndTurn(AbstractLogic):

    def logic(self):
        changes = []
        if len(self.handler.combat.enemies.members) > 0:
            if self.handler.state is EncounterStates.ENEMY_TURN:
                changes.append({'substate': EncounterStates.THINKING})
            else:
                changes.append({'substate': EncounterStates.ENEMY_TURN})
                changes.append({'automate': 'enemy_turn'})
        else:
            changes.append({'message': Message('YOU WIN THE FIGHT!', BLACK)})
            changes.append({'message': Message('Press [Enter] to loot.', BLACK)})
            changes.append({'substate': EncounterStates.VICTORY})
        return changes


class EnemyTurn(AbstractLogic):

    def logic(self):
        player = self.handler.combat.party.p1
        changes = self.handler.combat.enemies.p1.combatant.ai.take_turn_e(player)
        changes.append({'substate': EncounterStates.THINKING})
        return changes


class GoToReward(AbstractLogic):

    def logic(self):
        changes = [{'state': 'reward'}, {'substate': RewardStates.THINKING}]
        return changes


class RewardAuto(AbstractLogic):

    def logic(self):
        self.handler.loot.claimed.extend(self.handler.loot.items)
        self.handler.loot.items = []
        self.game.options.current.choice = 2
        return []


class RewardManual(AbstractLogic):

    def logic(self):
        loot = self.handler.loot
        if (len(loot.items) + len(loot.claimed)) > 0:
            if len(loot.items) > 0:
                changes = [{'substate': RewardStates.SIFTING}]
            else:
                changes = [{'substate': RewardStates.DEPOSITING}]
        else:
            changes = []
        return changes


class RewardToLife(AbstractLogic):

    def logic(self):
        loot = self.handler.loot
        changes = [{'xp': loot.xp}]
        self.game.party.inventory.take_loot(loot.claimed)
        self.game.options.current.choice = 0

        changes.append({'state': 'life'})
        return changes


class RewardSifting(AbstractLogic):

    def logic(self):
        changes = []
        loot = self.handler.loot
        loot.claim(self.game.options.current.choice)
        if len(loot.items) == 0:
            changes.append({'substate': RewardStates.THINKING})
            changes.append({'set_choice': 2})
        elif self.game.options.current.choice > len(loot.items) - 1:
            self.game.options.current.choice -= 1
        return changes


class RewardDepositing(AbstractLogic):

    def logic(self):
        changes = []
        loot = self.handler.loot
        loot.unclaim(self.game.options.current.choice)
        if len(loot.claimed) == 0:
            changes.append({'substate': RewardStates.SIFTING})
        elif self.game.options.current.choice > len(loot.claimed) - 1:
            self.game.options.current.choice -= 1
        return changes


class RewardToggle(AbstractLogic):

    def logic(self, direction):
        changes = []
        loot = self.handler.loot
        if self.handler.state == RewardStates.SIFTING and direction == 'right' and len(loot.claimed) > 0:
            changes.append({'substate': RewardStates.DEPOSITING})
        elif self.handler.state == RewardStates.DEPOSITING and direction == 'left' and len(loot.items) > 0:
            changes.append({'substate': RewardStates.SIFTING})
        return changes


class RewardExit(AbstractLogic):

    def logic(self):
        changes = []
        state = self.handler.state
        if state in (RewardStates.SIFTING, RewardStates.DEPOSITING):
            changes.append({'substate': RewardStates.THINKING})
        elif state == RewardStates.THINKING and self.game.options.current.choice == 2:
            changes.extend(RewardToLife.logic(self))
        elif state == RewardStates.THINKING:
            self.game.options.current.choice = 2
        return changes


class Debug(AbstractLogic):

    def logic(self):
        changes = [{'state': 'debug'}]
        return changes


class DebugExit(AbstractLogic):

    def logic(self, prev):
        string_dict = {
            GameStates.TITLE: 'title',
            GameStates.LIFE: 'life',
            GameStates.MENUS: 'menus',
            GameStates.ENCOUNTER: 'encounter',
            GameStates.REWARD: 'reward',
            GameStates.DIALOGUE: 'dialogue',
        }
        changes = [{'state': string_dict.get(prev)}]
        return changes


class DebugAttemptCommand(AbstractLogic):

    def logic(self):
        changes = [{'debug_message': Message('Command entered: ' + self.handler.current_input, WHITE)}]
        try:
            exec(self.handler.current_input, self.handler.allowed_inputs)
            changes.append({'debug_message': Message('COMMAND ACCEPTED', WHITE)})
            for message in self.handler.message_slot:
                changes.append({'debug_message': message})
            self.handler.current_input = ''
        except NameError:
            changes.append({'debug_message': Message('COMMAND NOT RECOGNIZED', WHITE)})

        return changes


class ShopExit(AbstractLogic):

    def logic(self):
        if self.handler.state == ShopStates.BASE:
            changes = [{'state': 'life'}]
        elif self.handler.state in (ShopStates.BUYING, ShopStates.SELLING, ShopStates.TRANSACTING):
            changes = [{'substate': ShopStates.BASE}]
        return changes


class FullscreenToggle(AbstractLogic):

    def logic(self):

        if self.game.fullscreen:
            self.game.screen = py.display.set_mode(SCREEN_SIZE)
            self.game.fullscreen = False
        else:
            self.game.screen = py.display.set_mode(SCREEN_SIZE, flags=py.FULLSCREEN)
            self.game.fullscreen = True

