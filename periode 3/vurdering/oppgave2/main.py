import json
import os
from collections import defaultdict

from matplotlib import pyplot as plt
from todo import Todo

ABSOLUTE_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))


def get_absolute_path(relative_path: str) -> str:
    return os.path.join(ABSOLUTE_DIRECTORY_PATH, relative_path)


def task2() -> list[Todo]:
    with open(get_absolute_path("test_data.json"), encoding="utf-8") as f:
        todos = json.load(f)
    
    seen_todo_ids = set()
    mapped_todos = []

    for todo in todos:
        todo_id = todo.get("id")

        if todo_id in seen_todo_ids:
            continue
    
        seen_todo_ids.add(todo_id)
        mapped_todos.append(Todo(**todo))

    return mapped_todos


def task3(todos: list[Todo]) -> None:
    unique_users = set()
    total_tasks = 0
    completed_tasks = 0

    for todo in todos:
        unique_users.add(todo.user_id)
        total_tasks += 1

        completed_tasks += 1 if todo.completed else 0

    print("\nOppgave 3:")

    print(
        f"Det jobber {len(unique_users)} brukere på prosjektet. Prosjektet har totalt {total_tasks} oppgaver og {completed_tasks} av dem har blitt gjort."
    )

def task4(todos: list[Todo]) -> None:
    completed_todo_ids = []
    incomplete_todo_ids = []

    for todo in todos:
        if todo.completed:
            completed_todo_ids.append(todo.id)
            continue

        incomplete_todo_ids.append(todo.id)

    print("\nOppgave 4:")
    
    print(f"Fullførte oppgaver (oppgave id-er): {", ".join(map(str, completed_todo_ids))}")
    print(f"Oppgaver som ikke er fullførte (oppgave id-er): {", ".join(map(str, incomplete_todo_ids))}")

def task5(todos: list[Todo]) -> None:
    tasks_completed_count = defaultdict(lambda: 0)

    for todo in todos:
        tasks_completed_count[todo.user_id] += 1 if todo.completed else 0
    
    user_id, completed_todos = max(tasks_completed_count.items(), key=lambda pair: pair[1])

    print("\nOppgave 5:")

    print(f"Brukeren med id = {user_id} har løst flest oppgaver. Hen har løst {completed_todos} oppgaver")

def task6(todos: list[Todo]) -> None:
    total_todos = len(todos)
    completed_todos = 0
    incomplete_todos = 0

    for todo in todos:
        if todo.completed:
            completed_todos += 1
            continue

        incomplete_todos += 1
    
    _, (bar_ax, pie_ax) = plt.subplots(1, 2, figsize=(15, 9))
    
    bar_ax.bar(["Fullførte oppgaver", "Ikke fullførte oppgaver"], [completed_todos, incomplete_todos])
    pie_ax.pie(
        [completed_todos, incomplete_todos], 
        labels=[
            f"Fullførte oppgaver ({completed_todos / total_todos * 100:.2f}%)", 
            f"Ikke fullførte oppgaver ({incomplete_todos / total_todos * 100:.2f}%)"
        ]
    )

    plt.suptitle("Fordeling av oppgaver som er fullført eller ikke")

    plt.savefig(get_absolute_path("task6.png"))

def task7(todos: list[Todo]) -> None:
    total_completed_todos = sum(todo.completed for todo in todos)
    tasks_completed_count = defaultdict(lambda: 0)

    for todo in todos:
        tasks_completed_count[todo.user_id] += 1 if todo.completed else 0
    
    _, (bar_ax, pie_ax) = plt.subplots(1, 2, figsize=(15, 9))

    bar_ax.bar(tasks_completed_count.keys(), tasks_completed_count.values())

    labels = [f"Bruker {user_id} ({todos_completed / total_completed_todos * 100:.2f}%)" for user_id, todos_completed in tasks_completed_count.items()]

    pie_ax.pie(tasks_completed_count.values(), labels=labels)

    plt.suptitle("Fordeling av løste oppgaver på brukere")

    plt.savefig(get_absolute_path("task7.png"))


def main() -> None:
    todos = task2()

    task3(todos)
    task4(todos)
    task5(todos)
    task6(todos)
    task7(todos)


if __name__ == "__main__":
    main()
