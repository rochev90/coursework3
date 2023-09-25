import pytest
from src.utils import load_operations_json, hide_number_from, hide_number_to, sorted_operations, get_date, \
     get_feedback
import os.path

test_json_path = os.path.join('data', 'test_operations.json')


@pytest.fixture
def data():
    expected_data = [{"id": 736942989,
                      "state": "EXECUTED",
                      "date": "2019-09-06T00:48:01.081967",
                      "operationAmount": {
                          "amount": "6357.56",
                          "currency": {
                              "name": "USD",
                              "code": "USD"
                          }
                      },
                      "description": "Перевод организации",
                      "from": "Visa Gold 3654412434951162",
                      "to": "Счет 59986621134048778289"
                      },
                     {
                         "id": 580054042,
                         "state": "EXECUTED",
                         "date": "2018-06-20T03:59:34.851630",
                         "operationAmount": {
                             "amount": "96350.51",
                             "currency": {
                                 "name": "USD",
                                 "code": "USD"
                             }
                         },
                         "description": "Перевод с карты на счет",
                         "from": "МИР 3766446452238784",
                         "to": "Счет 86655182730188443980"
                     }
                     ]
    return expected_data


def test_load_operations_json(data):
    actual_data = load_operations_json(test_json_path)
    assert actual_data == data
    assert isinstance(actual_data, list)


def test_hide_number_from():
    card_number_from = '1111110000003333'
    expected = '1111 11******3333'
    assert hide_number_from(card_number_from) == expected


def test_hide_number_to():
    input_data = '11111111111111110000'
    expected = '**0000'
    assert hide_number_to(input_data) == expected


def test_sorted_operations(data):
    assert sorted_operations(data)


def test_get_date():
    test_date = {"date": "2018-09-27T14:26:24.629306"}
    assert get_date(test_date) == '27.09.2018'


@pytest.fixture
def data_feedback():
    expected_data = {"id": 736942989,
                      "state": "EXECUTED",
                      "date": "2019-09-06T00:48:01.081967",
                      "operationAmount": {
                          "amount": "6357.56",
                          "currency": {
                              "name": "USD",
                              "code": "USD"
                          }
                      },
                      "description": "Перевод организации",
                      "from": "Visa Gold 3654412434951162",
                      "to": "Счет 59986621134048778289"
                      }
    return expected_data


def test_get_feedback(data_feedback):
    test_date = '06.09.2019'
    assert get_feedback(data_feedback, test_date) is None