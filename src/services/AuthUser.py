from src.models.modelUser import ModelUser
from src.models.entities.User import User
from flask import request
from flask_login import login_user

def authenticate_user():
    if request.method == "POST":
        user = User(
            0,
            "",
            "",
            "",
            request.form["email"],
            request.form["password"],
            "",
            "",
            "",
        )

        logged_user = ModelUser.login(user)
        if logged_user:
            if logged_user.password:
                login_user(logged_user)
                return True, "Authentication successful"
            else:
                return False, "Contraseña Incorrecta<br><br>"
        else:
            return False, "Usuario No Encontrado<br><br>"
    else:
        return False, "Void"
    
  