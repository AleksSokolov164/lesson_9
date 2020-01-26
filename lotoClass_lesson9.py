import random

class Card():

    def __init__(self,name,yes_no, break_game, win):
        import random
        numbers = [i for i in range(1,91)] #cписок on 1 от 90
        result = random.sample(numbers, 15) # 15 случайных чисел  из  списка numbers
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

        self.card = [str_1, # карточка
                    str_2,
                    str_3]
        self.name = name # имя - тип игрока
        self.yes_no = yes_no
        self.break_game = break_game
        self.win = win #  индикатор победы - у кого он первым станет = 0 вместо 15 (т.е. -1 при каждом вычеркивании) тот и победил


    def print_card(self): #  "печатаем" карточку на экран

        print('-'*10,self.name,'-'*(18-len(self.name)))
        [print(self.card[0][i], ' ', end='') for i in range(9)]
        print(' ')
        [print(self.card[1][i], ' ', end='') for i in range(9)]
        print(' ')
        [print(self.card[2][i], ' ', end='') for i in range(9)]
        print(' ')
        print('-' * 30)

    def bar_yes_no(self,bar): # фиксируем есть ли выпавший номер на карточке игрока
        if bar in self.card[0] or bar in self.card[1] or bar in self.card[2]:
            self.yes_no = True
        else:
            self.yes_no = False


    def bar_minus_card(self,bar): # в карточке заменяем выпавшее число на Х
        if bar in self.card[0]:
            str_1 = self.card[0]
            index_bar = str_1.index(bar)
            str_1.insert(index_bar, "X")
            str_1.remove(bar)
            self.card[0] = str_1
            self.win = self.win - 1
        elif bar in self.card[1]:
            str_2 = self.card[1]
            index_bar = str_2.index(bar)
            str_2.insert(index_bar, "X")
            str_2.remove(bar)
            self.card[1] = str_2
            self.win = self.win - 1
        elif bar in self.card[2]:
            str_3 = self.card[2]
            index_bar = str_3.index(bar)
            str_3.insert(index_bar, "X")
            str_3.remove(bar)
            self.card[2] = str_3
            self.win = self.win - 1

    def question_player (self,bar): # предлагаем ПРОДОЛЖИТЬ или ЗАЧЕКНУТЬ и фиксируем выбор.
        # в зависимости от правильности определяем ВЫИГРАЛ или ПРОИГРАЛ
        print('Посмотрите на свою карточку. Нужно ли вычеркнуть выпавший номер или нет? ')
        print('1. зачеркнуть')
        print('2. продолжить')
        choice = input('Ваш выбор (1 или 2):')
        self.bar_yes_no(bar)  # фиксируем есть ли номер на карточке игрока

        if choice == '1':
            if self.yes_no == False:
                print('Вы проиграли!')
                self.break_game = 0
            else:
                self.bar_minus_card(bar)  # вычеркиваем если есть
                self.break_game = 1

        elif choice == '2':
            if self.yes_no == True:
                print('Вы проиграли!')
                self.break_game = 0
            else:
                self.break_game = 1
        else:
            print('Неверный пункт меню')

