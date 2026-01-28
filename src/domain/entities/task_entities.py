from datetime import datetime

from src.domain.enums.task_enums import TaskStatus


class Task:
    id: int
    description: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime | None

    def __init__(self, id: int, description: str, status: TaskStatus, created_at: datetime,
                 updated_at: datetime | None):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
    
    def set_updated_at(self):
        self.updated_at = datetime.now()
    
    def set_description(self, description):
        self.description = description
        self.set_updated_at()
