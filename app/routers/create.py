"""TASK-04: Create an equipment item."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Equipment"])

@router.post("/equipments")
def create_equipment(payload: dict):
    # TODO TASK-04: implement the endpoint and return the expected JSON.
    raise HTTPException(status_code=501, detail="TASK-04 not implemented yet")
