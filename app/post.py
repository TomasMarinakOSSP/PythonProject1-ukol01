from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from app.db import execute
from app.login import login_required

bp = Blueprint('post', __name__, url_prefix='/posts')


@bp.route('/')
@login_required
def index():
    """
    Funkce pro zobrazení příspěvků
    """
    posts = execute("SELECT id, title, content, author, created_at FROM posts ORDER BY created_at DESC")
    return render_template('post.html', posts=posts)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """
    Funkce pro vytvoření nového příspěvku
    """
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = session['username']

        if not title or not content:
            flash('Vyplňte všechna pole.', 'warning')
            return redirect(url_for('post.create'))

        execute("INSERT INTO posts (title, content, author) VALUES (?, ?, ?)", (title, content, author))
        flash('Příspěvek byl vytvořen.', 'success')
        return redirect(url_for('post.index'))

    return render_template('create_post.html')


@bp.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    """
    Funkce pro úpravu příspěvku
    """
    post = execute("SELECT id, title, content, author FROM posts WHERE id = ?", (post_id,))
    if not post:
        flash('Příspěvek nenalezen.', 'danger')
        return redirect(url_for('post.index'))

    post = post[0]
    if post[3] != session['username']:
        flash('Nemáte oprávnění upravit tento příspěvek.', 'danger')
        return redirect(url_for('post.index'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        execute("UPDATE posts SET title = ?, content = ? WHERE id = ?", (title, content, post_id))
        flash('Příspěvek byl aktualizován.', 'success')
        return redirect(url_for('post.index'))

    return render_template('edit_post.html', post=post)


@bp.route('/delete/<int:post_id>', methods=['POST'])
@login_required
def delete(post_id):
    """
    Funkce pro smazání příspěvku
    :param post_id:
    :return:
    """
    post = execute("SELECT author FROM posts WHERE id = ?", (post_id,))
    if not post or post[0][0] != session['username']:
        flash('Nemáte oprávnění smazat tento příspěvek.', 'danger')
        return redirect(url_for('post.index'))

    execute("DELETE FROM posts WHERE id = ?", (post_id,))
    flash('Příspěvek byl smazán.', 'success')
    return redirect(url_for('post.index'))
