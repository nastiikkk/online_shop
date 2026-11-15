from src.product import Product


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        new_product_list = []
        for product in self.__products:
            new_product_list.append(str(product) + "\n")
        return "".join(new_product_list)

    def __str__(self) -> str:
        amount = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {amount} шт."
