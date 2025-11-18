import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map } from 'rxjs';

import { Task } from '../../shared/models/task.model';
import { ResponseModel } from '../../shared/models/ResponseModel.model';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class TaskService {
  private apiUrl = environment.apiUrl


  constructor(private http: HttpClient) {}


  // Obtain all tasks
  getAllTasks(): Observable<Task[]> {
    return this.http.get<ResponseModel<Task[]>>(
      '${this.apiUrl}/read_tasks/'
    )
    .pipe(
      map(res => res.response || [])
    )
  }

  // Filter task
  getTaskById(id: Number): Observable<Task | null> {
    return this.http.get<ResponseModel<Task>>(
      '${this.apiUrl}/read_task_by_id/${id}'
    ).pipe(
      map(res => res.response || null) // extract only the object task from ResponseModel
    )
  }
  
}
