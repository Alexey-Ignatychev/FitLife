# Проект FitLife - MVP версия 1.0
# 1. Знакомство
while True:
    user_name = str(input("Пожалуйста введите ваше имя ")).strip()
    if user_name == "" or user_name.isspace() or user_name.isdigit():
        print("Имя не может быть пустым или состоять цифр из пробелов! Пожалуйста, введите корректное имя.")
        continue
    break
while True:
    user_age = input("Пожалуйста введите ваш возраст ").strip()
    if not user_age:
        print("Возраст не может быть пустым!")
        continue
    try:
        age = int(user_age)
        if age <= 0 or age >= 123:
            print("Возраст должен быть положительным числом и не превышать 123 года!")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите число!")
# 2. Сбор данных
while True:
    user_weight = input("Пожалуйста введите ваш вес (66.6 кг) ").strip()
    if not user_weight:
        print("Вес не может быть пустым значением ")
        continue
    try:
        weight = float(user_weight)
        if weight <= 1 or weight >= 366.6:
            print("Вес должен быть положительным числом и не превышать 366.6 кг!")
            continue
        break
    except ValueError:
            print("Пожалуйста, введите число (66.6 кг)!")
while True:
    user_height = input("Пожалуйста введите ваш рост (1.66 м) ").strip()
    if not user_height:
        print("Рост не может быть пустым значением ")
        continue
    try:
        height = float(user_height)
        if weight <= 1 or height >= 366.6:
            print("Рост должен быть положительным числом и не превышать 3.6 м!")
            continue
        break
    except ValueError:
            print("Пожалуйста, введите число (1.66 м)!")
# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
bmi = (weight / (height ** 2))
okr_bmi = round(bmi, 1)
# Подсчет воды: вес * 30 мл
water_ml = weight * 30
water_l = water_ml / 1000
okr_water = round(water_l, 1)
def get_age_word(age):
    last = age % 10
    last2 = age % 100
    if last2 in range(11, 20):
        return "лет"
    elif last == 1:
        return "год"
    elif last in (2, 3, 4):
        return "года"
    else:
        return "лет"
age_word = get_age_word(age)
# 4. Вывод красивого результата
print(f"Здравствуйте {user_name}")
print(f"Отчёт для пользователя: {user_name}({user_age} {age_word})")
print(f"Ваш Индекс Массы Тела: {okr_bmi}")
print(f"Рекомендуемая норма воды: {okr_water} л в день")
print("Расчет окончен. Будьте здоровы!")
