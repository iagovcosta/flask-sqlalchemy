from flask import Flask
from .db import db
from .models.usuario import UsuarioModel
from .models.entidade import Entidade
from .models.usuario_entidade import UsuarioEntidade
from .models.aplicativo import Aplicativo
from .models.assinatura import Assinatura
from flask_migrate import Migrate

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        Usuario=UsuarioModel,
        Entidade=Entidade,
        UsuarioEntidade=UsuarioEntidade,
        Aplicativo=Aplicativo,
        Assinatura=Assinatura
    )

if __name__ == "__main__":
    app.run()
