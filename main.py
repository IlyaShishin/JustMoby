# Создадим нашему персонажу рюкзак, где он будет хранить свои вещи и монеты
backpack_dict = {
    'items': ['Меч', 'Карта'],
    'coins': 0
}


# Функция, определяющая действия в комнате Таверна
def action_inside_tavern():
    """
    Список действий:
      1 - Поговорить с бродягой
      2 - Осмотреть окрестности
    """
    print(action_inside_tavern.__doc__)
    command_list = []
    while True:
        user_command = input('Выберите номер действия - ')
        if user_command == '1':
            # Делаем проверку, чтобы персонаж смог забрать вещи бродяги только 1 раз
            if user_command not in command_list:
                command_list.append(user_command)
                print(
                    'Вы: “Жизнь или смерть, грязный бродяга!“\n'
                    'Бродяга: “Вот возьми всё что у меня есть, только не трогай меня“.\n'
                    'Список действий:\n'
                    '1 - Забрать всё что у него есть\n'
                    '2 - Оставить бродягу в покое'
                )
                user_command = input('Выберите номер действия - ')

                if user_command == '1':
                    coins = backpack_dict['coins']
                    coins = coins + 50
                    backpack_dict['coins'] = coins
                    items = backpack_dict['items']
                    items.append('Медальон')
                    backpack_dict['items'] = items
                    print(
                        'Бродяга: “Я теперь умру с голоду!“\n'
                        f"Теперь у вас {backpack_dict['coins']} монет и вы получили {backpack_dict['items'][-1]}"
                        f'{action_inside_tavern.__doc__}'
                    )

                elif user_command == '2':
                    print('“Бродяга всадил Вам нож в спину как только Вы отвернулись”')
                    break

            else:
                print(
                    'Бродяга: “У меня больше ничего нет”'
                    f'{action_inside_tavern.__doc__}'
                )

        elif user_command == '2':
            print(
                'Вы осмотрели таверну, вокруг грязь и разлитый на полу эль. В углу вы видете бродягу.'
                f'{action_inside_tavern.__doc__}'
            )

        else:
            print('Такого действия нет, выберите действие из списка')


def room_selection():
    """
    Функция определяет номер комнаты для дальнейших действий.
    """
    print(
        'Список комнат для посещения:\n'
        '1 - Таверна'
    )
    while True:
        user_command = input('Выберите номер комнаты, которую вы хотите посетить - ')
        if user_command == '1':
            action = action_inside_tavern()
            return action
        else:
            print('Такой комнаты нет, выберите действие из списка')


if __name__ == '__main__':
    room_selection()
