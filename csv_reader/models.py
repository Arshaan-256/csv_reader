from csv_reader import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    col1 = db.Column(db.String(50), nullable=False)
    col2 = db.Column(db.String(50), nullable=False)
    col3 = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"User({self.col1}, {self.col2}, {self.col3})"