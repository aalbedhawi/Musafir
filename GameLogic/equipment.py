
class Equipment():
    def __init__(self, name, description, slot, requirements, effect, gold_value):
        self.name = name
        self.slot = slot
        self.requirements = requirements
        self.effect = effect
        self.description = description
        self.gold_value = gold_value
    
    @classmethod
    def empty_slot(cls, slot):
        return cls(name = None,description = None, slot = slot, requirements = None, effect = None, gold_value = 0)