class SomeClass:
    """
    Популярные магические методы
    """

    def __str__(self):
        """
        Приведение объекта с строке
        """
        pass

    def __len__(self):
        """
        Длина объекта фукнция len
        """
        pass

    def __getitem__(self, item):
        """
        Получение значения по индексу, например a[2]
        :param item: индекс
        """
        pass

    def __init__(self, name, number):
        """
        Создание объекта класса
        """
        pass

    def __eq__(self, other):
        """
        сравнение объектов
        """
        pass

    def __contains__(self, item):
        """
        проверка на вхождение in
        """
        pass

    def __add__(self, other):
        """
        Сложение объектов
        """
        pass

    def __gt__(self, other):
        """
        Больше a > b
        """

    def __ge__(self, other):
        """
        Больше равно a >= b
        :param other:
        :return:
        """
        pass

    def __lt__(self, other):
        """
        Меньше a < b
        """
        pass