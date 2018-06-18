from flask import session, request, render_template, redirect
from web import app,  ALLOWED_EXTENSIONS
from web.models import User
from web.forms import RegForm, LoginForm
from hashlib import sha256
import json
from pprint import pprint


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/generic', methods=['GET'])
def generic():
    return render_template('generic.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegForm()
    if form.validate_on_submit():
        password = sha256(form.password.data.encode()).hexdigest()
        user = User(form.login.data, password)
        user.save()
        return redirect('/')
    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = sha256(form.password.data.encode()).hexdigest()
        user = User.query.filter(User.login == form.login.data).filter(User.password == password).first()
        if user:
            session['logged_in'] = True
        else:
            session['logged_in'] = False
        return redirect('/')
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return redirect('/')


@app.route('/check', methods=['GET'])
def check():
    return render_template('check.html')

@app.route('/upload', methods=['GET'])
def upload():
    if session['logged_in']:
        return render_template('upload.html')
    else:
        return redirect('/')