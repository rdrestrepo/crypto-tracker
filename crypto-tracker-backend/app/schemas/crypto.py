from typing import Optional
from pydantic import BaseModel


class CoinPrice(BaseModel):
    id: str
    symbol: str
    name: str
    image: Optional[str] = None
    current_price: Optional[float] = None
    price_change_percentage_24h: Optional[float] = None
    market_cap: Optional[float] = None


class CoinSearchResult(BaseModel):
    id: str
    name: str
    symbol: str
    thumb: Optional[str] = None
