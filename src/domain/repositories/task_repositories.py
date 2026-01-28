from json import load, dumps
from pathlib import Path

from src.domain.entities.task_entities import Task


class TaskRepository:
    FILE_NAME = "src/domain/repositories/task.json"
    ENCODING = "utf-8"
    data: list[Task]

    def __init__(self):
        path = Path(self.FILE_NAME)
        if not path.exists():
            path.write_text("[]", encoding=self.ENCODING)

    def get_data(self):
        with open(self.FILE_NAME, "r", encoding=self.ENCODING) as file:
            self.data = load(file)

    def save_data(self):
        with open(self.FILE_NAME, "w", encoding=self.ENCODING) as file:
            file.write(dumps(self.data))

    def get_next_id(self) -> int:
        self.get_data()
        return len(self.data) + 1

    def add(self, task: Task):
        self.get_data()
        self.data.append(task.to_json())
        self.save_data()
