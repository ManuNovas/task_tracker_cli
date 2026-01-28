from datetime import datetime

from src.domain.entities.task_entities import Task
from src.domain.enums.task_enums import TaskStatus
from src.domain.repositories.task_repositories import TaskRepository


class TaskInputPort:
    repository: TaskRepository

    def __init__(self):
        self.repository = TaskRepository()

    def add(self, description: str):
        task = Task(
            id=self.repository.get_next_id(),
            description=description,
            status=TaskStatus.TODO,
            created_at=datetime.now(),
            updated_at=None
        )
        self.repository.add(task)
        return task
