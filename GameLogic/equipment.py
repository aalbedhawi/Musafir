
class Equipment():
    def __init__(self, name, description, slot, requirements, effect, gold_value):
        self.name = name
        self.slot = slot
        self.requirements = requirements
        self.effect = effect
        self.description = description
        self.gold_value = gold_value