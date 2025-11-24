import { Component, inject, effect } from '@angular/core';
import { CommonModule } from '@angular/common';

import { TaskService } from '../services/task-service';


@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.html',
  styleUrl: './task-list.scss',
  standalone: true,
  imports: [CommonModule]

})
export class TaskList {

  private taskService = inject(TaskService)
  
  constructor() {
    effect(() => this.taskService.getTasks())
  }

  list_tasks = this.taskService.dataSignal

  // deleteTask(id: number) {
  //   this.taskService.deleteTask(id)
  // }
}