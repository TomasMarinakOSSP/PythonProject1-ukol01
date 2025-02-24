from flask import Blueprint, request, flash, render_template, Flask

bp = Blueprint('login', __name__, url_prefix='/login')

USERS = {'pokuston': 'kouzelnik', "admin": "admin", "student": "student"}


@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username] == password:
            flash('Přihlášení bylo úspěšné!', 'success')
        else:
            flash('Přihlášení selhalo! Zkuste to znovu.', 'warning')
        return render_template('index.html', username=username, password=password)
    return render_template('login.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash('Hesla se neshodují!', 'warning')
        elif username in USERS:
            flash('Tento uživatel již existuje!', 'warning')
        else:
            USERS[username] = password
            flash('Registrace byla úspěšná!', 'success')
        return render_template('register.html', username=username, password=password,
                               confirm_password=confirm_password)
    return render_template('register.html')