from .schemas import CreateUser, User
from database import create_session

from sqlmodel import select


class UserService:

    def get_user_by_id(self, user_id: int):
        with create_session() as session:
            statement = select(User). where(User.id == user_id)
            result = session.exec(statement)
            user = result.first()
        return user


    def create_user(self, user: CreateUser):
        with create_session() as session:
            session.add(user)
            session.flush()
            session.commit()
            session.refresh(user)
            session.expunge(user)
        return user 


    def update_user(self, user_id, user):
        with create_session() as session:
            statement = select(User).where(User.id == user_id)
            result = session.exec(statement)
            userData = result.one()
            if user.email: userData.email = user.email
            if user.first_name: userData.first_name = user.first_name
            if user.last_name: userData.last_name = user.last_name
            if user.nick_name: userData.nick_name = user.nick_name
            if user.profile_picture: userData.profile_picture = user.profile_picture

            session.add(userData)
            session.commit()
            session.refresh(userData)
        return userData


    def delete_user(self, user_id):
        user_bd = self.get_user_by_id(user_id)
        if user_bd is None:
            return None

        with create_session() as session:
            session.delete(user_bd)
            session.commit()
        
        return user_bd