"""TASK-06: Find equipment by ID."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Equipment"])

@router.get("/equipments/{equipment_id}")
def get_equipment(equipment_id: int):
    # TODO TASK-06: implement the endpoint and return the expected JSON.
    raise HTTPException(status_code=501, detail="TASK-06 not implemented yet")
