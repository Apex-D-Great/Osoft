from flask_restx import Namespace, Resource, fields
from ..models import Addproduct
from backend import app
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from flask import request, jsonify, make_response
import secrets
import os

product_ns = Namespace("product", description="product query")

product_model = product_ns.model(
    "Addproduct",
    {
        "name": fields.String(required=True, description="product name"),
        "discount": fields.Integer(default=0, required=True, description="discount 0-100"),
        "stock": fields.Integer(default=0, required=True, description="stock"),
        "price": fields.Integer(required=True, description="product price"),
        "description": fields.String(required=True, description="product description"),
        "image": fields.String(required=True, description="poduct image"),
    }
)

# from flask_restx import Namespace, Resource, fields
# @recipe_ns.route("/recipes")
# class RecipeResources(Resource):
#     @recipe_ns.marshal_list_with(recipes_model)
#     # @jwt_required()
#     @recipe_ns.doc(security="apikey")
#     def get(self):
#         authorization_header = request.headers.get('Authorization')
#         if not authorization_header:
#             error_message = 'Authorization header is missing.'
#             return jsonify({'error': error_message}), 401
#         """get all recipes"""
#         recipes = Recipe.query.all()
#         return recipes

#     @recipe_ns.marshal_with(recipe_model)
#     @recipe_ns.expect(recipe_model)
#     # @jwt_required()
#     @recipe_ns.doc(security="apikey")
#     def post(self):
#         authorization_header = request.headers.get('Authorization')
#         if not authorization_header:
#             error_message = 'Authorization header is missing.'
#             return jsonify({'error': error_message}), 401
#         """this method helps in creating a post"""
#         data = request.get_json()
#         get_title = Recipe.query.filter_by(title=data.get("title")).first()
#         if get_title:
#             return jsonify({"message":"title has to be unique"})
#         new_recipe = Recipe(title=data.get("title"), description=data.get("description"))
#         new_recipe.save()
#         get_title = Recipe.query.filter_by(title=data.get("title")).first()
#         return get_title

@product_ns.route('/addproduct')
class Product(Resource):
    @product_ns.expect(product_model)
    def post(self):
        name = request.form.get('name')
        discount = request.form.get('discount')
        stock = request.form.get('stock')
        price = request.form.get('price')
        description = request.form.get('description')
        image = request.files.get('image')
        
        
        random_hex =secrets.token_hex(10)
        f_ext = image.filename
        random_name = random_hex + f_ext
        # pic_path = os.path.join(app.root_path, "/static", random_name)

        # Save product data to the database
        new_product = Addproduct(
            name=name,
            discount=discount,
            stock=stock,
            price=price,
            description=description,
            image= random_name,  # Save image filenames to the database
        )
        new_product.save()

        # Save uploaded images to the server filesystem (optional)
        image.save(f'frontend/image/{random_name}')

        return {'success':True}
    @product_ns.marshal_list_with(product_model)
    def get(self):
        brands = Addproduct.query.all()
        return brands