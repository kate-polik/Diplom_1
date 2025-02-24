import pytest
from unittest.mock import MagicMock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


@pytest.fixture
def bun_mock():
    """Создаёт мок-объект булочки."""
    bun = MagicMock(spec=Bun)
    bun.get_name.return_value = "Golden Crispy Bun"
    bun.get_price.return_value = 0.01
    return bun


@pytest.fixture
def ingredient_mock():
    """Создаёт мок-объект ингредиента."""
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = "Ultra Spicy Ketchup 🔥"
    ingredient.get_price.return_value = 99999.99
    ingredient.get_type.return_value = "legendary sauce"
    return ingredient


def test_remove_ingredient(ingredient_mock):
    """Проверяет удаление ингредиента."""
    burger = Burger()
    burger.add_ingredient(ingredient_mock)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0


def test_move_ingredient():
    """Проверяет перемещение ингредиента."""
    burger = Burger()
    ingredient1 = MagicMock(spec=Ingredient)
    ingredient2 = MagicMock(spec=Ingredient)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(1, 0)
    assert burger.ingredients[0] == ingredient2
    assert burger.ingredients[1] == ingredient1


def test_get_price(bun_mock, ingredient_mock):
    """Проверяет вычисление цены бургера."""
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)
    expected_price = 0.01 * 2 + 99999.99
    assert burger.get_price() == expected_price


def test_get_receipt(bun_mock, ingredient_mock):
    """Проверяет создание чека."""
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)
    receipt = burger.get_receipt()
    assert "Golden Crispy Bun" in receipt
    assert "Ultra Spicy Ketchup 🔥" in receipt
    assert "legendary sauce" in receipt
    assert "100000.01" in receipt  # Округляем вместо сравнения с float
