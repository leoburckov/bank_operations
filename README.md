
## Описание
 Программа - на Python для банковского приложения.
 Программа вводит список словарей, фильтрует по введенному
 (или заранее установленному ключу), и сортирует по дате.
  Кроме того есть временно неиспользуемые модули маскировки номера счета или карты.
## Установка

1. Клонируйте репозиторий.
```
git clone https://github.com/VladimirMykalo883/projeckts2.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
``` 
## Использование:
" Пока не совсем понял где и как применять."

## Документация:
"Документация будет заполнятся в процессе..."


## 📥 Импорт транзакций (`importers.py`)

Модуль `src/importers.py` позволяет загружать транзакции из файлов:


from importers import read_transactions_from_csv, read_transactions_from_excel

csv_data = read_transactions_from_csv("data/transactions.csv")
xlsx_data = read_transactions_from_excel("data/transactions_excel.xlsx")

## Новый модуль generators

Модуль содержит генераторы для обработки транзакций:

### filter_by_currency
Фильтрует транзакции по валюте.
```python
from bank_operations.generators import filter_by_currency

transactions = [...]  # список транзакций
for tx in filter_by_currency(transactions, "USD"):
    print(tx)



