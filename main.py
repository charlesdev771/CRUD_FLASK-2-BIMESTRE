from flask import Flask
from database import db
from flask_migrate import Migrate
from usuarios import bp_usuarios

app = Flask(__name__)

conexao = 'sqlite:///meubanco.sqlite'

app.config['SECRET_KEY'] = 'chave'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
db.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Hello from Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
