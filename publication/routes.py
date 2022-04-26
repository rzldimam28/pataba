from publication import app, db
from publication.models import DinasA, DinasB, Users, Districts
from flask import render_template, flash, redirect, url_for, request
from publication.forms import LoginForm, EditTableForm
from flask_login import current_user, login_user, logout_user, login_required

# home page
@app.route('/')
@app.route('/home')
def home_page():
  return render_template('index.html')

# publication page
@app.route('/publikasi')
def publikasi_page():
  return render_template('publikasi.html')

# ------------------------------------  ( DINAS A) --------------------------------------------
# dinas A (Kota)
@app.route('/a')
def dinas_a():
  data = DinasA.query.filter_by(district_id=None).order_by(DinasA.tahun).all()
  return render_template('dinas_a.html', data=data)

# dinas A (Kecamatan)
@app.route('/a/<int:district_id>')
def dinas_a_kec(district_id):
  data = DinasA.query.filter_by(district_id=district_id).order_by(DinasA.tahun).all()
  id_path = int(str(request.path)[-1])
  district_name = Districts.query.filter_by(id=district_id).first()
  return render_template('dinas_a_kec.html', data=data, district_id=district_id, id_path=id_path, district_name=district_name)

# edit tabel
@app.route('/a/add', methods=['GET', 'POST'])
@login_required
def dinas_a_add():
  form = EditTableForm()
  if form.validate_on_submit():
    if form.district_id.data == 'None':
      form.district_id.data = eval(form.district_id.data)
    else:
      form.district_id.data = int(form.district_id.data)
    if current_user.role == 'admin' or current_user.officer_of_district == form.district_id.data:
      rows_to_create = DinasA(tahun=form.tahun.data,
                              col1=form.col1.data,
                              col2=form.col2.data,
                              col3=form.col3.data,
                              district_id=form.district_id.data
                              )
      db.session.add(rows_to_create)
      db.session.commit()
      flash('Table Edited!', category='success')
      return redirect(url_for('dinas_a'))
    else:  
      flash('Unauthorized', category='danger')
      return redirect(url_for('dinas_a_add')) 
  return render_template('edit_table.html', form=form)

# hapus record
@app.route('/a/delete/<int:id>')
@login_required
def delete_row_a(id):
  row_to_delete = DinasA.query.filter_by(id=id).first()
  if current_user.role == 'admin' or current_user.officer_of_district == row_to_delete.district_id:
    db.session.delete(row_to_delete)
    db.session.commit()
    return redirect(url_for('dinas_a'))
  else:
    flash('Unauthorized', category='danger')
    return redirect(url_for('dinas_a'))
# -------------------------------------- ( AKHIR DINAS A) -------------------------------------------

# ------------------------------------  ( DINAS B ) --------------------------------------------
# dinas b (Kota)
@app.route('/b')
def dinas_b():
  data = DinasB.query.filter_by(district_id=None).order_by(DinasB.tahun).all()
  return render_template('dinas_b.html', data=data)

# dinas b (Kecamatan)
@app.route('/b/<int:district_id>')
def dinas_b_kec(district_id):
  data = DinasB.query.filter_by(district_id=district_id).order_by(DinasB.tahun).all()
  id_path = int(str(request.path)[-1])
  district_name = Districts.query.filter_by(id=district_id).first()
  return render_template('dinas_b_kec.html', data=data, district_id=district_id, id_path=id_path, district_name=district_name)

# edit tabel
@app.route('/b/add', methods=['GET', 'POST'])
@login_required
def dinas_b_add():
  form = EditTableForm()
  if form.validate_on_submit():
    if form.district_id.data == 'None':
      form.district_id.data = eval(form.district_id.data)
    else:
      form.district_id.data = int(form.district_id.data)
    if current_user.role == 'admin' or current_user.officer_of_district == form.district_id.data:
      rows_to_create = DinasB(tahun=form.tahun.data,
                              col1=form.col1.data,
                              col2=form.col2.data,
                              col3=form.col3.data,
                              district_id=form.district_id.data
                              )
      db.session.add(rows_to_create)
      db.session.commit()
      flash('Table Edited!', category='success')
      return redirect(url_for('dinas_b'))
    else:  
      flash('Unauthorized', category='danger')
      return redirect(url_for('dinas_b_add')) 
  return render_template('edit_table.html', form=form)

# hapus record
@app.route('/b/delete/<int:id>')
@login_required
def delete_row_b(id):
  row_to_delete = DinasB.query.filter_by(id=id).first()
  if current_user.role == 'admin' or current_user.officer_of_district == row_to_delete.district_id:
    db.session.delete(row_to_delete)
    db.session.commit()
    return redirect(url_for('dinas_b'))
  else:
    flash('Unauthorized', category='danger')
    return redirect(url_for('dinas_b'))
# -------------------------------------- ( AKHIR DINAS A) -------------------------------------------

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
  return render_template('login.html', form=form)

# logout
@app.route('/logout')
def logout_page():
  logout_user()
  flash('You are now logged out', category="info")
  return redirect(url_for('login_page'))