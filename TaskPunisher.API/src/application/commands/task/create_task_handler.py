from src.domain.repositories.task.task_repository import TaskRepository
from src.application.dtos.Task.TaskCreateDTO import TaskCreateDTO


class CreateTaskHandler:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    
    async def execute(self, new_task: TaskCreateDTO) -> bool:
        """Handler que crea una nueva task"""

        result = await self.repository.create_task(new_task)
        return result