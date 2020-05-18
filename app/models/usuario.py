from app.db import db
from datetime import datetime


class TimestampMixin(object):

    data_criacao = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, onupdate=datetime.utcnow)


class UsuarioModel(TimestampMixin, db.Model):

    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    entidades = db.relationship('Entidade', secondary='usuario_entidade')