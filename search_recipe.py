import json
from recipe_manager import RecipeManager

class SearchRecipe(RecipeManager):
    """
    This class is responsible for searching recipes based on given criteria.
    It extends the RecipeManager abstract class and implements the
    manage_recipes method to allow for searching recipes by different parameters.
    """
    def __init__(self, recipe_file='recipes.json'):
        """
        Initialize the SearchRecipe object.
        """
        self.recipe_file = recipe_file

    def manage_recipes(self, search_query):
        """
        Manage the recipe searching process. It delegates the task to the search_recipe method.
        """
        return self.search_recipe(search_query)

    def search_recipe(self, search_query):
        """
        Searches for recipes that match the given query.
        """
        recipes = self._load_recipes()
        matched_recipes = []

        for recipe in recipes:
            if self._matches(recipe, search_query):
                matched_recipes.append(recipe)

        return matched_recipes

    def _matches(self, recipe, search_query):
        """
        Checks if the recipe matches the search query.
        """
        if 'title' in search_query:
            if search_query['title'].lower() in recipe['title'].lower():
                return True

        if 'ingredient' in search_query:
            for ingredient in recipe['ingredients']:
                if search_query['ingredient'].lower() in ingredient.lower():
                    return True

        return False

    def _load_recipes(self):
        """
        Loads recipes from the recipe file.
        :return: A list of recipes.
        """
        try:
            with open(self.recipe_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
