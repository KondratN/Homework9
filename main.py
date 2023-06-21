# Написать функцию для определения, является ли введённое число палиндромом.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def isPalindrome(someNumber):
#     if someNumber == someNumber[::-1]:
#         print('Число является палиндромом')
#     else:
#         print('Число не является палиндромом')
#
#
# someNumber = input("Введите число: \n")
# isPalindrome(someNumber)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Написать функцию, которая находит самую длинную подстроку, которая является префиксом среди массива строк.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def subString(someArray):
#     sub = ''
#     sub1 = []
#     index = 1
#     index1 = 0
#     while index < len(someArray):
#         while index1 < len(someArray[index]):
#             if someArray[index - 1][index1] == someArray[index][index1]:
#                 sub += someArray[index][index1]
#             else:
#                 sub.replace(someArray[index - 1][index1], '')
#                 break
#             index1 += 1
#         sub1.append(sub)
#         index += 1
#         index1 = 0
#     index = 1
#     while index < len(sub1):
#         sub = sub1[0]
#         if len(sub) > len(sub1[index - 1]):
#             sub = sub1[index - 1]
#         index += 1
#     return sub
#
#
# someArray = ["Полис", "Полиндром", 'Полимер']
# print(subString(someArray))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Написать функцию, которая определяет, правильно ли в строке расставлены скобки.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def isCorrect(someString):
#     count = 0
#     count1 = 0
#     index = 0
#     if someString.count('(') == someString.count(')'):
#         print('Строка с верным количеством скобок')
#         while index < len(someString):
#             if '(' in someString[index]:
#                 count += 1
#             elif ')' in someString[index]:
#                 count1 += 1
#             index += 1
#             if count1 - count >= 1:
#                 print('В строке неверно расставлены скобки')
#                 break
#         if count1 - count == 0:
#             print('В строке верно расставлены скобки')
#     else:
#         print('Строка с неверным количеством скобок')
#         print(someString.count('('), someString.count(')'))
#
#
# isCorrect('asd(ыавыф))ав)ыа((пва(вапы)выапвыа)пва(вапывыапвыа')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# someArray = ["Понис", "Полиндром", 'Полимер']
# sub = ''
# sub1 = []
# index = 1
# index1 = 0
# while index < len(someArray):
#     while index1 < len(someArray[index]):
#         if someArray[index - 1][index1] == someArray[index][index1]:
#             sub += someArray[index][index1]
#         else:
#             sub.replace(someArray[index - 1][index1], '')
#             break
#         index1 += 1
#     sub1.append(sub)
#     index += 1
#     index1 = 0
# index = 1
# while index < len(sub1):
#     sub = sub1[0]
#     if len(sub) > len(sub1[index - 1]):
#         sub = sub1[index - 1]
#     index += 1
# return sub