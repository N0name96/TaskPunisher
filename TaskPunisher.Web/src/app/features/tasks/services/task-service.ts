import { inject, Injectable, signal, WritableSignal } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '../../../../environments/environment';
import { TaskModel } from '../models/task-model';
import { ResponseModel } from '../../../models/ResponseModel.model';

@Injectable({
  providedIn: 'root',
})
export class TaskService {
  
  private apiUrl = environment.apiUrl
  private readonly http = inject(HttpClient)

  
  async getTasks(): Promise<TaskModel[]> {
    try {
      const response = await fetch(`${this.apiUrl}/task/read_tasks/`)
      if (!response.ok) {
        throw new Error(`Error ${response.status}: No se pudo obtener las tareas`)
      }
      const result = await response.json()
      if(!result.response){
        throw new Error('Respuesta invalida del servidor')
      }
      return result.response
    }
    catch (err: unknown) {
      console.error('Error obteniendo tareas:', err);
      throw err instanceof Error ? err : new Error('Error a la hora de obtener las tareas');
    }
  }


  async deleteTask(id: number): Promise<void> {
    try {
      const response = await fetch(
        `${this.apiUrl}/task/delete_task/${id}`,
        { method:'DELETE' }
      )
      if (!response.ok) {
        throw new Error(`Error ${response.status}: No se pudo realizar el borrado de la tarea`)
      }
    }
    catch (err: unknown) {
      console.error('Error a la hora de llamar al borraDo de tareas:', err);
      throw err instanceof Error ? err : new Error('Error a la hora llamar al borrado de tareas');
    }
  }
}
