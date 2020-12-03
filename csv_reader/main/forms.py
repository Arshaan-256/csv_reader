from flask_wtf import FlaskForm
from wtforms import IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class CSVFileForm(FlaskForm):
    file = FileField("File", validators=[FileRequired(),
                                         FileAllowed(["csv"], "Please upload a .csv file!")])
    submit = SubmitField("Open File")

class GoToPageForm(FlaskForm):
    page = IntegerField("Page", validators=[DataRequired()])
    go = SubmitField("Go")