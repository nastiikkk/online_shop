from unittest.mock import patch

import pytest

from src.product import Category, Product, LawnGrass, Smartphone


@pytest.fixture()
def product_and_category() -> tuple[Product, Category]:
    product_iphone = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category_phones = Category("Смартфоны", "Описание", [product_iphone])
    return product_iphone, category_phones


@pytest.fixture()
def smartphone_and_grass() -> tuple[Smartphone, LawnGrass]:
    smartphone = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space"
        )

    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
        )

    return smartphone, grass

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


def test_smartphone_init(smartphone_and_grass) -> None:
    """Тестирует корректность инициализации Smartphone"""
    
    smartphone, grass = smartphone_and_grass
    assert smartphone.name == "Iphone 15"
    assert smartphone.description == "512GB, Gray space"
    assert smartphone.price == 210000.0
    assert smartphone.quantity == 8
    assert smartphone.efficiency == 98.2
    assert smartphone.model == "15"
    assert smartphone.memory == 512
    assert smartphone.color == "Gray space"


def test_lawn_grass_init(smartphone_and_grass) -> None:
    """Тестирует корректность инициализации LawnGrass"""
    
    smartphone, grass = smartphone_and_grass
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_add_same_smartphones(smartphone_and_grass) -> None:
    """Тестирует сложение смартфонов одного класса"""

    smartphone1, grass = smartphone_and_grass
    smartphone2 = Smartphone(
        "Samsung",
        "256GB",
        100000.0,
        3,
        95.5,
        "S23",
        256,
        "Black",
    )

    assert smartphone1 + smartphone2 == 1980000.0


def test_add_same_lawn_grass(smartphone_and_grass) -> None:
    """Тестирует сложение газонной травы одного класса"""

    smartphone, grass1 = smartphone_and_grass
    grass2 = LawnGrass(
        "Газон 2",
        "Трава",
        300.0,
        3,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

    assert grass1 + grass2 == 10900.0


def test_add_different_products(smartphone_and_grass) -> None:
    """Тестирует ошибку при сложении товаров разных классов"""

    smartphone, grass = smartphone_and_grass

    with pytest.raises(TypeError):
        smartphone + grass


def test_add_smartphone_to_category(smartphone_and_grass) -> None:
    """Тестирует добавление смартфона в категорию"""

    smartphone, grass = smartphone_and_grass
    category = Category("Смартфоны", "Телефоны", [])

    category.add_product(smartphone)

    assert category.products == 'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'


def test_add_lawn_grass_to_category(smartphone_and_grass) -> None:
    """Тестирует добавление газонной травы в категорию"""

    smartphone, grass = smartphone_and_grass
    category = Category("Газон", "Газонная трава", [])

    category.add_product(grass)

    assert category.products == 'Газонная трава, 500.0 руб. Остаток: 20 шт.\n'


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
