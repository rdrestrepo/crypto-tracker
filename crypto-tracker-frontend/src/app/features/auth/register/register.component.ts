import { CommonModule } from '@angular/common';
import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../../core/services/auth.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './register.component.html',
})
export class RegisterComponent {
  private authService = inject(AuthService);
  private router = inject(Router);

  email = '';
  password = '';
  errorMessage = signal<string | null>(null);
  loading = signal(false);

  onSubmit(): void {
    this.errorMessage.set(null);
    this.loading.set(true);

    this.authService.register(this.email, this.password).subscribe({
      next: () => {
        // Tras registrar, iniciamos sesión automáticamente
        this.authService.login(this.email, this.password).subscribe({
          next: () => {
            this.loading.set(false);
            this.router.navigate(['/dashboard']);
          },
          error: () => {
            this.loading.set(false);
            this.router.navigate(['/login']);
          },
        });
      },
      error: (err) => {
        this.loading.set(false);
        this.errorMessage.set(err?.error?.detail ?? 'No se pudo registrar el usuario.');
      },
    });
  }
}
