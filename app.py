from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    dateofbirth = db.Column(db.String(80), nullable=False)
    idnumber = db.Column(db.Integer, nullable=False)
    placeofbirth = db.Column(db.String(80), nullable=False)

@app.route('/user/<int:id>')
def user(id):
    user = User.query.filter_by(id=id)
    return render_template('user.html', user=user)

app.run(port=5000)
