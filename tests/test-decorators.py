import os
import pytest
from decorators import log

# ------------------------------------
# Функции с декоратором для тестов
# ------------------------------------

@log()
def add(a, b):
    return a + b

@log()
def fail_divide(a, b):
    return a / b

@log("test_log.txt")
def add_file(a, b):
    return a + b

@log("test_log.txt")
def fail_divide_file(a, b):
    return a / b

# ------------------------------------
# Тесты для логов в консоли
# ------------------------------------

def test_add_console(capsys):
    result = add(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "add start" in captured.out
    assert "add ok" in captured.out

def test_fail_divide_console(capsys):
    with pytest.raises(ZeroDivisionError):
        fail_divide(1, 0)
    captured = capsys.readouterr()
    assert "fail_divide start" in captured.out
    assert "fail_divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out



