"""TASK-09: Filter by category."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Equipment"])

@router.get("/equipments/filter/category")
def filter_by_category(category: str):
    # TODO TASK-09: implement the endpoint and return the expected JSON.
    raise HTTPException(status_code=501, detail="TASK-09 not implemented yet")
