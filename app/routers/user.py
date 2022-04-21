from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.UsersResponse
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Before creating user, we need to create the hash of the password
    # password will be stored at user.password
    hashed_password = utils.hash(user.password)
    # Update password
    user.password = hashed_password

    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.delete("/{id}", response_model=schemas.UsersResponse)
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    user_to_delete = db.query(models.Users).filter(models.Users.id == str(id))
    if user_to_delete.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID: {id} not found.",
        )
    user_to_delete.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/{id}", response_model=schemas.UsersResponse)
def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    user = db.query(models.Users).filter(models.Users.id == str(id)).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID: {id} not found.",
        )

    return user


@router.get("/", response_model=List[schemas.UsersResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user: Session = Depends(oauth2.get_current_user),
):
    users = db.query(models.Users).all()

    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No users found"
        )

    return users
