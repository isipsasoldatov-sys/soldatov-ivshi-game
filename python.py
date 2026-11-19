import random

print("цикл for")

# Задание 1
print("Задание 1:", end=" ")
for i in range(1, 11):
    print(i, end=" ")
print()

# Задание 2
print("Задание 2:", end=" ")
for i in range(2, 51, 2):
    print(i, end=" ")
print()

# Задание 3
print("Задание 3:", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Задание 4
n = int(input("Задание 4. Введите n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Сумма:", total)

# Задание 5
n = int(input("Задание 5. Введите n: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Факториал:", factorial)

# Задание 6
n = int(input("Задание 6. Введите n: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")

# Задание 7
numbers = [-5, 3, 0, -2, 8, 10, -1]
positive_count = 0
for num in numbers:
    if num > 0:
        positive_count += 1
print("Задание 7. Положительных чисел:", positive_count)

# Задание 8
text = "программирование"
vowels = "аеёиоуыэюя"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print("Задание 8. Гласных:", vowel_count)

# Задание 9
numbers = [5, 12, 3, 45, 8]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Задание 9. Максимум:", maximum)

# Задание 10
print("Задание 10:")
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print()


#вторая часть
print("\n цикл while")

# Задание 1
print("Задание 1:", end=" ")
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

# Задание 2
print("Задание 2:")
total = 0
while True:
    num = int(input("Введите число (0 для выхода): "))
    if num == 0:
        break
    total += num
print("Сумма:", total)

# Задание 3
n = int(input("Задание 3. Введите число: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Количество цифр:", count)

# Задание 4
n = int(input("Задание 4. Введите число: "))
sum_digits = 0
while n > 0:
    sum_digits += n % 10
    n //= 10
print("Сумма цифр:", sum_digits)

# Задание 5
n = int(input("Задание 5. Введите число: "))
reversed_num = 0
while n > 0:
    reversed_num = reversed_num * 10 + n % 10
    n //= 10
print("Перевернутое число:", reversed_num)

# Задание 6
n = int(input("Задание 6. Введите n: "))
power = 1
while power <= n:
    print(power, end=" ")
    power *= 2
print()

# Задание 7
print("Задание 7:")
password = ""
while password != "1234":
    password = input("Введите пароль: ")
print("Пароль верный!")

# Задание 8
a = int(input("Задание 8. Введите первое число: "))
b = int(input("Введите второе число: "))
# Алгоритм Евклида
while b != 0:
    a, b = b, a % b
print("НОД:", a)

# Задание 9
n = int(input("Задание 9. Введите n: "))
a, b = 0, 1
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
print()

# Задание 10
print("Задание 10. Угадайте число от 1 до 100.")
secret_number = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Ваш вариант: "))
    attempts += 1
    if guess < secret_number:
        print("Больше")
    elif guess > secret_number:
        print("Меньше")
    else:
        print(f"Угадали! Попыток: {attempts}")
        break