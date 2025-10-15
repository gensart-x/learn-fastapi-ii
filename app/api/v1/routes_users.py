from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.models.user import User
from app.db.session import get_session

router = APIRouter()


@router.get('/')
async def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return {
        'success': True,
        'data': users
    }
    
@router.post('/')
async def add_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user