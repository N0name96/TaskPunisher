import { effect, inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map } from 'rxjs';

import { Task } from '../models/task';
import { ResponseModel } from '../../../models/ResponseModel.model';
import { environment } from '../../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class TaskService {
  private apiUrl = environment.apiUrl

  private readonly http = inject(HttpClient)

  constructor(){
    effect(()=>{
      this.http
      console.log("componente")
    })
  }


  // Create a trask
  createTask(task: Partial<Task>): Observable<string>{
    return this.http.post<ResponseModel<null>>(
      `${this.apiUrl}/task/create_task/`,
      task
    )
    .pipe(map(res => res.message))
  }


  // Obtain all tasks
  getAllTasks(): Observable<Task[]> {
    return this.http.get<ResponseModel<Task[]>>(
      `${this.apiUrl}/task/read_tasks/`
    )
    .pipe(map(res => res.response || []))
  }


  // Filter task
  getTaskById(id: Number): Observable<Task | null> {
    return this.http.get<ResponseModel<Task>>(
      `${this.apiUrl}/task/read_task_by_id/${id}`
    )
    .pipe(map(res => res.response || null)) // extract only the object task from ResponseModel
    
  }


  // Update task
  updateTask(id: Number, task: Partial<Task>): Observable<string>{
    return this.http.put<ResponseModel<null>>(
      `${this.apiUrl}/task/update_task/${id}/`,
      task
    )
    .pipe(map(res => res.message))
  }


  // Update task to false
  updateTaskToFalse(): Observable<string>{
    return this.http.put<ResponseModel<null>>(
      `${this.apiUrl}/task/update_tasks_false/`,
      null
    )
    .pipe(map(res => res.message))
  }


  // Delete task
  deleteTask(id: number): Observable<string>{
    return this.http.delete<ResponseModel<null>>(
      `${this.apiUrl}/task/delete_task/${id}`
    )
    .pipe(map(res => res.message))
  }
}
