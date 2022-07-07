import click
from ext.database import db
from ext.auth import create_user
from ext.database import Products



def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Products(
            id=1, name="Ciabatta", price="10", description="Italian Bread"
        ),
        Products(id=2, name="Baguete", price="15", description="French Bread"),
        Products(id=3, name="Pretzel", price="20", description="German Bread"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Products.query.all()


def init_app(app):
    @app.before_first_request
    def create_db():
        db.create_all()
        