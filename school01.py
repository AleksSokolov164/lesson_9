"""
Прогфрамма "Школа"
В школе есть школьники
У шеольгтков есть родители
У группы есть номер и название например 3пк3
"""
class Group:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self._students = []

    def add (self, students):
        self._students.append(students)
    def count (self):
        return len(self._students)
    def __str__(self):
        return f'{self.name}{self.number} количество человек в группе:{len(self)}'
    def __len__(self):
        return len(self._students)

if __name__ == '__main__':

    leo = 'Leo'
    max = 'Max'
    kate = 'Kate'

    group = Group('A',11)
    group.add(leo)
    group.add(kate)

    group_one = Group('B',10)
    group_one.add(max)
    print(group_one)
    print(group)
    print(group.name, group.number)
    print(group._students)
    print(len(group_one._students))
    print(group.count())

    # наслдеование, инкапсуляция, полиморфизм, абстракция
    # Утиная типизация

    print(len(group))
