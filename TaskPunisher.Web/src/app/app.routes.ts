import { Routes } from '@angular/router';

import { TaskList } from './features/tasks/components/task-list';

export const routes: Routes = [
    {
        path:'', 
        redirectTo:'tasks', 
        pathMatch:'full'
    },
    {
        path: 'tasks',
        component: TaskList
    }
];
