'''
map
map () преобразует элементы;
'''

rus_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и']
use = list(map(lambda x: x + '1', rus_letters))
print(use)

numbers = [1, 2, 3, 4, 5]
string_numbers = list(map(str, numbers))
print(string_numbers)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, list1, list2))
sums2= list(map(lambda x, y, z: f'{x} + {y} = {z}', list1, list2, sums))
sums3= list(map(lambda x, y: f'{x} + {y} = {x+y}', list1, list2))
print(sums2)
print(sums3)

phrases = ['  hello ', ' world ', ' python  ']
cleaned_phrases = list(map(str.strip, phrases))
print(cleaned_phrases)


'''
filter
filter () отбирает элементы;
'''

numbers = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)


def is_not_even(x):
   return x % 2 == 1
elements = [1, 2, 3, 4, 5, 6]
built = list(filter(is_not_even, elements))
print(built)


'''
reduce
reduce () сводит коллекцию к одному значению, комбинируя элементы
'''

from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)




# создаём список натуральных чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# фильтруем чётные числа
filtered_numbers = filter(lambda x: x % 2 == 0, numbers)

# удваиваем каждое отфильтрованное число
doubled_numbers = map(lambda x: x * 2, filtered_numbers)

# суммируем все удвоенные числа
sum_of_numbers = reduce(lambda x, y: x + y, doubled_numbers)

# выводим результат
print(sum_of_numbers)