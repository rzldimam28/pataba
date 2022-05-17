from publication import app, db
from publication.models import DinasA, DinasB, Users, Districts, Setda, Dprd
from flask import render_template, flash, redirect, url_for, request
from publication.forms import FormDprd, LoginForm, EditTableForm, FormSetda
from flask_login import current_user, login_user, logout_user, login_required


# ------------------------------------  ( DINAS B ) --------------------------------------------
# dinas b (Kota)
@app.route('/publikasi/b')
def dinas_b():
  data = DinasB.query.filter_by(district_id=None).order_by(DinasB.tahun).all()
  return render_template('dinas_b.html', data=data)

# dinas b (Kecamatan)
@app.route('/publikasi/b/<int:district_id>')
def dinas_b_kec(district_id):
  data = DinasB.query.filter_by(district_id=district_id).order_by(DinasB.tahun).all()
  id_path = int(str(request.path)[-1])
  district_name = Districts.query.filter_by(id=district_id).first()
  return render_template('dinas_b_kec.html', data=data, district_id=district_id, id_path=id_path, district_name=district_name)

# edit tabel
@app.route('/publikasi/b/add', methods=['GET', 'POST'])
@login_required
def dinas_b_add():
  if current_user.role == 'admin' or current_user.officer_of_agency == 2 or current_user.officer_of_agency == None:
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
  else:
    flash('Bukan Dinasmu', category='danger')
    return redirect(url_for('publikasi_page')) 
  return render_template('dinas_b_edit.html', form=form)

# hapus record
@app.route('/publikasi/b/delete/<int:id>')
@login_required
def delete_row_b(id):
  row_to_delete = DinasB.query.filter_by(id=id).first()
  if current_user.role == 'admin' or current_user.officer_of_agency == 1 or current_user.officer_of_agency == None:
    if current_user.officer_of_district == row_to_delete.district_id:
      db.session.delete(row_to_delete)
      db.session.commit()
      return redirect(url_for('dinas_b'))
    else:
      flash('Unauthorized', category='danger')
      return redirect(url_for('dinas_b'))
  else:
    flash('Bukan Dinasmu', category='danger')
    return redirect(url_for('dinas_b'))
