# Задание 1
grades = {"Анна": 5, "Иван": 4, "Мария": 5}
print("Задание 1:", grades["Иван"])

# Задание 2
d = {"a": 1, "b": 2}
d["c"] = 3
d["a"] = 10
del d["b"]
print("Задание 2:", d)

# Задание 3
d = {"name": "Alex", "age": 18}
key = input("Задание 3. Введите ключ: ")
if key in d:
    print(d[key])
else:
    print("Нет такого ключа")

# Задание 4
d = {"x": 1, "y": 2, "z": 3}
print("Задание 4. Ключи:", list(d.keys()))
print("Значения:", list(d.values()))
print("Количество пар:", len(d))

# Задание 5
products = {"хлеб": 50, "молоко": 80, "сыр": 300}
print("Задание 5:")
for product, price in products.items():
    print(product, "-", price)

# Задание 6
total_sum = sum(products.values())
most_expensive = max(products, key=products.get)
print("Задание 6. Сумма:", total_sum, "| Самый дорогой:", most_expensive)

# Задание 7
text = "привет"
char_counts = {}
for char in text:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1
print("Задание 7:", char_counts)

# Задание 8
text = "яблоко груша яблоко банан яблоко"
words = text.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
most_common = max(word_counts, key=word_counts.get)
print("Задание 8:", word_counts, "| Самое частое:", most_common)

# Задание 9
old_dict = {"a": 1, "b": 2}
new_dict = {}
for key, value in old_dict.items():
    new_dict[value] = key
print("Задание 9:", new_dict)

# Задание 10
countries = ["Россия", "Франция", "Япония"]
capitals = ["Москва", "Париж", "Токио"]
country_dict = {}
for i in range(len(countries)):
    country_dict[countries[i]] = capitals[i]

user_country = input("Задание 10. Введите страну: ")
if user_country in country_dict:
    print("Столица:", country_dict[user_country])
else:
    print("Страна не найдена")