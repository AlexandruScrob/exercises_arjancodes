from __future__ import annotations

from typing import Protocol

from model import Model


class View(Protocol):
    def create_ui(self, presenter: Presenter) -> None:
        ...

    def clear_entry(self) -> None:
        ...

    def get_entry_text(self) -> str:
        ...

    def update_task_list(self, tasts: list[str]) -> None:
        ...

    def mainloop() -> None:
        ...


class Presenter:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def handle_add_task(self, event=None) -> None:
        task = self.view.get_entry_text()
        self.view.clear_entry()
        self.model.add_task(task)
        self.update_task_list()

    def handle_delete_task(self, event=None) -> None:
        self.model.delete_task(self.view.selected_task)
        self.update_task_list()

    def update_task_list(self) -> None:
        tasks = self.model.get_tasks()
        self.view.update_task_list(tasks)

    def run(self) -> None:
        self.view.create_ui(self)
        self.update_task_list()
        self.view.mainloop()
