class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
     """
     Метод доступа на чтение
    :return: age
     """
     return self.name+' - '+str(self.age)

    def set_age(self, new_age):
        """
        Метод для записи возраста
        :param new_age:
        :return:
        """
        if new_age < 0:
            raise ValueError('Возраст не может быть отрицательными')
        self._age = new_age


class B:
    def __private(self):
        print("Это приватный метод!")

    def _private(self):
        print("Это приватный метод!")


if __name__ == '__main__':
    max = Person('Max', 20)

    print(max.get_age())

    max.set_age(10)

    print(max.get_age())

    # Возраст не может быть отрицательным, будет Exception
    # max.set_age(-10)

    print(max.get_age())

