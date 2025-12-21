from typing import List

from src.domain.repositories.task.task_repository import TaskRepository
from src.application.dtos.task.TaskBaseDTO import TaskBaseDTO


class GetAllTasksHandler:
    def __init__(self, repository: TaskRepository):
        self.repository = repository


    async def execute(self) -> List[TaskBaseDTO]:
        """
        Handler que obtiene todos los tasks
        :return:
        """

        list_tasks = await self.repository.get_all_tasks()
        return [TaskBaseDTO.model_validate(task) for task in list_tasks] # Realiza el mapeo de datos