class Учитель:
    def __init__(self, id: int, имя: str, предмет: str):
        self.id = id
        self.имя = имя
        self.предмет = предмет

    def __str__(self):
        return f'Учитель [ID: {self.id}, Имя: {self.имя}, Предмет: {self.предмет}]'
    
class УчительСервис:
    def __init__(self):
        self.учителя = []
        self.next_id = 1  # Для автоматического назначения ID

    def добавить_учителя(self, имя: str, предмет: str) -> Учитель:
        учитель = Учитель(self.next_id, имя, предмет)
        self.учителя.append(учитель)
        self.next_id += 1
        return учитель

    def получить_учителей(self):
        return self.учителя

    def найти_учителя_по_id(self, id: int) -> Учитель:
        for учитель in self.учителя:
            if учитель.id == id:
                return учитель
        return None

    def редактировать_учителя(self, id: int, новое_имя: str, новый_предмет: str) -> bool:
        учитель = self.найти_учителя_по_id(id)
        if учитель:
            учитель.имя = новое_имя
            учитель.предмет = новый_предмет
            return True
        return False
