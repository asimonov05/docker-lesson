from typing import Text
from flask import Flask, render_template, request, redirect, url_for
from flask_forms import TextForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'veryverystrongkey'
text = ''

@app.route('/', methods=["GET", "POST"])
def index():
    global text
    form = TextForm()
    if form.validate_on_submit():
        text += ' ' + request.form['name']
        return redirect(url_for('index'))
    return render_template('base.html', form=form, text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0')