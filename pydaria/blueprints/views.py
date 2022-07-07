from flask import render_template, abort 
from ext.database import Products


def init_app(app):        
    @app.route('/')
    def index():
        products= Products.query.all()
        return render_template('index.html', products=products)

    @app.route("/product/<product_id>")
    def product(product_id):
        product= Products.query.filter_by(id=product_id).first() or abort (
            404, "PRODUCT NOT FOUND"
        )
        return render_template("product.html", product=product)
        