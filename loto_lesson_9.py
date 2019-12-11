import random

class Card():

    def __init__(self,name):
        import random
        numbers = [i for i in range(1,91)] #cписок on 1 от 90
        result = random.sample(numbers, 15) # 15 - количество случайных элементов списка из случайных чисел
        result.sort() #сортируем по возрастанию
        str_1 = result[0:5] # формируем 1 строку карточки лото из 5 первых элементов списка и 4-х " " на случайных местах
        for i in range(4):
            str_1.append(" ")
            spot = random.randint(1, len(str_1))
            for i in range(len(str_1) - 1, spot, -1):
                str_1[i], str_1[i - 1] = str_1[i - 1], str_1[i]
        str_2 = result[5:10]#формируем 2 строку карточки лото из 5 последующих элементов списка и 4-х " " на случайных местах
        for i in range(4):
            str_2.append(" ")
            spot = random.randint(1, len(str_2))
            for i in range(len(str_2) - 1, spot, -1):
                str_2[i], str_2[i - 1] = str_2[i - 1], str_2[i]
        str_3 = result[10:15] #формируем 3 строку карточки лото из 5 последующих элементов списка и 4-х " " на случайных местах
        for i in range(4):
            str_3.append(" ")
            spot = random.randint(1, len(str_3))
            for i in range(len(str_3) - 1, spot, -1):
                str_3[i], str_3[i - 1] = str_3[i - 1], str_3[i]

        self.card = [str_1,
                    str_2,
                    str_3]
        self.name = name

    def print_card(self):

        print('-'*10,self.name,'-'*(18-len(self.name)))
        [print(self.card[0][i], ' ', end='') for i in range(9)]
        print(' ')
        [print(self.card[1][i], ' ', end='') for i in range(9)]
        print(' ')
        [print(self.card[2][i], ' ', end='') for i in range(9)]
        print(' ')
        print('-' * 30)
    def bar_minus_card(self,bar):
        if bar in self.card[0]:
            str_1 = self.card[0]
            index_bar = str_1.index(bar)
            str_1.insert(index_bar, "X")
        elif bar in self.card[1]:
            str_2 = self.card[1]
            index_bar = str_2.index(bar)
            str_2.insert(index_bar, "X")
        elif bar in self.card[2]:
            str_3 = self.card[2]
            index_bar = str_3.index(bar)
            str_3.insert(index_bar, "X")
        else:
            print('Нет совпадений')


bar = 0
barrels = [i for i in range(1,91)]
def bar_print(barrels):
    import random
    result_list = random.sample(barrels, 1)  # 15
    result = result_list[0]
    barrels.remove(result)
    barMinus = len(barrels)
    print(f"Бочонок: {result}, осталось:{barMinus}")
    return result






card_player = Card('Player') #формируем карточку игрока
card_comp = Card('Comp')# формируем карточку комп

for i in range(90):
    bar = bar_print(barrels) # Выбераем бочонок
    print (bar)
    card_player.print_card() # печатаем карточку
    card_comp.print_card()# печатаем карточку
    card_player.bar_minus_card(bar)# вычеркиваем если есть
    card_comp.bar_minus_card(bar)# вычеркиваем если есть


# def card(): # формируем список из 15 случайных чисел от 1 до 90
#     import random
#     numbers = [i for i in range(1,91)] #cписок on 1 от 90
#     result = random.sample(numbers, 15) # 15 - количество случайных элементов
#     result.sort()
#     return result
#
#
#
# # n = 15
# # a = [random.randrange(1, 100) for i in range(n)]
# # a.sort()
# # print(a)
#
# # Функция декоратор
# # f - исходная фукнция
# def add_separators(f):
#     # inner - итоговая функция с новым поведение
#     def inner(*args, **kwargs):
#         # поведение до вызова
#         print('*' * 60)
#         result = f(*args, **kwargs)
#         # поведение после вызова
#         print('*' * 60)
#         return result
#
#     # возвращается функция inner с новым поведением
#     return inner
# @add_separators
# def print_card(numbers_card): # печатаем по 5 элементов списка
#     [print(numbers_card[i],' ', end='') for i in range(5)]
#     print(' ')
#     [print(numbers_card[i], ' ', end='') for i in range(5,10)]
#     print(' ')
#     [print(numbers_card[i], ' ', end='') for i in range(10,15)]
#     print(' ')
#
#
# import random
#
# numbers_card = card()
#
# print(numbers_card) #выводим список полностью
#
# print_card(numbers_card)#выводим декорированный сверху и снизу список по 5 элементов в строке
#
# # выводим случайным образом список из первых 5 элементов и 4 пробелов
#
# card_str_1 = numbers_card[0:5]+([' ']*4)
# random.shuffle(card_str_1)
# print(card_str_1)
#
# str_2 = numbers_card[5:10]
# card_str_2 = str_2+([' ']*4)
# random.shuffle(card_str_2)
# print(card_str_2)
#
# str_3 = numbers_card[10:15]
# card_str_3 = str_3+([' ']*4)
# random.shuffle(card_str_3)
# print(card_str_3)
#
# for i in range(4):
#     str_3.append(" ")
#     mesto = random.randint(1, len(str_3))
#     for i in range( len(str_3)-1,mesto,-1):
#         str_3[i],str_3[i-1]=str_3[i-1],str_3[i]
