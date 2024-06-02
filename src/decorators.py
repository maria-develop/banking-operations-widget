from typing import Any


def log(filename: Any = None) -> Any:
    """Функция логирует вызов функции и ее результат в файл или в консоль"""

    def decorator(func: Any) -> Any:
        def wrapper(*args: Any, **kwargs: dict) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                result = None
                message = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}"

            if filename:
                with open(filename, "a") as file:
                    file.write(message + "\n")
            else:
                print(message)

            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
