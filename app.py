from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Index</h1>'

@app.route('/home')
def home():
    return "<h1>Hello world by Flask and Python!</h1>"


@app.route('/login/id/<int:id>')
def login(id):
    return f'<h1>O ID desse login é o {id}</h1>'


@app.route('/login/name/<string:nome>')
def login_name(nome):
    return f'<h1>O nome desse usuário é {nome}</h1>'


if __name__ ==  '__main__':
    app.run(debug=True)