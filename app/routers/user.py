from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schema, models, utils
from .routes import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.UserOut)
def create_user(users: schema.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email == users.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Email {users.email} already registered")
    hashed_password = utils.hash(users.password)
    users.password = hashed_password
    new_user = models.User(**users.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user