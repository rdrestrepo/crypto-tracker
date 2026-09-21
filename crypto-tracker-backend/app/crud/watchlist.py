from sqlalchemy.orm import Session

from app.models.watchlist import WatchlistItem
from app.schemas.watchlist import WatchlistItemCreate


def get_watchlist(db: Session, user_id: int) -> list[WatchlistItem]:
    return db.query(WatchlistItem).filter(WatchlistItem.owner_id == user_id).all()


def add_to_watchlist(db: Session, user_id: int, item_in: WatchlistItemCreate) -> WatchlistItem:
    db_item = WatchlistItem(**item_in.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def remove_from_watchlist(db: Session, user_id: int, item_id: int) -> bool:
    item = (
        db.query(WatchlistItem)
        .filter(WatchlistItem.id == item_id, WatchlistItem.owner_id == user_id)
        .first()
    )
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True
