import random

def number():
    import random
    numbers = [i for i in range(100)]
    # 2 - количество случайных элементов
    result = random.sample(numbers, 15)
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
def print_card():
    numbers_card = number()
    [print(numbers_card[i],' ', end='') for i in range(5)]
    print(' ')
    [print(numbers_card[i], ' ', end='') for i in range(5,10)]
    print(' ')
    [print(numbers_card[i], ' ', end='') for i in range(10,15)]
    print(' ')


number()
print_card()