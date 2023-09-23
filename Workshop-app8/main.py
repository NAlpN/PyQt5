import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QHeaderView, QTableWidgetItem, QMessageBox, QDialog
from HastaKaydıUI import *
from hakkinda import *

uygulama = QApplication(sys.argv)
pencere = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()

penhakkinda = QDialog()
ui2 = Ui_Dialog()
ui2.setupUi(penhakkinda)


import sqlite3
global curs
global conn

conn = sqlite3.connect('HastaVerisi.db')
curs = conn.cursor()
sorgu = ("CREATE TABLE IF NOT EXISTS spor                     \
         (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,      \
          TCNo TEXT NOT NULL UNIQUE,                          \
          HastaAdi TEXT NOT NULL,                             \
          HastaSoyadi TEXT NOT NULL,                          \
          HastaneAdi TEXT NOT NULL,                           \
          Sikayet TEXT NOT NULL ,                             \
          Cinsiyet TEXT NOT NULL,                             \
          DogumTarihi TEXT NOT NULL,                          \
          MedeniHal TEXT NOT NULL,                            \
          Kilo TEXT NOT NULL)")
curs.execute(sorgu)
conn.commit()

def ekle():
    _lneTC = ui.lneTC.text()
    _lneAd = ui.lneAd.text()
    _lneSoyad = ui.lneSoyad.text()
    _cmbHastaneAdi = ui.cmbHastaneAdi.currentText()
    _lswSikayet = ui.lswSikayet.currentItem().text()
    _cmbCinsiyet = ui.cmbCinsiyet.currentText()
    _clwDgTarihi = ui.clwDgTarihi.selectedDate().toString(QtCore.Qt.ISODate)
    if ui.cbxMedeniHal.isChecked():
        _medeniHal = "Evli"
    else:
        _medeniHal = "Bekar"
    _spnKilo = ui.spnKilo.value()
    curs.execute("INSERT INTO spor \
                (TCNo, HastaAdi, HastaSoyadi, HastaneAdi, Sikayet, Cinsiyet, DogumTarihi, MedeniHal, Kilo) \
                VALUES (?,?,?,?,?,?,?,?,?)", \
                (_lneTC, _lneAd, _lneSoyad, _cmbHastaneAdi, _lswSikayet, _cmbCinsiyet, _clwDgTarihi, _medeniHal, _spnKilo))
    conn.commit()
    LISTELE()

def LISTELE():
    ui.tblwListe.clear()
    ui.tblwListe.setHorizontalHeaderLabels(('No', 'TC Kimlik No', 'Hasta Adı', 'Hasta Soyadı', \
                                            'Hastane Adı', 'Şikayet', 'Cinsiyet', 'Doğum Tarihi', \
                                            'Medeni Hal', 'Hasta Kilosu'))
    ui.tblwListe.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    curs.execute("SELECT * FROM spor")
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblwListe.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
    ui.lneTC.clear()
    ui.lneAd.clear()
    ui.lneSoyad.clear()
    ui.cmbHastaneAdi.setCurrentIndex(-1)
    ui.spnKilo.setValue(-1)
    curs.execute("SELECT COUNT(*) FROM spor")
    KayitSayisi = curs.fetchone()   
    ui.lblToplam.setText(str(KayitSayisi[0]))

LISTELE()

def Cikis():
    cevap = QMessageBox.question(pencere, "ÇIKIŞ", "Çıkmak İstediğinize Emin Misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        conn.close()
        sys.exit(uygulama.exec_())
    else:
        pencere.show()

def sil():
        cevap = QMessageBox.question(pencere, "KAYIT SİL", "Kaydı silmek istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
        if cevap == QMessageBox.Yes:
            secilen = ui.tblwListe.selectedItems()
            silinecek = secilen[1].text()
            try:
                curs.execute("DELETE FROM spor WHERE TCNo='%s'"%(silinecek))
                conn.commit()
                LISTELE()
                ui.statusbar.showMessage("Kayıt silme işlemi başarılı...", 10000)
            except Exception as Hata:
                ui.statusbar.showMessage("Bir hata ile karşılaşıldı:" + str(Hata))
        else:
            ui.statusbar.showMessage("Silme işlemi iptal edildi..", 10000)
def Ara():
    ara1 = ui.lneTC.text()            
    ara2 = ui.lneAd.text()
    ara3 = ui.lneSoyad.text()
    curs.execute("SELECT * FROM spor WHERE TCNo=? OR HastaAdi=? OR HastaSoyadi=? OR (HastaAdi=? AND HastaSoyadi=?)", \
                 (ara1,ara2,ara3,ara2,ara3))
    conn.commit()
    ui.tblwListe.clear()
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblwListe.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
def Doldur():
    secili = ui.tblwListe.selectedItems()
    if len(secili) >= 9:
        ui.lneTC.setText(secili[1].text())
        ui.lneAd.setText(secili[2].text())            
        ui.lneSoyad.setText(secili[3].text())            
        ui.cmbHastaneAdi.setCurrentText(secili[4].text())
    
        if secili[5].text() == "Şok":
            ui.lswSikayet.item(0).setSelected(True)
            ui.lswSikayet.setCurrentItem(ui.lswSikayet.item(0))
        elif secili[5].text() == "Kalp Ağrısı":
            ui.lswSikayet.item(1).setSelected(True)
            ui.lswSikayet.setCurrentItem(ui.lswSikayet.item(1)) 
        elif secili[5].text() == "Solunum Sıkıntısı":
            ui.lswSikayet.item(2).setSelected(True)
            ui.lswSikayet.setCurrentItem(ui.lswSikayet.item(2))
        elif secili[5].text() == "Zehirlenme":
            ui.lswSikayet.item(3).setSelected(True)
            ui.lswSikayet.setCurrentItem(ui.lswSikayet.item(3))            
        elif secili[5].text() == "Doğum":
            ui.lswSikayet.item(4).setSelected(True)
            ui.lswSikayet.setCurrentItem(ui.lswSikayet.item(4))
        elif secili[5].text() == "Karın Ağrısı":
            ui.lswSikayet.item(5).setSelected(True)
            ui.lswSikayet.setCurrentItem(ui.lswSikayet.item(5))
        elif secili[5].text() == "Yanık":
            ui.lswSikayet.item(6).setSelected(True)
            ui.lswSikayet.setCurrentItem(ui.lswSikayet.item(6)) 
        elif secili[5].text() == "Kırık":
            ui.lswSikayet.item(7).setSelected(True)
            ui.lswSikayet.setCurrentItem(ui.lswSikayet.item(7)) 
        elif secili[5].text() == "Kanamalar":
            ui.lswSikayet.item(8).setSelected(True)
            ui.lswSikayet.setCurrentItem(ui.lswSikayet.item(8)) 
        elif secili[5].text() == "Baş Ağrısı":
            ui.lswSikayet.item(9).setSelected(True)
            ui.lswSikayet.setCurrentItem(ui.lswSikayet.item(9)) 
        elif secili[5].text() == "Soğuk Algınlığı Şikayetleri":
            ui.lswSikayet.item(10).setSelected(True)
            ui.lswSikayet.setCurrentItem(ui.lswSikayet.item(10))
    
        ui.cmbCinsiyet.setCurrentText(secili[6].text())
        yil = int(secili[7].text()[0:4])        
        ay = int(secili[7].text()[5:7])
        gun = int(secili[7].text()[8:10])
        ui.clwDgTarihi.setSelectedDate(QtCore.QDate(yil,ay,gun))

        if secili[8].text() == "Evli":
            ui.cbxMedeniHal.setChecked(True)
        else:
            ui.cbxMedeniHal.setChecked(False)    

        ui.spnKilo.setValue(int(secili[9].text()))
    else:
        ui.statusbar.showMessage("Bir satır seçilmedi.", 5000)    

def Guncelle():
    try:
        cevap = QMessageBox.question(pencere, "KAYIT GÜNCELLE", "Kaydı güncellemek istediğinize emin misiniz?", QMessageBox.Yes | QMessageBox.No)
        if cevap == QMessageBox.Yes:    
                secili = ui.tblwListe.selectedItems()
                _Id = int(secili[0].text())
                _lneTC = ui.lneTC.text()
                _lneAd = ui.lneAd.text()
                _lneSoyad = ui.lneSoyad.text()
                _cmbHastaneAdi = ui.cmbHastaneAdi.currentText()
                _lswSikayet = ui.lswSikayet.currentItem().text()
                _cmbCinsiyet = ui.cmbCinsiyet.currentText()
                _clwDgTarihi = ui.clwDgTarihi.selectedDate().toString(QtCore.Qt.ISODate)
                
                if ui.cbxMedeniHal.isChecked():
                    _medeniHal = "Evli"
                else:
                    _medeniHal = "Bekar"
                
                _spnKilo = ui.spnKilo.value()

                curs.execute("UPDATE spor SET TCNo=?, HastaAdi=?, HastaSoyadi=?, HastaneAdi=?, Sikayet=?, \
                Cinsiyet=?, DogumTarihi=?, MedeniHal=?, Kilo=? WHERE Id=?", \
                (_lneTC, _lneAd, _lneSoyad, _cmbHastaneAdi, _lswSikayet, _cmbCinsiyet, _clwDgTarihi, _medeniHal, _spnKilo, _Id))
                conn.commit()
                LISTELE()
    except Exception as Hata:
        ui.statusbar.showMessage("Bir hata ile karşılaşıldı:"+str(Hata))
    else:
        ui.statusbar.showMessage("Güncelleme iptal edildi..", 10000)
def Hakkinda():
    penhakkinda.show()

    

ui.btnCikis.clicked.connect(Cikis)
ui.btnEkle.clicked.connect(ekle)
ui.btnListele.clicked.connect(LISTELE)
ui.btnSil.clicked.connect(sil)
ui.btnAra.clicked.connect(Ara)
ui.tblwListe.itemSelectionChanged.connect(Doldur)
ui.btnGuncelle.clicked.connect(Guncelle)
ui.menuHakkinda.triggered.connect(Hakkinda)

sys.exit(uygulama.exec_())
