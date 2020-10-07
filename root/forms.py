from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TodoForm(FlaskForm):
    task = StringField('Task Name',
                        validators=[DataRequired(message='Bsdk Task kya hein bata de fatafat'),
                        Length(min=5, message='Bsdk at least 5 characer to likh le')])
    submit = SubmitField('Add Task')