from .home import home


def init_app(app):
    app.register_blueprint(home)
