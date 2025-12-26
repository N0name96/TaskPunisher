from typing import Protocol, List, Optional

from src.domain.models.task_model import TaskModel


class TaskProtocol(Protocol):
    async def get_all_tasks(self) -> List[TaskModel]: ...

    async def get_task_by_id(self, task_id: int) -> Optional[TaskModel]: ...