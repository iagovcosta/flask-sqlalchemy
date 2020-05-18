from app.db import db


class Entidade(db.Model):
    __tablename__ = 'entidades'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    usuarios = db.relationship('UsuarioModel', secondary='usuario_entidade')
