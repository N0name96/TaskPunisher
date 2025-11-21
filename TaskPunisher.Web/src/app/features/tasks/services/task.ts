import { effect, inject, Injectable, Signal, signal, WritableSignal } from '@angular/core';
import { HttpClient } from '@angular/common/http';


import { environment } from '../../../../environments/environment';
import { ResponseModel } from '../../../models/ResponseModel.model';


@Injectable({
  providedIn: 'root',
})
export class Task {
  private apiUrl = environment.apiUrl

  public dataSignal: WritableSignal<Task[]> = signal([])

  private readonly http = inject(HttpClient)


  getTasks() {
    return this.http
    .get<ResponseModel<Task[]>>(
      `${this.apiUrl}/task/read_tasks/`
    )
    .subscribe(response =>{
        this.dataSignal.set(response.response || [])
    })
  }

}
