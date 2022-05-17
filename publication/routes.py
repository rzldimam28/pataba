from publication import app, db
from publication.models import Users
from flask import render_template, flash, redirect, url_for, request
from publication.forms import LoginForm
from flask_login import login_user, logout_user

# home page
@app.route('/')
@app.route('/home')
def home_page():
  return render_template('index_agi.html')

# publication page
@app.route('/publikasi')
def publikasi_page():
  return render_template('publikasi_agi.html')

# login
@app.route('/login', methods=['GET', 'POST'])
def login_page():
  form = LoginForm()
  if form.validate_on_submit():
    attempted_user = Users.query.filter_by(email=form.email.data).first()
    if attempted_user:
      if attempted_user.check_password_correction(attempted_password=form.password.data):
        login_user(attempted_user)
        flash('You are login', category="success")
        return redirect(url_for('home_page'))
      else:
        flash('password salah', category="danger")
    else:
      flash('usernome not found', category="danger")
  return render_template('login_agi.html', form=form)

# logout
@app.route('/logout')
def logout_page():
  logout_user()
  flash('You are now logged out', category="info")
  return redirect(url_for('login_page'))