from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Users"]
)

@router.get("/")
def health_check():
    return {"Health": "OK"}