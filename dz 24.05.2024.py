user_age_groups = {
    "Олександр": "18-24",
    "Марія": "25-34",
    "Іван": "35-44",
    "Наталя": "45-54",
    "Андрій": "55-64",
}

user_name = input("Олександр ")

if user_name in user_age_groups:
    print(f"{user_name} належить до вікової групи {user_age_groups[user_name]}.")
else:
    print(f"Ім'я {user_name} не знайдено у словнику.")