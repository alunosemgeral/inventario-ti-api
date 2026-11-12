"""TASK-08: Delete equipment."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Equipment"])

@router.delete("/equipments/{equipment_id}")
def delete_equipment(equipment_id: int):
    # TODO TASK-08: implement the endpoint and return the expected JSON.
    raise HTTPException(status_code=501, detail="TASK-08 not implemented yet")
