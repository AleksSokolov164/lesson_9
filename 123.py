import random
print(type(1))
numbers = [i for i in range(1,91)] #cписок on 1 от 90
result = random.sample(numbers, 15) # 15 - количество случайных элементов
result.sort()
card_str_1 = result[0:5] + ([' '] * 4)
random.shuffle(card_str_1)
print(card_str_1)
card_str_2 = result[5:10]+ ([' '] * 4)
random.shuffle(card_str_2)
print(card_str_2)
card_str_3 = result[10:15]+ (['  '] * 4)
random.shuffle(card_str_3)
card_str_3 = sorted([ i  for i in card_str_3 if type(i)== int])
print(card_str_3)
