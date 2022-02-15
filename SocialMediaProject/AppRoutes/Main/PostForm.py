from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    content = TextAreaField("Write your new post: ", validators=[DataRequired(), Length(max=150)])
    submit = SubmitField("Add Post")
