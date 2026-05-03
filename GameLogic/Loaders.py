import json
import os
from exceptions import EntryNotFoundError
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
            self.skills[skill] = Skill(skill, skill_value["description"], skill_value["effect"], skill_value["mana_cost"], skill_value.get("allowed_classes", None))
    
    def load_skill_data(self, skill_name):
        if skill_name in self.skills:
            return self.skills[skill_name]
        else:
            raise EntryNotFoundError(f"Skill: {skill_name} not found")

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
            raise EntryNotFoundError(f"Equipment: {equipment_name} not found")

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
            raise EntryNotFoundError(f"Class {class_name} not found in classes.json")

class EnemyLoader:
    def __init__(self, skill_loader: SkillLoader, equipment_loader: EquipmentLoader):
        self.equipment_loader = equipment_loader
        self.skill_loader = skill_loader
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, '..', 'Data', 'enemies.json')
        with open(file_path) as f:
            enemy_data = json.load(f)
        self.enemy_data = enemy_data

    def load_enemy_data(self, name):
        skills = {}
        equipment = {}
        if name in self.enemy_data:
            enemy_info = self.enemy_data[name]
            for skill_name in enemy_info["skills"]:
                skills[skill_name] = self.skill_loader.load_skill_data(skill_name)
            for slot, equipment_name in enemy_info["equipment"].items():
                if equipment_name is None:
                    equipment[slot] = Equipment.empty_slot(slot)
                else:
                    equipment[slot] = self.equipment_loader.load_equipment_data(equipment_name)
            new_enemy_info = {**enemy_info, "skills": skills, "equipment": equipment}
            return new_enemy_info
        else:
            raise EntryNotFoundError(f"Enemy: {name} not found in enemies.json")