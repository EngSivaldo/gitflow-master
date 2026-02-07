from flask import Blueprint, render_template, request, redirect, url_for, flash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == '123':
            # Em vez de retornar texto, redirecionamos para o Dashboard
            return redirect(url_for('web.index')) 
        else:
            return "<h1>Erro!</h1><a href='/login'>Tentar novamente</a>"
            
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    return redirect(url_for('auth.login'))