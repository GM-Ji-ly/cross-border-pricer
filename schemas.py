from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# --- Car Depreciation ---
class CarDepreciationRecordCreate(BaseModel):
    brand: str
    model: str
    year: int
    purchase_price: float
    current_mileage: Optional[float] = None
    new_car_price: Optional[float] = None
    market_high_price: Optional[float] = None
    market_low_price: Optional[float] = None
    fuel_type: Optional[str] = None
    equipment: Optional[str] = None
    accident_level: Optional[str] = None
    has_maintenance_record: Optional[int] = 0
    color: Optional[str] = None
    depreciation_data: Optional[str] = None

class CarDepreciationRecordResponse(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    purchase_price: float
    current_mileage: Optional[float] = None
    new_car_price: Optional[float] = None
    market_high_price: Optional[float] = None
    market_low_price: Optional[float] = None
    fuel_type: Optional[str] = None
    equipment: Optional[str] = None
    accident_level: Optional[str] = None
    has_maintenance_record: Optional[int] = None
    color: Optional[str] = None
    depreciation_data: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class CarDepreciationSyncRequest(BaseModel):
    records: list[CarDepreciationRecordCreate]
