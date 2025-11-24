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

  public dataSignal: WritableSignal<TaskModel[]> = signal([])

  private readonly http = inject(HttpClient)

  async getTasks(): Promise<ResponseModel<TaskModel[]>> {
    const response = await fetch(`${this.apiUrl}/task/read_tasks/`)

    if (!response.ok) {
      throw new Error(`Error ${response.status}: No se pudo obtener el usuario`)
    }
    
    console.log(response.json())
    return response.json()
  }

  // getTasks() {
  //   return this.http
  //     .get<ResponseModel<TaskModel[]>> (
  //       `${this.apiUrl}/task/read_tasks/`
  //     )
  //     .subscribe(res => {
  //       this.dataSignal.set(res.response || [])
  //     })
  // }


  // deleteTask(id: number) {
  //   return this.http
  //     .delete<string> (
  //       `${this.apiUrl}/task/delete_task/${id}`
  //     )
  //     .subscribe(() => {
  //       this.dataSignal.set(
  //         this.dataSignal().filter(task => task.id !== id)
  //       )
  //     })
  // }
}
