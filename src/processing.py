def filter_by_state(card_details: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
       Функция, которая принимает на вход список словарей и значение для ключа state
    (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение
    """
    if len(card_details) == 0:
        raise ValueError("Выгрузите данные корректно")

    filtered_card_details = []

    for detail in card_details:
        if detail["state"] == state:
            filtered_card_details.append(detail)
        else:
            pass

    return filtered_card_details


def sorted_by_date(data: list[dict], ascending: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате.
    """
    sorted_list = sorted(data, key=lambda item: item["date"], reverse=ascending)
    return sorted_list


# if __name__ == "__main__":
#     print(
#         filter_by_state(
#             [
#                 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#                 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#                 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#                 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#             ],
#             "CANCELED",
#         )
#     )
#     print(
#         filter_by_state(
#             [
#                 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#                 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#                 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#                 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#             ]
#         )
#     )
#
#     Выход функции со статусом по умолчанию EXECUTED
#     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    #
    # Выход функции, если вторым аргументов передано 'CANCELED'
    # [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    #  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    # Пример использования
    # print(
    #     sorted_by_date(
    #         [
    #             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    #             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    #             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    #             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    #         ]
    #     )
    # )
    # print(
    #     sorted_by_date(
    #         [
    #             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    #             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    #             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    #             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    #         ],
    #         False,
    #     )
    # )
    # Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
    # [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    #  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    #  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    #  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
