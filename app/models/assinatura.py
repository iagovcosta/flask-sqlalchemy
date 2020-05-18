from app.db import db

class Assinatura(db.Model):

    __tablename__ = 'assinaturas'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String)
    aplicativo = db.relationship('Aplicativo', secondary='assinatura_aplicativo')