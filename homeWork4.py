# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2, 3, 5, 9, 3]
# print(my_list)
# sum = 0
# for i in range(len(my_list)):
#     if i%2 != 0:
#         sum += my_list[i]
# print(sum)




# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]


# size = int(input('Write a size of list'))
# my_list = []
# for i in range(size):
#     my_list.append(i)
# print(*my_list)
# count = 0
# steps = 0
# new_list = []
# for i in range(len(my_list)):
#     count = int(my_list[0+i] * my_list[-1-i])
#     steps += 1
#     new_list.append(count)
#     if steps >= len(my_list)/2:
#         break
# print(new_list)



# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random, random

# size = int(input("Write a size of list: "))
#
# my_list = []
# for i in range(size):
#     i = random.uniform(0, 10000)
#     my_list.append(round(i, 2))
# print(*my_list)
# new_list = []
# desim = 0
# for i in range(len(my_list)):
#     desim = my_list[i]-int(my_list[i])
#     new_list.append(round(desim, 2))
# print(*new_list)
# max_desim_number = max(new_list)
# print(max_desim_number)
# min_desim_number = min(new_list)
# print(min_desim_number)
# result = max_desim_number - min_desim_number
# print(f'Difference between maximal and minimal fractional parts of elements is {round(result, 2)}')





# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# number = int(input('Write a number: '))
# double_num = []
# div = 0
# while number > 0:
#     div = number % 2
#     double_num.append(div)
#     number //= 2
# print(*double_num[::-1])


  # SECOND OPTION

# number = int(input('Write a number: '))
# double_num = ''
# while number > 0:
#     double_num = str(number % 2) + double_num
#     number //= 2
# print(double_num)




# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# n = int(input("Write a size of list: "))
# fib_array = []
# for i in range(n):
#     if i == 0:
#         fib_array[i] = 0
#         fib_array.append(fib_array[i])
#     if i == 1:
#         fib_array[i] = 1
#         fib_array.append(fib_array[i])
#     else:
#         fib_array[i] = fib_array[i - 1] + fib_array[i - 2]
#         fib_array.append(fib_array[i])
# for i in range(-n, 0):
#     if i == 0:
#         fib_array[i] = 0
#         fib_array.insert(fib_array[i])
#     if i == 1:
#         fib_array[i] = 1
#         fib_array.insert(fib_array[i])
#     else:
#         fib_array[i] = fib_array[i - 1] - fib_array[i - 2]
#         fib_array.insert(fib_array[i])
# print(fib_array)



# OTHER OPTION
# f1 = 0
# f2 = 1
# print(f1, f2, end=' ')
# for i in range(-n, 0):
#     f1, f2 = f2, f1 - f2
#     print(f2, end=' ')
# fib1 = fib2 = 1
# print(fib1, fib2, end=' ')
#
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')


# BOTH OF OPTIONS DOESN'T WORK, BUT I WROTE HOW I UNDERSTAND. SORRY(((((
