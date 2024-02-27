import os

from todo_list import TodoList

ABSOLUTE_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))


def get_absolute_path(relative_path: str) -> str:
    return os.path.join(ABSOLUTE_DIRECTORY_PATH, relative_path)


def main() -> None:
    todo_list = TodoList.from_json(get_absolute_path("data/todos.json"))


if __name__ == "__main__":
    main()
