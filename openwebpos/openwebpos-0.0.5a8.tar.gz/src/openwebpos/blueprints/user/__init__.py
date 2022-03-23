from flask import Blueprint, render_template

from .models import User

bp = Blueprint('user', __name__, template_folder='templates', url_prefix='/user/')


@bp.route('/login')
def login():
    return render_template('user/login.html', title='Login')
