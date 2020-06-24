import pygame as py
from ECS.image_bundle import ImageBundle

TITLE_SCREEN_BG = py.image.load('images\\background\\main_menu.png')
TITLE_MENU_BG = py.image.load('images\\GUI\\main_menu.png')
TITLE_MENU_BUTTON = py.image.load('images\\GUI\\mm_button.png')

MESSAGE_BG = py.image.load('images\\GUI\\message_bg.png')
ENCOUNTER_MESSAGE_BG = py.image.load('images\\GUI\\encounter\\message_bg.png')
ENCOUNTER_MENU = py.image.load('images\\GUI\\menus\\encounter_menu.png')
ENCOUNTER_BUTTON = py.image.load('images\\GUI\\menus\\option_button.png')
DIALOGUE_MENU = py.image.load('images\\GUI\\dialogue_menu.png')
LEVELUP_MENU = py.image.load('images\\GUI\\levelup_menu.png')
INVENTORY_MENU = py.image.load('images\\GUI\\inventory_menu.png')

JOURNAL_OBJS = {
    'bg': py.image.load('images\\GUI\\journal\\journal_bg.png'),
    'icon0': py.image.load('images\\GUI\\journal\\current.png'),
    'text0': py.image.load('images\\GUI\\journal\\current_text.png'),
    'icon1': py.image.load('images\\GUI\\journal\\completed.png'),
    'text1': py.image.load('images\\GUI\\journal\\completed_text.png'),
    'icon2': py.image.load('images\\GUI\\journal\\codex.png'),
    'text2': py.image.load('images\\GUI\\journal\\codex_text.png'),
    'icon3': py.image.load('images\\GUI\\journal\\history.png'),
    'text3': py.image.load('images\\GUI\\journal\\history_text.png'),
    'quest_holder': py.image.load('images\\GUI\\journal\\quest_holder.png'),
}

LOOT_BG = py.image.load('images\\GUI\\looting\\loot_bg.png')
LOOT_BANNER = py.image.load('images\\GUI\\looting\\loot_banner.png')

CALENDAR_BG = py.image.load('images\\GUI\\calendar.png')
CALENDAR_CIRCLE = py.image.load('images\\GUI\\calendar_circle.png')

INDICATOR_H = py.image.load('images\\GUI\\menus\\indicator_h.png')
INDICATOR_V = py.image.load('images\\GUI\\menus\\indicator_v.png')

STAIRS_DOWN = ImageBundle(py.image.load('images\\entities\\transitions\\stairsdown.png'))
STAIRS_UP = ImageBundle(py.image.load('images\\entities\\transitions\\stairsup.png'))
ALPHA = ImageBundle(py.image.load('images\\entities\\transitions\\alpha.png'))

BUNDLE_HERO = ImageBundle(py.image.load('images\\entities\\combatants\\hero\\sprite.png'),
                          py.image.load('images\\entities\\combatants\\hero\\portrait.png'),
                          py.image.load('images\\entities\\combatants\\hero\\port_mini.png'),
                          py.image.load('images\\entities\\combatants\\hero\\actor.png'))
CORPSE = py.image.load('images\\entities\\combatants\\corpse.png')

BUNDLE_SAMWISE = ImageBundle(py.image.load('images\\entities\\noncombatants\\samwise\\sprite.png'),
                             py.image.load('images\\entities\\noncombatants\\samwise\\portrait.png'),
                             py.image.load('images\\entities\\noncombatants\\samwise\\port_mini.png'))

BUNDLE_STICK = ImageBundle(py.image.load('images\\entities\\items\\equippables\\weapons\\stick\\sprite.png'))

BUNDLE_WEAPONS = {
    'staff': ImageBundle(py.image.load('images\\entities\\items\\equippables\\weapons\\staff\\sprite.png')),
    'dagger': ImageBundle(py.image.load('images\\entities\\items\\equippables\\weapons\\dagger\\sprite.png')),
    'shield': ImageBundle(py.image.load('images\\entities\\items\\equippables\\weapons\\shield\\sprite.png')),
    'longsword': ImageBundle(py.image.load('images\\entities\\items\\equippables\\weapons\\longsword\\sprite.png'),
                             py.image.load('images\\entities\\items\\equippables\\weapons\\longsword\\portrait.png')),
}

BUNDLE_POTION = ImageBundle(py.image.load('images\\entities\\items\\useables\\potion\\sprite.png'),
                            py.image.load('images\\entities\\items\\useables\\potion\\portrait.png'))
SCROLL = py.image.load('images\\entities\\items\\useables\\scroll\\sprite.png')

BUNDLE_MOBS = {
    'rat': ImageBundle(py.image.load('images\\entities\\combatants\\rat\\sprite.png'),
                       actor=py.image.load('images\\entities\\combatants\\rat\\actor.png')),
    'bat': ImageBundle(actor=py.image.load('images\\entities\\combatants\\bat\\actor.png')),
    'bear': ImageBundle(actor=py.image.load('images\\entities\\combatants\\bear\\actor.png')),
    'goblin': ImageBundle(py.image.load('images\\entities\\combatants\\goblin\\sprite.png'),
                          actor=py.image.load('images\\entities\\combatants\\goblin\\actor.png')),
    'kobold': ImageBundle(actor=py.image.load('images\\entities\\combatants\\kobold\\actor.png')),
    'raccoon': ImageBundle(actor=py.image.load('images\\entities\\combatants\\raccoon\\actor.png')),
    'salamander': ImageBundle(actor=py.image.load('images\\entities\\combatants\\salamander\\actor.png')),
    'snail': ImageBundle(actor=py.image.load('images\\entities\\combatants\\snail\\actor.png')),
    'shrimp': ImageBundle(actor=py.image.load('images\\entities\\combatants\\shrimp\\actor.png')),
    'spider': ImageBundle(actor=py.image.load('images\\entities\\combatants\\spider\\actor.png')),
}

CHARACTER_SCREEN = {
    'bg': py.image.load('images\\GUI\\character_sheet\\char_sheet.png'),
    'level': py.image.load('images\\GUI\\character_sheet\\level_icon.png'),
    'age': py.image.load('images\\GUI\\character_sheet\\age_icon.png'),
    'power': py.image.load('images\\GUI\\character_sheet\\power.png'),
    'resistance': py.image.load('images\\GUI\\character_sheet\\resistance.png'),
    'slash': py.image.load('images\\GUI\\character_sheet\\slash.png'),
    'pierce': py.image.load('images\\GUI\\character_sheet\\pierce.png'),
    'blunt': py.image.load('images\\GUI\\character_sheet\\blunt.png'),
    'heat': py.image.load('images\\GUI\\character_sheet\\heat.png'),
    'cold': py.image.load('images\\GUI\\character_sheet\\cold.png'),
    'acid': py.image.load('images\\GUI\\character_sheet\\acid.png'),
    'current': py.image.load('images\\GUI\\character_sheet\\current.png'),
    'aether': py.image.load('images\\GUI\\character_sheet\\aether.png'),
    'accuracy': py.image.load('images\\GUI\\character_sheet\\accuracy.png'),
    'dodge': py.image.load('images\\GUI\\character_sheet\\dodge.png'),
    'initiative': py.image.load('images\\GUI\\character_sheet\\initiative.png'),
    'speed': py.image.load('images\\GUI\\character_sheet\\speed.png'),
    'teamwork': py.image.load('images\\GUI\\character_sheet\\teamwork.png'),
    'leadership': py.image.load('images\\GUI\\character_sheet\\leadership.png'),
    'presence': py.image.load('images\\GUI\\character_sheet\\presence.png'),
    'reflex': py.image.load('images\\GUI\\character_sheet\\reflex.png'),
    'balance': py.image.load('images\\GUI\\character_sheet\\balance.png'),
    'breath': py.image.load('images\\GUI\\character_sheet\\breath.png'),
    'grapple': py.image.load('images\\GUI\\character_sheet\\grapple.png'),
    'stun': py.image.load('images\\GUI\\character_sheet\\stun.png'),
    'panic': py.image.load('images\\GUI\\character_sheet\\panic.png'),
    'apathy': py.image.load('images\\GUI\\character_sheet\\apathy.png'),
    'pain': py.image.load('images\\GUI\\character_sheet\\pain.png'),
    'bewitch': py.image.load('images\\GUI\\character_sheet\\bewitch.png'),
    'enrage': py.image.load('images\\GUI\\character_sheet\\enrage.png'),
    'illness': py.image.load('images\\GUI\\character_sheet\\illness.png'),
    'tenacity': py.image.load('images\\GUI\\character_sheet\\tenacity.png'),
    'pressure': py.image.load('images\\GUI\\character_sheet\\pressure.png'),
    'bleed': py.image.load('images\\GUI\\character_sheet\\bleed.png'),
    'injury': py.image.load('images\\GUI\\character_sheet\\injury.png'),
    'xp_bar': py.image.load('images\\GUI\\character_sheet\\xp_bar.png'),
    'xp0': py.image.load('images\\GUI\\character_sheet\\xp0.png'),
    'xp1': py.image.load('images\\GUI\\character_sheet\\xp1.png'),
    'xp2': py.image.load('images\\GUI\\character_sheet\\xp2.png'),
    'xp3': py.image.load('images\\GUI\\character_sheet\\xp3.png'),
    'xp4': py.image.load('images\\GUI\\character_sheet\\xp4.png'),
    'human': py.image.load('images\\GUI\\character_sheet\\human_icon.png'),
    'male': py.image.load('images\\GUI\\character_sheet\\male_icon.png'),
    'female': py.image.load('images\\GUI\\character_sheet\\female_icon.png'),
}

RESOURCE_HUD = {
    'frame': py.image.load('images\\GUI\\resources_hud\\portrait_mini_frame.png'),
    'resource_bar': py.image.load('images\\GUI\\resources_hud\\resource_bar.png'),
    'HP': py.image.load('images\\GUI\\resources_hud\\HP.png'),
    'MP': py.image.load('images\\GUI\\resources_hud\\MP.png'),
    'TP': py.image.load('images\\GUI\\resources_hud\\TP.png'),
    'VP': py.image.load('images\\GUI\\resources_hud\\VP.png'),
    'HPleft0': py.image.load('images\\GUI\\resources_hud\\real_hp\\left0.png'),
    'HPleft1': py.image.load('images\\GUI\\resources_hud\\real_hp\\left1.png'),
    'HPmid': py.image.load('images\\GUI\\resources_hud\\real_hp\\mid.png'),
    'HPright0': py.image.load('images\\GUI\\resources_hud\\real_hp\\right0.png'),
    'HPright1': py.image.load('images\\GUI\\resources_hud\\real_hp\\right1.png'),
    'MPleft0': py.image.load('images\\GUI\\resources_hud\\real_mp\\left0.png'),
    'MPleft1': py.image.load('images\\GUI\\resources_hud\\real_mp\\left1.png'),
    'MPmid': py.image.load('images\\GUI\\resources_hud\\real_mp\\mid.png'),
    'MPright0': py.image.load('images\\GUI\\resources_hud\\real_mp\\right0.png'),
    'MPright1': py.image.load('images\\GUI\\resources_hud\\real_mp\\right1.png'),
    'TPleft0': py.image.load('images\\GUI\\resources_hud\\real_tp\\left0.png'),
    'TPleft1': py.image.load('images\\GUI\\resources_hud\\real_tp\\left1.png'),
    'TPmid': py.image.load('images\\GUI\\resources_hud\\real_tp\\mid.png'),
    'TPright0': py.image.load('images\\GUI\\resources_hud\\real_tp\\right0.png'),
    'TPright1': py.image.load('images\\GUI\\resources_hud\\real_tp\\right1.png'),
    'VPleft0': py.image.load('images\\GUI\\resources_hud\\real_vp\\left0.png'),
    'VPleft1': py.image.load('images\\GUI\\resources_hud\\real_vp\\left1.png'),
    'VPmid': py.image.load('images\\GUI\\resources_hud\\real_vp\\mid.png'),
    'VPright0': py.image.load('images\\GUI\\resources_hud\\real_vp\\right0.png'),
    'VPright1': py.image.load('images\\GUI\\resources_hud\\real_vp\\right1.png'),
}
BACKGROUNDS = {
    'deep': py.image.load('images\\background\\deep.png'),
    'desert': py.image.load('images\\background\\desert.png'),
    'forest': py.image.load('images\\background\\forest.png'),
    'plains': py.image.load('images\\background\\plains.png'),
    'savannah': py.image.load('images\\background\\savannah.png'),
    'shallow': py.image.load('images\\background\\shallow.png'),
    'snow': py.image.load('images\\background\\snow.png'),
    'taiga': py.image.load('images\\background\\taiga.png'),
    'temprain': py.image.load('images\\background\\temprain.png'),
    'tropicrain': py.image.load('images\\background\\tropicrain.png'),
    'tundra': py.image.load('images\\background\\tundra.png'),
    'cave': py.image.load('images\\background\\cave.png'),
}

MINIMAP = {
    'deep': py.image.load('images\\tiles\\world_map\\mini_map\\deep.png'),
    'desert': py.image.load('images\\tiles\\world_map\\mini_map\\desert.png'),
    'forest': py.image.load('images\\tiles\\world_map\\mini_map\\forest.png'),
    'plains': py.image.load('images\\tiles\\world_map\\mini_map\\plains.png'),
    'savannah': py.image.load('images\\tiles\\world_map\\mini_map\\savannah.png'),
    'shallow': py.image.load('images\\tiles\\world_map\\mini_map\\shallow.png'),
    'snow': py.image.load('images\\tiles\\world_map\\mini_map\\snow.png'),
    'taiga': py.image.load('images\\tiles\\world_map\\mini_map\\taiga.png'),
    'temprain': py.image.load('images\\tiles\\world_map\\mini_map\\temprain.png'),
    'tropicrain': py.image.load('images\\tiles\\world_map\\mini_map\\tropicrain.png'),
    'tundra': py.image.load('images\\tiles\\world_map\\mini_map\\tundra.png')

}

LIGHT_DEEP = [py.image.load('images\\tiles\\world_map\\deep\\light_deep0.png'),
              py.image.load('images\\tiles\\world_map\\deep\\light_deep1.png'),
              py.image.load('images\\tiles\\world_map\\deep\\light_deep2.png'),
              py.image.load('images\\tiles\\world_map\\deep\\light_deep3.png'),
              py.image.load('images\\tiles\\world_map\\deep\\light_deep4.png'),
              py.image.load('images\\tiles\\world_map\\deep\\light_deep5.png'),
              py.image.load('images\\tiles\\world_map\\deep\\light_deep6.png'),
              py.image.load('images\\tiles\\world_map\\deep\\light_deep7.png'),
              py.image.load('images\\tiles\\world_map\\deep\\light_deep8.png')]
DARK_DEEP = [py.image.load('images\\tiles\\world_map\\deep\\dark_deep0.png'),
             py.image.load('images\\tiles\\world_map\\deep\\dark_deep1.png'),
             py.image.load('images\\tiles\\world_map\\deep\\dark_deep2.png'),
             py.image.load('images\\tiles\\world_map\\deep\\dark_deep3.png'),
             py.image.load('images\\tiles\\world_map\\deep\\dark_deep4.png'),
             py.image.load('images\\tiles\\world_map\\deep\\dark_deep5.png'),
             py.image.load('images\\tiles\\world_map\\deep\\dark_deep6.png'),
             py.image.load('images\\tiles\\world_map\\deep\\dark_deep7.png'),
             py.image.load('images\\tiles\\world_map\\deep\\dark_deep8.png')]
LIGHT_DESERT = [py.image.load('images\\tiles\\world_map\\desert\\light_desert0.png'),
                py.image.load('images\\tiles\\world_map\\desert\\light_desert1.png'),
                py.image.load('images\\tiles\\world_map\\desert\\light_desert2.png'),
                py.image.load('images\\tiles\\world_map\\desert\\light_desert3.png'),
                py.image.load('images\\tiles\\world_map\\desert\\light_desert4.png'),
                py.image.load('images\\tiles\\world_map\\desert\\light_desert5.png'),
                py.image.load('images\\tiles\\world_map\\desert\\light_desert6.png'),
                py.image.load('images\\tiles\\world_map\\desert\\light_desert7.png'),
                py.image.load('images\\tiles\\world_map\\desert\\light_desert8.png')]
DARK_DESERT = [py.image.load('images\\tiles\\world_map\\desert\\dark_desert0.png'),
               py.image.load('images\\tiles\\world_map\\desert\\dark_desert1.png'),
               py.image.load('images\\tiles\\world_map\\desert\\dark_desert2.png'),
               py.image.load('images\\tiles\\world_map\\desert\\dark_desert3.png'),
               py.image.load('images\\tiles\\world_map\\desert\\dark_desert4.png'),
               py.image.load('images\\tiles\\world_map\\desert\\dark_desert5.png'),
               py.image.load('images\\tiles\\world_map\\desert\\dark_desert6.png'),
               py.image.load('images\\tiles\\world_map\\desert\\dark_desert7.png'),
               py.image.load('images\\tiles\\world_map\\desert\\dark_desert8.png')]
LIGHT_FOREST = [py.image.load('images\\tiles\\world_map\\forest\\light_forest0.png'),
                py.image.load('images\\tiles\\world_map\\forest\\light_forest1.png'),
                py.image.load('images\\tiles\\world_map\\forest\\light_forest2.png'),
                py.image.load('images\\tiles\\world_map\\forest\\light_forest3.png'),
                py.image.load('images\\tiles\\world_map\\forest\\light_forest4.png'),
                py.image.load('images\\tiles\\world_map\\forest\\light_forest5.png'),
                py.image.load('images\\tiles\\world_map\\forest\\light_forest6.png'),
                py.image.load('images\\tiles\\world_map\\forest\\light_forest7.png'),
                py.image.load('images\\tiles\\world_map\\forest\\light_forest8.png')]
DARK_FOREST = [py.image.load('images\\tiles\\world_map\\forest\\dark_forest0.png'),
               py.image.load('images\\tiles\\world_map\\forest\\dark_forest1.png'),
               py.image.load('images\\tiles\\world_map\\forest\\dark_forest2.png'),
               py.image.load('images\\tiles\\world_map\\forest\\dark_forest3.png'),
               py.image.load('images\\tiles\\world_map\\forest\\dark_forest4.png'),
               py.image.load('images\\tiles\\world_map\\forest\\dark_forest5.png'),
               py.image.load('images\\tiles\\world_map\\forest\\dark_forest6.png'),
               py.image.load('images\\tiles\\world_map\\forest\\dark_forest7.png'),
               py.image.load('images\\tiles\\world_map\\forest\\dark_forest8.png')]
LIGHT_PLAINS = [py.image.load('images\\tiles\\world_map\\plains\\light_plains0.png'),
                py.image.load('images\\tiles\\world_map\\plains\\light_plains1.png'),
                py.image.load('images\\tiles\\world_map\\plains\\light_plains2.png'),
                py.image.load('images\\tiles\\world_map\\plains\\light_plains3.png'),
                py.image.load('images\\tiles\\world_map\\plains\\light_plains4.png'),
                py.image.load('images\\tiles\\world_map\\plains\\light_plains5.png'),
                py.image.load('images\\tiles\\world_map\\plains\\light_plains6.png'),
                py.image.load('images\\tiles\\world_map\\plains\\light_plains7.png'),
                py.image.load('images\\tiles\\world_map\\plains\\light_plains8.png')]
DARK_PLAINS = [py.image.load('images\\tiles\\world_map\\plains\\dark_plains0.png'),
               py.image.load('images\\tiles\\world_map\\plains\\dark_plains1.png'),
               py.image.load('images\\tiles\\world_map\\plains\\dark_plains2.png'),
               py.image.load('images\\tiles\\world_map\\plains\\dark_plains3.png'),
               py.image.load('images\\tiles\\world_map\\plains\\dark_plains4.png'),
               py.image.load('images\\tiles\\world_map\\plains\\dark_plains5.png'),
               py.image.load('images\\tiles\\world_map\\plains\\dark_plains6.png'),
               py.image.load('images\\tiles\\world_map\\plains\\dark_plains7.png'),
               py.image.load('images\\tiles\\world_map\\plains\\dark_plains8.png')]
LIGHT_SAVANNAH = [py.image.load('images\\tiles\\world_map\\savannah\\light_savannah0.png'),
                  py.image.load('images\\tiles\\world_map\\savannah\\light_savannah1.png'),
                  py.image.load('images\\tiles\\world_map\\savannah\\light_savannah2.png'),
                  py.image.load('images\\tiles\\world_map\\savannah\\light_savannah3.png'),
                  py.image.load('images\\tiles\\world_map\\savannah\\light_savannah4.png'),
                  py.image.load('images\\tiles\\world_map\\savannah\\light_savannah5.png'),
                  py.image.load('images\\tiles\\world_map\\savannah\\light_savannah6.png'),
                  py.image.load('images\\tiles\\world_map\\savannah\\light_savannah7.png'),
                  py.image.load('images\\tiles\\world_map\\savannah\\light_savannah8.png'), ]
DARK_SAVANNAH = [py.image.load('images\\tiles\\world_map\\savannah\\dark_savannah0.png'),
                 py.image.load('images\\tiles\\world_map\\savannah\\dark_savannah1.png'),
                 py.image.load('images\\tiles\\world_map\\savannah\\dark_savannah2.png'),
                 py.image.load('images\\tiles\\world_map\\savannah\\dark_savannah3.png'),
                 py.image.load('images\\tiles\\world_map\\savannah\\dark_savannah4.png'),
                 py.image.load('images\\tiles\\world_map\\savannah\\dark_savannah5.png'),
                 py.image.load('images\\tiles\\world_map\\savannah\\dark_savannah6.png'),
                 py.image.load('images\\tiles\\world_map\\savannah\\dark_savannah7.png'),
                 py.image.load('images\\tiles\\world_map\\savannah\\dark_savannah8.png'), ]
LIGHT_SHALLOW = [py.image.load('images\\tiles\\world_map\\shallow\\light_shallow0.png'),
                 py.image.load('images\\tiles\\world_map\\shallow\\light_shallow1.png'),
                 py.image.load('images\\tiles\\world_map\\shallow\\light_shallow2.png'),
                 py.image.load('images\\tiles\\world_map\\shallow\\light_shallow3.png'),
                 py.image.load('images\\tiles\\world_map\\shallow\\light_shallow4.png'),
                 py.image.load('images\\tiles\\world_map\\shallow\\light_shallow5.png'),
                 py.image.load('images\\tiles\\world_map\\shallow\\light_shallow6.png'),
                 py.image.load('images\\tiles\\world_map\\shallow\\light_shallow7.png'),
                 py.image.load('images\\tiles\\world_map\\shallow\\light_shallow8.png')]
DARK_SHALLOW = [py.image.load('images\\tiles\\world_map\\shallow\\dark_shallow0.png'),
                py.image.load('images\\tiles\\world_map\\shallow\\dark_shallow1.png'),
                py.image.load('images\\tiles\\world_map\\shallow\\dark_shallow2.png'),
                py.image.load('images\\tiles\\world_map\\shallow\\dark_shallow3.png'),
                py.image.load('images\\tiles\\world_map\\shallow\\dark_shallow4.png'),
                py.image.load('images\\tiles\\world_map\\shallow\\dark_shallow5.png'),
                py.image.load('images\\tiles\\world_map\\shallow\\dark_shallow6.png'),
                py.image.load('images\\tiles\\world_map\\shallow\\dark_shallow7.png'),
                py.image.load('images\\tiles\\world_map\\shallow\\dark_shallow8.png')]
LIGHT_SNOW = [py.image.load('images\\tiles\\world_map\\snow\\light_snow0.png'),
              py.image.load('images\\tiles\\world_map\\snow\\light_snow1.png'),
              py.image.load('images\\tiles\\world_map\\snow\\light_snow2.png'),
              py.image.load('images\\tiles\\world_map\\snow\\light_snow3.png'),
              py.image.load('images\\tiles\\world_map\\snow\\light_snow4.png'),
              py.image.load('images\\tiles\\world_map\\snow\\light_snow5.png'),
              py.image.load('images\\tiles\\world_map\\snow\\light_snow6.png'),
              py.image.load('images\\tiles\\world_map\\snow\\light_snow7.png'),
              py.image.load('images\\tiles\\world_map\\snow\\light_snow8.png')]
DARK_SNOW = [py.image.load('images\\tiles\\world_map\\snow\\dark_snow0.png'),
             py.image.load('images\\tiles\\world_map\\snow\\dark_snow1.png'),
             py.image.load('images\\tiles\\world_map\\snow\\dark_snow2.png'),
             py.image.load('images\\tiles\\world_map\\snow\\dark_snow3.png'),
             py.image.load('images\\tiles\\world_map\\snow\\dark_snow4.png'),
             py.image.load('images\\tiles\\world_map\\snow\\dark_snow5.png'),
             py.image.load('images\\tiles\\world_map\\snow\\dark_snow6.png'),
             py.image.load('images\\tiles\\world_map\\snow\\dark_snow7.png'),
             py.image.load('images\\tiles\\world_map\\snow\\dark_snow8.png')]
LIGHT_TAIGA = [py.image.load('images\\tiles\\world_map\\taiga\\light_taiga0.png'),
               py.image.load('images\\tiles\\world_map\\taiga\\light_taiga1.png'),
               py.image.load('images\\tiles\\world_map\\taiga\\light_taiga2.png'),
               py.image.load('images\\tiles\\world_map\\taiga\\light_taiga3.png'),
               py.image.load('images\\tiles\\world_map\\taiga\\light_taiga4.png'),
               py.image.load('images\\tiles\\world_map\\taiga\\light_taiga5.png'),
               py.image.load('images\\tiles\\world_map\\taiga\\light_taiga6.png'),
               py.image.load('images\\tiles\\world_map\\taiga\\light_taiga7.png'),
               py.image.load('images\\tiles\\world_map\\taiga\\light_taiga8.png')]
DARK_TAIGA = [py.image.load('images\\tiles\\world_map\\taiga\\dark_taiga0.png'),
              py.image.load('images\\tiles\\world_map\\taiga\\dark_taiga1.png'),
              py.image.load('images\\tiles\\world_map\\taiga\\dark_taiga2.png'),
              py.image.load('images\\tiles\\world_map\\taiga\\dark_taiga3.png'),
              py.image.load('images\\tiles\\world_map\\taiga\\dark_taiga4.png'),
              py.image.load('images\\tiles\\world_map\\taiga\\dark_taiga5.png'),
              py.image.load('images\\tiles\\world_map\\taiga\\dark_taiga6.png'),
              py.image.load('images\\tiles\\world_map\\taiga\\dark_taiga7.png'),
              py.image.load('images\\tiles\\world_map\\taiga\\dark_taiga8.png')]
LIGHT_TEMPRAIN = [py.image.load('images\\tiles\\world_map\\temprain\\light_temprain0.png'),
                  py.image.load('images\\tiles\\world_map\\temprain\\light_temprain1.png'),
                  py.image.load('images\\tiles\\world_map\\temprain\\light_temprain2.png'),
                  py.image.load('images\\tiles\\world_map\\temprain\\light_temprain3.png'),
                  py.image.load('images\\tiles\\world_map\\temprain\\light_temprain4.png'),
                  py.image.load('images\\tiles\\world_map\\temprain\\light_temprain5.png'),
                  py.image.load('images\\tiles\\world_map\\temprain\\light_temprain6.png'),
                  py.image.load('images\\tiles\\world_map\\temprain\\light_temprain7.png'),
                  py.image.load('images\\tiles\\world_map\\temprain\\light_temprain8.png'), ]
DARK_TEMPRAIN = [py.image.load('images\\tiles\\world_map\\temprain\\dark_temprain0.png'),
                 py.image.load('images\\tiles\\world_map\\temprain\\dark_temprain1.png'),
                 py.image.load('images\\tiles\\world_map\\temprain\\dark_temprain2.png'),
                 py.image.load('images\\tiles\\world_map\\temprain\\dark_temprain3.png'),
                 py.image.load('images\\tiles\\world_map\\temprain\\dark_temprain4.png'),
                 py.image.load('images\\tiles\\world_map\\temprain\\dark_temprain5.png'),
                 py.image.load('images\\tiles\\world_map\\temprain\\dark_temprain6.png'),
                 py.image.load('images\\tiles\\world_map\\temprain\\dark_temprain7.png'),
                 py.image.load('images\\tiles\\world_map\\temprain\\dark_temprain8.png'), ]
LIGHT_TROPICRAIN = [py.image.load('images\\tiles\\world_map\\tropicrain\\light_tropicrain0.png'),
                    py.image.load('images\\tiles\\world_map\\tropicrain\\light_tropicrain1.png'),
                    py.image.load('images\\tiles\\world_map\\tropicrain\\light_tropicrain2.png'),
                    py.image.load('images\\tiles\\world_map\\tropicrain\\light_tropicrain3.png'),
                    py.image.load('images\\tiles\\world_map\\tropicrain\\light_tropicrain4.png'),
                    py.image.load('images\\tiles\\world_map\\tropicrain\\light_tropicrain5.png'),
                    py.image.load('images\\tiles\\world_map\\tropicrain\\light_tropicrain6.png'),
                    py.image.load('images\\tiles\\world_map\\tropicrain\\light_tropicrain7.png'),
                    py.image.load('images\\tiles\\world_map\\tropicrain\\light_tropicrain8.png'), ]
DARK_TROPICRAIN = [py.image.load('images\\tiles\\world_map\\tropicrain\\dark_tropicrain0.png'),
                   py.image.load('images\\tiles\\world_map\\tropicrain\\dark_tropicrain1.png'),
                   py.image.load('images\\tiles\\world_map\\tropicrain\\dark_tropicrain2.png'),
                   py.image.load('images\\tiles\\world_map\\tropicrain\\dark_tropicrain3.png'),
                   py.image.load('images\\tiles\\world_map\\tropicrain\\dark_tropicrain4.png'),
                   py.image.load('images\\tiles\\world_map\\tropicrain\\dark_tropicrain5.png'),
                   py.image.load('images\\tiles\\world_map\\tropicrain\\dark_tropicrain6.png'),
                   py.image.load('images\\tiles\\world_map\\tropicrain\\dark_tropicrain7.png'),
                   py.image.load('images\\tiles\\world_map\\tropicrain\\dark_tropicrain8.png'), ]
LIGHT_TUNDRA = [py.image.load('images\\tiles\\world_map\\tundra\\light_tundra0.png'),
                py.image.load('images\\tiles\\world_map\\tundra\\light_tundra1.png'),
                py.image.load('images\\tiles\\world_map\\tundra\\light_tundra2.png'),
                py.image.load('images\\tiles\\world_map\\tundra\\light_tundra3.png'),
                py.image.load('images\\tiles\\world_map\\tundra\\light_tundra4.png'),
                py.image.load('images\\tiles\\world_map\\tundra\\light_tundra5.png'),
                py.image.load('images\\tiles\\world_map\\tundra\\light_tundra6.png'),
                py.image.load('images\\tiles\\world_map\\tundra\\light_tundra7.png'),
                py.image.load('images\\tiles\\world_map\\tundra\\light_tundra8.png')]
DARK_TUNDRA = [py.image.load('images\\tiles\\world_map\\tundra\\dark_tundra0.png'),
               py.image.load('images\\tiles\\world_map\\tundra\\dark_tundra1.png'),
               py.image.load('images\\tiles\\world_map\\tundra\\dark_tundra2.png'),
               py.image.load('images\\tiles\\world_map\\tundra\\dark_tundra3.png'),
               py.image.load('images\\tiles\\world_map\\tundra\\dark_tundra4.png'),
               py.image.load('images\\tiles\\world_map\\tundra\\dark_tundra5.png'),
               py.image.load('images\\tiles\\world_map\\tundra\\dark_tundra6.png'),
               py.image.load('images\\tiles\\world_map\\tundra\\dark_tundra7.png'),
               py.image.load('images\\tiles\\world_map\\tundra\\dark_tundra8.png')]

BIOMES = {
    'light_deep': LIGHT_DEEP,
    'dark_deep': DARK_DEEP,
    'light_desert': LIGHT_DESERT,
    'dark_desert': DARK_DESERT,
    'light_forest': LIGHT_FOREST,
    'dark_forest': DARK_FOREST,
    'light_plains': LIGHT_PLAINS,
    'dark_plains': DARK_PLAINS,
    'light_savannah': LIGHT_SAVANNAH,
    'dark_savannah': DARK_SAVANNAH,
    'light_shallow': LIGHT_SHALLOW,
    'dark_shallow': DARK_SHALLOW,
    'light_snow': LIGHT_SNOW,
    'dark_snow': DARK_SNOW,
    'light_temprain': LIGHT_TEMPRAIN,
    'dark_temprain': DARK_TEMPRAIN,
    'light_tropicrain': LIGHT_TROPICRAIN,
    'dark_tropicrain': DARK_TROPICRAIN,
    'light_taiga': LIGHT_TAIGA,
    'dark_taiga': DARK_TAIGA,
    'light_tundra': LIGHT_TUNDRA,
    'dark_tundra': DARK_TUNDRA,
}

TILE_BASE = {
    'black': py.image.load('images\\tiles\\black.png'),
    'dark_wall': py.image.load('images\\tiles\\dark_wall.png'),
    'light_wall': py.image.load('images\\tiles\\light_wall.png'),
}

LIGHT_GRASS = [py.image.load('images\\tiles\\grass\\light_grass00.png'),
               py.image.load('images\\tiles\\grass\\light_grass01.png'),
               py.image.load('images\\tiles\\grass\\light_grass02.png'),
               py.image.load('images\\tiles\\grass\\light_grass03.png'),
               py.image.load('images\\tiles\\grass\\light_grass04.png'),
               py.image.load('images\\tiles\\grass\\light_grass05.png'),
               py.image.load('images\\tiles\\grass\\light_grass06.png'),
               py.image.load('images\\tiles\\grass\\light_grass07.png'),
               py.image.load('images\\tiles\\grass\\light_grass08.png'),
               py.image.load('images\\tiles\\grass\\light_grass09.png'),
               py.image.load('images\\tiles\\grass\\light_grass10.png'),
               py.image.load('images\\tiles\\grass\\light_grass11.png'),
               py.image.load('images\\tiles\\grass\\light_grass12.png')]
DARK_GRASS = [py.image.load('images\\tiles\\grass\\dark_grass00.png'),
              py.image.load('images\\tiles\\grass\\dark_grass01.png'),
              py.image.load('images\\tiles\\grass\\dark_grass02.png'),
              py.image.load('images\\tiles\\grass\\dark_grass03.png'),
              py.image.load('images\\tiles\\grass\\dark_grass04.png'),
              py.image.load('images\\tiles\\grass\\dark_grass05.png'),
              py.image.load('images\\tiles\\grass\\dark_grass06.png'),
              py.image.load('images\\tiles\\grass\\dark_grass07.png'),
              py.image.load('images\\tiles\\grass\\dark_grass08.png'),
              py.image.load('images\\tiles\\grass\\dark_grass09.png'),
              py.image.load('images\\tiles\\grass\\dark_grass10.png'),
              py.image.load('images\\tiles\\grass\\dark_grass11.png'),
              py.image.load('images\\tiles\\grass\\dark_grass12.png')]
LIGHT_ROAD = {
    '00001011': py.image.load('images\\road\\light_road00001011.png'),
    '00010110': py.image.load('images\\road\\light_road00010110.png'),
    '00011111': py.image.load('images\\road\\light_road00011111.png'),
    '01101000': py.image.load('images\\road\\light_road01101000.png'),
    '01101011': py.image.load('images\\road\\light_road01101011.png'),
    '01111111': py.image.load('images\\road\\light_road01111111.png'),
    '11010000': py.image.load('images\\road\\light_road11010000.png'),
    '11010110': py.image.load('images\\road\\light_road11010110.png'),
    '11011011': py.image.load('images\\road\\light_road11011011.png'),
    '11111000': py.image.load('images\\road\\light_road11111000.png'),
    '11111110': py.image.load('images\\road\\light_road11111110.png'),
    '11111111': py.image.load('images\\road\\light_road11111111.png'),
}
DARK_ROAD = {
    '00001011': py.image.load('images\\road\\dark_road00001011.png'),
    '00010110': py.image.load('images\\road\\dark_road00010110.png'),
    '00011111': py.image.load('images\\road\\dark_road00011111.png'),
    '01101000': py.image.load('images\\road\\dark_road01101000.png'),
    '01101011': py.image.load('images\\road\\dark_road01101011.png'),
    '01111111': py.image.load('images\\road\\dark_road01111111.png'),
    '11010000': py.image.load('images\\road\\dark_road11010000.png'),
    '11010110': py.image.load('images\\road\\dark_road11010110.png'),
    '11011011': py.image.load('images\\road\\dark_road11011011.png'),
    '11111000': py.image.load('images\\road\\dark_road11111000.png'),
    '11111110': py.image.load('images\\road\\dark_road11111110.png'),
    '11111111': py.image.load('images\\road\\dark_road11111111.png'),
}
LIGHT_DIRT = [py.image.load('images\\tiles\\dirt\\light_dirt0.png'),
              py.image.load('images\\tiles\\dirt\\light_dirt1.png'),
              py.image.load('images\\tiles\\dirt\\light_dirt2.png'),
              py.image.load('images\\tiles\\dirt\\light_dirt3.png'),
              py.image.load('images\\tiles\\dirt\\light_dirt4.png'),
              py.image.load('images\\tiles\\dirt\\light_dirt5.png'),
              py.image.load('images\\tiles\\dirt\\light_dirt6.png'),
              py.image.load('images\\tiles\\dirt\\light_dirt7.png'),
              py.image.load('images\\tiles\\dirt\\light_dirt8.png')]
DARK_DIRT = [py.image.load('images\\tiles\\dirt\\dark_dirt0.png'),
             py.image.load('images\\tiles\\dirt\\dark_dirt1.png'),
             py.image.load('images\\tiles\\dirt\\dark_dirt2.png'),
             py.image.load('images\\tiles\\dirt\\dark_dirt3.png'),
             py.image.load('images\\tiles\\dirt\\dark_dirt4.png'),
             py.image.load('images\\tiles\\dirt\\dark_dirt5.png'),
             py.image.load('images\\tiles\\dirt\\dark_dirt6.png'),
             py.image.load('images\\tiles\\dirt\\dark_dirt7.png'),
             py.image.load('images\\tiles\\dirt\\dark_dirt8.png')]
