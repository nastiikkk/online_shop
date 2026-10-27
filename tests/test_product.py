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


def test_init_category(classes: tuple[Product, Category]) -> None:
    """Тестирует корректность инициализации объекта Category"""
    product_iphone, category_phones = classes
    assert category_phones.name == "Смартфоны"
    assert category_phones.description == "Описание"
    assert category_phones.products == [product_iphone]


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
