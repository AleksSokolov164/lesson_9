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

    def print_card(self): #  печатаем карточку

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





def bar_print(barrels): #функция определения бочонка и его удаления из "мешка"
    import random
    result_list = random.sample(barrels, 1)  # 15
    result = result_list[0]
    barrels.remove(result)
    barMinus = len(barrels)
    print(f"Бочонок: {result}, осталось:{barMinus} бочонков")
    return result





print('Сыграем в ЛОТО!?')
number_players = int(input('Введите количество игроков:')) #количество игроков
players_typ = [i for i in range(1,number_players+1)] # формируем непустой массив по количеству игроков
for i in range(len(players_typ)):# определяем тип игроков
    players_typ[i] = int(input(f'Введите тип {i+1}-го игрока: Компьютер -1 \ Человек-2):'))
players = []
numder_comp = 0
number_homo = 0
for i in range(len(players_typ)):
    if players_typ[i] == 1:
        numder_comp = numder_comp+1
        card_comp = Card(f'Комп-{numder_comp}', True, 1, 15) # формируем карточку комп
        players.append([players_typ[i],card_comp,numder_comp])
    else:
        number_homo = number_homo+1
        card_player = Card(f'Игрок- {number_homo}',True,1,15) #формируем карточку игрока
        players.append([players_typ[i], card_player,number_homo])

stop_win = 0

bar = 0
barrels = [i for i in range(1,91)] # формируем мешок бочонков

for k in range(1,91):
    bar = bar_print(barrels)  # Выбираем бочонок
    for i in range(len(players)):
        players[i][1].print_card() # печатаем карточки игроков
    for i in range(len(players)):
        if players[i][0] == 1:
            players[i][1].bar_minus_card(bar)# вычеркиваем если есть в карточке комп
        else:
            print(f'Вопрос игроку -{i+1}')
            players[i][1].question_player (bar) #задаем вопрос игроку и проверяем ответ? если нужно - вычеркиваем
    for i in range(len(players)):
        if  players[i][1].break_game == 0:
            stop_win = 1
            break
    if stop_win == 1:
        break
    for i in range(len(players)):
        if players[i][0] == 1 and players[i][1].win == 0:
            print(f'Выиграл компьютер - {players[i][2]}')
            stop_win = 1
            break
        elif players[i][0] == 2 and players[i][1].win == 0:
            print(f'Выиграл игрок - {players[i][2]} !')
            stop_win = 1
            break
    if stop_win == 1:
                break


# неправильное прерываение при выигрыше ВЫИГРАЛ комп 1 или выиграл комп 2  и не хватает ничья!!!

