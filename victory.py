again = 'да'
while again == 'да':
    right: int = 0
    wrong: int = 0

    query1 = input("Год рождения Ленин В.И.: ")  # год рождения 1870
    if query1 == "1870":
        print("Верно")
        right += 1
    else:
        print("Ошибка")
        wrong += 1


    query2 = input("Год рождения Сталина И.В.: ") # год рождения 1879
    if query2 == "1879":
        print("Верно")
        right += 1
    else:
        print("Ошибка")
        wrong += 1

    query3 = input("Год рождения Брежнева Л.И.: ") # год рождения 1906
    if query3 == "1906":
        print("Верно")
        right += 1
    else:
        print("Ошибка")
        wrong += 1


    query4 = input("Год рождения Ельцин Б.Н.: ") # год рождения 1931
    if query4 == "1931":
        print("Верно")
        right += 1
    else:
        print("Ошибка")
        wrong += 1

    query5 = input("Год рождения Путина В.В.: ") # год рождения 1952
    if query5 == "1952":
        print("Верно")
        right += 1
    else:
        print("Ошибка")
        wrong += 1

    print("Верно", right)
    print("Ошибок", wrong)
    print("Верно", right * 100 / 5, "%")
    print("Ошибок", wrong * 100 / 5, "%")

    again = input("Хотите ли начать игру сначала? ")  # да/нет