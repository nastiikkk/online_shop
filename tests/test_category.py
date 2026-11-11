import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product_and_category() -> tuple[Product, Category]:
    product_iphone = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category_phones = Category("Смартфоны", "Описание", [product_iphone])
    return product_iphone, category_phones


def test_add_not_product_to_category() -> None:
    """Тестирует ошибку при добавлении не продукта в категорию"""

    category = Category("Смартфоны", "Телефоны", [])

    with pytest.raises(TypeError):
        category.add_product("Можно добавлять только продукты")


def test_init_category(product_and_category) -> None:
    """Тестирует корректность инициализации объекта Category"""
    product_iphone, category_phones = product_and_category
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


def test_add_product(product_and_category) -> None:
    product_iphone, category_phones = product_and_category
    initial_products = category_phones.products
    initial_count = Category.product_count

    product_samsung = Product("Samsung", "Описание", 180000.0, 5)
    category_phones.add_product(product_samsung)

    assert category_phones.products != initial_products
    assert product_samsung.name in category_phones.products
    assert Category.product_count == initial_count + 1


def test_str_category() -> None:
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )

    assert str(category1) == "Смартфоны, количество продуктов: 13 шт."


def test_str_empty_category() -> None:
    category = Category("Пустая категория", "Описание", [])

    assert str(category) == "Пустая категория, количество продуктов: 0 шт."
