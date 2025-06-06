from flask import Blueprint, request, flash, render_template, Flask, session, redirect, url_for

from app.db import execute, db_query

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/', methods=['GET', 'POST'])
def login():
    """
    Funkce pro přihlášení uživatele
    bere si to z formuláře a porovnává to s databází uživatelů a hesel
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        command = "SELECT password FROM users WHERE username = ?"
        result = db_query(command, (username,))

        if result and result[0][0] == password:
            session['username'] = username
            flash('Přihlášení bylo úspěšné!', 'success')
        else:
            flash('Přihlášení selhalo! Zkuste to znovu.', 'warning')

        return render_template('index.html', username=username, password=password)

    return render_template('login.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Funkce pro registraci uživatele
    bere si to z formuláře a ukládá to do databáze uživatelů
    """
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Hesla se neshodují!', 'warning')
        else:
            try:
                command = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)"
                execute(command, (username, email, password))
                flash('Registrace byla úspěšná!', 'success')
            except Exception as e:
                flash(f'Chyba při registraci: {str(e)}', 'danger')

    return render_template('register.html')


@bp.route('/users')
def user_list():
    """
    Funkce pro zobrazení uživatelů
    zobrazuje všechny uživatele z databáze
    """
    command = "SELECT username, password FROM users"
    result = execute(command)
    return render_template("user.html", result=result)


@bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login.login'))


@bp.route('/post')
def post():
    if 'username' not in session:
        flash('Musíte být přihlášeni, abyste mohli zobrazit tuto stránku.', 'warning')
        return redirect(url_for('login.login'))
    return render_template('post.html')

def log_required():
    if 'username' not in session:
        flash('Musíte být přihlášeni, abyste mohli zobrazit tuto stránku.', 'warning')
        return redirect(url_for('login.login'))

def login_required(func):
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            flash('Musíte být přihlášeni, abyste mohli zobrazit tuto stránku.', 'warning')
            return redirect(url_for('login.login'))
        return func(*args, **kwargs)
    return wrapper