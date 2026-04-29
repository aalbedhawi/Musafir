import json
import os
from skills import Skill
from equipment import Equipment

class SkillLoader:
    def __init__(self):
        self.skills = {}
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, '..', 'Data', 'skills.json')
        with open(file_path) as f:
            skill_data = json.load(f)
        for skill, skill_value in skill_data.items():
            self.skills[skill] = Skill(skill, skill_value["description"], skill_value["effect"], skill_value["mana_cost"], skill_value["allowed_classes"])
    
    def load_skill_data(self, skill_name):
        if skill_name in self.skills:
            return self.skills[skill_name]
        else:
            raise ValueError(f"Skill: {skill_name} not found")

class EquipmentLoader:
    def __init__(self):
        self.equipment = {}
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, '..', 'Data', 'equipment.json')
        with open(file_path) as f:
            equipment_data = json.load(f)
        for equipment, equipment_value in equipment_data.items():
            self.equipment[equipment] = Equipment(equipment, equipment_value["description"], equipment_value["slot"], equipment_value["requirements"], equipment_value["effect"], equipment_value["gold_value"])

    def load_equipment_data(self, equipment_name):
        if equipment_name in self.equipment:
            return self.equipment[equipment_name]
        else:
            raise ValueError(f"Equipment: {equipment_name} not found")

class ClassLoader:
    def __init__(self, skill_loader: SkillLoader, equipment_loader: EquipmentLoader):
        self.equipment_loader = equipment_loader
        self.skill_loader = skill_loader
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, '..', 'Data', 'classes.json')
        with open(file_path) as f:
            class_data = json.load(f)
        self.class_data = class_data

    def load_class_data(self, class_name):
        starting_skills = {}
        starting_equipment = {}
        if class_name in self.class_data:
            class_info = self.class_data[class_name]
            for skill_name in class_info["starting_skills"]:
                starting_skills[skill_name] = self.skill_loader.load_skill_data(skill_name)
            for equipment_name in class_info["starting_equipment"].values():
                starting_equipment[equipment_name] = self.equipment_loader.load_equipment_data(equipment_name)
            new_class_info = {**class_info, "starting_skills": starting_skills, "starting_equipment": starting_equipment}
            return new_class_info
        else:
            raise ValueError(f"Class {class_name} not found in classes.json")