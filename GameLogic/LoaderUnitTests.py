from Loaders import ClassLoader

class TestClassLoaders:
    def test_load_class_data(self):
        loader = ClassLoader()
        class_data = loader.load_class_data("Fighter")
        assert class_data["description"] == "A strong and resilient warrior, the fighter is the defender of the people. The fighter excels in close combat, heavy armor, both offensive and defensive skills."
        assert class_data["starting_stats"]["health"] == 150
        assert class_data["starting_stats"]["mana"] == 50
        assert class_data["starting_stats"]["strength"] == 14
        assert class_data["starting_stats"]["dexterity"] == 12
        assert class_data["starting_stats"]["constitution"] == 15
        assert class_data["starting_stats"]["wisdom"] == 8
        assert class_data["starting_stats"]["intelligence"] == 8
        assert class_data["starting_stats"]["charisma"] == 10
        assert class_data["starting_equipment"] == {
            "weapon": "Iron Seif",
            "offhand": "Hide Shield", 
            "body_armor": "Studded Leather Armor",
            "helmet": "Iron Plated Helmet",
            "accessory": "Sun Pendant" }
        try:
            loader.load_class_data("NonExistentClass")
            assert False, "Expected ValueError for non-existent class"
        except ValueError as e:
            assert str(e) == "Class NonExistentClass not found in classes.json"


def main():
        tests = TestClassLoaders()
        tests.test_load_class_data()
        print("All tests passed!")

if __name__ == "__main__":
    main()
        