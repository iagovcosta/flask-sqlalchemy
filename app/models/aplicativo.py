from app.db import db

class Aplicativo(db.Model):

    __tablename__ = 'aplicativos'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String)
    nome = db.Column(db.String)
    valor = db.Column(db.Integer)
    assinatura = db.relationship('Assinatura', secondary='assinatura_aplicativo')