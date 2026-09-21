import { CommonModule } from '@angular/common';
import { Component, OnDestroy, OnInit, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { Subscription, interval, startWith, switchMap } from 'rxjs';
import { CryptoService } from '../../core/services/crypto.service';
import { AuthService } from '../../core/services/auth.service';
import { Coin } from '../../shared/models/crypto.model';

const REFRESH_MS = 30000;
const DEFAULT_COINS = ['bitcoin', 'ethereum', 'solana', 'cardano', 'dogecoin'];

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent implements OnInit, OnDestroy {
  private cryptoService = inject(CryptoService);
  private authService = inject(AuthService);

  coins = signal<Coin[]>([]);
  loading = signal(true);
  lastUpdated = signal<Date | null>(null);

  private sub?: Subscription;

  ngOnInit(): void {
    this.sub = interval(REFRESH_MS)
      .pipe(
        startWith(0),
        switchMap(() => this.cryptoService.getPrices(DEFAULT_COINS))
      )
      .subscribe({
        next: (data) => {
          this.coins.set(data);
          this.loading.set(false);
          this.lastUpdated.set(new Date());
        },
        error: () => this.loading.set(false),
      });
  }

  ngOnDestroy(): void {
    this.sub?.unsubscribe();
  }

  logout(): void {
    this.authService.logout();
  }
}
