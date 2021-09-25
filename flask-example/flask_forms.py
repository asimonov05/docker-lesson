from flask_wtf import Form
from wtforms import TextField

class TextForm(Form):
    name = TextField()