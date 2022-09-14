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
    
@app.route('/old')
def index():
    return '<h1 style="color: blue">Index<h1> <button>Clique aqui</button>'


@app.route('/users')    # Qeury string params
def usuarios():
    
    query_params = request.args
    q = query_params.get('q')
    page = query_params.get('page')
    
    users = {'users': [
        {'username': 'maria', 'email': 'maria@gmail.com'},
        {'username': 'antonio', 'email': 'antonio@gmail.com'},
        {'username': 'carlos', 'email': 'carlos@gmail.com'}
    ],
    'q':q,
    'page':page
    }
    
    return users


@app.route('/signup', methods=['GET', 'POST', 'PUT', 'DELETE'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        # obter email e senha para cadastrar usuário
        email = request.form.get['email_usuario'] or None
        senha = request.form['senha_usuario']
        
        if not (email or senha):
            return render_template('signup.html')
        
        usuario = {'email': email}
        
        return render_template('signup_ok.html', usuario=usuario) 




if __name__ ==  '__main__':
    app.run(debug=True)