import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi
from BilgisayarlıGörü import Ui_Form2
from MedikalTeknolojiler import Ui_Form6
from Instagram import Ui_Form4
from Linkedin import Ui_Form5
from Twitter import Ui_Form8
from BiyoteknolojiInovasyon import Ui_Form3
from AfetYönetimi import Ui_Form
from WebSayfası import Ui_Form9
import logo_rc

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()


        loadUi('SYZ_Arayüz.ui', self)

        self.pushButton.clicked.connect(self.medikal_teknolojiler)
        self.pushButton_2.clicked.connect(self.bilgisayarli_goru)
        self.pushButton_3.clicked.connect(self.biyoteknoloji_inovasyon)
        self.pushButton_4.clicked.connect(self.afet_yonetimi)
        self.pushButton_5.clicked.connect(self.web_sayfasi)
        self.pushButton_6.clicked.connect(self.instagram_sayfasi)
        self.pushButton_7.clicked.connect(self.linkedin_sayfasi)
        self.pushButton_8.clicked.connect(self.twitter_sayfasi)

    def medikal_teknolojiler(self):
        self.medikal_teknolojiler_window = QWidget()
        ui = Ui_Form6()
        ui.setupUi(self.medikal_teknolojiler_window)
        self.medikal_teknolojiler_window.show()
    def bilgisayarli_goru(self):
        self.bilgisayarli_goru_window = QWidget()
        ui = Ui_Form2()
        ui.setupUi(self.bilgisayarli_goru_window)
        self.bilgisayarli_goru_window.show()

    def biyoteknoloji_inovasyon(self):
        self.biyoteknoloji_inovasyon_window = QWidget()
        ui = Ui_Form3()
        ui.setupUi(self.biyoteknoloji_inovasyon_window)
        self.biyoteknoloji_inovasyon_window.show()

    def afet_yonetimi(self):
        self.afet_yonetimi_window = QWidget()
        ui = Ui_Form()
        ui.setupUi(self.afet_yonetimi_window)
        self.afet_yonetimi_window.show()

    def web_sayfasi(self):
        self.web_sayfasi_window = QWidget()
        ui = Ui_Form9()
        ui.setupUi(self.web_sayfasi_window)
        self.web_sayfasi_window.show()

    def instagram_sayfasi(self):
        self.instagram_sayfasi_window = QWidget()
        ui = Ui_Form4()
        ui.setupUi(self.instagram_sayfasi_window)
        self.instagram_sayfasi_window.show()

    def linkedin_sayfasi(self):
        self.linkedin_sayfasi_window = QWidget()
        ui = Ui_Form5()
        ui.setupUi(self.linkedin_sayfasi_window)
        self.linkedin_sayfasi_window.show()

    def twitter_sayfasi(self):
        self.twitter_sayfasi_window = QWidget()
        ui = Ui_Form8()
        ui.setupUi(self.twitter_sayfasi_window)
        self.twitter_sayfasi_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
