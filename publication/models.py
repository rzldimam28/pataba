from publication import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Districts(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(), nullable=False)
  # type
  user = db.relationship('Users', backref='district_owned_user', lazy=True)

class Agencies(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(), nullable=False)
  # type
  user = db.relationship('Users', backref='agencies_owned_user', lazy=True)

class Users(db.Model, UserMixin):
  id = db.Column(db.Integer(), primary_key=True)
  email = db.Column(db.String(), unique=True, nullable=False)
  password_hash = db.Column(db.String(), nullable=False)
  name = db.Column(db.String(), nullable=False)
  role = db.Column(db.String(), nullable=False)
  officer_of_district = db.Column(db.Integer(), db.ForeignKey('districts.id'), nullable=True)
  officer_of_agency = db.Column(db.Integer(), db.ForeignKey('agencies.id'), nullable=True)

  @property
  def password(self):
    return self.password
  
  @password.setter
  def password(self, plain_text_password):
    self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
  def check_password_correction(self, attempted_password):
    return bcrypt.check_password_hash(self.password_hash, attempted_password)

class DinasA(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  tahun = db.Column(db.String(length=4), nullable=False)
  col1 = db.Column(db.Integer())
  col2 = db.Column(db.Integer())
  col3 = db.Column(db.Integer())
  district_id = db.Column(db.Integer(), db.ForeignKey('districts.id'), nullable=True)

class DinasB(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  tahun = db.Column(db.String(length=4), nullable=False)
  col1 = db.Column(db.Integer())
  col2 = db.Column(db.Integer())
  col3 = db.Column(db.Integer())
  district_id = db.Column(db.Integer(), db.ForeignKey('districts.id'), nullable=True)

class Setda(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  tahun = db.Column(db.String(length=4), nullable=False)
  # ---
  u1 = db.Column(db.Integer())
  u2 = db.Column(db.Integer())
  u3 = db.Column(db.Integer())
  u4 = db.Column(db.Integer())
  u5 = db.Column(db.Integer())
  u6 = db.Column(db.Integer())
  u7 = db.Column(db.Integer())
  u8 = db.Column(db.Integer())
  u9 = db.Column(db.Integer())
  u10 = db.Column(db.Integer())
  u11 = db.Column(db.Integer())
  u12 = db.Column(db.Integer())
  u13 = db.Column(db.Integer())
  u14 = db.Column(db.Integer())
  u15 = db.Column(db.Integer())
  u16 = db.Column(db.Integer())
  u17 = db.Column(db.Integer())
  u18 = db.Column(db.Integer())
  u19 = db.Column(db.Integer())
  u20 = db.Column(db.Integer())
  u21 = db.Column(db.Integer())
  u22 = db.Column(db.Integer())
  u23 = db.Column(db.Integer())
  u24 = db.Column(db.Integer())
  u25 = db.Column(db.Integer())
  u26 = db.Column(db.Integer())
  u27 = db.Column(db.Integer())
  u28 = db.Column(db.Integer())
  u29 = db.Column(db.Integer())
  u30 = db.Column(db.Integer())
  u31 = db.Column(db.Integer())
  u32 = db.Column(db.Integer())
  u33 = db.Column(db.Integer())
  u34 = db.Column(db.Integer())
  u35 = db.Column(db.Integer())
  u36 = db.Column(db.Integer())
  u37 = db.Column(db.Integer())
  u38 = db.Column(db.Integer())
  u39 = db.Column(db.Integer())
  u40 = db.Column(db.Integer())
  u41 = db.Column(db.Integer())
  u42 = db.Column(db.Integer())
  u43 = db.Column(db.Integer())
  u44 = db.Column(db.Integer())
  u45 = db.Column(db.Integer())
  u46 = db.Column(db.Integer())
  u47 = db.Column(db.Integer())
  u48 = db.Column(db.Integer())
  u49 = db.Column(db.Integer())
  u50 = db.Column(db.Integer())
  u51 = db.Column(db.Integer())
  u52 = db.Column(db.Integer())
  u53 = db.Column(db.Integer())
  u54 = db.Column(db.Integer())
  u55 = db.Column(db.Integer())
  u56 = db.Column(db.Integer())
  u57 = db.Column(db.Integer())
  u58 = db.Column(db.Integer())
  u59 = db.Column(db.Integer())
  u60 = db.Column(db.Integer())
  u61 = db.Column(db.Integer())
  u62 = db.Column(db.Integer())
  u63 = db.Column(db.Integer())
  u64 = db.Column(db.Integer())
  u65 = db.Column(db.Integer())
  u66 = db.Column(db.Integer())
  u67 = db.Column(db.Integer())
  u68 = db.Column(db.Integer())
  u69 = db.Column(db.Integer())
  u70 = db.Column(db.Integer())
  u71 = db.Column(db.Integer())
  u72 = db.Column(db.Integer())
  u73 = db.Column(db.Integer())
  u74 = db.Column(db.Integer())
  u75 = db.Column(db.Integer())
  u76 = db.Column(db.Integer())
  u77 = db.Column(db.Integer())
  u78 = db.Column(db.Integer())
  u79 = db.Column(db.Integer())
  u80 = db.Column(db.Integer())
  u81 = db.Column(db.Integer())
  u82 = db.Column(db.Integer())
  u83 = db.Column(db.Integer())
  u84 = db.Column(db.Integer())
  u85 = db.Column(db.Integer())
  u86 = db.Column(db.Integer())
  u87 = db.Column(db.Integer())
  u88 = db.Column(db.Integer())
  u89 = db.Column(db.Integer())
  u90 = db.Column(db.Integer())
  u91 = db.Column(db.Integer())
  u92 = db.Column(db.Integer())
  u93 = db.Column(db.Integer())
  u94 = db.Column(db.Integer())
  u95 = db.Column(db.Integer())
  u96 = db.Column(db.Integer())
  u97 = db.Column(db.Integer())
  u98 = db.Column(db.Integer())
  u99 = db.Column(db.Integer())
  u100 = db.Column(db.Integer())
  u101 = db.Column(db.Integer())
  u102 = db.Column(db.Integer())
  u103 = db.Column(db.Integer())
  u104 = db.Column(db.Integer())
  u105 = db.Column(db.Integer())
  u106 = db.Column(db.Integer())
  u107 = db.Column(db.Integer())
  u108 = db.Column(db.Integer())
  u109 = db.Column(db.Integer())
  u110 = db.Column(db.Integer())
  u111 = db.Column(db.Integer())
  u112 = db.Column(db.Integer())
  u113 = db.Column(db.Integer())
  u114 = db.Column(db.Integer())
  u115 = db.Column(db.Integer())
  u116 = db.Column(db.Integer())
  u117 = db.Column(db.Integer())
  u118 = db.Column(db.Integer())
  u119 = db.Column(db.Integer())
  u120 = db.Column(db.Integer())
  u121 = db.Column(db.Integer())
  u122 = db.Column(db.Integer())
  u123 = db.Column(db.Integer())
  u124 = db.Column(db.Integer())
  u125 = db.Column(db.Integer())
  u126 = db.Column(db.Integer())
  u127 = db.Column(db.Integer())
  u128 = db.Column(db.Integer())
  u129 = db.Column(db.Integer())
  u130 = db.Column(db.Integer())
  u131 = db.Column(db.Integer())
  u132 = db.Column(db.Integer())
  u133 = db.Column(db.Integer())
  u134 = db.Column(db.Integer())
  u135 = db.Column(db.Integer())
  u136 = db.Column(db.Integer())
  u137 = db.Column(db.Integer())
  u138 = db.Column(db.Integer())
  u139 = db.Column(db.Integer())
  u140 = db.Column(db.Integer())
  u141 = db.Column(db.Integer())
  u142 = db.Column(db.Integer())
  u143 = db.Column(db.Integer())
  u144 = db.Column(db.Integer())
  u145 = db.Column(db.Integer())
  u146 = db.Column(db.Integer())
  u147 = db.Column(db.Integer())
  u148 = db.Column(db.Integer())
  u149 = db.Column(db.Integer())
  u150 = db.Column(db.Integer())
  u151 = db.Column(db.Integer())
  u152 = db.Column(db.Integer())
  u153 = db.Column(db.Integer())
  u154 = db.Column(db.Integer())
  u155 = db.Column(db.Integer())
  u156 = db.Column(db.Integer())
  u157 = db.Column(db.Integer())
  u158 = db.Column(db.Integer())
  u159 = db.Column(db.Integer())
  u160 = db.Column(db.Integer())
  u161 = db.Column(db.Integer())
  u162 = db.Column(db.Integer())
  u163 = db.Column(db.Integer())
  u164 = db.Column(db.Integer())
  u165 = db.Column(db.Integer())
  u166 = db.Column(db.Integer())
  u167 = db.Column(db.Integer())
  u168 = db.Column(db.Integer())
  u169 = db.Column(db.Integer())
  u170 = db.Column(db.Integer())
  u171 = db.Column(db.Integer())
  u172 = db.Column(db.Integer())
  u173 = db.Column(db.Integer())
  u174 = db.Column(db.Integer())
  u175 = db.Column(db.Integer())
  u176 = db.Column(db.Integer())
  u177 = db.Column(db.Integer())
  u178 = db.Column(db.Integer())
  u179 = db.Column(db.Integer())
  u180 = db.Column(db.Integer())
  u181 = db.Column(db.Integer())
  u182 = db.Column(db.Integer())
  u183 = db.Column(db.Integer())
  u184 = db.Column(db.Integer())
  u185 = db.Column(db.Integer())
  u186 = db.Column(db.Integer())
  u187 = db.Column(db.Integer())
  u188 = db.Column(db.Integer())
  u189 = db.Column(db.Integer())
  u190 = db.Column(db.Integer())
  u191 = db.Column(db.Integer())
  u192 = db.Column(db.Integer())
  u193 = db.Column(db.Integer())
  u194 = db.Column(db.Integer())
  u195 = db.Column(db.Integer())
  u196 = db.Column(db.Integer())
  u197 = db.Column(db.Integer())
  u198 = db.Column(db.Integer())
  u199 = db.Column(db.Integer())
  u200 = db.Column(db.Integer())
  u201 = db.Column(db.Integer())
  u202 = db.Column(db.Integer())
  u203 = db.Column(db.Integer())
  u204 = db.Column(db.Integer())
  u205 = db.Column(db.Integer())
  u206 = db.Column(db.Integer())
  u207 = db.Column(db.Integer())
  u208 = db.Column(db.Integer())
  u209 = db.Column(db.Integer())
  u210 = db.Column(db.Integer())
  u211 = db.Column(db.Integer())
  u212 = db.Column(db.Integer())
  u213 = db.Column(db.Integer())
  u214 = db.Column(db.Integer())
  u215 = db.Column(db.Integer())
  u216 = db.Column(db.Integer())
  u217 = db.Column(db.Integer())
  u218 = db.Column(db.Integer())
  u219 = db.Column(db.Integer())
  u220 = db.Column(db.Integer())
  u221 = db.Column(db.Integer())
  u222 = db.Column(db.Integer())
  u223 = db.Column(db.Integer())
  u224 = db.Column(db.Integer())
  u225 = db.Column(db.Integer())
  u226 = db.Column(db.Integer())
  u227 = db.Column(db.Integer())
  u228 = db.Column(db.Integer())
  u229 = db.Column(db.Integer())
  u230 = db.Column(db.Integer())
  u231 = db.Column(db.Integer())
  u232 = db.Column(db.Integer())
  u233 = db.Column(db.Integer())
  u234 = db.Column(db.Integer())
  u235 = db.Column(db.Integer())
  u236 = db.Column(db.Integer())
  # 236
  # 7 hilang, 131 dobel
  # ---
  district_id = db.Column(db.Integer(), db.ForeignKey('districts.id'), nullable=True)

class Dprd(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  tahun = db.Column(db.String(length=4), nullable=False)
  # ---
  u1 = db.Column(db.Integer())
  u2 = db.Column(db.Integer())
  u3 = db.Column(db.Integer())
  u4 = db.Column(db.Integer())
  u5 = db.Column(db.Integer())
  u6 = db.Column(db.Integer())
  u7 = db.Column(db.Integer())
  u8 = db.Column(db.Integer())
  u9 = db.Column(db.Integer())
  u10 = db.Column(db.Integer())
  u11 = db.Column(db.Integer())
  u12 = db.Column(db.Integer())
  u13 = db.Column(db.Integer())
  u14 = db.Column(db.Integer())
  u15 = db.Column(db.Integer())
  u16 = db.Column(db.Integer())
  u17 = db.Column(db.Integer())
  u18 = db.Column(db.Integer())
  u19 = db.Column(db.Integer())
  u20 = db.Column(db.Integer())
  u21 = db.Column(db.Integer())
  u22 = db.Column(db.Integer())
  u23 = db.Column(db.Integer())
  u24 = db.Column(db.Integer())
  u25 = db.Column(db.Integer())
  u26 = db.Column(db.Integer())
  u27 = db.Column(db.Integer())
  u28 = db.Column(db.Integer())
  u29 = db.Column(db.Integer())
  u30 = db.Column(db.Integer())
  u31 = db.Column(db.Integer())
  u32 = db.Column(db.Integer())
  u33 = db.Column(db.Integer())
  u34 = db.Column(db.Integer())
  u35 = db.Column(db.Integer())
  u36 = db.Column(db.Integer())
  u37 = db.Column(db.Integer())
  u38 = db.Column(db.Integer())
  u39 = db.Column(db.Integer())
  u40 = db.Column(db.Integer())
  u41 = db.Column(db.Integer())
  u42 = db.Column(db.Integer())
  u43 = db.Column(db.Integer())
  u44 = db.Column(db.Integer())
  u45 = db.Column(db.Integer())
  # ---
  district_id = db.Column(db.Integer(), nullable=True)
