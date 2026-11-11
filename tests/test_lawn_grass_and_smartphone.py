import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone


@pytest.fixture()
def smartphone_and_grass() -> tuple[Smartphone, LawnGrass]:
    smartphone = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )

    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    return smartphone, grass


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

    assert category.products == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"


def test_add_lawn_grass_to_category(smartphone_and_grass) -> None:
    """Тестирует добавление газонной травы в категорию"""

    smartphone, grass = smartphone_and_grass
    category = Category("Газон", "Газонная трава", [])

    category.add_product(grass)

    assert category.products == "Газонная трава, 500.0 руб. Остаток: 20 шт.\n"
