from src.domain.repositories.task.task_repository import TaskRepository
from src.application.dtos.task.TaskCreateDTO import TaskCreateDTO


class CreateTaskHandler:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    
    async def execute(self, new_task: TaskCreateDTO) -> int:
        """Handler que crea una nueva task"""

        result: int = 0
        
        result = await self.repository.create_task(new_task)

        return result