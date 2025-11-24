import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class Prueba {
  private apiUrl = 'https://api.ejemplo.com/users';

  // Método asíncrono estándar (Devuelve Promise<User>)
  async getUserById(id: number): Promise<User> {
    const response = await fetch(${this.apiUrl}/${id});
    
    if (!response.ok) {
      throw new Error(Error ${response.status}: No se pudo obtener el usuario);
    }
    
    return response.json();
}