import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

def mesaj_goster():
    QMessageBox.information(window, "Bilgi", "Butona tıklandı!")
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Buton İşleme")
window.setGeometry(100,100,300,300)

button = QPushButton("Tıkla", window)
button.setGeometry(5,5,150,50)
button.clicked.connect(mesaj_goster)

window.show()

sys.exit(app.exec_())