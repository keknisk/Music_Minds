from PIL import Image
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test1'
db = SQLAlchemy(app)

class Test(db.Model):
    image = db.Column(db.BLOB)
    backgr = db.Column(db.BLOB)
    id = db.Column(db.Integer)
    name = db.column(db.Integer)



@app.route('/')
def home():
    return render_template("index.html")


app.run(debug=True)