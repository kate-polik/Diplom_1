from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self, mocker, mock_bun):
        """Тест проверки списка булочек"""
        mocker.patch.object(Database, 'available_buns', return_value=[mock_bun])
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 1
        assert buns[0].get_name() == 'black bun'

    def test_available_ingredients(self, mocker, mock_ingredient):
        """Тест проверки списка ингредиентов"""
        mocker.patch.object(Database, 'available_ingredients', return_value=[mock_ingredient])
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 1
        assert ingredients[0].get_name() == 'hot sauce'
