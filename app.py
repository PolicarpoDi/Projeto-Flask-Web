from flask import Flask, render_template


app = Flask(__name__)



@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/home/<int:id>')
def id(id):
    valor = id ** 2
    return render_template('home.html', valor=valor)


@app.route('/login/name/<string:nome>')
def login_name(nome):
    return f'<h1>O nome desse usuário é {nome}</h1>'


if __name__ ==  '__main__':
    app.run(debug=True)