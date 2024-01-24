from flask import Blueprint, render_template, request, redirect, url_for
from app.db import session
from app.models import Post
from app.utils import generate_code

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/create', methods=['POST'])
def create():
    text = request.form.get('textarea', None)
    if not text:
        return redirect(url_for('index'))
    code = generate_code()
    new_post = Post(text=text, code=code)
    session.add(new_post)
    session.commit()
    return redirect(url_for('main.share', code=code))


@main.route('/code/<code>')
def share(code):
    post = session.query(Post).filter_by(code=code).first()
    if not post:
        '<h1 style="color: red">Post not founded!</h1>'
    url = url_for('main.share', code=code)
    return render_template('share.html', text=post.text, url=url)
