def reshenie():
    try:
        a = int(input("Введите целое значение a: "))
        b = int(input("Введите целое значение b: "))
        c = int(input("Введите целое значение c: "))
        x = a * b + 4 * c
#Вывод результата
        print(f"Результат {x}")
    except ValueError:
        print("Ошибка: пожалуйста, введите целое число")
reshenie()