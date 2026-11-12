"""Application entry point. Shared file: changes require teacher approval."""
from fastapi import FastAPI
from app.routers import create, list_all, filter_category, filter_status, statistics, get_by_id, update, delete

app = FastAPI(title="Inventário de TI API", version="0.1.0")

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}

# Specific routes must be registered before /equipments/{equipment_id}.
for router in (create.router, list_all.router, filter_category.router, filter_status.router, statistics.router, get_by_id.router, update.router, delete.router):
    app.include_router(router)
