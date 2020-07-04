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
        self.items.extend(dead_entity.combatant.satchel.items)
        self.items.extend(dead_entity.combatant.equipment.drop_dead())

    def reset(self):
        self.items = []
        self.claimed = []
        self.current_option = 0
