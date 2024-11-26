import json

def save_recipe(recipe, recipe_file='recipes.json'):
    """
    Saves a new recipe to the recipe file.
    :param recipe: A dictionary containing the recipe details.
    :param recipe_file: The path to the recipe file.
    """
    try:
        recipes = load_recipes(recipe_file)
        if isinstance(recipe, dict):
            recipes.append(recipe)
        elif isinstance(recipe, list):
            recipes.extend(recipe)  
        with open(recipe_file, 'w') as file:
            json.dump(recipes, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving the recipe: {e}")


def load_recipes(recipe_file='recipes.json'):
    """
    Loads recipes from the recipe file.
    :param recipe_file: The path to the recipe file.
    :return: A list of recipes.
    """
    try:
        with open(recipe_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


