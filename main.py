from src.utils import read_json_file
from src.masks import get_mask_card_number, get_mask_account, get_date
from src.importers import read_transactions_from_csv, read_transactions_from_excel
from src.analytics import process_bank_search, process_bank_operations, normalize_status
from src.processing import sort_by_date, filter_by_state

AVAILABLE_STATUSES = {"EXECUTED", "CANCELED", "PENDING"}


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()

    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        data = read_json_file("data/operations.json")
    elif choice == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        data = read_transactions_from_csv("data/transactions.csv")
    elif choice == "3":
        print("Программа: Для обработки выбран Excel-файл.")
        data = read_transactions_from_excel("data/transactions_excel.xlsx")
    else:
        print("Программа: Неверный выбор. Завершение работы.")
        return

    if not data:
        print("Программа: Нет данных для обработки.")
        return

    # Фильтрация по статусу
    while True:
        status = input("\nВведите статус (EXECUTED, CANCELED, PENDING): ").strip()
        norm_status = normalize_status(status)
        if norm_status in AVAILABLE_STATUSES:
            break
        print(f'Программа: Статус операции "{status}" недоступен.')

    data = [tx for tx in data if normalize_status(tx.get("state", "")) == norm_status]
    print(f'Программа: Операции отфильтрованы по статусу "{norm_status}"')

    # Сортировка по дате
    sort_answer = input("\nОтсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_answer == "да":
        direction = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = direction != "по возрастанию"
        data = sort_by_date(data)
        if reverse:
            data = data[::-1]

    # Фильтрация по валюте
    currency_answer = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_answer == "да":
        data = filter_by_state(data)

    # Поиск по описанию
    search_answer = input("Отфильтровать по слову в описании? Да/Нет: ").strip().lower()
    if search_answer == "да":
        word = input("Введите слово для поиска в описании: ").strip()
        data = process_bank_search(data, word)

    if not data:
        print("\nПрограмма: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("\nПрограмма: Распечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(data)}\n")

    for tx in data:
        date = get_date(tx.get("date", ""))
        desc = tx.get("description", "")
        from_acc = tx.get("from", "")
        to_acc = tx.get("to", "")

        try:
            if from_acc:
                from_masked = get_mask_card_number(from_acc) if " " in from_acc else get_mask_account(from_acc)
            else:
                from_masked = ""

            if to_acc:
                to_masked = get_mask_card_number(to_acc) if " " in to_acc else get_mask_account(to_acc)
            else:
                to_masked = ""
        except ValueError:
            from_masked = from_acc
            to_masked = to_acc

        amount = tx.get("operationAmount", {}).get("amount", "")
        currency = tx.get("operationAmount", {}).get("currency", {}).get("name", "")

        print(f"{date} {desc}")
        if from_masked:
            print(f"{from_masked} -> {to_masked}")
        else:
            print(f"{to_masked}")
        print(f"Сумма: {amount} {currency}\n")

    # Подсчет категорий операций
    count_answer = input("Подсчитать количество операций по категориям? Да/Нет: ").strip().lower()
    if count_answer == "да":
        categories = list(set(tx.get("description", "") for tx in data if tx.get("description")))
        counts = process_bank_operations(data, categories)
        print("\nСтатистика по категориям операций:")
        for cat, count in counts.items():
            print(f"{cat}: {count}")


if __name__ == "__main__":
    main()
