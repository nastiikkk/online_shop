from abc import ABC, abstractmethod

from src.print_mixin import PrintMixin


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass


class Product(PrintMixin, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict) -> Product:
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if price < self.__price:
                answer = input(
                    "Цена меньше прошлой. "
                    " Введите y - для подтверждения, n - для отмены: "
                )
                if answer == "y":
                    self.__price = price
            else:
                self.__price = price

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float:
        if type(self) is type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError("Можно складывать только товары одного класса")
