import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize(
    "name, price",
    [
        ("Super Crispy Bun", 0.01),  # Минимальная возможная цена
        ("Mega Soft Bun", 1000000.0),  # Гипотетически огромная цена
        ("🔥 Spicy Bun 🔥", 250.75),  # Название с эмодзи
        ("BunWithAVeryVeryVeryLongNameThatNeverEnds", 150.5),  # Очень длинное название
        ("", 50.0),  # Пустое название
    ],
)
def test_bun_initialization(name, price):
    """Тест инициализации объекта Bun"""
    bun = Bun(name, price)
    assert bun.name == name
    assert bun.price == price
    assert bun.get_name() == name
    assert bun.get_price() == price
