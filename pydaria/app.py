from ext import configuration
from flask import Flask

def minimal_app():
    app= Flask(__name__)
    configuration.init_app(app)
    return app


def create_app():
    app= minimal_app()
    configuration.load_extensions(app)
    return app
    
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    
        