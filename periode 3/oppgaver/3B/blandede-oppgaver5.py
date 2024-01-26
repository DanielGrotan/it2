import json
import os
from collections import defaultdict

from pydantic import BaseModel, Field

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def get_absolute_path(relative_path: str) -> str:
    return os.path.join(ROOT_PATH, relative_path)


class Todo(BaseModel):
    user_id: int = Field(alias="userId")
    id: int
    title: str
    completed: bool

    def __str__(self) -> str:
        return f"Id: {self.id}, User Id: {self.user_id}, Title: {self.title}, Completed: {self.completed}"


def print_todos(todos: list[Todo]) -> None:
    print("Todos:")
    print(*todos, sep="\n")


def print_uncompleted_todos(todos: list[Todo]) -> None:
    print("Uferdige todos:")

    is_todo_uncompleted = lambda todo: todo.completed is False

    print(*filter(is_todo_uncompleted, todos), sep="\n")


def print_most_active_user(todos: list[Todo]) -> None:
    todos_completed_count = defaultdict(lambda: 0)

    for todo in todos:
        if not todo.completed:
            continue

        todos_completed_count[todo.user_id] += 1

    user_id, most_completions = max(
        todos_completed_count.items(), key=lambda item: item[1]
    )

    print(
        f"Brukeren med id = {user_id} har gjort flest todos. Hen har gjort {most_completions} todos"
    )


def print_least_active_user(todos: list[Todo]) -> None:
    todos_completed_count = defaultdict(lambda: 0)

    for todo in todos:
        if not todo.completed:
            continue

        todos_completed_count[todo.user_id] += 1

    user_id, most_completions = min(
        todos_completed_count.items(), key=lambda item: item[1]
    )

    print(
        f"Brukeren med id = {user_id} har gjort færrest todos. Hen har gjort {most_completions} todos"
    )


def main() -> None:
    with open(get_absolute_path("datafiler/todos.json")) as f:
        todos = json.load(f)

    todos = [Todo(**todo) for todo in todos]

    print_todos(todos)
    print()
    print_uncompleted_todos(todos)
    print()
    print_most_active_user(todos)
    print()
    print_least_active_user(todos)


if __name__ == "__main__":
    main()
