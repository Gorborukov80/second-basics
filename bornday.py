# Спросить у пользователя год рождения А.С Пушкина
age = int(input('Введите год рождения А.С. Пушкина: '))

if age == 1799:
    print('Верно')
    birthday = int(input('Введите день рождения: '))
    if birthday == 26:
        print('верный день рождения')

    else:
        print('Не верный день рождения')
else:
    print('Неверный год рождения')