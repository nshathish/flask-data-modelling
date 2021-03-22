from flask import Blueprint

from api.catalog.controllers import product as pc
from api.catalog.controllers import category as cc

catalog = Blueprint("catalog", __name__)


@catalog.route("/")
@catalog.route("/products")
def get_all_products():
    return pc.get_all_products()


@catalog.route("/products/<product_id>")
def get_product(product_id):
    return pc.get_product(product_id)


@catalog.route("/products", methods=["POST"])
def create_product():
    return pc.create_product()


@catalog.route("/categories")
def get_all_categories():
    return cc.get_all_categories()


@catalog.route("/categories", methods=["POST"])
def create_category():
    return cc.create_category()


