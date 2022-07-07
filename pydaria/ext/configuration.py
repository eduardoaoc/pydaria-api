from importlib import import_module
from dynaconf import FlaskDynaconf

#importa todas as extensões que estão no settings, faz um loop para ver todas presentes
def load_extensions(app):
    for extensions in app.config.get("EXTENSIONS"):
        mod= import_module(extensions)
        mod.init_app(app)


def init_app(app):
    FlaskDynaconf(app)
    