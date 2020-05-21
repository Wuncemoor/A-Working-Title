from enum import Enum	

class GameStates(Enum):
    PLAYERS_TURN = 1
    ENEMY_TURN = 2
    PLAYER_DEAD = 3
    SHOW_INVENTORY = 4
    DROP_INVENTORY = 5
    TARGETING = 6
    LEVEL_UP = 7
    CHARACTER_MENU = 8
    PRIMARY_STATS_SCREEN = 9
    COMBAT_STATS_SCREEN = 10
    NONCOMBAT_STATS_SCREEN = 11
    COMPETENCE_MENU = 12
    STRENGTH_FEATS = 13
    INSTINCT_FEATS = 14
    COORDINATION_FEATS = 15
    VITALITY_FEATS = 16
    ARCANA_FEATS = 17
    IMPROVISATION_FEATS = 18
    WISDOM_FEATS = 19
    FINESSE_FEATS = 20
    CHARISMA_FEATS = 21
    DEVOTION_FEATS = 22
    ENCOUNTER = 23
    DIALOGUE = 24
    SHOW_MAP = 25