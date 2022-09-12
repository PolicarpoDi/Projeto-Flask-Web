from urllib import request
from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

"""@app.route('/home/<int:id>')
def id(id):
    valor = id ** 2
    return render_template('home.html', valor=valor)"""

"""@app.route('/login/name/<string:nome>')
def login_name(nome):
    return f'<h1>O nome desse usuário é {nome}</h1>'"""


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        # obter email e senha para cadastrar usuário
        email = request.form['email_usuario']
        senha = request.form['senha_usuario']
        
        if not (email or senha):
            return render_template('signup.html')
        
        usuario = {'email': email}
        
        return render_template('signup_ok.html', usuario=usuario) 




if __name__ ==  '__main__':
    app.run(debug=True)