from flask import Blueprint, render_template, flash, session, redirect, url_for
from app.login import log_required

bp = Blueprint('library', __name__, url_prefix='/library')

@bp.route('/')
def index():
    log_required()
    return render_template('library.html')
