from unittest.mock import patch

import pytest

from src.product import Category, Product


@pytest.fixture()
def classes() -> tuple[Product, Category]:
    product_iphone = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category_phones = Category("Смартфоны", "Описание", [product_iphone])
    return product_iphone, category_phones


def test_init_product(classes: tuple[Product, Category]) -> None:
    """Тестирует корректность инициализации объекта Product"""
    product_iphone, category_phones = classes
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


def test_price(classes: tuple[Product, Category]) -> None:
    product_iphone, category_phones = classes

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


def test_init_category(classes: tuple[Product, Category]) -> None:
    """Тестирует корректность инициализации объекта Category"""
    product_iphone, category_phones = classes
    assert category_phones.name == "Смартфоны"
    assert category_phones.description == "Описание"
    assert category_phones.products == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"


def test_category_count() -> None:
    """Тестирует увеличение счётчика при создании категории"""
    initial_count = Category.category_count

    Category("Смартфоны", "Описание", [])

    assert Category.category_count == initial_count + 1


def test_product_count() -> None:
    """Тестирует увеличение счётчика на количество товаров в категории"""
    initial_count = Category.product_count

    product1 = Product("Iphone 15", "Описание", 100000.0, 5)
    product2 = Product("Samsung", "Описание", 80000.0, 3)

    Category("Смартфоны", "Описание", [product1, product2])

    assert Category.product_count == initial_count + 2


def test_add_product(classes: tuple[Product, Category]) -> None:
    product_iphone, category_phones = classes
    initial_products = category_phones.products
    initial_count = Category.product_count

    product_samsung = Product("Samsung", "Описание", 180000.0, 5)
    category_phones.add_product(product_samsung)

    assert category_phones.products != initial_products
    assert product_samsung.name in category_phones.products
    assert Category.product_count == initial_count + 1
