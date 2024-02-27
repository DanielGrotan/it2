import json
from typing import Generator, Optional, Self

from todo import Todo


class TodoList:
    def __init__(self, todos: list[Todo]) -> None:
        self.__todos = todos

    @classmethod
    def from_json(cls, filepath: str, encoding: str = "utf-8") -> Self:
        with open(filepath, encoding=encoding) as f:
            todos = json.load(f)

        if not isinstance(todos, list):
            raise ValueError("Invalid JSON file. File should contain a list of objects")

        seen_todo_ids = set()
        mapped_todos = []

        for todo in todos:
            todo_id = todo.get("id")

            if todo_id in seen_todo_ids:
                continue

            seen_todo_ids.add(todo_id)
            mapped_todos.append(Todo(**todo))

        return cls(mapped_todos)

    def get_todos(
        self, user_id_filter: Optional[int] = None, only_completed: bool = False
    ) -> Generator[Todo, None, None]:
        for todo in self.__todos:
            if user_id_filter is not None and todo.id != user_id_filter:
                continue

            if only_completed and not todo.completed:
                continue

            yield todo
