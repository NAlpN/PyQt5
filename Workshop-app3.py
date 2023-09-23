import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QLineEdit, QPushButton, QVBoxLayout

def mesaj_goster():
    input_text = text_input.text()
    QMessageBox.information(window, "Metin", f"Girilen Metin: {input_text}")
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Metin Kutusu")
window.setGeometry(300,300,500,350)

layout = QVBoxLayout()

text_input = QLineEdit(window)
layout.addWidget(text_input)

button = QPushButton("Metni Göster", window)
button.clicked.connect(mesaj_goster)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())