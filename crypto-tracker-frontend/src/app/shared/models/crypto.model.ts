export interface Coin {
  id: string;
  symbol: string;
  name: string;
  image: string;
  current_price: number;
  price_change_percentage_24h: number;
  market_cap?: number;
  sparkline_in_7d?: { price: number[] };
}

export interface CoinSearchResult {
  id: string;
  name: string;
  symbol: string;
  thumb?: string;
}

export interface WatchlistItem {
  id: number;
  coin_id: string;
  alert_price?: number;
  alert_active: boolean;
}
