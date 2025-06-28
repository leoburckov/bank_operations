from utils import read_json_file


def test_read_valid_json(tmp_path) -> None:
    data = '[{"id": 1}, {"id": 2}]'
    file = tmp_path / "valid.json"
    file.write_text(data, encoding="utf-8")
    result = read_json_file(str(file))
    assert isinstance(result, list)
    assert len(result) == 2


def test_read_empty_file(tmp_path) -> None:
    file = tmp_path / "empty.json"
    file.write_text("", encoding="utf-8")
    result = read_json_file(str(file))
    assert result == []


def test_read_non_list_json(tmp_path) -> None:
    file = tmp_path / "notalist.json"
    file.write_text('{"id": 1}', encoding="utf-8")
    result = read_json_file(str(file))
    assert result == []


def test_read_file_not_found() ->None:
    result = read_json_file("non_existent.json")
    assert result == []
