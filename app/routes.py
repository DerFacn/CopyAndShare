from flask import Blueprint, render_template
from app.db import session
from app.models import Post

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/create', methods=['POST'])
def create():
    pass


@main.route('/<code>')
def share(code):
    pass
