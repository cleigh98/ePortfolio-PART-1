import unittest
from search_recipe import SearchRecipe
from recipe_storage import save_recipe

class TestSearchRecipe(unittest.TestCase):
    """
    Unit tests for the SearchRecipe class.
    This test class covers the functionality of searching for recipes by title and ingredient.
    It uses a test JSON file for storing and retrieving recipes to avoid impacting the actual recipe data.
    """

    def setUp(self):
        """
        Set up method to initialize test environment.
        Creates a SearchRecipe object and a test recipe data, and then saves the test recipe
        to a test JSON file.
        """
        self.search_recipe = SearchRecipe("test_recipes.json")
        self.test_recipe_data = {
            "title": "Test Recipe",
            "ingredients": ["ingredient1", "ingredient2"],
            "instructions": "Test instructions"
        }
        save_recipe(self.test_recipe_data, "test_recipes.json")

    def test_search_by_title(self):
        """
        Test searching for a recipe by its title.
        Ensures that the search functionality correctly finds a recipe based on its title and
        verifies that the returned list has the correct length and contains the expected recipe.
        """
        result = self.search_recipe.manage_recipes({"title": "Test Recipe"})
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['title'], "Test Recipe")

    def test_search_by_ingredient(self):
        """
        Test searching for recipes by an ingredient.
        Checks if the search functionality can find recipes containing a specified ingredient and
        verifies that the returned list contains the expected recipe with the correct ingredient.
        """
        result = self.search_recipe.manage_recipes({"ingredient": "ingredient1"})
        self.assertEqual(len(result), 1)
        self.assertIn("ingredient1", result[0]['ingredients'])

    def tearDown(self):
        """
        Tear down method to clean up after tests.
        Resets the test JSON file to an empty list, ensuring that each test starts with a clean state.
        """
        with open("test_recipes.json", "w") as file:
            file.write("[]")

if __name__ == '__main__':
    unittest.main()
