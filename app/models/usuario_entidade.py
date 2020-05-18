from .usuario import UsuarioModel
from .entidade import Entidade
from app.db import db

class UsuarioEntidade(db.Model):
    __tablename__= 'usuario_entidade'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    entidade_id = db.Column(db.Integer, db.ForeignKey('entidades.id'))
    usuario = db.relationship(UsuarioModel, backref=db.backref("usuario_assoc"))
    entidade = db.relationship(Entidade, backref=db.backref("entidade_assoc"))

    