# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def Exponentiation(firstNumber, secondNumber):
    if (secondNumber == 1):
        return firstNumber
    else:
        return (firstNumber * Exponentiation(firstNumber, secondNumber - 1))


firstNumber = int(input("Введите число: "))
secondNumber = int(input("Введите степень, в которую хотите возвести: "))
result = Exponentiation(firstNumber, secondNumber)
print(f"Число {firstNumber} в степени {secondNumber} равно: {result}")
