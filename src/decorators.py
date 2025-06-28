import functools
import sys


def log(filename=None):
    """
    Декоратор для логирования начала и конца выполнения функции, её результатов или ошибок.

    :param filename: путь к файлу для логов (по умолчанию None — вывод в консоль)
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Определяем поток вывода
            output = sys.stdout
            file_handle = None
            if filename:
                file_handle = open(filename, "a", encoding="utf-8")
                output = file_handle

            try:
                # Логируем начало
                print(f"{func.__name__} start", file=output)

                # Выполняем функцию
                result = func(*args, **kwargs)

                # Логируем успешное завершение
                print(f"{func.__name__} ok", file=output)

                if file_handle:
                    file_handle.close()

                return result

            except Exception as e:
                # Логируем ошибку
                print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}", file=output)
                if file_handle:
                    file_handle.close()
                raise

        return wrapper

    return decorator
