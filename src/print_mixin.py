class PrintMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект {self!r}")

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"('{self.name}', '{self.description}', "
            f"{self.price}, {self.quantity})"
        )
