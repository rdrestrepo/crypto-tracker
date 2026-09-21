import httpx

from app.core.config import settings


class CoinGeckoClient:
    """Cliente sencillo para la API pública de CoinGecko (sin API key)."""

    def __init__(self) -> None:
        self.base_url = settings.COINGECKO_BASE_URL

    async def get_market_prices(self, coin_ids: list[str]) -> list[dict]:
        params = {
            "vs_currency": "usd",
            "ids": ",".join(coin_ids),
            "order": "market_cap_desc",
            "sparkline": "true",
            "price_change_percentage": "24h",
        }
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(f"{self.base_url}/coins/markets", params=params)
            resp.raise_for_status()
            return resp.json()

    async def search_coins(self, query: str) -> list[dict]:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(f"{self.base_url}/search", params={"query": query})
            resp.raise_for_status()
            return resp.json().get("coins", [])


coingecko_client = CoinGeckoClient()
