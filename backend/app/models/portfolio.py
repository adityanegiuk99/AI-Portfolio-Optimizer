"""Portfolio ORM model for storing optimized allocations and performance."""

from sqlalchemy import Column, Integer, Float, String, DateTime, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    name = Column(String(255), default="My Portfolio")

    # ── Allocation ──
    allocations = Column(
        JSON, nullable=False,
        doc='Dict of {ticker: weight}, e.g. {"AAPL": 0.15, "MSFT": 0.10}'
    )
    optimization_method = Column(
        String(50), default="mpt",
        doc="mpt | rl | equal_weight"
    )

    # ── Performance Snapshot ──
    expected_return = Column(Float, nullable=True)
    expected_volatility = Column(Float, nullable=True)
    sharpe_ratio = Column(Float, nullable=True)
    sortino_ratio = Column(Float, nullable=True)
    max_drawdown = Column(Float, nullable=True)
    var_95 = Column(Float, nullable=True, doc="Value at Risk at 95% confidence")
    cvar_95 = Column(Float, nullable=True, doc="Conditional VaR at 95%")

    # ── Regime Context ──
    market_regime = Column(
        String(20), nullable=True,
        doc="bull | bear | sideways — regime at optimization time"
    )

    # ── Metadata ──
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # ── Relationships ──
    owner = relationship("User", back_populates="portfolios")

    def __repr__(self):
        return f"<Portfolio(id={self.id}, name='{self.name}', method='{self.optimization_method}')>"
