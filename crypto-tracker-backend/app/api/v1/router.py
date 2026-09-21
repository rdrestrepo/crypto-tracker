from fastapi import APIRouter

from app.api.v1.endpoints import auth, crypto, watchlist

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(crypto.router, prefix="/crypto", tags=["crypto"])
api_router.include_router(watchlist.router, prefix="/watchlist", tags=["watchlist"])
