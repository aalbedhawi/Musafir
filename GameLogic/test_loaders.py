from Loaders import SkillLoader, EquipmentLoader, ClassLoader
from unittest.mock import patch
import unittest

class TestSkillLoader(unittest.TestCase):
    fake_skill = {
        "Slash": {
            "description": "Slash an enemy",
            "effect":{"damage": 5},
            "mana_cost": 5,
            "allowed_classes": ["Fighter", "Faris"] 
        }
    }

    def setUp(self):
        with patch("builtins.open"), patch("json.load", return_value = self.fake_skill):
            self.skill_loader = SkillLoader()

    def test_skill_creation(self):
        skill = self.skill_loader.load_skill_data("Slash")
        assert skill.description == "Slash an enemy"
        assert skill.mana_cost == 5
        assert skill.allowed_classes == ["Fighter", "Faris"]
        assert skill.effect == {"damage": 5}
        assert skill.name == "Slash"
    
    def test_skill_error(self):
        self.assertRaises(ValueError, self.skill_loader.load_skill_data, "Slash a enemy")

class TestEquipmentLoader(unittest.TestCase):
    fake_equipment = {
        "Iron Seif": {
            "description": "The typical armament for any warrior or traveler in the lands of Amel.",
            "slot": "weapon",
            "requirements": {"strength": 12},
            "effect": {"damage": 5},
            "gold_value": 2
        }
    }

    def setUp(self):
        with patch("builtins.open"), patch("json.load", return_value = self.fake_equipment):
            self.equipment_loader = EquipmentLoader()

    def test_equipment_creation(self):
        equipment = self.equipment_loader.load_equipment_data("Iron Seif")
        assert equipment.description == "The typical armament for any warrior or traveler in the lands of Amel."
        assert equipment.slot == "weapon"
        assert equipment.requirements == {"strength": 12}
        assert equipment.effect == {"damage": 5}
        assert equipment.gold_value == 2
        assert equipment.name == "Iron Seif"

    def test_equipment_error(self):
        self.assertRaises(ValueError, self.equipment_loader.load_equipment_data, "wepon")

class TestClassLoader(unittest.TestCase):
    fake_equipment = {
        "Iron Seif": {
            "description": "The typical armament for any warrior or traveler in the lands of Amel.",
            "slot": "weapon",
            "requirements": {"strength": 12},
            "effect": {"damage": 5},
            "gold_value": 2
        }
    }

    fake_skill = {
        "Slash": {
            "description": "Slash an enemy",
            "effect":{"damage": 5},
            "mana_cost": 5,
            "allowed_classes": ["Fighter", "Faris"] 
        }
    }

    fake_class = {
            "Fighter": {
        "description": "A strong and resilient warrior, the fighter is the defender of the people. The fighter excels in close combat, heavy armor, both offensive and defensive skills.",
        "starting_stats": {
            "health": 150,
            "mana": 50,
            "strength": 14,
            "dexterity": 12,
            "constitution": 15,
            "wisdom": 8,
            "intelligence": 8,
            "charisma": 10
        },
        "starting_equipment":{
            "weapon": "Iron Seif"
        },
        "starting_skills": 
            ["Slash"]
        }
    }

    def setUp(self):
        with patch("builtins.open"), patch("json.load", return_value = self.fake_equipment):
            self.equipment_loader = EquipmentLoader()
        with patch("builtins.open"), patch("json.load", return_value = self.fake_skill):
            self.skill_loader = SkillLoader()
        with patch("builtins.open"), patch("json.load", return_value = self.fake_class):
            self.class_loader = ClassLoader(self.skill_loader, self.equipment_loader)

    def test_load_class_data(self):
        class_data = self.class_loader.load_class_data("Fighter")
        skill = class_data["starting_skills"]["Slash"]
        equipment = class_data["starting_equipment"]["Iron Seif"]

        assert class_data["description"] == "A strong and resilient warrior, the fighter is the defender of the people. The fighter excels in close combat, heavy armor, both offensive and defensive skills."
        assert class_data["starting_stats"]["health"] == 150
        assert class_data["starting_stats"]["mana"] == 50
        assert class_data["starting_stats"]["strength"] == 14
        assert class_data["starting_stats"]["dexterity"] == 12
        assert class_data["starting_stats"]["constitution"] == 15
        assert class_data["starting_stats"]["wisdom"] == 8
        assert class_data["starting_stats"]["intelligence"] == 8
        assert class_data["starting_stats"]["charisma"] == 10
        assert skill.description == "Slash an enemy"
        assert skill.mana_cost == 5
        assert skill.allowed_classes == ["Fighter", "Faris"]
        assert skill.effect == {"damage": 5}
        assert skill.name == "Slash"
        assert equipment.description == "The typical armament for any warrior or traveler in the lands of Amel."
        assert equipment.slot == "weapon"
        assert equipment.requirements == {"strength": 12}
        assert equipment.effect == {"damage": 5}
        assert equipment.gold_value == 2
        assert equipment.name == "Iron Seif"

    def test_loadclassdata_error(self):
        self.assertRaises(ValueError, self.class_loader.load_class_data, "Fightr")



if __name__ == "__main__":
    unittest.main()
        