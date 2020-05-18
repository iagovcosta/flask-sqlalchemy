from .assinatura import Assinatura
from .aplicativo import Aplicativo
from app.db import db

class UsuarioEntidade(db.Model):
    __tablename__= 'assinatura_aplicativo'
    id = db.Column(db.Integer, primary_key=True)
    assinatura_id = db.Column(db.Integer, db.ForeignKey('assinaturas.id'))
    aplicativo_id = db.Column(db.Integer, db.ForeignKey('aplicativos.id'))
    assinatura = db.relationship(Assinatura, backref=db.backref("assinatura_assoc"))
    aplicativo = db.relationship(Aplicativo, backref=db.backref("aplicativo_assoc"))
