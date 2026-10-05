import json
import logging
from pathlib import Path
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models import CarDepreciationRecord
from schemas import (
    CarDepreciationRecordCreate,
    CarDepreciationRecordResponse,
    CarDepreciationSyncRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/car-depreciation", tags=["car-depreciation"])

CURVES_FILE = Path(__file__).resolve().parent.parent / "curves.json"


@router.post("/sync", response_model=list[CarDepreciationRecordResponse])
async def sync_records(request: CarDepreciationSyncRequest, db: AsyncSession = Depends(get_db)):
    """批量同步本地记录到服务器"""
    created = []
    for record_data in request.records:
        record = CarDepreciationRecord(**record_data.model_dump())
        db.add(record)
        created.append(record)
    await db.commit()
    for r in created:
        await db.refresh(r)
    return created


@router.get("/records", response_model=list[CarDepreciationRecordResponse])
async def get_records(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    """获取服务器端记录列表"""
    result = await db.execute(
        select(CarDepreciationRecord).order_by(CarDepreciationRecord.created_at.desc()).offset(skip).limit(limit)
    )
    return result.scalars().all()


@router.get("/curves")
async def get_curves():
    """取得品牌折舊曲線配置"""
    try:
        with open(CURVES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"讀取 curves.json 失敗: {e}")
        return {"error": "無法讀取曲線配置", "curves": {}}


@router.put("/curves")
async def update_curves(data: dict):
    """更新品牌折舊曲線配置"""
    try:
        with open(CURVES_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return {"status": "ok", "message": "曲線配置已更新"}
    except Exception as e:
        logger.error(f"寫入 curves.json 失敗: {e}")
        return {"error": f"寫入失敗: {e}"}
