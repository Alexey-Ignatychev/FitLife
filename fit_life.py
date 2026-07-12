# Проект FitLife - MVP версия 1.0
# 1. Знакомство
user_name = input("Пожалуйста введите ваше имя ")
user_age = int(input("Пожалуйста введите ваш возраст "))
# 2. Сбор данных
user_weight = float(input("Пожалуйста введите ваш вес (66.6кг) "))
user_height = float(input("Пожалуйста введите ваш рост (1.66м) "))
# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
bmi = (user_weight / (user_height ** 2))
okr_bmi = round(bmi, 1)
# Подсчет воды: вес * 30 мл
water_ml = user_weight * 30
water_l = water_ml / 1000
okr_water = round(water_l, 1)
# 4. Вывод красивого результата
print(f"Здравствуйте {user_name}")
print(f"Отчёт для пользователя: {user_name}({user_age} лет/года)")
print(f"Ваш Индекс Массы Тела: {okr_bmi}")
print(f"Рекомендуемая норма воды: {okr_water}л. в день")
print("Расчет окончен. Будьте здоровы!")
