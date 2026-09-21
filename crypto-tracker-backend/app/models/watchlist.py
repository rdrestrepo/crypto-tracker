from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class WatchlistItem(Base):
    __tablename__ = "watchlist_items"

    id = Column(Integer, primary_key=True, index=True)
    coin_id = Column(String, nullable=False)  # ej: "bitcoin"
    alert_price = Column(Float, nullable=True)
    alert_active = Column(Boolean, default=False)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="watchlist_items")
