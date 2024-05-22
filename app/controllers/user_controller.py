from flask import Blueprint, request, jsonify
from models.user_model import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

user_bp = Blueprint("user", __name__)

# id: Identificador único del usuario. De tipo entero y autoincremental.
# name: Nombre del usuario. De tipo cadena de texto.
# email: Correo electrónico del usuario. De tipo cadena de texto.
# password: Contraseña del usuario. De tipo cadena de texto.
# role: Rol del usuario (admin, member). De tipo cadena de texto.


@user_bp.route("/register", methods=["POST"])
def register():
  data = request.json
  name = data.get("name")
  email = data.get("email")
  password = data.get("password")
  role = data.get("role")

  
  if not name or not password or not email:
    return jsonify({"error": "Se requiren nombre, email y contraseña"}), 400
  
  existing_user = User.get_user_by_email(email)
  if existing_user:
    return jsonify({"error": "El email ya está en uso"}), 400
  new_user = User(name,email,password,role)
  new_user.save()
  
  return jsonify({"message": "Usuario creado exitosamente"}), 201

@user_bp.route("/login", methods=["POST"])
def login():
  data = request.json
  name = data.get("name")
  email = data.get("email")
  password = data.get("password")
  
  user = User.get_user_by_email(email)
  if user and check_password_hash(user.password_hash,password):
    access_token = create_access_token(identity={"name": name, "role": user.role})
    return jsonify(access_token=access_token), 200
  else:
    return jsonify({"error": "Credenciales inválidas"}), 401