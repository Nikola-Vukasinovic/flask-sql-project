import os
from forms import AddForm, DelForm, AddOwnerForm
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"

#################################
### SQL DATABASE ################
#################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

Migrate(app, db)

#################################
### MODELS ######################
#################################


class Puppy(db.Model):
    __tablename__ = "puppies"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db. Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Puppy ID: {self.id}, puppy name: {self.name}"
    

class Owner(db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db. Text)
    pup_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))

    def __init__(self, name, pup_id):
        self.name = name
        self.pup_id = pup_id

    def __repr__(self):
        return f"Owner name: {self.name} and pup id:{self.pup_id}"

#################################
### VIEW FUNCTIONS###############
#################################

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_pup = Puppy(name)

        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for("list"))
    
    return render_template("add.html", form = form)


@app.route("/add_owner", methods=["GET", "POST"])
def add_owner():
    form = AddOwnerForm()

    if form.validate_on_submit():
        name_owner = form.name_owner.data
        pup_id = form.pup_id.data
        new_owner = Owner(name_owner, pup_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for("list_owners"))
    
    return render_template("add_owner.html", form = form)


@app.route("/list")
def list():
    puppies = Puppy.query.all()
    return render_template("list.html", puppies = puppies)


@app.route("/list_owners")
def list_owners():
    owners = Owner.query.all()
    return render_template("list_owners.html", owners = owners)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for("list"))
    
    return render_template("delete.html", form = form)


if __name__ == "__main__":
    app.run(debug=True)