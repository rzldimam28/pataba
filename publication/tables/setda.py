from publication import db

class Setda(db.Model):
  # bagian pemerintahan
  id = db.Column(db.Integer(), primary_key=True)
  tahun = db.Column(db.String(length=4), nullable=False)
  sarana_prasarana_baik = db.Column(db.Integer())
  luas_daerah = db.Column(db.Integer())
  j_pulau = db.Column(db.Integer())
  tinggi_wilayah = db.Column(db.Integer())
  jarak_ibukota = db.Column(db.Integer())
  j_bumdes_berkembang = db.Column(db.Integer())
  j_bumdes_maju = db.Column(db.Integer())
  j_bumdes_bersama_berkembang = db.Column(db.Integer())
  j_bumdes_bersama_maju = db.Column(db.Integer())
  indeks_perkembangan_kppn = db.Column(db.Integer())
  j_desa_berkembang = db.Column(db.Integer())
  j_aparatur_terlatih = db.Column(db.Integer())
  j_desa_tertib = db.Column(db.Integer())
  j_desa_batas_adminsitrasi = db.Column(db.Integer())
  penguatan_pembangunan_desa = db.Column(db.Integer())
  j_desa_tertinggal = db.Column(db.Integer())
  p_opd_internet = db.Column(db.Integer())
  r_indeks_perkembangan = db.Column(db.Integer())
  j_desa_mendukung_wisata = db.Column(db.Integer())
  j_desa_tekad = db.Column(db.Integer())
  j_desa_bumdes_produk = db.Column(db.Integer())
  j_terintegrasi_bumdes = db.Column(db.Integer())
  j_pendamping_desa = db.Column(db.Integer())
  j_kec_dana_kelurahan = db.Column(db.Integer())
  j_kab_pencegahan_stunting = db.Column(db.Integer())
  j_bumdes_ditingkatkan = db.Column(db.Integer())
  j_kawasan_dibangun = db.Column(db.Integer())
  j_desa_mandiri = db.Column(db.Integer())
  pkk_aktif = db.Column(db.Integer())
  # ---
  # 30
  cakupan_sarana_baik  = db.Column(db.Integer())
  j_kantor_baik = db.Column(db.Integer())
  j_seluruh_pemerintahan = db.Column(db.Integer())
  # 31
  r_lpm = db.Column(db.Integer())
  j_binaan_lpm = db.Column(db.Integer())
  j_lpm = db.Column(db.Integer())
  # 32
  p_lpm_aktif = db.Column(db.Integer())
  j_lsm_aktif = db.Column(db.Integer())
  j_lsm = db.Column(db.Integer())
  # 33
  r_binaan_pkk = db.Column(db.Integer())
  j_binaan_pkk = db.Column(db.Integer())
  j_pkk = db.Column(db.Integer())
  # 34
  lpm_berprestasi = db.Column(db.Integer())
  j_lpm_aktif = db.Column(db.Integer())
  j_lpm = db.Column(db.Integer())
  # 35
  swadaya_masyarakat = db.Column(db.Integer())
  j_swadaya_masyarakat = db.Column(db.Integer())
  total_swadaya_masyarakat = db.Column(db.Integer())
  # 36
  pemeliharaan_pppm  = db.Column(db.Integer())
  pppm_yg_dikembangkan = db.Column(db.Integer())
  total_pppm = db.Column(db.Integer())
  # ---
  j_lkpj = db.Column(db.Integer())
  j_executive_summary = db.Column(db.Integer())
  j_lppd = db.Column(db.Integer())
  j_ekkpd = db.Column(db.Integer())
  j_penetapan_batas = db.Column(db.Integer())
  # 42 skip
  # 43 skip
  # 44 skip
  # bagian hukum
  # 45
  j_penanganan_ham = db.Column(db.Integer())
  ham_target_nas = db.Column(db.Integer())
  ham_capaian_nas = db.Column(db.Integer())
  ham_target_kot = db.Column(db.Integer())
  ham_capaian_kot = db.Column(db.Integer())
  # 46
  j_ham_perempuan = db.Column(db.Integer())
  ham_p_target_nas = db.Column(db.Integer())
  ham_p_capaian_nas = db.Column(db.Integer())
  ham_p_target_kot = db.Column(db.Integer())
  ham_p_capaian_kot  = db.Column(db.Integer())
  # --- 
  j_data_jdih = db.Column(db.Integer())
  j_perda = db.Column(db.Integer())
  j_perwali = db.Column(db.Integer())
  j_sk = db.Column(db.Integer())
  j_mou_pks = db.Column(db.Integer())
  # bagian perekonomian
  pertumbuhan_pdrb = db.Column(db.Integer())
  laju_inflasi = db.Column(db.Integer())
  pdrb_per_kapita = db.Column(db.Integer())
  # 55
  indeks_gini = db.Column(db.Integer())
  ketimpangan_rendah = db.Column(db.Integer())
  ketimpangan_sedang = db.Column(db.Integer())
  ketimpangan_tinggi = db.Column(db.Integer())
  # 56
  pemerataan_pendapatan = db.Column(db.Integer())
  pendapatan_rendah_40 = db.Column(db.Integer())
  pendapatan_menengah_40 = db.Column(db.Integer())
  pendapatan_tinggi_20 = db.Column(db.Integer())
  # ---
  indeks_ketimpangan_williamson = db.Column(db.Integer())
  p_penduduk_diatas_kemiskinan = db.Column(db.Integer())
  # 59
  rasio_kesenjangan_kemiskinan = db.Column(db.Integer())
  garis_kemiskinan = db.Column(db.Integer())
  j_penduduk_miskin = db.Column(db.Integer())
  pendapatan_individu = db.Column(db.Integer())
  j_penduduk = db.Column(db.Integer())
  # 60
  proporsi_dibawah_1 = db.Column(db.Integer())
  j_penduduk_dibawah_1 = db.Column(db.Integer())
  j_penduduk_1 = db.Column(db.Integer())
  # 61
  ipm = db.Column(db.Integer())
  indeks_harapan_hidup = db.Column(db.Integer())
  indeks_pendidikan = db.Column(db.Integer())
  indeks_standar_hidup = db.Column(db.Integer())
  # 62
  skor_pph = db.Column(db.Integer())
  akg = db.Column(db.Integer())
  bobot_klp_pangan = db.Column(db.Integer())
  # 63
  penguatan_cadangan_pangan = db.Column(db.Integer())
  j_cadangan_pangan = db.Column(db.Integer())
  # 64
  penanganan_rawan_pangan = db.Column(db.Integer())
  pertanian = db.Column(db.Integer())
  kesehatan = db.Column(db.Integer())
  sosial_budaya = db.Column(db.Integer())
  # 65
  kontribusi_pertanian_pdrb = db.Column(db.Integer())
  j_kontribusi_pertanian_pdrb = db.Column(db.Integer())
  j_pdrb = db.Column(db.Integer())
  # 66
  kontribusi_palawijaya_pdrb = db.Column(db.Integer())
  j_kontribusi_palawijaya = db.Column(db.Integer())
  j_pdrb_pertanian = db.Column(db.Integer())
  # 67
  produksi_sektor_pertanian = db.Column(db.Integer())
  # 68
  kontribusi_tanaman_keras_pdrb = db.Column(db.Integer())
  j_kontribusi_tanaman_keras = db.Column(db.Integer())
  j_pdrb_tanaman_keras = db.Column(db.Integer())
  # 69
  kontribusi_petani_pdrb = db.Column(db.Integer())
  j_produksi_padi_lokal = db.Column(db.Integer())
  j_produksi_padi = db.Column(db.Integer())
  # 70
  kontribusi_kehutanan = db.Column(db.Integer())
  j_kontribusi_kehutanan = db.Column(db.Integer())
  j_pdrb_kehutanan = db.Column(db.Integer())
  # 71
  kontribusi_pertambangan = db.Column(db.Integer())
  j_kontribusi_pertambangan = db.Column(db.Integer())
  j_pdrb_pertambangan = db.Column(db.Integer())
  # 72
  kontribusi_pariwisata = db.Column(db.Integer())
  j_kontribusi_pariwisata = db.Column(db.Integer())
  j_pdrb_pariwisata = db.Column(db.Integer())
  # 73
  kontribusi_kelautan = db.Column(db.Integer())
  j_kontribusi_kelautan = db.Column(db.Integer())
  j_pdrb_kelautan = db.Column(db.Integer())
  # 74
  kontribusi_perdagangan = db.Column(db.Integer())
  j_kontribusi_perdagangan = db.Column(db.Integer())
  j_pdrb_perdangangan = db.Column(db.Integer())
  # 75
  kontribusi_industri = db.Column(db.Integer())
  j_kontribusi_industri = db.Column(db.Integer())
  j_pdrb_industri = db.Column(db.Integer())
  # 76
  kontribusi_rt = db.Column(db.Integer())
  j_kontribusi_rt = db.Column(db.Integer())
  j_pdrb_rt = db.Column(db.Integer())
  # 77
  pertumbuhan_industri = db.Column(db.Integer())
  j_industri_nn1 = db.Column(db.Integer())
  j_industri_n = db.Column(db.Integer())
  # 78
  kontribusi_transmigrasi_pdrb = db.Column(db.Integer())
  j_kontribusi_pdrb = db.Column(db.Integer())
  j_pdrb_transmigrasi = db.Column(db.Integer())
  # 79
  pengeluaran_konsumsi_rt = db.Column(db.Integer())
  total_pengeluaran_rt = db.Column(db.Integer())
  jumlah_rt = db.Column(db.Integer())
  # 80
  nilai_tukar_petani = db.Column(db.Integer())
  indeks_terima_petani = db.Column(db.Integer())
  indeks_bayar_petani = db.Column(db.Integer())
  # 81
  p_pengeluaran_konsumsi_non_pangan = db.Column(db.Integer())
  total_pengeluaran_rt = db.Column(db.Integer())
  total_pengeluaran = db.Column(db.Integer())
  # 82
  produktivitas_total_daerah = db.Column(db.Integer())
  nilai_tambah_sektor_i = db.Column(db.Integer())
  j_angkatan_kerja = db.Column(db.Integer())
  # 83
  desa_berstatus_swasembada = db.Column(db.Integer())
  j_desa_swasembada = db.Column(db.Integer())
  j_desa_kelurahan = db.Column(db.Integer())
  # 84
  rasio_ekspor_impor = db.Column(db.Integer())
  j_ekspor_impor = db.Column(db.Integer())
  j_pdb = db.Column(db.Integer())
  # 85
  # kegiatan_bumd = db.Column(db.Integer())
  # PDAM
  pembinaan_adm_pdam = db.Column(db.Integer())
  pembinaan_aset_pdam = db.Column(db.Integer())
  pembinaan_laporan_pdam = db.Column(db.Integer())
  realisasi_laporan_masuk_pdam = db.Column(db.Integer())
  # PERUSDA
  pembinaan_adm_perusda = db.Column(db.Integer())
  pembinaan_aset_perusda = db.Column(db.Integer())
  pembinaan_laporan_perusda = db.Column(db.Integer())
  realisasi_laporan_masuk_perusda = db.Column(db.Integer())
  # BPST
  pembinaan_adm_bpst = db.Column(db.Integer())
  pembinaan_aset_bpst = db.Column(db.Integer())
  pembinaan_laporan_bpst = db.Column(db.Integer())
  realisasi_laporan_masuk_bpst = db.Column(db.Integer())
  # CNE
  pembinaan_adm_cne = db.Column(db.Integer())
  pembinaan_aset_cne = db.Column(db.Integer())
  pembinaan_laporan_cne = db.Column(db.Integer())
  realisasi_laporan_masuk_cne = db.Column(db.Integer())
  # 86
  # kegiatan sumber daya alam
  # LPG
  pertamina_lpg = db.Column(db.Integer())
  agen_lpg = db.Column(db.Integer())
  pangkalan_lpg = db.Column(db.Integer())
  realisasi_pangkalan_lpg = db.Column(db.Integer())
  realisasi_3kg_lpg = db.Column(db.Integer())
  satgas_lpg = db.Column(db.Integer())
  # BBM
  pertamina_bbm  = db.Column(db.Integer())
  depot_bpm = db.Column(db.Integer())
  spbu_bbm = db.Column(db.Integer())
  satgas_bbm = db.Column(db.Integer())
  # 87
  # kegiatan TPID
  perkembangan_inflasi = db.Column(db.Integer())
  perkembangan_harga_bahan_pokok = db.Column(db.Integer())
  perkembangan_ketersediaan_pangan = db.Column(db.Integer())
  laporan = db.Column(db.Integer())
  pengawasan_beras_asn = db.Column(db.Integer())
  realisasi_opd = db.Column(db.Integer())
  realisasi_beras = db.Column(db.Integer())
  pengawasan_ekonomi_mikro = db.Column(db.Integer())
  mikro_terdata = db.Column(db.Integer())
  mikro_pembinaan = db.Column(db.Integer())
  mikro_laporan = db.Column(db.Integer())
  # Bagian pembangunan
  penyusunan_dokumen_ppd = db.Column(db.Integer())
  koordinasi_penyusunan_rka_dpa = db.Column(db.Integer())
  koordinasi_penyusunan_lck = db.Column(db.Integer())
  koordinasi_penyusunan_rka_skpd = db.Column(db.Integer())
  fasilitasi_penyusunan_pembangunan = db.Column(db.Integer())
  monitoring_evaluasi_pembangunan = db.Column(db.Integer())
  pengendalian_evaluasi_program = db.Column(db.Integer())
  # Bagian Organisasi
  j_daerah_rb_baik = db.Column(db.Integer())
  j_daerah_portal_elegislasi = db.Column(db.Integer())
  j_daerah_ditata = db.Column(db.Integer())
  j_daerah_ptsp = db.Column(db.Integer())
  j_perizinan = db.Column(db.Integer())
  j_pelaksaan_pks = db.Column(db.Integer())
  # Bagian Kesra
  program_bina_sosial = db.Column(db.Integer())
  pembinaan_qori_qoriah = db.Column(db.Integer())
  # 103
  itsbat_nikah = db.Column(db.Integer())
  nikah_massal = db.Column(db.Integer())
  # 104
  pembinaan_keagamaan  = db.Column(db.Integer())
  kemah_pemuda_lintas_agama = db.Column(db.Integer())
  kegiatan_lasqi = db.Column(db.Integer())
  indeks_kerukunan_umat_beragama = db.Column(db.Integer())
  # ---
  program_bina_kelembagaan = db.Column(db.Integer())
  safari_ramadhan = db.Column(db.Integer())
  keberangkatan_mtq_stq = db.Column(db.Integer())
  # 108
  # kegiatan_lppd = db.Column(db.Integer())
  tot = db.Column(db.Integer())
  pesparawi = db.Column(db.Integer())
  festival_paduan_suara = db.Column(db.Integer())
  # 109
  pemberangkatan_tphd_plw = db.Column(db.Integer())
  pemberangkatan_tphd = db.Column(db.Integer())
  domestik_transpor_haji = db.Column(db.Integer())
  # ---
  festival_raodha = db.Column(db.Integer())
  pelaksanaan_stq_mtq = db.Column(db.Integer())
  # 112
  # peringatan hari hari besar
  isra_miraj = db.Column(db.Integer())
  nyepi = db.Column(db.Integer())
  wafat_isa_almasih = db.Column(db.Integer())
  paskah = db.Column(db.Integer())
  waisak = db.Column(db.Integer())
  kenaikan_yesus = db.Column(db.Integer())
  idul_adha = db.Column(db.Integer())
  tahun_baru_hijriah = db.Column(db.Integer())
  maulid = db.Column(db.Integer())
  natal = db.Column(db.Integer())
  # 113
  pelatihan_ps_mt = db.Column(db.Integer())
  pelatihan_pegawai_syara = db.Column(db.Integer())
  porseni_majelis_talim = db.Column(db.Integer())
  pelatihan_pkd_risma = db.Column(db.Integer())
  zikir_sholawat = db.Column(db.Integer())
  safari_jumat = db.Column(db.Integer())
  # Bagian Pengadaan Barang dan Jasa
  # 114
  daftar_pelaksanaan_tender = db.Column(db.Integer())
  pengadaan_barang = db.Column(db.Integer())
  kontruksi = db.Column(db.Integer())
  konsultan = db.Column(db.Integer())
  jasa_lain = db.Column(db.Integer())
  # Bagian Umum
  evaluasi_kinerja_perangkat_daerah = db.Column(db.Integer())
  # 116
  penyediaan_gaji_tunjangan = db.Column(db.Integer())
  lka_skpd = db.Column(db.Integer())
  lkb_skpd = db.Column(db.Integer())
  # ---
  pengamanan_barang_skpd = db.Column(db.Integer())
  # 118
  penyediaan_komponen_listrik = db.Column(db.Integer())
  penyediaan_bahan_logistik = db.Column(db.Integer())
  penyediaan_barang_cetakan = db.Column(db.Integer())
  fasilitasi_kunjungan_tamu = db.Column(db.Integer())
  # 119
  penyediaan_surat_menyurat = db.Column(db.Integer())
  penyediaan_komunikasi = db.Column(db.Integer())
  penyediaan_peralatan_kantor = db.Column(db.Integer())
  penyediaan_pelayanan_kantor = db.Column(db.Integer())
  # 120
  penyediaan_pemeliharaan_pajak = db.Column(db.Integer())
  pemeliharaan_peralatan_mesin = db.Column(db.Integer())
  pemeliharaan_gedung = db.Column(db.Integer())
  pemeliharaan_sarana_prasarana = db.Column(db.Integer())
  # 121
  penyediaan_gaji_kd = db.Column(db.Integer())
  penyediaan_atribut_kd = db.Column(db.Integer())
  # 122
  penyediaan_kebutuhan_kd = db.Column(db.Integer())
  penyediaan_kebutuhan_wkd = db.Column(db.Integer())
  penyediaan_kebutuhan_sd = db.Column(db.Integer())
  # district_id = db.Column(db.Integer(), nullable=True)
  district_id = db.Column(db.Integer(), db.ForeignKey('districts.id'), nullable=True)