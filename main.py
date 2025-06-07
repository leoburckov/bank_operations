from src.masks import get_mask_card_number, get_mask_account, get_date
from processing import filter_by_state, sort_by_date, data_bank
from src import widget


if __name__ == "__main__":
    print(get_mask_card_number(input()))
    print(get_mask_account(input()))
    print(get_date(input()))


sorted_data = sort_by_date(data_bank)
print("----------Sorted Data----------------")
for i in range(len(sorted_data)):
    print(sorted_data[i])

#state_key = input("Введите значение state")
#if not state_key.isalpha():
   # state_key = "EXECUTED"
# переходим в модуль processing.py с возможностью поменять ключ фильтрации

#filtered_operations = filter_by_state(operations_list, state:= state_key)

#sorted_operations = sort_by_date(filtered_operations)

#for operation in sorted_operations:
 #   print(operation)
