import json
from recipe_manager import RecipeManager
from recipe_storage import save_recipe, load_recipes 

class AddRecipe(RecipeManager):
    """
    This class handles the addition of new recipes to a recipe file.
    It extends the RecipeManager abstract class and implements the
    manage_recipes abstract method for adding recipes.
    """
    def __init__(self, recipe_file='recipes.json'):
        """
        Initialize the AddRecipe object.
        """
        self.recipe_file = recipe_file

    def manage_recipes(self, recipe_data):
        try:
            self.add_recipe(recipe_data)
        except Exception as e:
            print(f"An error occurred: {e}")
            raise  

    def add_recipe(self, recipe_data):
        """
        Adds a new recipe to the recipe file.
        :param recipe_data: A dictionary containing the recipe details.
        """
        try:
            recipes = load_recipes(self.recipe_file)
            recipes.append(recipe_data)
            save_recipe(recipes, self.recipe_file)
            print("Recipe added successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
