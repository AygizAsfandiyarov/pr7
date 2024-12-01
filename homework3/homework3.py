def get_decimal_number():
    try:
        decimal_number = int(input("Введите положительное целое число: "))
        if decimal_number > 0:
            return decimal_number
        else:
            print("Ошибка: пожалуйста, введите положительное целое число.")
    except ValueError:
        print("Ошибка: пожалуйста, введите целое число.")

def decimal_to_ternary(decimal_number):
    if decimal_number == 0:
        return "0"
    
    ternary_number = ""
    while decimal_number > 0:
        ternary_number = str(decimal_number % 3) + ternary_number
        decimal_number //= 3
    
    return ternary_number

def convert_number():
    decimal_number = get_decimal_number()
    ternary = decimal_to_ternary(decimal_number)
    result = ternary
    return result

print(convert_number())

