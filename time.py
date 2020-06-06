import datetime

class FileRecipes:

    def __init__(self, file_path):
        global begining_time
        begining_time = datetime.datetime.now()
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        ending_time = datetime.datetime.now()
        print(f"время запуска кода: {begining_time}")
        print(f"время работы кода: {ending_time - begining_time}")
        print(f"время окончания работы кода: {ending_time}")

        self.file.close()

with FileRecipes('recipes.txt') as recipes:
    cook_book = {}

    def recipe_dict():
        dishes = recipes.readline().strip()
        if dishes:
            cook_book[dishes] = []
            ingredients = recipes.readline()
            for line in range(int(ingredients)):
                ingredient = recipes.readline().strip().split(' | ')
                ingredient_dictionary = {'ingredient_name': ingredient[0], 'quantity': ingredient[1],
                                         'measure': ingredient[2]}
                cook_book[dishes].append(ingredient_dictionary)
        else:
            return cook_book
        print(recipe_dict())

    recipe_dict()


