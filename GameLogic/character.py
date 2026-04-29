class Character:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.max_health = 0
        self.mana = 0
        self.max_mana = 0
        self.level = 1
        self.strength = 0
        self.dexterity = 0
        self.wisdom = 0
        self.intelligence = 0
        self.charisma = 0
        self.constitution = 0
        self.gold = 0
        self.equipment = {
            "weapon": None,
            "offhand": None,
            "body_armor": None,
            "helmet": None,
            "accessory": None
        }
        self.skills = {}
        self.status_effects = {}

class Player(Character):
    def __init__(self, name, class_type):
        super().__init__(name)
        self.class_type = class_type
        self.experience = 0
        self.experience_to_next_level = 100
        self.inventory = {}
        self._load_class_data()

class Enemy(Character):
    def __init__(self, name, enemy_type):
        super().__init__(name)
        self.enemy_type = enemy_type
        self.experience_reward = 0
