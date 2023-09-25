import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi
from AnaSayfa import Ui_MainWindow
from BilgisayarliGoru import Ui_BilgisayarliGoru
from MedikalTeknolojiler import Ui_Medikal
from Instagram import Ui_Instagram
from Linkedin import Ui_Linkedin
from Twitter import Ui_Twitter
from Biyoteknoloji_Inovasyon import Ui_BiyoteknolojiInovasyon
from AfetYonetimi import Ui_Afet_Yonetimi
from Web_Sayfasi import Ui_Web_Sayfasi
from Iletisim import Ui_Iletisim
from SaglikVeIlkYardim import Ui_SaglikVeIlkYardim
import logo_rc

class MyMainWindow(QMainWindow):
        def __init__(self):
            super(MyMainWindow, self).__init__()


            loadUi('Anasayfa.ui', self)

            self.pushButton.clicked.connect(self.afet_yonetimi)
            self.pushButton_2.clicked.connect(self.saglik_ve_ilk_yardim)
            self.pushButton_3.clicked.connect(self.bilgisayarli_goru)
            self.pushButton_4.clicked.connect(self.biyoteknoloji_inovasyon)
            self.pushButton_5.clicked.connect(self.medikal_teknolojiler)
            self.pushButton_6.clicked.connect(self.web_sayfasi)
            self.pushButton_7.clicked.connect(self.instagram_sayfasi)
            self.pushButton_8.clicked.connect(self.twitter_sayfasi)
            self.pushButton_9.clicked.connect(self.linkedin_sayfasi)
            self.pushButton_10.clicked.connect(self.iletisim_sayfasi)


        def medikal_teknolojiler(self):
            self.medikal_teknolojiler_window = QWidget()
            ui = Ui_Medikal()
            ui.setupUi(self.medikal_teknolojiler_window)
            self.medikal_teknolojiler_window.show()
        def bilgisayarli_goru(self):
            self.bilgisayarli_goru_window = QWidget()
            ui = Ui_BilgisayarliGoru()
            ui.setupUi(self.bilgisayarli_goru_window)
            self.bilgisayarli_goru_window.show()

        def saglik_ve_ilk_yardim(self):
            self.saglik_ve_ilk_yardim_window = QWidget()
            ui = Ui_SaglikVeIlkYardim()
            ui.setupUi(self.saglik_ve_ilk_yardim_window)
            self.saglik_ve_ilk_yardim_window.show() 
            
        def iletisim_sayfasi(self):
            self.iletisim_sayfasi_window = QWidget()
            ui = Ui_Iletisim()
            ui.setupUi(self.iletisim_sayfasi_window)
            self.iletisim_sayfasi_window.show()       

        def biyoteknoloji_inovasyon(self):
            self.biyoteknoloji_inovasyon_window = QWidget()
            ui = Ui_BiyoteknolojiInovasyon()
            ui.setupUi(self.biyoteknoloji_inovasyon_window)
            self.biyoteknoloji_inovasyon_window.show()

        def afet_yonetimi(self):
            self.afet_yonetimi_window = QWidget()
            ui = Ui_Afet_Yonetimi()
            ui.setupUi(self.afet_yonetimi_window)
            self.afet_yonetimi_window.show()

        def web_sayfasi(self):
            self.web_sayfasi_window = QWidget()
            ui = Ui_Web_Sayfasi()
            ui.setupUi(self.web_sayfasi_window)
            self.web_sayfasi_window.show()

        def instagram_sayfasi(self):
            self.instagram_sayfasi_window = QWidget()
            ui = Ui_Instagram()
            ui.setupUi(self.instagram_sayfasi_window)
            self.instagram_sayfasi_window.show()

        def linkedin_sayfasi(self):
            self.linkedin_sayfasi_window = QWidget()
            ui = Ui_Linkedin()
            ui.setupUi(self.linkedin_sayfasi_window)
            self.linkedin_sayfasi_window.show()

        def twitter_sayfasi(self):
            self.twitter_sayfasi_window = QWidget()
            ui = Ui_Twitter()
            ui.setupUi(self.twitter_sayfasi_window)
            self.twitter_sayfasi_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())