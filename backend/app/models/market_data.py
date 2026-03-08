"""MarketData ORM model for storing OHLCV and computed features."""

from sqlalchemy import Column, Integer, Float, String, Date, DateTime, UniqueConstraint
from datetime import datetime, timezone
from app.database import Base


class MarketData(Base):
    __tablename__ = "market_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ticker = Column(String(20), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)

    # ── OHLCV ──
    open = Column(Float, nullable=True)
    high = Column(Float, nullable=True)
    low = Column(Float, nullable=True)
    close = Column(Float, nullable=False)
    adj_close = Column(Float, nullable=True)
    volume = Column(Float, nullable=True)

    # ── Computed Features ──
    daily_return = Column(Float, nullable=True)
    log_return = Column(Float, nullable=True)
    sma_20 = Column(Float, nullable=True)
    sma_50 = Column(Float, nullable=True)
    ema_12 = Column(Float, nullable=True)
    ema_26 = Column(Float, nullable=True)
    rsi_14 = Column(Float, nullable=True)
    macd = Column(Float, nullable=True)
    macd_signal = Column(Float, nullable=True)
    bollinger_upper = Column(Float, nullable=True)
    bollinger_lower = Column(Float, nullable=True)
    atr_14 = Column(Float, nullable=True)
    obv = Column(Float, nullable=True)
    volatility_20 = Column(Float, nullable=True)

    # ── Metadata ──
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        UniqueConstraint("ticker", "date", name="uq_ticker_date"),
    )

    def __repr__(self):
        return f"<MarketData(ticker='{self.ticker}', date={self.date}, close={self.close})>"
