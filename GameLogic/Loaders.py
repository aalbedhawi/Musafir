import json
import os

class ClassLoader:
    def load_class_data(self, class_name):
        # TODO: load starting stats and skills from classes.json via a classloader
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, '..', 'Data', 'classes.json')
        with open(file_path) as f:
            # need to pull the key which is the class name
            class_data = json.load(f)
            if class_name in class_data:
                return class_data[class_name]
            else:
                raise ValueError(f"Class {class_name} not found in classes.json")