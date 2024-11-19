from sqlalchemy.orm import Session
from sqlalchemy import select, func
from database import db
from models.user import User
from models.schemas.userSchema import users_schema
from utils.utils import encode_token

def save(user_data):
    with Session(db.engine) as session:
        with session.begin():
            new_user = User(username=user_data['username'], password = user_data['password'])
            session.add(new_user)
            session.commit()

        session.refresh(new_user)
        return new_user

def get():
    with Session(db.engine) as session:
        with session.begin():
            users = session.query(User).all()
            json_users = users_schema.jsonify(users).json
            return json_users
        
def login_customer(username, password):
    user = (db.session.execute(db.select(User).where(User.username == username, User.password == password)).scalar_one_or_none())
    role_names = [role.role_name for role in user.roles]
    if user:
        auth_token = encode_token(user.id, role_names)
        print(auth_token)
        print(user.id)
        resp = {
            'status': 'success',
            'message': 'Successfully logged in',
            'auth_token': auth_token
        }
        return resp
    else:
        return None