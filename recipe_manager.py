from abc import ABC, abstractmethod

class RecipeManager(ABC):
    """
    Abstract base class for managing recipes.
    This class provides a template for recipe management tasks such as adding,
    searching, or deleting recipes.
    """

    @abstractmethod
    def manage_recipes(self):
        """
        Abstract method to manage recipes, 
        searching for existing recipes, or deleting recipes.
        """
        pass
