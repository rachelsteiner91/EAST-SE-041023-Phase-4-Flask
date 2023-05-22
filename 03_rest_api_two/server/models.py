from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    title = db.Column(db.String) 
    genre = db.Column(db.String)
    length = db.Column(db.Integer) 
    year = db.Column(db.Integer) 
    image = db.Column(db.String)
    language = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String) 
    composer = db.Column(db.String)

    roles = db.relationship('Role', back_populates='production')

    serialize_rules = ('-created_at', '-updated_at', '-roles.production')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Role(db.Model, SerializerMixin):
    __tablename__ = "roles"
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    role_name = db.Column(db.String)

    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    production = db.relationship('Production', back_populates='roles')

    serialize_rules = ('-created_at', '-updated_at', '-production.roles')

    