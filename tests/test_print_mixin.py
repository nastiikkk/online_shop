from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product_print(capsys):
    Product("Продукт1", "Описание продукта", 1200, 10)

    captured = capsys.readouterr()

    assert "Создан объект Product" in captured.out
    assert "Продукт1" in captured.out
    assert "1200" in captured.out


def test_smartphone_print(capsys):
    Smartphone(
        "Iphone 15",
        "512GB",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray",
    )

    captured = capsys.readouterr()

    assert "Создан объект Smartphone" in captured.out
    assert "Iphone 15" in captured.out
    assert "210000.0" in captured.out


def test_lawn_grass_print(capsys):
    LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    captured = capsys.readouterr()

    assert "Создан объект LawnGrass" in captured.out
    assert "Газонная трава" in captured.out
    assert "500.0" in captured.out
