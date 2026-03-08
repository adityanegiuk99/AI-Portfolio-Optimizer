"""
Central configuration management using pydantic-settings.
All environment variables are loaded from .env file or system environment.
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    """Application-wide configuration settings."""

    # ── Application ──
    APP_NAME: str = "AI Wealth Manager"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # ── Database ──
    DATABASE_URL: str = Field(
        default="sqlite+aiosqlite:///./wealth_manager.db",
        description="Database connection string. Defaults to local SQLite.",
    )

    # ── JWT Authentication ──
    JWT_SECRET_KEY: str = Field(
        default="change-this-to-a-secure-random-key-in-production",
        description="Secret key for JWT token signing.",
    )
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # ── API Keys ──
    ALPHA_VANTAGE_API_KEY: Optional[str] = Field(
        default=None,
        description="Alpha Vantage API key. Optional — Yahoo Finance is default.",
    )

    # ── Risk Thresholds ──
    MAX_PORTFOLIO_DRAWDOWN: float = Field(
        default=0.20, description="Maximum tolerated portfolio drawdown (20%)."
    )
    MAX_SINGLE_ASSET_WEIGHT: float = Field(
        default=0.40, description="Max allocation to a single asset (40%)."
    )
    VAR_CONFIDENCE_LEVEL: float = Field(
        default=0.95, description="Confidence level for Value at Risk."
    )
    REBALANCE_DRIFT_THRESHOLD: float = Field(
        default=0.05, description="Minimum drift to trigger rebalance (5%)."
    )

    # ── ML Model Settings ──
    LSTM_SEQUENCE_LENGTH: int = 60
    LSTM_HIDDEN_SIZE: int = 128
    LSTM_NUM_LAYERS: int = 2
    LSTM_DROPOUT: float = 0.2

    ENSEMBLE_WEIGHTS: dict = Field(
        default={"lstm": 0.4, "xgboost": 0.35, "random_forest": 0.25},
        description="Weights for ensemble prediction model.",
    )

    # ── Data Ingestion ──
    DEFAULT_TICKERS: list = Field(
        default=[
            "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA",
            "META", "TSLA", "JPM", "JNJ", "V",
            "SPY", "QQQ", "TLT", "GLD", "VNQ",
        ],
        description="Default ticker universe.",
    )
    DATA_LOOKBACK_YEARS: int = 5
    MARKET_DATA_INTERVAL: str = "1d"

    # ── Server ──
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    CORS_ORIGINS: list = Field(
        default=["http://localhost:5173", "http://localhost:3000"],
        description="Allowed CORS origins.",
    )

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
    }


@lru_cache()
def get_settings() -> Settings:
    """Cached settings singleton."""
    return Settings()
