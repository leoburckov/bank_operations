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

# ------------------------------------
# Тесты для логов в файл
# ------------------------------------

def test_add_file():
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    result = add_file(4, 5)
    assert result == 9

    with open("test_log.txt", "r", encoding="utf-8") as f:
        content = f.read()
        assert "add_file start" in content
        assert "add_file ok" in content

def test_fail_divide_file():
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    with pytest.raises(ZeroDivisionError):
        fail_divide_file(10, 0)

    with open("test_log.txt", "r", encoding="utf-8") as f:
        content = f.read()
        assert "fail_divide_file start" in content
        assert "fail_divide_file error: ZeroDivisionError" in content
        assert "Inputs: (10, 0), {}" in content
