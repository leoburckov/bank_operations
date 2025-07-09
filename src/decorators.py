import functools
import sys
from typing import Any, Callable, Optional, TypeVar, cast

# Общий тип для декорируемых функций
F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор для логирования начала и конца выполнения функции, её результатов или ошибок.

    :param filename: путь к файлу для логов (по умолчанию None — вывод в консоль)
    :return: декоратор
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            output = sys.stdout
            file_handle = None

            if filename:
                file_handle = open(filename, "a", encoding="utf-8")
                output = file_handle

            try:
                print(f"{func.__name__} start", file=output)
                result = func(*args, **kwargs)
                print(f"{func.__name__} ok", file=output)

                if file_handle:
                    file_handle.close()

                return result

            except Exception as e:
                print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}", file=output)
                if file_handle:
                    file_handle.close()
                raise

        return cast(F, wrapper)

    return decorator
