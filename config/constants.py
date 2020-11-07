# (screen, title)
SCREEN_SIZE = (1920, 1080)
CAPTION = 'Wuncemoor: The Eternal Dream'

TILESIZE = 48
# (width, height)
TILES_ON_SCREEN = (29, 21)
# (width, height)
DUNGEON_ALPHA = (200, 150)
DUNGEON_BETA = (100, 50)
DUNGEON_GAMMA = (200, 100)
DUNGEON_DELTA = (100, 40)
# (width, height)
OVERWORLD = (100, 100)
# (width, height)
MINI_MAP = (400, 400)
# (width, height)
CAVE = (80, 37)

FPS = 60
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 3
FOV_RADIUS = 50

# (octaves, persist, lacuna, scale, moist_mod, temp_mod, water_level)
SIMPLEX = (5, 0.5, 2.5, 0.0075, 0.5, 0.1, 0.15)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
DARK_RED = (191, 0, 0)
LIGHT_GREY = (190, 190, 190)
GREY = (128, 128, 128)
DARK_PURPLE = (143, 0, 191)
DARK_BLUE = (0, 0, 191)
DARK_ORANGE = (191, 95, 0)

DUNGEON_FLOOR = {
    'town': 'grass',
    'cave': 'dirt',
    'deep': 'deep',
    'desert': 'desert',
    'forest': 'forest',
    'plains': 'plains',
    'savannah': 'savannah',
    'shallow': 'shallow',
    'snow': 'snow',
    'taiga': 'taiga',
    'temprain': 'temprain',
    'tropicrain': 'tropicrain',
    'tundra': 'tundra',
}
IMAGE_OPTIONS = {
    'grass': 13,
    'dirt': 9,
    'biome': 9,
}