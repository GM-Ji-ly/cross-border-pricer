from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from database import Base

class CarDepreciationRecord(Base):
    __tablename__ = "car_depreciation_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    purchase_price = Column(Float)
    current_mileage = Column(Float, nullable=True)
    new_car_price = Column(Float, nullable=True)
    market_high_price = Column(Float, nullable=True)
    market_low_price = Column(Float, nullable=True)
    fuel_type = Column(String, nullable=True)
    equipment = Column(Text, nullable=True)          # JSON 陣列
    accident_level = Column(String, nullable=True)
    has_maintenance_record = Column(Integer, default=0)  # 0/1 boolean
    color = Column(String, nullable=True)
    depreciation_data = Column(Text, nullable=True)  # JSON 完整計算結果
    created_at = Column(DateTime, default=datetime.utcnow)
