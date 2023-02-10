# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def Summ(firstNumber, secondNumber):
    if firstNumber == 0:
        return secondNumber
    return Summ(firstNumber - 1, secondNumber + 1)


firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите второе число: "))
result = Summ(firstNumber, secondNumber)
print(f"Сумма чисел {firstNumber} и {secondNumber} равна: {result}")
