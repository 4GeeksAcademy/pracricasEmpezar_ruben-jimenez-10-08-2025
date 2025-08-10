from flask import Blueprint, jsonify, request
from models.product import Product


products_bp = Blueprint("products", __name__, url_prefix="/products")

# @products_bp.route("/", methods=["GET"])
# def get_products():
#     return jsonify({"msg":"DORMIDO DE LAS NARICES"})
products = []
next_id = 1


@products_bp.route("/", methods=["GET"])
def get_products():
    return jsonify([p.serializer() for p in products]), 200


@products_bp.route("/", methods=["POST"])
def create_product():
    global next_id
    data = request.get_json()
    if (
        not isinstance(data.get("name"), str)
        or not isinstance(data.get("year"), str)
        or not isinstance(data.get("brand"), str)
    ):
        return jsonify("Falta meter datos"), 400
    new_product = Product(
        id=next_id, name=data["name"], year=data["year"], brand=data["brand"]
    )
    products.append(new_product)
    next_id += 1
    return jsonify({"msg": "Daros guardos", "Product": new_product.serializer()}), 201


@products_bp.route("/<int:id>", methods=["GET"])
def show_product(id):
    for p in products:
        if id == p.id:
            return (
                jsonify({"msg": "Producto encontrado", "Product": p.serializer()}),
                201,
            )
    return jsonify({"msg": "Producto no encontrado"}), 404


@products_bp.route("/<int:id>", methods=["DELETE"])
def delete_product(id):
    for p in products:
        if id == p.id:
            products.remove(p)
            return (
                jsonify({"msg": "Producto eliminado", "Producto": p.serializer()}),
                201,
            )
    return jsonify({"msg": "Producto no encontrado"}), 404


@products_bp.route("/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()
    for p in products:
        if id == p.id:
            p.name = data.get("name", p.name)
            p.year = data.get("year", p.year)
            p.brand = data.get("brand", p.brand)
            return (
                jsonify({"msg": "Producto actualizado", "Product": p.serializer()}),
                200,
            )
    return jsonify({"msg": "Error"}), 400
