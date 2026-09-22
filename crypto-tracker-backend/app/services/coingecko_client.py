import httpx

from app.core.config import settings

MOCK_DATA = [
    {
        "id": "bitcoin", "symbol": "btc", "name": "Bitcoin",
        "image": "https://coin-images.coingecko.com/coins/images/1/large/bitcoin.png",
        "current_price": 86635.0, "price_change_percentage_24h": 7.16,
        "market_cap": 1740421471841,
    },
    {
        "id": "ethereum", "symbol": "eth", "name": "Ethereum",
        "image": "https://coin-images.coingecko.com/coins/images/279/large/ethereum.png",
        "current_price": 2766.91, "price_change_percentage_24h": 5.53,
        "market_cap": 337753761507,
    },
    {
        "id": "solana", "symbol": "sol", "name": "Solana",
        "image": "https://coin-images.coingecko.com/coins/images/4128/large/solana.png",
        "current_price": 210.5, "price_change_percentage_24h": -2.3,
        "market_cap": 98000000000,
    },
    {
        "id": "cardano", "symbol": "ada", "name": "Cardano",
        "image": "https://coin-images.coingecko.com/coins/images/975/large/cardano.png",
        "current_price": 0.45, "price_change_percentage_24h": 1.2,
        "market_cap": 16000000000,
    },
    {
        "id": "dogecoin", "symbol": "doge", "name": "Dogecoin",
        "image": "https://coin-images.coingecko.com/coins/images/5/large/dogecoin.png",
        "current_price": 0.12, "price_change_percentage_24h": -0.8,
        "market_cap": 17000000000,
    },
]


class CoinGeckoClient:
    """Cliente sencillo para la API pública de CoinGecko (sin API key)."""

    def __init__(self) -> None:
        self.base_url = settings.COINGECKO_BASE_URL
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; CryptoTrackerApp/1.0)"}
        self.use_mock = settings.USE_MOCK_CRYPTO_DATA

    async def get_market_prices(self, coin_ids: list[str]) -> list[dict]:
        if self.use_mock:
            return [c for c in MOCK_DATA if c["id"] in coin_ids] or MOCK_DATA

        params = {
            "vs_currency": "usd",
            "ids": ",".join(coin_ids),
            "order": "market_cap_desc",
            "sparkline": "true",
            "price_change_percentage": "24h",
        }
        async with httpx.AsyncClient(timeout=10, headers=self.headers) as client:
            resp = await client.get(f"{self.base_url}/coins/markets", params=params)
            resp.raise_for_status()
            return resp.json()

    async def search_coins(self, query: str) -> list[dict]:
        if self.use_mock:
            return [
                {"id": c["id"], "name": c["name"], "symbol": c["symbol"], "thumb": c["image"]}
                for c in MOCK_DATA if query.lower() in c["name"].lower()
            ]

        async with httpx.AsyncClient(timeout=10, headers=self.headers) as client:
            resp = await client.get(f"{self.base_url}/search", params={"query": query})
            resp.raise_for_status()
            return resp.json().get("coins", [])


coingecko_client = CoinGeckoClient()
