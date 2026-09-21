from fastapi import APIRouter, Query

from app.services.coingecko_client import coingecko_client

router = APIRouter()


@router.get("/prices")
async def get_prices(ids: str = Query(..., description="ej: bitcoin,ethereum,solana")):
    coin_ids = [c.strip() for c in ids.split(",") if c.strip()]
    return await coingecko_client.get_market_prices(coin_ids)


@router.get("/search")
async def search(q: str = Query(..., min_length=1)):
    return await coingecko_client.search_coins(q)
