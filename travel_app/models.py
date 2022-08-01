import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  hashed_password = Column(String)
  is_active = Column(Boolean, default=True)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  updated_at = Column(DateTime)

  travels = relationship("Travel", back_populates="owner")

class Travel(Base):
  __tablename__ = "travels"

  id = Column(Integer, primary_key=True, index=True)
  departure_date_start = Column(DateTime)
  arrival_date_start = Column(DateTime)
  departure_date_end = Column(DateTime)
  arrival_date_end = Column(DateTime)
  origin_std_format = Column(String)
  origin_name = Column(String)
  destination_std_format = Column(String)
  destination_name = Column(String)
  forecasted_weather_departure = Column(String)
  forecasted_weather_arrival = Column(String)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  updated_at = Column(DateTime)
  travel_user_id = Column(Integer, ForeignKey("users.id"))

  owner = relationship("User", back_populates="travels")
