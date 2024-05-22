import json
from database import db

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
  __tablename__ = "users"
  
# id: Identificador único del usuario. De tipo entero y autoincremental.
# name: Nombre del usuario. De tipo cadena de texto.
# email: Correo electrónico del usuario. De tipo cadena de texto.
# password: Contraseña del usuario. De tipo cadena de texto.
# role: Rol del usuario (admin, member). De tipo cadena de texto.

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False, unique=True)
  email = db.Column(db.String(100), nullable=False, unique=True)
  password_hash = db.Column(db.String(128), nullable=False)
  role = db.Column(db.String(50), nullable=False)
  
  # roles=["user"]
  def __init__(self,name,email,password,role=["user"]):
    self.name=name
    self.email=email
    self.password_hash=generate_password_hash(password)
    self.role=json.dumps(role)
    
  def save(self):
    db.session.add(self)
    db.session.commit()
    
  @staticmethod
  def get_user_by_email(email):
    return User.query.filter_by(email=email).first()
  
