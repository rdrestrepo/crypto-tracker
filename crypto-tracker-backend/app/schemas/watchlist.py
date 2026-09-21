from typing import Optional
from pydantic import BaseModel, ConfigDict


class WatchlistItemBase(BaseModel):
    coin_id: str
    alert_price: Optional[float] = None
    alert_active: bool = False


class WatchlistItemCreate(WatchlistItemBase):
    pass


class WatchlistItemOut(WatchlistItemBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
