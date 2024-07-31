from cities import cities_list

cities_set = {city["name"] for city in cities_list}
computer_city = None

while True:

    user_city = input("Введите город: ")

    if user_city == "стоп":
        print("Вы проиграли!")
        break
    elif user_city in cities_set:
        print("Город найден!")
    else:
        print("Город не найден!")
        print("Вы проиграли!")
        break

    if computer_city and computer_city[-1].lower() != user_city[0].lower():
        print("Вы проиграли!")
        break

    cities_set.remove(user_city)

    for city in cities_set:
        if city[0].lower() == user_city[-1]:
            computer_city = city
            print(f"Компьютер: {computer_city}")
            cities_set.remove(city)
            break
    else:
        print("вы выиграли!")
        break
