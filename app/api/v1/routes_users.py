from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlmodel import Session, select, or_
from app.models.user import User
from app.db.session import get_session

router = APIRouter()


@router.get('/')
async def get_users(session: Session = Depends(get_session)):

    statement = select(User)
    users = session.exec(statement).all()

    return JSONResponse(status_code=200, content={
        'success': True,
        'data': jsonable_encoder(users)
    })


@router.get('/{user_id}')
async def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    return JSONResponse(status_code=200, content={
        'success': True,
        'data': jsonable_encoder(user)
    })


@router.post('/')
async def add_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return JSONResponse(status_code=201, content={
        'success': True,
        'data': jsonable_encoder(user)
    })


@router.post('/{user_id}')
async def update_user(user_id: int, updated_user: User, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        return JSONResponse(status_code=404, content={
            'success': False,
            'message': 'User not found'
        })

    user.name = updated_user.name
    user.age = updated_user.age
    session.add(user)
    session.commit()
    session.refresh(user)

    return JSONResponse(status_code=200, content={
        'success': True,
        'data': jsonable_encoder(user)
    })
