import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:

    # Тестирование метода get_price()
    def test_get_price_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15)
        # Проверяем, что цена соуса правильная
        assert ingredient.get_price() == 15

    # Тестирование метода get_name()
    def test_get_name_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15)
        # Проверяем, что название соуса правильное
        assert ingredient.get_name() == 'Соус традиционный галактический'

    # Параметризация теста для метода get_type()
    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Хрустящие минеральные кольца', 300, 'FILLING']
        ]
    )
    # Тестирование метода get_type()
    def test_get_type_correct_type(self, type, name, price, expected_ingredient):
        ingredient = Ingredient(type, name, price)
        # Проверяем, что тип ингредиента правильный
        assert ingredient.get_type() == expected_ingredient
