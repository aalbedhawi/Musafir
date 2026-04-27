 
class ClassLoader:
    def _load_class_data(self, class_name):
        # TODO: load starting stats and skills from classes.json via a classloader
        with open('classes.json') as f:
            # need to pull the key which is the class name
            # Need to load the stats, skills, and other information for the class based on the name
            # need to return this value so it can be used by the player class to set the character
            pass 