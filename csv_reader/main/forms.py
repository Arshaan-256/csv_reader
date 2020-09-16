from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileRequired, FileAllowed

class CSVFileForm(FlaskForm):
    file = FileField("File", validators=[FileRequired(),
                                         FileAllowed(["csv"], "Please upload a .csv file!")])
    submit = SubmitField("Open File")
