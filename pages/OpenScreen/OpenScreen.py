from flask import Blueprint, render_template,redirect,url_for

# OpenScreen blueprint definition
OpenScreen = Blueprint('OpenScreen', __name__, static_folder='static', static_url_path='/OpenScreen', template_folder='templates')


# Routes
@OpenScreen.route('/')
def index():
    return render_template('OpenScreen.html')



@OpenScreen.route('/OpenScreen')
def redirect_OpenScreen():
    return redirect(url_for('OpenScreen.index'))

