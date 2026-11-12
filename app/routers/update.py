"""TASK-07: Update equipment."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Equipment"])

@router.put("/equipments/{equipment_id}")
def update_equipment(equipment_id: int, payload: dict):
    # TODO TASK-07: implement the endpoint and return the expected JSON.
    raise HTTPException(status_code=501, detail="TASK-07 not implemented yet")
