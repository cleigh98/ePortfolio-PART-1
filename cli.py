import argparse
from add_recipe import AddRecipe
from search_recipe import SearchRecipe
from recipe_storage import save_recipe, load_recipes

def main():
    """
    The main function to handle command-line arguments for the Recipe Manager CLI.
    It supports adding new recipes and searching for existing recipes.
    The add command requires title, ingredients, and instructions for the recipe.
    The search command allows searching by recipe title or ingredient.
    """
    parser = argparse.ArgumentParser(description='Recipe Manager CLI')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new recipe')
    add_parser.add_argument('--title', required=True, help='Title of the recipe')
    add_parser.add_argument('--ingredients', required=True, nargs='+', help='List of ingredients')
    add_parser.add_argument('--instructions', required=True, help='Cooking instructions')

    search_parser = subparsers.add_parser('search', help='Search for recipes')
    search_parser.add_argument('--title', help='Search by title')
    search_parser.add_argument('--ingredient', help='Search by ingredient')

    args = parser.parse_args()

    if args.command == 'add':
        recipe_data = {
            'title': args.title,
            'ingredients': args.ingredients,
            'instructions': args.instructions
        }
        save_recipe(recipe_data)
        print('Recipe added successfully.')

    elif args.command == 'search':
        searcher = SearchRecipe()
        if args.title:
            matched_recipes = searcher.manage_recipes({'title': args.title})
        elif args.ingredient:
            matched_recipes = searcher.manage_recipes({'ingredient': args.ingredient})
        else:
            print('Please specify a search criterion.')
            return

        if matched_recipes:
            print('Matched Recipes:')
            for recipe in matched_recipes:
                print(recipe)
        else:
            print('No recipes found.')

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
