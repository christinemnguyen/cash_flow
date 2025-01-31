from flask import Flask, render_template, flash, redirect, url_for

from app import app

from app.forms import loginForm
from app.forms import signUp
import os
image_folder = os.path.join('static','image')
app.config['UPLOAD_FOLDER'] = image_folder
@app.route('/')
def home():
    filename_logo1 = os.path.join(app.config['UPLOAD_FOLDER'],'logo1.jpg')
    #filename_logo2 = os.path.join(app.config['UPLOAD_FOLDER'],'logo2.jpg')
    #filename_logo3 = os.path.join(app.config['UPLOAD_FOLDER'],'logo3.png')
    return render_template('home.html',logo1 = filename_logo1 )
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = loginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, rememberMe={}'.format(
            form.username.data, form.rememberMe.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)


@app.route('/output')
def output():
    # form = completeForm()
    valid = False

    return render_template('output.html', valid=valid)


app.run(debug=True)


# @app.route('/register', methods=["Get", "Post"])
# def register():
#     try:
#         c, conn = connection()
#         return ("okay")
#     except Exception as e:
#         return (str(e))
