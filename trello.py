import sys
import requests

auth_params = {
    'key' : "e13de85337f1a1e2753fc720a4669e35",
    'token':"96cc80bb44c9f2dd184c2ad5718569d1136695fea955c204c8b965e3f723ad15"
}

# Адрес, на котором расположен API Trello, # Именно туда мы будем отправлять HTTP запросы.
base_url = "https://api.trello.com/1/{}"

board_id = "ScA4JaQk"

def read():
    #получим данные всех колонок на доске
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()

    #теперь выведем название каждой колонки ивсех заданий, которые к ней относятся
    for column in column_data:
        print(column['name'])
        #получим данные всех задачи и перечислим все названия
        task_data = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()
        if not task_data:
            print('\t' + 'Нет задач')
            continue
        for task in task_data:
            print('\t' + task['name'])

def create(name, column_name):
    #получим данные всех колонок на доске
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()

    #переберем данные о всех колонках, пока не найдем ту которая нужна
    for column in column_data:
        if column['name'] == column_name:
            #создадим задачу с именем '_name_' в найденной колонке
            requests.post(base_url.format('cards'), data={'name':name, 'idList':column['id'], **auth_params})
            break

if __name__ == "__main__":
    if len(sys.argv)<=2:
        read()
    else:
        create(sys.argv[2], sys.argv[3])