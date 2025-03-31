from flask import Blueprint, render_template, flash, session, redirect, url_for

bp = Blueprint('library', __name__, url_prefix='/library')

@bp.route('/')
def ind():
    if 'username' not in session:
        flash('Musíte být přihlášeni, abyste mohli zobrazit tuto stránku.', 'warning')
        return redirect(url_for('login.login'))
    return render_template('library.html')