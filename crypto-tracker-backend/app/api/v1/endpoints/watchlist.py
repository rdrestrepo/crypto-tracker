from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.crud.watchlist import add_to_watchlist, get_watchlist, remove_from_watchlist
from app.db.session import get_db
from app.models.user import User
from app.schemas.watchlist import WatchlistItemCreate, WatchlistItemOut

router = APIRouter()


@router.get("/", response_model=list[WatchlistItemOut])
def read_watchlist(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_watchlist(db, current_user.id)


@router.post("/", response_model=WatchlistItemOut, status_code=status.HTTP_201_CREATED)
def create_watchlist_item(
    item_in: WatchlistItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return add_to_watchlist(db, current_user.id, item_in)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_watchlist_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    deleted = remove_from_watchlist(db, current_user.id, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item no encontrado")
