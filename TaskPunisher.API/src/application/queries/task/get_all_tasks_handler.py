from typing import List

from src.domain.repositories.task.task_repository import TaskRepository
from src.application.dtos import TaskBaseDTO


class GetAllTasksHandler:
    def __init__(self, repository: TaskRepository):
        self.repository = repository


    async def execute(self) -> List[TaskBaseDTO]:
        """
        Handler que obtiene todos los tasks
        :return:
        """

        return await self.repository.get_all_tasks()