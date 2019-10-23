from flask import Blueprint, render_template


frontend_bp = Blueprint('frontend_bp', __name__)


@frontend_bp.route('/')
def index():
    sample_text = '# This is some markdown text'
    return render_template('index.html', text=sample_text)