from abstracts.abstract_tile import AbstractTile
from abstracts.abstract_tile_component import AbstractTileFloor
from map_objects.floors.basic_floors import GrassTileFloor, DirtTileFloor
from ECS.__entity.blocker import RockTileBlocker


class FakeTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.name = None

    name = 'Fake'


class FakeTile(AbstractTile):

    def __init__(self, variant):
        super().__init__(variant)

    def initialize_floor(self, variant):
        return FakeTileFloor()

    def initialize_blocker(self, variant):
        return None


class Tile(AbstractTile):
    """
    Map tile. It may or may not be blocked, and may or may not block sight.
    On the world map, type is the biome and subtype is the closest exuding Node. (Ex. Rainforest near a goblin cave.)
    Otherwise, type is the location and subtype is the unique infestation. (Ex. Cave infested with goblins.)
    Mode changes tile appearance based on neighboring nodes. (Ex. Different road pieces)
    Node power increases risk/reward
    """
    def __init__(self, variant):
        self.floor = self.initialize_floor(variant)
        self.blocker = self.initialize_blocker(variant)
        self.explored = False
        self.type = None
        self.subtype = None
        self.mode = None
        self.np = 0

    def initialize_floor(self, variant):
        if variant in ('alpha', 'beta', 'gamma', 'delta'):
            base = GrassTileFloor()
        elif variant == 'cave':
            base = DirtTileFloor()
        else:
            base = None
        return base

    def initialize_blocker(self, variant):
        if variant == 'cave':
            return RockTileBlocker()
        else:
            return None
