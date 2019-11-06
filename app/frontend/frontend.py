from flask import Blueprint, render_template, request, redirect, url_for
from .forms import EditPageForm


frontend_bp = Blueprint("frontend_bp", __name__)


@frontend_bp.route("/")
def index():
    sample_text = "! This is some markdown text"
    return render_template("index.html", text=sample_text)


@frontend_bp.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditPageForm()

    if form.validate_on_submit():
        print(request.form['content'])
        return redirect(url_for('frontend_bp.index'))

    else:
        return render_template("edit.html", form=form)

