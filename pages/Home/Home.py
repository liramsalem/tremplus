from flask import Blueprint, render_template, redirect, url_for, session

# Home blueprint definition
Home = Blueprint('Home', __name__, static_folder='static', static_url_path='/Home', template_folder='templates')


# Routes
@Home.route('/Home')
def index():
    return render_template('Home.html')


@Home.route('/Homepage')
@Home.route('/Home')
def redirect_homepage():
    return redirect(url_for('Home.index'))

