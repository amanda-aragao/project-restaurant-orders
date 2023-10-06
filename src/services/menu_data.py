# Req 3
from models.dish import Dish
from models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.path = source_path
        self.file_open()

    def file_open(self):

        with open(self.path, encoding="utf-8") as file_csv:
            menu_items = csv.reader(file_csv, delimiter=",", quotechar='"')
            next(menu_items, None)  # pula o cabeçalho

            for row in menu_items:
                dish_name, price_str, ingredient_str, amount_str = row
                price = float(price_str)
                ingredient = Ingredient(ingredient_str)
                amount = int(amount_str)
                dish = Dish(dish_name, price)

                if dish in self.dishes:
                    dish_exist = next(
                        (n_dish for n_dish in self.dishes
                         if n_dish == dish), None
                    )
                    dish_exist.add_ingredient_dependency(ingredient, amount)
                else:
                    dish.add_ingredient_dependency(ingredient, amount)
                    self.dishes.add(dish)
