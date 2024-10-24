number = input("Введите целое десятичное число: ")

if number.lstrip('-').isdigit():
    number = int(number)
    if number >= 0:
        binary = bin(number)[2:]
        octal = oct(number)[2:]
    else:
        binary = '-' + bin(abs(number))[2:]
        octal = '-' + oct(abs(number))[2:]
    print(f"Двоичное представление: {binary}")
    print(f"Восьмеричное представление: {octal}")
else:
    print("Ошибка: введите корректное целое число.")