
class Skill():
    def __init__(self, name, effect, mana_cost, allowed_classes, description):
        self.name = name
        self.effect = effect
        self.mana_cost = mana_cost
        self.allowed_classes = allowed_classes
        self.description = description