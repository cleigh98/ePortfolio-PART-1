import unittest
from add_recipe import AddRecipe
from recipe_storage import load_recipes

class TestAddRecipe(unittest.TestCase):
    """
    Unit test class for testing the AddRecipe class functionality.
    This class provides tests for ensuring that recipes are correctly added
    to the recipe file using methods from the AddRecipe class.
    """

    def setUp(self):
        """
        Set up method to initialize test environment.
        This method is run before each test. It sets up an AddRecipe object
        and a test recipe data dictionary for use in the tests.
        """
        self.add_recipe = AddRecipe("test_recipes.json")
        self.test_recipe_data = {
            "title": "Test Recipe",
            "ingredients": ["ingredient1", "ingredient2"],
            "instructions": "Test instructions"
        }

    def test_add_recipe(self):
        """
        Test the addition of a recipe.
        This method tests the manage_recipes method of the AddRecipe class
        to ensure it properly adds a new recipe to the recipe file.
        """
        self.add_recipe.manage_recipes(self.test_recipe_data)
        recipes = load_recipes("test_recipes.json")
        self.assertIn(self.test_recipe_data, recipes, "Recipe not added correctly")

    def tearDown(self):
        """
        Tear down method to clean up after tests.
        This method is run after each test. It resets the test recipe file
        to its initial empty state.
        """
        with open("test_recipes.json", "w") as file:
            file.write("[]")

if __name__ == '__main__':
    unittest.main()
