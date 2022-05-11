from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Login')

class EditTableForm(FlaskForm):
  tahun = IntegerField('Tahun', validators=[DataRequired()])
  col1 = IntegerField('Col1')
  col2 = IntegerField('Col2')
  col3 = IntegerField('Col3')
  district_id = SelectField('Kecamatan', choices=[(None, 'Kota Palu'), (1, 'Palu Barat'), (2, 'Palu Selatan'), (3, 'Tatanga'), (4, 'Ulujadi'), (5, 'Mantikulore'), (6, 'Palu Timur'), (7, 'Palu Utara'), (8, 'Tawaili')])
  submit = SubmitField('Submit')
  
class FormSetda(FlaskForm):
  # bagian pemerintahan
  tahun = IntegerField('Tahun', validators=[DataRequired()])
  # ---
  u1 = IntegerField('Cakupan Sarana Prasarana Perkantoran Pemerintahan Desa yang Baik')
  u2 = IntegerField('Luas Daerah')
  u3 = IntegerField('Jumlah Pulau')
  u4 = IntegerField('Tinggi Wilayah')
  u5 = IntegerField('Jarak Ke Ibukota')
  u6 = IntegerField('Jumlah Revitalisasi Bumdes Berkembang')
  u7 = IntegerField('Jumlah Revitalisasi Bumdes Maju')
  u8 = IntegerField('Jumlah Revitalisasi Bumdes Bersama Berkembang')
  u9 = IntegerField('Jumlah Revitalisasi Bumdes Bersama Maju')
  u10 = IntegerField('Rata-Rata Nilai Indeks Perkembangan 62 Kawasan Perdesaan Prioritas Nasional (KPPN)')
  u11 = IntegerField('Jumlah Desa Berkembang')
  u12 = IntegerField('Jumlah Aparatur Pemerintahan Desa dan Pengurus Lembaga Kemasyarakatan Desa Lingkup Regional yang Terlatih')
  u13 = IntegerField('Jumlah Desa yang Desanya Tertib Administrasi Pengelolaan Aset Desa')
  u14 = IntegerField('Jumlah Desa yang Telah Memiliki Batas Wilayah Administrasi Desa')
  u15 = IntegerField('Penguatan Pemerintahan dan Pembangunan Desa')
  u16 = IntegerField('Jumlah Desa Tertinggal')
  u17 = IntegerField('Persentase Organisasi Perangkat Daerah yang Terhubung dengan Akses Internet')
  u18 = IntegerField('Rata-Rata Nilai Indeks Perkembangan 50 Kawasan Perdesaan Prioritas Kementerian')
  u19 = IntegerField('Jumlah Desa yang Dibangun Sarana dan Prasarananya ')
  u20 = IntegerField('Jumlah Desa yang Memperoleh Bantuan Pendampingan Melalui Program TEKAD')
  u21 = IntegerField('Jumlah Desa yang Mengembangkan BUMDES untuk Mendukung Produk Unggulan Desa')
  u22 = IntegerField('Jumlah Desa yang Mengembangkan Usaha Ekonomi Desa yang Terintegrasi dengan BUMDES')
  u23 = IntegerField('Jumlah Pendamping Desa yang Melakukan Pendampingan pada 74957 Desa')
  u24 = IntegerField('Jumlah Kecamatan yang Melakukan Pengendalian Penggunaan Dana Kelurahan')
  u25 = IntegerField('Jumlah Kabupaten yang Melakukan Konvergensi Pencegahan Stunting Di Desa')
  u26 = IntegerField('Jumlah BUMDES bersama yang Ditingkatkan Kapasitas dan Pemasarannya')
  u27 = IntegerField('Jumlah Kawasan yang Dibangun, Dikembangkan, dan Direhabilitasi Sarana Prasarana Ekonomi di Kawasan Perdesaannya')
  u28 = IntegerField('Jumlah Desa Mandiri')
  u29 = IntegerField('PKK Aktif')
  u30 = IntegerField('Jumah Kantor Pemerintahan Desa yang Baik')
  u31 = IntegerField('Jumlah Seluruh Pemerintahan Desa')
  u32 = IntegerField('Jumlah Kelompok Binaan LPM')
  u33 = IntegerField('Jumlah LPM')
  u34 = IntegerField('Jumlah LSM Aktif')
  u35 = IntegerField('Jumlah LSM')
  u36 = IntegerField('Jumlah Kelompok Binaan PKK')
  u37 = IntegerField('Jumlah PKK')
  u38 = IntegerField('Jumlah LPM Aktif')
  u39 = IntegerField('Jumlah LPM')
  u40 = IntegerField('Jumlah Swadaya Masyarakat Mendukung Program Pemberdayaan Masyarakat')
  u41 = IntegerField('Total Program Pemberdayaan Masyarakat')
  u42 = IntegerField('Program Pemberdayaan Masyarakat yang Dikembangkan dan Diperlihara Masyarakat')
  u43 = IntegerField('Total Pasca Program Pemberdayaan Masyarakat')
  u44 = IntegerField('Jumlah Laporan Keterangan Pertanggungjawaban Walikota')
  u45 = IntegerField('Jumlah Executive Summary')
  u46 = IntegerField('Jumlah Laporan Penyelenggara Pemerintah Daerah (LPPD)')
  u47 = IntegerField('Jumlah Evaluasi Kinerja Penyelenggara Pemerintah Daerah (EKKPD)')
  u48 = IntegerField('Jumlah Berita Acara Penetapan dan Penegasan Batas')
  u49 = IntegerField('Jumlah Pemasangan Tugu Kapal Batas Kelurahan dan Kecamatan')
  u50 = IntegerField('Jumlah Pemantauan Lingkungan dan Evaluasi Kinerja Kecamatan dan Kelurharan')
  u51 = IntegerField('Jumlah Pembakuan Rupabumi (Toponimi) Menurut Kecamatan')
  # Bagian 2 (Hukum)
  u52 = IntegerField('Target Nasional')
  u53 = IntegerField('Capaian Nasional')
  u54 = IntegerField('Target Kota')
  u55 = IntegerField('Capaian Kota')
  u56 = IntegerField('Bantuan Hukum Bagi Masyarakat Miskin')
  u57 = IntegerField('Target Nasional')
  u58 = IntegerField('Capaian Nasional')
  u59 = IntegerField('Target Kota')
  u60 = IntegerField('Capaian Kota')
  u61 = IntegerField('Jumlah Data JDIH')
  u62 = IntegerField('Jumlah Peraturan Daerah')
  u63 = IntegerField('Jumlah Perwali')
  u64 = IntegerField('Jumlah Surat Keputusan')
  u65 = IntegerField('Jumlah MOU/PKS')
  # Bagian 3 (Perekonomian)
  u66 = IntegerField('Pertumbuhan PDRB')
  u67 = IntegerField('Laju Inflasi')
  u68 = IntegerField('PDRB per Kapita')
  u69 = IntegerField('Ketimpangan Rendah')
  u70 = IntegerField('Ketimpangan Sedang')
  u71 = IntegerField('Ketimpangan Tinggi')
  u72 = IntegerField('40% Penduduk Berpenghasilan Rendah')
  u73 = IntegerField('40% Penduduk Berpenghasilan Menengah')
  u74 = IntegerField('40% Penduduk Berpenghasilan Tinggi')
  u75 = IntegerField('Indeks Ketimpangan Wiliamson')
  u76 = IntegerField('Persentase Penduduk di Atas Garis Kemiskinan')
  u77 = IntegerField('Garis Kemiskinan')
  u78 = IntegerField('Jumlah Penduduk Miskin')
  u79 = IntegerField('Pendapatan Individu Penduduk Miskin')
  u80 = IntegerField('Jumlah Penduduk')
  u81 = IntegerField('Jumlah Penduduk Miskin dengan Pendapatan di Bawah $1 PPP')
  u82 = IntegerField('Jumlah Penduduk')
  u83 = IntegerField('Indeks Harapan Hidup')
  u84 = IntegerField('Indeks Harapan')
  u85 = IntegerField('Indeks Standar Hidup Layak')
  u86 = IntegerField('Angka Kecukupan Gizi (AKG)')
  u87 = IntegerField('Bobot Masing-Masing Kelompok Pangan')
  u88 = IntegerField('Jumlah Cadangan Pangan Kabupaten/Kota')
  u89 = IntegerField('Pertanian: Ketersediaan Pangan')
  u90 = IntegerField('Kesehatan: Preferensi Energi')
  u91 = IntegerField('Sosial Budaya: Kemiskinan')
  u92 = IntegerField('Jumlah Kontribusi PDRB dari Sektor Pertanian/ Perkebunan')
  u93 = IntegerField('Jumlah PDRB')
  u94 = IntegerField('Jumlah Kontribusi Sektor Pertanian (Palawijaya)')
  u95 = IntegerField('Jumlah PDRB Sektor Pertanian/ Perkebunan')
  u96 = IntegerField('Produksi Sektor Pertanian')
  u97 = IntegerField('Jumlah Kontribusi Perkebunan (Tanaman Keras)')
  u98 = IntegerField('Jumlah PDRB Sektor Pertanian/ perkebunan')
  u99 = IntegerField('Jumlah Produksi Padi/ Bahan Pangan Utama Lokal Hasil Kelompok Petani (ton)')
  u100 = IntegerField('Jumlah Produksi Padi/ Bahan Pangan Utama di Daerah (ton)')
  u101 = IntegerField('Jumlah Kontribusi PDRB dari Sektor Kehutanan')
  u102 = IntegerField('Jumlah PDRB')
  u103 = IntegerField('Jumlah Kontribusi PDRB dari Sektor Pertambangan')
  u104 = IntegerField('Jumlah PDRB')
  u105 = IntegerField('Jumlah Kontribusi PDRB dari Sektor Pariwisata')
  u106 = IntegerField('Jumlah PDRB')
  u107 = IntegerField('Jumlah Kontribusi PDRB dari Sektor Kelautan dan Perikanan')
  u108 = IntegerField('Jumlah PDRB')
  u109 = IntegerField('Jumlah Kontribusi PDRB dari Sektor Perdagangan')
  u110 = IntegerField('Jumlah PDRB')
  u111 = IntegerField('Jumlah Kontribusi PDRB dari Sektor Industri')
  u112 = IntegerField('Jumlah PDRB')
  u113 = IntegerField('Jumlah Kontribusi PDRB dari Sektor Rumah Tangga')
  u114 = IntegerField('Jumlah PDRB Sektor Industri')
  u115 = IntegerField('Jumlah Industri Tahun n - Jumlah Industri Tahun (n-1)')
  u116 = IntegerField('Jumlah Industri s/d Tahun n')
  u117 = IntegerField('Jumlah Kontribusi PDRB dari Transmigrasi')
  u118 = IntegerField('Jumlah PDRB')
  u119 = IntegerField('Total Pengeluaran RT')
  u120 = IntegerField('Jumlah RT')
  u121 = IntegerField('Indeks yang Diterima Petani')
  u122 = IntegerField('Indeks yang Dibayar Petani')
  u123 = IntegerField('Total Pengeluaran RT Non Pangan')
  u124 = IntegerField('Total Pengeluaran')
  u125 = IntegerField('Nilai Tambah Sektor ke-i')
  u126 = IntegerField('Jumlah Angkatan Kerja')
  u127 = IntegerField('Jumlah Desa atau Kelurahan Berswasembada')
  u128 = IntegerField('Jumlah Desa atau Kelurahan')
  u129 = IntegerField('Jumlah Ekspor dan Impor Barang dan Jasa')
  u130 = IntegerField('PDB')
  u131 = IntegerField('Pembinaan Administrasi')
  u132 = IntegerField('Pembinaan Aset')
  u133 = IntegerField('Pembinaan Laporan')
  u134 = IntegerField('Realisasi Laporan Masuk')
  u135 = IntegerField('Pembinaan Administrasi')
  u136 = IntegerField('Pembinaan Aset')
  u137 = IntegerField('Pembinaan Laporan')
  u138 = IntegerField('Pembinaan Laporan Masuk')
  u139 = IntegerField('Pembinaan Administrasi')
  u140 = IntegerField('Pembinaan Aset')
  u141 = IntegerField('Pembinaan Laporan')
  u142 = IntegerField('Pembinaan Laporan Masuk')
  u143 = IntegerField('Pembinaan Administrasi')
  u144 = IntegerField('Pembinaan Aset')
  u145 = IntegerField('Pembinaan Laporan')
  u146 = IntegerField('Realisasi Laporan Masuk')
  u147 = IntegerField('Pertamina')
  u148 = IntegerField('Agen')
  u149 = IntegerField('Pangkalan')
  u150 = IntegerField('Realisasi Pangkalan')
  u151 = IntegerField('Realisasi LPG 3 Kilo')
  u152 = IntegerField('Satgas LPG')
  u153 = IntegerField('Pertamina')
  u154 = IntegerField('Depot')
  u155 = IntegerField('SPBU')
  u156 = IntegerField('Satgas BBM')
  u157 = IntegerField('Perkembangan Inflasi')
  u158 = IntegerField('Perkembangan Harga dan Bahan Pokok')
  u159 = IntegerField('Perkembangan Ketersidiaan Pangan Strategis')
  u160 = IntegerField('Laporan')
  u161 = IntegerField('Realisasi OPD')
  u162 = IntegerField('Realisasi Beras')
  u163 = IntegerField('Yang Terdata')
  u164 = IntegerField('Pembinaan')
  u165 = IntegerField('Laporan')
  # Bagian 4 (Pembangunan) 
  u166 = IntegerField('Penyusunan Dokumen Perencanaan Perangkat Daerah')
  u167 = IntegerField('Koordinasi dan Penyusunan Dokumen RKA-DPA')
  u168 = IntegerField('Koordinasi dan Penyusunan Laporan Capaian Kinerja dan Iktisiar Realisasi Kinerja SKPD')
  u169 = IntegerField('Koordinasi dan Penyusunan Dokumen Perubahan RKA-SKPD')
  u170 = IntegerField('Fasilitasi Penyusunan Program Pembangunan')
  u171 = IntegerField('Monitoring dan Evaluasi Program Pembangunan')
  u172 = IntegerField('Pengendalian dan Evaluasi Pelaksanaan Program')
  # Bagian 5 (Organisasi)
  u173 = IntegerField('Jumlah Daerah Provinsi dengan Indeks RB >= Baik')
  u174 = IntegerField('Jumlah Daerah yang Membentuk Portal e-Legislasi')
  u175 = IntegerField('Jumlah Daerah yang Ditata dan Diselesaikan Permasalahan Kelembagaan dan Kepegawaian Perangkat Daerah')
  u176 = IntegerField('Jumlah Daerah yang Memiliki PTSP PRima Berbasis Elektronik')
  u177 = IntegerField('Jumlah Perizinan dengan Kewenangan Sudah Didelegasikan ke PTSP Prima Berbasis Elektronik')
  u178 = IntegerField('Jumlah Pelaksanaan Perjanjian Kerja Sama dakam Permasalahan Pelayanan Publik')
  # Bagian 6 (Kesra)
  u179 = IntegerField('Program Bina Sosial')
  u180 = IntegerField('Pembinaan Qori dan Qoriah')
  u181 = IntegerField('Itsbat Nikah')
  u182 = IntegerField('Nikah Massal')
  u183 = IntegerField('Kemah Pemuda Lintas Agama')
  u184 = IntegerField('Kegiatan Lembaga Seni Qasidah (LASQI) Kota Palu')
  u185 = IntegerField('Indeks Kerukunan Umat Beragama')
  u186 = IntegerField('Program Bina Kelembagaan')
  u187 = IntegerField('Safari Ramadhan Pemerintah Kota Palu')
  u188 = IntegerField('Keberangkatan Kafilah Kota Palu pada STQ/MTQ Tingkat Provinsi Sulteng')
  u189 = IntegerField('TOT')
  u190 = IntegerField('PESPARAWI')
  u191 = IntegerField('Festival Faduan Suara')
  u192 = IntegerField('Pemberangkatan TPHD')
  u193 = IntegerField('Domestik Transportasi Jamaah Haji')
  u194 = IntegerField('Festival RAODHA Sis Aljufrie')
  u195 = IntegerField('Pelaksanaan STQ/MTQ Tingkat Kota Palu')
  u196 = IntegerField('Isra Miraj')
  u197 = IntegerField('Nyepi')
  u198 = IntegerField('Wafat Isa Almasih')
  u199 = IntegerField('Paskah')
  u200 = IntegerField('Waisak')
  u201 = IntegerField('Kenaikan Yesus Kristus')
  u202 = IntegerField('Idul Adha')
  u203 = IntegerField('Tahun Baru Hijriah')
  u204 = IntegerField('Maulid Nabi Muhammad')
  u205 = IntegerField('Natal')
  u206 = IntegerField('Pelatihan Pegawai Syara')
  u207 = IntegerField('PORSENI Majelis Talim')
  u208 = IntegerField('Pelatihan PKD Risma')
  u209 = IntegerField('Zikir dan Shalawatan')
  u210 = IntegerField('Safari Jumat')
  # Bagian 7 (Pengadaan Barang dan Jasa)
  u211 = IntegerField('Pengadaan Barang')
  u212 = IntegerField('Konstruksi')
  u213 = IntegerField('Konsultan')
  u214 = IntegerField('Jasa Lainnya')
  # Bagian 8 (Umum)
  u215 = IntegerField('Evaluasi Kinerja Perangkat Daerah')
  u216 = IntegerField('Penyediaan Gaji dan Tunjangan ASN')
  u217 = IntegerField('Koordinasi dan Penyusunan Laporan Keuangan Akhir Tahun SKPD')
  u218 = IntegerField('Koordinasi dan Penyusunan Laporan Keuangan Bulanan/Triwulan/Semesteran SKPD')
  u219 = IntegerField('Pengamanan Barang Milik Daerah SKPD')
  u220 = IntegerField('Penyediaan Komponen Instalasi Listrik/ Penerangan Bangunan Kantor')
  u221 = IntegerField('Penyediaan Bahan Logistik Kantor')
  u222 = IntegerField('Penyediaan Barang Cetakan dan Penggandaan')
  u223 = IntegerField('Fasilitasi Kunjungan Tamu')
  u224 = IntegerField('Penyediaan Jasa Surat Menyurat')
  u225 = IntegerField('Penyediaan Jasa Komunikasi, Sumber Daya Air dan Listrik')
  u226 = IntegerField('Penyediaan Jasa Peralatan dan Perlengkapan Kantor')
  u227 = IntegerField('Penyediaan Jasa Pelayanan Umum Kantor')
  u228 = IntegerField('Penyediaan Jasa Pemeliharaan, Biaya Pemeliharaan dan Pajak Kendaraan Perorangan Dinas')
  u229 = IntegerField('Pemelihraan Peralatan dan Mesin Lainnya')
  u230 = IntegerField('Pemeliharaan/ Rehabilitasi Gedung Kantor dan Bangunan Lainnya')
  u231 = IntegerField('Pemeliharaan/ Rehabilitasi Sarana dan Prasarana Pendukung Gedung Kantor Bangunan Lainnya')
  u232 = IntegerField('Penyediaan Gaji dan Tunjangan Kepala Daerah')
  u233 = IntegerField('Penyediaan Pakaian Dinas dan Atribut Kelengkapan KDH dan WKDH')
  u234 = IntegerField('Penyediaan Kebutuhan Rumah Tangga Kepala Daerah')
  u235 = IntegerField('Penyediaan Kebutuhan Rumah Tangga Wakil Kepala Daerah')
  u236 = IntegerField('Penyediaan Kebutuhan Rumah Tangga Sekretariat Daerah')
  # ---
  district_id = SelectField('Kecamatan', choices=[(None, 'Kota Palu'), (1, 'Palu Barat'), (2, 'Palu Selatan'), (3, 'Tatanga'), (4, 'Ulujadi'), (5, 'Mantikulore'), (6, 'Palu Timur'), (7, 'Palu Utara'), (8, 'Tawaili')])
  submit = SubmitField('Tambahkan')

class FormDprd(FlaskForm):
  tahun = IntegerField('Tahun', validators=[DataRequired()])
  # ---
  u1 = IntegerField('Pertanyaan')
  u2 = IntegerField('Pertanyaan')
  u3 = IntegerField('Pertanyaan')
  u4 = IntegerField('Pertanyaan')
  u5 = IntegerField('Pertanyaan')
  u6 = IntegerField('Pertanyaan')
  u7 = IntegerField('Pertanyaan')
  u8 = IntegerField('Pertanyaan')
  u9 = IntegerField('Pertanyaan')
  u10 = IntegerField('Pertanyaan')
  u11 = IntegerField('Pertanyaan')
  u12 = IntegerField('Pertanyaan')
  u13 = IntegerField('Pertanyaan')
  u14 = IntegerField('Pertanyaan')
  u15 = IntegerField('Pertanyaan')
  u16 = IntegerField('Pertanyaan')
  u17 = IntegerField('Pertanyaan')
  u18 = IntegerField('Pertanyaan')
  u19 = IntegerField('Pertanyaan')
  u20 = IntegerField('Pertanyaan')
  u21 = IntegerField('Pertanyaan')
  u22 = IntegerField('Pertanyaan')
  u23 = IntegerField('Pertanyaan')
  u24 = IntegerField('Pertanyaan')
  u25 = IntegerField('Pertanyaan')
  u26 = IntegerField('Pertanyaan')
  u27 = IntegerField('Pertanyaan')
  u28 = IntegerField('Pertanyaan')
  u29 = IntegerField('Pertanyaan')
  u30 = IntegerField('Pertanyaan')
  u31 = IntegerField('Pertanyaan')
  u32 = IntegerField('Pertanyaan')
  u33 = IntegerField('Pertanyaan')
  u34 = IntegerField('Pertanyaan')
  u35 = IntegerField('Pertanyaan')
  u36 = IntegerField('Pertanyaan')
  u37 = IntegerField('Pertanyaan')
  u38 = IntegerField('Pertanyaan')
  u39 = IntegerField('Pertanyaan')
  u40 = IntegerField('Pertanyaan')
  u41 = IntegerField('Pertanyaan')
  u42 = IntegerField('Pertanyaan')
  u43 = IntegerField('Pertanyaan')
  u44 = IntegerField('Pertanyaan')
  u45 = IntegerField('Pertanyaan')
  # ---
  district_id = SelectField('Kecamatan', choices=[(None, 'Kota Palu'), (1, 'Palu Barat'), (2, 'Palu Selatan'), (3, 'Tatanga'), (4, 'Ulujadi'), (5, 'Mantikulore'), (6, 'Palu Timur'), (7, 'Palu Utara'), (8, 'Tawaili')])
  submit = SubmitField('Tambahkan')

