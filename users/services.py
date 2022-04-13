from sqlmodel import Session, select
from .schemas import CreateUser, User
from database import create_session

class UserService:

    def get_user_by_id(self, user_id: int):
        with create_session() as session:
            row = session.execute(select(User).where(User.id == user_id)).scalar()
        return row

    def create_user(self, user: CreateUser):
        user = User.from_dict(user.dict())
        with create_session() as session:
            session.add(user)
            session.flush()
            session.commit()
            session.refresh(user)
            session.expunge(user)
        return user 

    def update_user(self, user_id, user: CreateUser):
        with create_session() as session:
            session.merge(User.from_dict({**{"id": user_id}, **user.dict()}))
            session.flush()
            session.commit()
        return self.get_user_by_id(user_id)

    def delete_user(self, user_id):
        user_bd = self.get_user_by_id(user_id)
        if user_bd is None:
            return None
        
        with create_session() as session:
            session.delete(user_bd)
            session.commit()
        
        return user_bd