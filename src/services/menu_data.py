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

                dish_exist = next(
                    # busca o prato no conjunto de pratos se ñ achar None
                    (n_dish for n_dish in self.dishes if n_dish == dish),
                    None
                )

                if dish_exist:
                    # se o prato já existe adiciona a dependencia de ingredient
                    dish_exist.add_ingredient_dependency(ingredient, amount)
                else:
                    dish.add_ingredient_dependency(ingredient, amount)
                    # se não adiciona o prato no conjunto de pratos
                    self.dishes.add(dish)
