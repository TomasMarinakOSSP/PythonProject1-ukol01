from flask import Blueprint, render_template, flash, session, redirect, url_for
from app.login import login_required

bp = Blueprint('library', __name__, url_prefix='/library')

@bp.route('/')
@login_required
def ind():
    return render_template('library.html')
