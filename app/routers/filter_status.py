"""TASK-10: Filter by status."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Equipment"])

@router.get("/equipments/filter/status")
def filter_by_status(status: str):
    # TODO TASK-10: implement the endpoint and return the expected JSON.
    raise HTTPException(status_code=501, detail="TASK-10 not implemented yet")
