from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Crypto Tracker API"
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    COINGECKO_BASE_URL: str = "https://api.coingecko.com/api/v3"
    USE_MOCK_CRYPTO_DATA: bool = False

    class Config:
        env_file = ".env"


settings = Settings()


