from flask import request, jsonify

from api import db
from api.catalog.models.category import Category


def get_all_categories():
    categories = Category.query.all()
    res = {}
    for category in categories:
        res[category.id] = {
            "name": category.name
        }
        for product in category.products:
            res[category.id]["products"] = {
                "id": product.id,
                "name": product.name,
                "price": product.price
            }
    return jsonify(res)


def create_category():
    json_dict = request.get_json()
    name = json_dict["name"]
    category = Category(name)
    db.session.add(category)
    db.session.commit()
    return f"Category created {category}"
