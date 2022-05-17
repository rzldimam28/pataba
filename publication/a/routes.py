from publication import app, db
from publication.models import DinasA, Districts
from flask import render_template, flash, redirect, url_for, request
from publication.forms import EditTableForm
from flask_login import current_user, login_required


# ------------------------------------  ( DINAS A) --------------------------------------------
# dinas A (Kota)
@app.route('/publikasi/a')
def dinas_a():
  data = DinasA.query.filter_by(district_id=None).order_by(DinasA.tahun).all()
  return render_template('dinas_a.html', data=data)

# dinas A (Kecamatan)
@app.route('/publikasi/a/<int:district_id>')
def dinas_a_kec(district_id):
  data = DinasA.query.filter_by(district_id=district_id).order_by(DinasA.tahun).all()
  id_path = int(str(request.path)[-1])
  district_name = Districts.query.filter_by(id=district_id).first()
  return render_template('dinas_a_kec.html', data=data, district_id=district_id, id_path=id_path, district_name=district_name)

# edit tabel
@app.route('/publikasi/a/add', methods=['GET', 'POST'])
@login_required
def dinas_a_add():
  if current_user.role == 'admin' or current_user.officer_of_agency == 1 or current_user.officer_of_agency == None:
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
  else:
    flash('Bukan Dinasmu', category='danger')
    return redirect(url_for('publikasi_page')) 
  return render_template('dinas_a_edit.html', form=form)

# hapus record
@app.route('/publikasi/a/delete/<int:id>')
@login_required
def delete_row_a(id):
  row_to_delete = DinasA.query.filter_by(id=id).first()
  if current_user.role == 'admin' or current_user.officer_of_agency == 1 or current_user.officer_of_agency == None:
    if current_user.officer_of_district == row_to_delete.district_id:
      db.session.delete(row_to_delete)
      db.session.commit()
      flash('Data berhasil dihapus', category='success')
      return redirect(url_for('dinas_a'))
    else:
      flash('Unauthorized', category='danger')
      return redirect(url_for('dinas_a'))
  else:
    flash('Bukan Dinasmu', category='danger')
    return redirect(url_for('dinas_a'))

