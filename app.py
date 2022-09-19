from urllib import request
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    email = request.args.get('email', None)
    
    return render_template('about.html', email=email)

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


@app.route('/users')    # Query string params
def usuarios():
    
    query_params = request.args
    q = query_params.get('q')
    page = query_params.get('page')
    order = query_params.get('order_by')
    
    users = {'users': [
        {'username': 'maria', 'email': 'maria@gmail.com'},
        {'username': 'antonio', 'email': 'antonio@gmail.com'},
        {'username': 'carlos', 'email': 'carlos@gmail.com'}
    ],
    'q':q,
    'page':page,
    'ordenado_por': order
    }
    
    return users

@app.route('/result_ok')
def signup_ok():
    return render_template('signup_ok.html') 


@app.route('/signup', methods=['GET', 'POST', 'PUT', 'DELETE'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        # obter email e senha para cadastrar usuário
        email = request.form['email_usuario'] or None
        senha = request.form['senha_usuario']
        
        if not (email or senha):
            return render_template('signup.html')
        
        return redirect(url_for('signup_ok')) # redireciona sem precisar alterar a rota, pois chama pela função 




if __name__ ==  '__main__':
    app.run(debug=True)