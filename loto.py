from lotoClass_lesson9 import Card

import random


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
players = [] # список игроков, запись - [тип игрока 1 или 2, Карточка(класс -к ней применимы методы), номер игрока по типу]
numder_comp = 0
number_homo = 0
for i in range(len(players_typ)):
    if players_typ[i] == 1:
        numder_comp = numder_comp+1
        card_comp = Card(f'Комп-{numder_comp}', True, 1, 15) # формируем карточку комп
        players.append([players_typ[i],card_comp,numder_comp])
    else:
        number_homo = number_homo+1
        card_player = Card(f'Игрок-{number_homo}',True,1,15) #формируем карточку игрока
        players.append([players_typ[i], card_player,number_homo])


stop_win = 0

bar = 0
barrels = [i for i in range(1,91)] # формируем мешок бочонков

for k in range(1,91):
    bar = bar_print(barrels)  # Выбираем бочонок
    for i in range(len(players)):
        print(players[i][1]) # печатаем карточки игроков
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


#  не хватает ничья!!!
