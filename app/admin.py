from flask import Blueprint, render_template, flash, session, redirect, url_for, request
from functools import wraps
from app.db import execute

bp = Blueprint('admin', __name__, url_prefix='/admin')


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Funkce pro kontrolu, zda je uživatel admin
        """
        if 'username' not in session or session["role"] != 'admin':
            flash('Musíte být přihlášeni jako admin, abyste mohli zobrazit tuto stránku.', 'warning')
            return redirect(url_for('login.login'))
        return func(*args, **kwargs)

    return wrapper


@bp.route('/')
@admin_required
def admin():
    """
    Funkce pro zobrazení admin stránky
    """
    return render_template('admin.html')


@bp.route('/users')
@admin_required
def manage_users():
    """
    Funkce pro správu uživatelů
    """
    users = execute("SELECT id, username, role FROM users")
    return render_template('manage_users.html', users=users)


@bp.route('/delete_user/<int:user_id>', methods=['POST'])
@admin_required
def delete_user(user_id):
    """
    Funkce pro smazání uživatele
    """
    execute("DELETE FROM users WHERE id = ?", (user_id,))
    flash('Uživatel byl úspěšně smazán.', 'success')
    return redirect(url_for('admin.manage_users'))


@bp.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
@admin_required
def edit_user(user_id):
    """
    Funkce pro úpravu uživatele
    """
    if request.method == 'POST':
        new_password = request.form['password']
        new_role = request.form['role']
        execute("UPDATE users SET password = ?, role = ? WHERE id = ?", (new_password, new_role, user_id))
        flash('Uživatel byl úspěšně upraven.', 'success')
        return redirect(url_for('admin.manage_users'))

    user = execute("SELECT id, username, role FROM users WHERE id = ?", (user_id,))
    if not user:
        flash('Uživatel nenalezen.', 'danger')
        return redirect(url_for('admin.manage_users'))

    return render_template('edit_user.html', user=user[0])