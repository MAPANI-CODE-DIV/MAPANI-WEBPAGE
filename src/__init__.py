from flask import Flask

# Routes
from .routes import adminRoutes, siteRoutes



def init_app(config):
    # Configuration
    app = Flask(__name__)
    app.config.from_object(config)
    





    # Blueprints
    app.register_blueprint(adminRoutes.admin_, url_prefix='/admin')
    app.register_blueprint(siteRoutes.site_, url_prefix='/')

    return app