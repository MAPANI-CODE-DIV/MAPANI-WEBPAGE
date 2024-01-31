from flask_login import LoginManager
from src.models.modelUser import ModelUser

login_manager = LoginManager()

@login_manager.user_loader
def load_user(id):
    return ModelUser.get_id(id)