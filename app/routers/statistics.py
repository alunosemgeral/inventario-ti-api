"""TASK-11: Equipment statistics."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Equipment"])

@router.get("/equipments/statistics")
def equipment_statistics():
    # TODO TASK-11: implement the endpoint and return the expected JSON.
    raise HTTPException(status_code=501, detail="TASK-11 not implemented yet")
