from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField("Name of Pup:")
    submit = SubmitField("Add puppy")


class AddOwnerForm(FlaskForm):

    name_owner = StringField("Name of Owner:")
    pup_id = IntegerField("Id of Puppy:")
    submit = SubmitField("Add Owner")


class DelForm(FlaskForm):
    id = IntegerField("Id Number of puppy to delete")
    submit = SubmitField("Delete puppy")
                       