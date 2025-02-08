import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import patch


@pytest.fixture
def mock_buns():
    """Мокает список булочек с нужными значениями."""
    return [
        Bun("Void Bun", 0),
        Bun("Diamond Bun", 999999),
        Bun("Ultra Thin Air Bun", 0.01)
    ]


@pytest.fixture
def mock_ingredients():
    """Мокает список ингредиентов с нужными значениями."""
    return [
        Ingredient(INGREDIENT_TYPE_SAUCE, "Ghost Pepper Sauce 🌶️", 0.99),
        Ingredient(INGREDIENT_TYPE_SAUCE, "Lava Sauce 🔥", 50000),
        Ingredient(INGREDIENT_TYPE_SAUCE, "Quantum Foam Sauce", 0),
        Ingredient(INGREDIENT_TYPE_FILLING, "Gold-Leaf Steak 🥩", 999999.99),
        Ingredient(INGREDIENT_TYPE_FILLING, "Air", 0.01),
        Ingredient(INGREDIENT_TYPE_FILLING, "Mega Meat Tower", 1)
    ]


@pytest.fixture
def database():
    """Создает экземпляр базы данных для тестов."""
    return Database()


def test_database_content_structure(database, mock_buns, mock_ingredients):
    """Проверяет структуру и содержимое базы данных."""
    with patch.object(database, 'available_buns', return_value=mock_buns), \
            patch.object(database, 'available_ingredients', return_value=mock_ingredients):
        # Проверка булочек
        buns = database.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)

        # Проверка характеристик каждой булочки
        bun_data = [(bun.get_name(), bun.get_price()) for bun in buns]
        expected_bun_data = [
            ("Void Bun", 0),
            ("Diamond Bun", 999999),
            ("Ultra Thin Air Bun", 0.01)
        ]
        assert all(data in bun_data for data in expected_bun_data)

        # Проверка ингредиентов
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

        # Проверка характеристик каждого ингредиента
        ingredient_data = [
            (ingredient.get_type(), ingredient.get_name(), ingredient.get_price())
            for ingredient in ingredients
        ]
        expected_ingredient_data = [
            (INGREDIENT_TYPE_SAUCE, "Ghost Pepper Sauce 🌶️", 0.99),
            (INGREDIENT_TYPE_SAUCE, "Lava Sauce 🔥", 50000),
            (INGREDIENT_TYPE_SAUCE, "Quantum Foam Sauce", 0),
            (INGREDIENT_TYPE_FILLING, "Gold-Leaf Steak 🥩", 999999.99),
            (INGREDIENT_TYPE_FILLING, "Air", 0.01),
            (INGREDIENT_TYPE_FILLING, "Mega Meat Tower", 1)
        ]
        assert all(data in ingredient_data for data in expected_ingredient_data)