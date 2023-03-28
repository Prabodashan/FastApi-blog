from fastapi import APIRouter,Depends, status, HTTPException
from .. import schemas, models, database
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter()
get_db = database.get_db

@router.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request:schemas.User, db: Session = Depends(get_db)):
    new_User = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_User)
    db.commit()
    db.refresh(new_User)
    return new_User

@router.get('/user/{id}',response_model=schemas.ShowUser, tags=['users'])
def show(id:int,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    return user