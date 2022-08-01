from typing import List, Union

from datetime import date, datetime, time, timedelta
from pydantic import BaseModel

class TravelBase(BaseModel):
  departure_date_start: datetime = None
  arrival_date_start: datetime = None
  departure_date_end: datetime = None
  arrival_date_end: datetime = None
  origin_std_format: str
  origin_name: str
  destination_std_format: str
  destination_name: str
  forecasted_weather_departure: str
  forecasted_weather_arrival: str

class TravelCreate(TravelBase):
  pass

class Travel(TravelBase):
  id: int
  travel_user_id: int
  
  class Config:
    orm_mode = True

class UserBase(BaseModel):
  email: str

class UserCreate(UserBase):
  password: str

class User(UserBase):
  id: int
  is_active: bool
  travels: List[Travel] = []

  class Config:
    orm_mode = True
