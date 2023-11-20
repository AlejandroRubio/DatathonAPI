from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"The API is up and running"}
