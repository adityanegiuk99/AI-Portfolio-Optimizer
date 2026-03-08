"""User ORM model for authentication and personalization."""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)

    # ── Investment Profile ──
    risk_tolerance = Column(
        String(20), default="moderate",
        doc="conservative | moderate | aggressive"
    )
    investment_horizon = Column(
        Integer, default=5,
        doc="Investment horizon in years"
    )
    initial_capital = Column(Float, default=100_000.0)
    financial_goals = Column(
        Text, nullable=True,
        doc="JSON string of financial goals"
    )

    # ── Timestamps ──
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # ── Relationships ──
    portfolios = relationship("Portfolio", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"
