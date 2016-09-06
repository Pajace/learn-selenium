import math

from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators

app = Flask(__name__)


# Model
class InputForm(Form):
    r = FloatField(validators=[validators.InputRequired()])


# view
@app.route('/demo', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        r = form.r.data
        s = math.sin(r)
    else:
        s = "Please enter number"

    return render_template('view.html', form=form, s=s)


@app.route('/')
def root():
    return render_template('entry.html')


if __name__ == '__main__':
    app.run(debug=True)
