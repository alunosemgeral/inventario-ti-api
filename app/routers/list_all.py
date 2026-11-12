"""TASK-05: List all equipment."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Equipment"])

@router.get("/equipments")
def list_equipments():
    # TODO TASK-05: implement the endpoint and return the expected JSON.
    raise HTTPException(status_code=501, detail="TASK-05 not implemented yet")
