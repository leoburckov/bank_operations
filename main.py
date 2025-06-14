#from src.masks import get_mask_card_number, get_mask_account, get_date
from processing import filter_by_state, sort_by_date, data_bank
from src import widget
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


#if __name__ == "__main__":
#    print(get_mask_card_number(input()))
#    print(get_mask_account(input()))
#    print(get_date(input()))


sorted_data = sort_by_date(data_bank)
print("----------Sorted Data----------------")
for i in range(len(sorted_data)):
    print(sorted_data[i])

print("🔹 Транзакции в USD:")
usd_gen = filter_by_currency(transactions, "USD")
for tx in usd_gen:
    print(tx)

print("\n🔹 Описания всех транзакций:")
desc_gen = transaction_descriptions(transactions)
for desc in desc_gen:
    print(desc)

print("\n🔹 Генерация номеров карт от 1 до 3:")
card_gen = card_number_generator(1, 3)
for card in card_gen:
    print(card)
