from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class EditPageForm(FlaskForm):
    content = TextAreaField('content', validators=[DataRequired()])