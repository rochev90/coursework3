import json
import datetime
from operator import itemgetter


def load_operations_json(file_path):
    """Читает json и возвращает список словарей"""

    with open(file_path, 'r', encoding='utf-8') as file:
        temp_file = json.load(file)

        list_operations = []
        for f in temp_file:  # если в списке есть пустой словарь
            if f == {}:
                continue
            else:
                list_operations.append(f)
        return list_operations


def sorted_operations(list_operations):
    """Сортирует операции и возвращает отсортированный список"""

    sort_date = sorted(list_operations, key=itemgetter('date'), reverse=True)
    sort_operations = sorted(sort_date, key=itemgetter('state'), reverse=True)
    return sort_operations


def get_date(i):
    """Возвращает дату в нужном виде"""
    date_time_str = i['date']
    date_time_obj = datetime.datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%S.%f")
    date = date_time_obj.date().strftime('%d.%m.%Y')
    return date


def hide_number_from(card_number_from):
    """Маскирует номер карты отправителя"""
    hide_number_from_ = card_number_from[0:4] + " " + card_number_from[4:6] + '*' * len(
        card_number_from[6:-4]) + card_number_from[-4:]
    return hide_number_from_


def hide_number_to(card_number_to):
    """Маскирует номер карты получателя"""
    hide_number_to_ = '*' * len(card_number_to[-6:-4]) + card_number_to[-4:]
    return hide_number_to_

def get_feedback(i, date):
    """"Генерирует сообщение с информацией об операциях"""
    print(f"{date} {i['description']}")
    if 'from' not in i:
        card = i['to'].split()
        card_number_to = card[-1]
        number_to = hide_number_to(card_number_to)
        print(f" > {' '.join(card[0:-1])} {number_to}")
    else:
        card = i['to'].split()
        card_number_to = card[-1]
        number_to = hide_number_to(card_number_to)
        card_ = i['from'].split()
        card_number_from = card_[-1]
        number_from = hide_number_from(card_number_from)
        print(f"{' '.join(card_[:-1])} {number_from} > {' '.join(card[:-1])} {number_to}")

    print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
    print(" ")


