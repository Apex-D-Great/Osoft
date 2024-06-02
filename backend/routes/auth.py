from flask_restx import Namespace, Resource, fields
from flask import jsonify, make_response, render_template, url_for
from ..models import User
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash



auth_ns = Namespace("auth", description="everything authentication endpoint")

signup_model = auth_ns.model(
    "Signup",
    {
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
    }
)

login_model = auth_ns.model(
    "Login",
    {
        "email": fields.String(),
        "password": fields.String(),
    }
)


@auth_ns.route("/signup")
class Signup(Resource):
    @auth_ns.expect(signup_model)
    def post(self):
        """sign up method"""
        data = request.get_json()
        admins = ["sirapex5@gmail.com", "osoft@gmail.com"]
        email = User.query.filter_by(email=data.get("email")).first()
        signup_email = data["email"]
        username = User.query.filter_by(username=data.get("username")).first()
        if username or email:
            return jsonify({"sucess": False, "message":"email/username already exist in our database, use a new valid email/try a new username"})
        password = generate_password_hash(data.get("password"))
        for admin in admins:
            if admin == signup_email:
                new_user = User(username=data.get("username"), email=data.get("email"), password=password, is_admin=True, is_vendor=True)
                new_user.save()
                return make_response(jsonify({"success":True, "message":"admin user created successfully"}),201)
        new_user = User(username=data.get("username"), email=data.get("email"), password=password)
        new_user.save()
        return make_response(jsonify({"success":True, "message":"user created successfully"}),201)


@auth_ns.route("/login")
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        """login method"""
        data = request.get_json()
        user = User.query.filter_by(email=data.get("email")).first()
        if user is not None and check_password_hash(user.password, data.get("password")):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return jsonify({"success":True, "access_token":access_token, "refresh_token":refresh_token, "message":f"welcome {user.username}", "is_admin":user.is_admin, "is_vendor":user.is_vendor})
        return jsonify({"success":False, "message":"incorrect credentials or you probably dont have an account, sign up"})
    # def get(self):
    #     headers = {'Content-Type': 'text/html'}
    #     return make_response(render_template("login.html"),200,headers)


@auth_ns.route("/token/refresh")
class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        id = get_jwt_identity()
        access_token = create_access_token(identity=id)
        return jsonify({"access_token":access_token})


