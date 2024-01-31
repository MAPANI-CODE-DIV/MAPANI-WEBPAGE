from flask_wtf.csrf import CSRFProtect
from config import config
from src.services.LMLoader import login_manager
from src import init_app


configuration = config["development"]
app = init_app(configuration)
csrf = CSRFProtect()


if __name__ == "__main__":
    login_manager.init_app(app)
    csrf.init_app(app)
    app.run( host="192.168.68.115", port="7000")
