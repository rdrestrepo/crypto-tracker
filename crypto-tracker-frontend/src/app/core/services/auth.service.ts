import { HttpClient } from '@angular/common/http';
import { Injectable, inject, signal } from '@angular/core';
import { Observable, tap } from 'rxjs';
import { environment } from '../../../environments/environment';

interface TokenResponse {
  access_token: string;
  token_type: string;
}

const TOKEN_KEY = 'crypto_tracker_token';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private http = inject(HttpClient);
  private baseUrl = `${environment.apiUrl}/auth`;

  // Signal reactivo para saber en templates si el usuario está logueado
  isAuthenticated = signal<boolean>(!!this.getToken());

  register(email: string, password: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/register`, { email, password });
  }

  login(email: string, password: string): Observable<TokenResponse> {
    const body = new URLSearchParams();
    body.set('username', email);
    body.set('password', password);

    return this.http
      .post<TokenResponse>(`${this.baseUrl}/login`, body.toString(), {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      })
      .pipe(
        tap((res) => {
          localStorage.setItem(TOKEN_KEY, res.access_token);
          this.isAuthenticated.set(true);
        })
      );
  }

  logout(): void {
    localStorage.removeItem(TOKEN_KEY);
    this.isAuthenticated.set(false);
  }

  getToken(): string | null {
    return localStorage.getItem(TOKEN_KEY);
  }
}
