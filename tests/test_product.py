from unittest.mock import patch

import pytest

from src.category import Category
from src.product import BaseProduct, Product


@pytest.fixture()
def product_and_category() -> tuple[Product, Category]:
    product_iphone = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category_phones = Category("Смартфоны", "Описание", [product_iphone])
    return product_iphone, category_phones


def test_init_product(product_and_category) -> None:
    """Тестирует корректность инициализации объекта Product"""

    product_iphone, category_phones = product_and_category
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_new_product() -> None:
    result = Product.new_product(
        {"name": "Samsung", "description": "Описание", "price": 180000.0, "quantity": 5}
    )
    assert isinstance(result, Product)
    assert result.name == "Samsung"
    assert result.description == "Описание"
    assert result.price == 180000.0
    assert result.quantity == 5


def test_price(product_and_category) -> None:
    product_iphone, category_phones = product_and_category

    product_iphone.price = 300000.0
    assert product_iphone.price == 300000.0

    with patch("builtins.input", return_value="y"):
        product_iphone.price = 20000.0
    assert product_iphone.price == 20000.0

    with patch("builtins.input", return_value="n"):
        product_iphone.price = 5000.0
    assert product_iphone.price == 20000.0

    product_iphone.price = -100.0
    assert product_iphone.price == 20000.0

    product_iphone.price = 0.0
    assert product_iphone.price == 20000.0


def test_str_product(product_and_category) -> None:
    product_iphone, category_phones = product_and_category

    result = str(product_iphone)

    assert result == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_add_products() -> None:
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    result = product1 + product2

    assert result == 2580000.0


def test_add_products_with_zero_quantity() -> None:
    product1 = Product("Samsung", "Описание", 1000.0, 0)
    product2 = Product("Iphone", "Описание", 2000.0, 2)

    assert product1 + product2 == 4000.0


def test_add_products_with_invalid_type() -> None:
    product = Product("Samsung", "Описание", 1000.0, 2)

    with pytest.raises(TypeError):
        product.__add__(5)


def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct()
