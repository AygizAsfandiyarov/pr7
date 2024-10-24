def get_decimal_number():
    try:
        decimal_number = int(input("Введите положительное целое число: "))
        if decimal_number > 0:
            return decimal_number
        else:
            print("Ошибка: пожалуйста, введите положительное целое число.")
    except ValueError:
        print("Ошибка: пожалуйста, введите целое число.")
    


def decimal_to_ternary(n):
    if n == 0:
        return ""
    return str(n % 3) + decimal_to_ternary(n // 3)
def convert_number():
    decimal_number = get_decimal_number()
    ternary = decimal_to_ternary(decimal_number)
    result = ternary
    return result

# Выполнение функции
print(convert_number())
