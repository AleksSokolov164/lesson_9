import random

def card(): # формируем список из 15 случайных чисел от 1 до 100
    import random
    numbers = [i for i in range(1,101)] #cписок on 1 от 100
    result = random.sample(numbers, 15) # 15 - количество случайных элементов
    result.sort()
    return result



# n = 15
# a = [random.randrange(1, 100) for i in range(n)]
# a.sort()
# print(a)

# Функция декоратор
# f - исходная фукнция
def add_separators(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('*' * 60)
        result = f(*args, **kwargs)
        # поведение после вызова
        print('*' * 60)
        return result

    # возвращается функция inner с новым поведением
    return inner
@add_separators
def print_card(numbers_card): # печатаем по 5 элементов списка
    [print(numbers_card[i],' ', end='') for i in range(5)]
    print(' ')
    [print(numbers_card[i], ' ', end='') for i in range(5,10)]
    print(' ')
    [print(numbers_card[i], ' ', end='') for i in range(10,15)]
    print(' ')


import random

numbers_card = card()

print(numbers_card) #выводим список полностью

print_card(numbers_card)#выводим декорированный сверху и снизу список по 5 элементов в строке

# выводим случайным образом список из первых 5 элементов и 4 пробелов
str_1 = numbers_card[0:5]
card_str_1 = str_1+([' ']*4)
random.shuffle(card_str_1)
print(card_str_1)

str_2 = numbers_card[5:10]
card_str_2 = str_2+([' ']*4)
random.shuffle(card_str_2)
print(card_str_2)

str_3 = numbers_card[10:15]
card_str_3 = str_3+([' ']*4)
random.shuffle(card_str_3)
print(card_str_3)