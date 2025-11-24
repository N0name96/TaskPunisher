import { Component, inject, resource, signal } from '@angular/core';
import { TaskService } from '../../services/task-service';


@Component({
  selector: 'app-prueba',
  imports: [],
  templateUrl: './prueba.html',
  styleUrl: './prueba.scss',
})
export class Prueba {

  private taskService = inject(TaskService)

  task = signal([])

  taskResource = resource({
    request: () => {{ task: this.task()}}
  })

// @Component({
//   selector: 'app-user-profile',
//   standalone: true,
  // template: `
  //   @if (userResource.isLoading()) {
  //     <p>Cargando desde el servicio...</p>
  //   } 
  //   @else if (userResource.error(); as err) {
  //     <p>Error: {{ err }}</p>
  //   } 
  //   @else if (userResource.value(); as user) {
  //     <h1>{{ user.name }}</h1>
  //     <p>{{ user.email }}</p>
  //   }

  //   <button (click)="nextId()">Siguiente ID</button>
  // `
// })

// export class UserProfileComponent {
//   private userService = inject(UserService);

//   // Señal que controla "qué" usuario queremos
//   userId = signal(1);

//   // El Resource reacciona a cambios en 'userId' y llama al servicio
//   userResource = resource({
//     request: () => ({ id: this.userId() }), 
//     loader: ({ request }) => this.userService.getUserById(request.id)
//   });

//   nextId() {
//     this.userId.update(id => id + 1);
//   }
// }

}
