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
    
    def update(self, id: int, description: str):
        task = self.repository.find_by_id(id)
        if task is None:
            return None
        task.set_description(description)
        self.repository.update(task)
        return task

    def delete(self, id: int):
        task = self.repository.find_by_id(id)
        if task is None:
            return None
        self.repository.delete(task)
        return task
