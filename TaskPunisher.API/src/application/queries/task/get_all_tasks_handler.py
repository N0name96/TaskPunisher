from typing import List

from src.domain.protocols.task_protocol import TaskProtocol
from src.domain.models.task_model import TaskModel

class GetAllTasksHandler:
    def __init__(self, protocol: TaskProtocol):
        self.protocol = protocol

    async def get_all_tasks(self) -> List[TaskModel]:
        """Handler que llama al repositorio para obtener todas las tareas"""
        return await self.protocol.get_all_tasks()