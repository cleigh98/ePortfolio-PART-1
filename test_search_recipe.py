import unittest
from search_recipe import SearchRecipe
from recipe_storage import save_recipe

class TestSearchRecipe(unittest.TestCase):
    """
    A unit test class for testing the SearchRecipe functionality.
    This class tests the ability to search for recipes by title and ingredient in a recipe database.
    It uses a test recipe file (test_recipes.json) to perform the tests.
    """

    def setUp(self):
        """
        Set up the test environment before each test method is executed.
        This method initializes a SearchRecipe object and saves a test recipe to the test recipe file.
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
        Test the ability to search for a recipe by its title.
        This method tests that the search functionality correctly finds a recipe based on its title.
        It asserts that the number of results and the title of the first result match the expectations.
        """
        result = self.search_recipe.manage_recipes({"title": "Test Recipe"})
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['title'], "Test Recipe")

    def test_search_by_ingredient(self):
        """
        Test the ability to search for a recipe by an ingredient.
        This method tests that the search functionality correctly finds a recipe based on an ingredient.
        It asserts that the number of results is correct and that the specified ingredient is in the ingredients of the first result.
        """
        result = self.search_recipe.manage_recipes({"ingredient": "ingredient1"})
        self.assertEqual(len(result), 1)
        self.assertIn("ingredient1", result[0]['ingredients'])

    def tearDown(self):
        """
        Clean up the test environment after each test method is executed.
        This method resets the test recipe file to an empty state.
        """
        with open("test_recipes.json", "w") as file:
            file.write("[]")

if __name__ == '__main__':
    unittest.main()
