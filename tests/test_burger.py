import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    # Тестирование метода set_buns()
    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Name_bun', 100.0)
        burger.set_buns(bun)
        # Проверяем, что булка установлена правильно
        assert burger.bun == bun

    # Тестирование метода add_ingredient()
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Name_bun'
        mock_ingredient.get_price.return_value = 9.0
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        # Проверяем, что добавленный ингредиент имеет правильные данные
        assert burger.ingredients[0].get_price() == 9.0
        assert burger.ingredients[0].get_name() == 'Name_bun'
        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_FILLING

    # Тестирование метода remove_ingredient()
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        # Проверяем, что ингредиент был удалён и список ингредиентов пуст
        assert len(burger.ingredients) == 0

    # Параметризация теста для проверки метода get_price()
    @pytest.mark.parametrize(
        "bun_index, ingredients, expected_price",
        [
            (0, [], 100.0 * 2),  # без ингредиентов, только булка
            (0, [0], 100.0 * 2 + 100),  # булка + один ингредиент
        ]
    )
    def test_get_price(self, bun_index, ingredients, expected_price):
        burger = Burger()
        bun = Database().available_buns()[bun_index]
        burger.set_buns(bun)

        for ingredient_index in ingredients:
            ingredient = Database().available_ingredients()[ingredient_index]
            burger.add_ingredient(ingredient)

        # Проверяем, что цена бургера соответствует ожиданиям
        assert burger.get_price() == expected_price

    # Тестирование метода get_receipt()
    def test_get_receipt(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 400"
        )

        # Проверяем, что чек соответствует ожидаемому
        assert expected_receipt.strip() == burger.get_receipt().strip()

    # Параметризация теста для проверки метода move_ingredient()
    @pytest.mark.parametrize(
        'initial_index, new_index, expected_order',
        [
            (0, 1, [1, 0]),  # mock_1 -> pos 1
            (1, 0, [1, 0]),  # mock_2 -> pos 0
            (0, 0, [0, 1]),  # no change
        ]
    )
    # Тестирование метода move_ingredient()
    def test_move_ingredient(self, initial_index, new_index, expected_order):
        burger = Burger()

        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = 'Ingredient1'
        mock_ingredient1.get_price.return_value = 100
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE

        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = 'Ingredient2'
        mock_ingredient2.get_price.return_value = 200
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.move_ingredient(initial_index, new_index)

        # Проверяем, что ингредиенты перемещены в правильном порядке
        assert burger.ingredients[expected_order[0]] == mock_ingredient1
        assert burger.ingredients[expected_order[1]] == mock_ingredient2
