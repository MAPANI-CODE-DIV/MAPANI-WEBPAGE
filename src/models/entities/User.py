from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,id,firstname,lastname,username,email,password,created_at,updated_at,role) -> None:
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
        self.role = role

    @classmethod
    def check_password(self, hashed_password, password):
        print(hashed_password,password)
        
        return check_password_hash(str(hashed_password), password)

          