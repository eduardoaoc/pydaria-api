from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    
class Products(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(140))
    price= db.Column(db.Numeric())
    description= db.Column(db.Text)
    