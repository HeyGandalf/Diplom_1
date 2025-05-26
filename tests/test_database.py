from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDataBase:

    # Тестирование получения списка булок
    def test_get_available_buns(self):
        data_bun = Database()
        available_buns = data_bun.available_buns()
        # Проверяем, что есть 3 доступные булки
        assert len(available_buns) == 3

    # Тестирование получения списка ингредиентов
    def test_get_available_ingredients(self):
        data_ingredients = Database()
        available_ingredients = data_ingredients.available_ingredients()
        # Проверяем, что есть 6 доступных ингредиентов
        assert len(available_ingredients) == 6

    # Тестирование получения списка соусов
    def test_get_quantity_available_sauces(self):
        quantity_ingredients = Database()
        ingredients = quantity_ingredients.available_ingredients()
        type_sauce = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        # Проверяем, что есть 3 соуса
        assert len(type_sauce) == 3

    # Тестирование получения списка начинок
    def test_get_quantity_available_fillings(self):
        quantity_ingredients = Database()
        ingredients = quantity_ingredients.available_ingredients()
        type_fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        # Проверяем, что есть 3 начинки
        assert len(type_fillings) == 3

    # Тестирование получения цен на ингредиенты
    def test_get_available_ingredients_prices(self):
        data_price = Database()
        ingredients = data_price.available_ingredients()
        price = {i.get_name(): i.get_price() for i in ingredients}
        # Проверяем цену одного из ингредиентов
        assert price['hot sauce'] == 100
