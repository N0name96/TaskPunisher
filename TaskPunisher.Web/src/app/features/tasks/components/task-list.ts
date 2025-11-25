import { 
  Component, 
  inject, 
  effect, 
  signal, 
  resource 
} from '@angular/core';
import { CommonModule } from '@angular/common';

import { TaskService } from '../services/task-service';
import { TaskModel } from '../models/task-model';


@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.html',
  styleUrl: './task-list.scss',
  standalone: true,
  imports: [CommonModule]

})
export class TaskList {

  private taskService = inject(TaskService)

  tasks = signal([] as TaskModel[])

  taskResource = resource({
    loader: async () => {
      return await this.taskService.getTasks()
    }
  })

  constructor() {
    effect(() => {
      const data = this.taskResource.value()
      if (data) {
        this.tasks.set(data)
      }
    })
  }

  async deleteTask(id: number) {
    await this.taskService.deleteTask(id)
    this.tasks.update(t => t.filter(t => t.id !== id))
  }
}