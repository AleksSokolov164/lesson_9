ООП - процедурное программирование

# процедурное программирование - программа из некоторых действий
# ООП - программа состоит из оъектов и классов (данные + действие)

# В реальной жизни все состоит из объектов

# ООП
# . 1. Класс - семейство объектов (Кошка)
# . 2. Свойства - характеристики сеймества объектов (Порода, Кол во лап, Цвет, Возраст, Длина хвоста)
# 3. Методы - действия которые могут делать кошки (Кусаться, Царапать, Ходить, Спать, ...)
# 4. Объект - конкретная Кошка "Муся" свойства (Сиамсая, 4 лапы, серый, 3, 30см)
class NotEnoughMoney(Exception):

    def __str__(self):
        return 'Не хватает денег на счете'



class Bill:

    def __init__(self):
        self.money = 0
        self.history = []

    def add(self, count):
        """
        Добавить деньги на счет
        :param count:
        :return:
        """
        self.money += count

    def can_by(self, count):
        return count <= self.money

    def buy(self, count, name):
        """
        Покупка
        :param count:
        :param name:
        :return:
        """
        if self.can_by(count):
            # снимаем деньги
            self.money -= count
            self.history.append((name, count))
        else:
            raise NotEnoughMoney()
            # print('Денег недостаточно')


class SavingBill(Bill):

    def can_by(self, count):
        return False

    def buy(self, count, name):
        raise Exception('Нельзя снимать с накопительного счета')