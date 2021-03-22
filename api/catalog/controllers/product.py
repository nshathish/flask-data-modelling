from flask import request, jsonify

from api import db
from api.catalog.models.product import Product
from api.catalog.models.category import Category


def get_all_products():
    all_products = Product.query.all()
    res = {}
    for product in all_products:
        res[product.id] = {
            "name": product.name,
            "price": product.price,
            "category": product.category.name
        }
    return jsonify(res)


def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return f"Product - {product.name}, £{product.price}"


def create_product():
    json_dict = request.get_json()
    name = json_dict["name"]
    price = json_dict["price"]
    category_name = json_dict["category_name"]
    category = Category.query.filter_by(name=category_name).first()
    if not category:
        category = Category(category_name)
    product = Product(name, price, category)
    db.session.add(product)
    db.session.commit()
    return f"Product created {product}"
