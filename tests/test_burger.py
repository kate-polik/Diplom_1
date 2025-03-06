from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient(self, burger, mock_ingredient, mocker):
        mock_ingredient_2 = mocker.Mock(spec=Ingredient)
        mock_ingredient_2.get_name.return_value = 'cutlet'
        mock_ingredient_2.get_price.return_value = 100
        mock_ingredient_2.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient

    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == mock_bun.get_price() * 2 + mock_ingredient.get_price()

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert f'(==== {mock_bun.get_name()} ====)' in receipt
        assert f'= {str(mock_ingredient.get_type()).lower()} {mock_ingredient.get_name()} =' in receipt
        assert f'Price: {burger.get_price()}' in receipt