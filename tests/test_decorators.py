import pytest

from src.decorators import log


@pytest.fixture
def tmp_path_log(tmp_path):
    return tmp_path


def test_log_console(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_file(tmp_path_log):
    log_file = tmp_path_log / "test_log.txt"

    @log(filename=log_file)
    def my_function(x, y):
        return x + y

    my_function(3, 4)

    with open(log_file, 'r') as file:
        content = file.read()
        assert content == "my_function ok\n"


def test_log_error(capsys):
    @log()
    def my_function(x, y):
        raise ValueError("Invalid input")

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: Invalid input. Inputs: (1, 2), {}\n"
