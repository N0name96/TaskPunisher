import { Component, inject, effect } from '@angular/core';
import { CommonModule } from '@angular/common';

import { Task } from '../models/task';
import { Task as TaskService} from '../services/task';


@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.html',
  styleUrl: './task-list.scss',
  standalone: true,
  imports: [CommonModule]

})
export class TaskList {

  private taskService = inject(TaskService)

  tasks = this.taskService.dataSignal

  constructor() {
    effect(() => this.taskService.getTasks())
  }
}
