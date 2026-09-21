import { CommonModule } from '@angular/common';
import { Component, OnInit, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { CryptoService } from '../../core/services/crypto.service';
import { WatchlistItem } from '../../shared/models/crypto.model';

@Component({
  selector: 'app-watchlist',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './watchlist.component.html',
})
export class WatchlistComponent implements OnInit {
  private cryptoService = inject(CryptoService);

  items = signal<WatchlistItem[]>([]);
  newCoinId = '';
  newAlertPrice: number | null = null;
  loading = signal(true);

  ngOnInit(): void {
    this.load();
  }

  load(): void {
    this.loading.set(true);
    this.cryptoService.getWatchlist().subscribe({
      next: (data) => {
        this.items.set(data);
        this.loading.set(false);
      },
      error: () => this.loading.set(false),
    });
  }

  addCoin(): void {
    if (!this.newCoinId.trim()) return;

    this.cryptoService
      .addToWatchlist(this.newCoinId.trim().toLowerCase(), this.newAlertPrice ?? undefined)
      .subscribe(() => {
        this.newCoinId = '';
        this.newAlertPrice = null;
        this.load();
      });
  }

  remove(itemId: number): void {
    this.cryptoService.removeFromWatchlist(itemId).subscribe(() => this.load());
  }
}
