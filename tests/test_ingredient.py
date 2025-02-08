import pytest
from praktikum.ingredient import Ingredient


@pytest.mark.parametrize(
    "ingredient_type, name, price",
    [
        ("SAUCE", "Ghost Pepper Sauce 🌶️", 0.99),  # Минимальная цена соуса
        ("FILLING", "Gold-Leaf Steak 🥩", 999999.99),  # Очень дорогая начинка
        ("SAUCE", "Quantum Foam Sauce", 0),  # Нулевая цена
        ("FILLING", "Air", 0.01),  # Почти нулевая цена
        ("SAUCE", "Lava Sauce 🔥", 50000),  # Высокая цена соуса
        ("FILLING", "Mega Meat Tower", 1),  # Минимальная возможная цена начинки
    ],
)
def test_ingredient_creation(ingredient_type, name, price):
    """Проверяет корректное создание объекта Ingredient и его свойств."""
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.get_type() == ingredient_type, "Тип ингредиента не совпадает"
    assert ingredient.get_name() == name, "Имя ингредиента не совпадает"
    assert ingredient.get_price() == price, "Цена ингредиента не совпадает"
