import os, csv
from flask import ( Blueprint, 
                    render_template, 
                    redirect, 
                    url_for, 
                    flash, 
                    request, 
                    abort )
from csv_reader import db
from csv_reader.models import Data
from werkzeug.utils import secure_filename
from csv_reader.main.forms import CSVFileForm

main = Blueprint('main', __name__)

def store_into_db(filename):
    file_path = os.path.join('./data', filename)
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data = Data(col1=row[1],col2=row[2],col3=row[3])
            db.session.add(data)
    db.session.commit()

@main.route("/", methods=["GET", "POST"])
def home():
    form = CSVFileForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('./data/' + filename)
        flash(f"{filename} uploaded!", "success")
        store_into_db(filename);
        return redirect(url_for('main.home'))
    return render_template("home.html", title="Home Page", form=form)

@main.route("/display/<int:page>", methods=["GET"])
def displayData(page):
    rows_per_page = 100
    data = Data.query.order_by(Data.col1.asc()).paginate(page=page, per_page=rows_per_page, error_out=False)
    data_ = Data.query.all()
    return render_template("display_data.html", title="Display Data", data=data)