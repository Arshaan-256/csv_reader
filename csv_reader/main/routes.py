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
from csv_reader.main.forms import CSVFileForm, GoToPageForm

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

def getData(context):
    if context["order_by"] == "id":
        if context["sort_by"] == "asc":
            data = Data.query.order_by(Data.id.asc()).paginate(page=context["page_num"], 
                                                            per_page=context["per_page"], 
                                                            error_out=False)
        else:
            data = Data.query.order_by(Data.id.desc()).paginate(page=context["page_num"], 
                                                            per_page=context["per_page"], 
                                                            error_out=False)
    elif context["order_by"] == "col1":
        if context["sort_by"] == "asc":
            data = Data.query.order_by(Data.col1.asc()).paginate(page=context["page_num"], 
                                                            per_page=context["per_page"], 
                                                            error_out=False)
        else:
            data = Data.query.order_by(Data.col1.desc()).paginate(page=context["page_num"], 
                                                            per_page=context["per_page"], 
                                                            error_out=False)
    elif context["order_by"] == "col2":
        if context["sort_by"] == "asc":
            data = Data.query.order_by(Data.col2.asc()).paginate(page=context["page_num"], 
                                                            per_page=context["per_page"], 
                                                            error_out=False)
        else:
            data = Data.query.order_by(Data.col2.desc()).paginate(page=context["page_num"], 
                                                            per_page=context["per_page"], 
                                                            error_out=False)  
    elif context["order_by"] == "col3":
        if context["sort_by"] == "asc":
            data = Data.query.order_by(Data.col3.asc()).paginate(page=context["page_num"], 
                                                            per_page=context["per_page"], 
                                                            error_out=False)
        else:
            data = Data.query.order_by(Data.col3.desc()).paginate(page=context["page_num"], 
                                                            per_page=context["per_page"], 
                                                            error_out=False)   
    else:
        data = Data.query.order_by(Data.id.asc()).paginate(page=context["page_num"], 
                                                            per_page=context["per_page"], 
                                                            error_out=False)

    return data                                                    

@main.route("/display", methods=["GET", "POST"])
def displayData():
    form = GoToPageForm()
     
    context = dict()
    context["page_num"] = request.args.get('page_num', 1, type=int)
    context["per_page"] = request.args.get('per_page', 100, type=int) 
    context["order_by"] = request.args.get('order_by', None)
    context["sort_by"] = request.args.get('sort_by', None)

    if form.validate_on_submit():
        context["page_num"] = form.page.data       
        data = getData(context)
        return redirect(url_for('main.displayData', 
                        page_num=context["page_num"], 
                        order_by=context["order_by"], 
                        sort_by=context["sort_by"]))

    data = getData(context)
         
    return render_template("display_data.html", title="Display Data", data=data, context=context, form=form)