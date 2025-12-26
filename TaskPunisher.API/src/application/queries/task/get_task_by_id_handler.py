from typing import List, Optional

from src.domain.models import TaskModel
from src.domain.protocols.task_protocol import TaskProtocol


class GetTaskByIdHandler:
    def __init__(self, protocol: TaskProtocol):
        self.protocol = protocol


    async def get_task_by_id(self, id: int) -> Optional[TaskModel]:
        """Handler que hace la llamada al repositorio para obtener una tarea filtrada"""
        task = await self.protocol.get_task_by_id(id)

        if not task:
            return None

        return task