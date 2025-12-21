from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.task.task_entity import Tasks


class TaskRepository(ABC):
    @abstractmethod
    async def get_all_tasks(self) -> List[Tasks]:
        """Define el contrato para obtener todas las tareas"""
        raise NotImplementedError

    @abstractmethod
    async def get_task_by_id(self, task_id: int) -> Tasks:
        """Define el contrato para obtner una tarea filtrado por id"""
        raise NotImplementedError