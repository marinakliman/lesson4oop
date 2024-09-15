class Учитель:
    def __init__(self, id: int, имя: str, предмет: str):
        self.id = id
        self.имя = имя
        self.предмет = предмет

    def __str__(self):
        return f'Учитель [ID: {self.id}, Имя: {self.имя}, Предмет: {self.предмет}]'