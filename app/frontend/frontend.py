from flask import Blueprint, render_template, request
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
        print(request.form)
        return redirect('/success')

    else:
        return render_template("edit.html", form=form)

