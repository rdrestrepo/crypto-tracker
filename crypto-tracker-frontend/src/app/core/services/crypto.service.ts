import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { Coin, CoinSearchResult, WatchlistItem } from '../../shared/models/crypto.model';
import { environment } from '../../../environments/environment';

@Injectable({ providedIn: 'root' })
export class CryptoService {
  private http = inject(HttpClient);
  private baseUrl = environment.apiUrl;

  getPrices(ids: string[]): Observable<Coin[]> {
    return this.http.get<Coin[]>(`${this.baseUrl}/crypto/prices`, {
      params: { ids: ids.join(',') },
    });
  }

  searchCoins(query: string): Observable<CoinSearchResult[]> {
    return this.http.get<CoinSearchResult[]>(`${this.baseUrl}/crypto/search`, {
      params: { q: query },
    });
  }

  getWatchlist(): Observable<WatchlistItem[]> {
    return this.http.get<WatchlistItem[]>(`${this.baseUrl}/watchlist/`);
  }

  addToWatchlist(coinId: string, alertPrice?: number): Observable<WatchlistItem> {
    return this.http.post<WatchlistItem>(`${this.baseUrl}/watchlist/`, {
      coin_id: coinId,
      alert_price: alertPrice ?? null,
      alert_active: !!alertPrice,
    });
  }

  removeFromWatchlist(itemId: number): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/watchlist/${itemId}`);
  }
}
