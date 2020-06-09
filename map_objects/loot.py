from enums.game_states import LootStates


class Loot:

    def __init__(self, xp=0, items=[]):
        self.xp = xp
        self.items = items
        self.options = ['AUTO', 'MANUAL', 'LEAVE']
        self.current_option = 0
        self.claimed = []
        self.state = LootStates.THINKING

    def add_loot(self, dead_entity):
        self.items.extend(dead_entity.combatant.inventory.items)
