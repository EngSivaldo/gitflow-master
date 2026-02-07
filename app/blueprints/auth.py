from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
# O segredo: Importamos o User aqui para as rotas usarem
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simulação sênior de login (admin/123)
        if username == 'admin' and password == '123':
            user = User.get("1")
            login_user(user)
            return redirect(url_for('web.index'))
        else:
            flash('Login inválido')
            
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))