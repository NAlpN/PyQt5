import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QPushButton, QMessageBox
def item_goster():
    item_secim = liste.currentItem()
    if item_secim:
        QMessageBox.information(window, "Seçim", f"Seçilen Öğe: {item_secim.text()}")
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Liste Kutusu")
window.setGeometry(200,200,500,400)

layout = QVBoxLayout()

liste = QListWidget(window)
layout.addWidget(liste)

items = ["A", "B", "C"]
liste.addItems(items)

button = QPushButton("Seçimi Göster", window)
button.clicked.connect(item_goster)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
