import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Çoklu Menü")
window.setGeometry(100,100,500,200)

layout = QVBoxLayout()

tab_widget = QTabWidget(window)
layout.addWidget(tab_widget)

tab1 = QWidget()
tab2 = QWidget()

tab_widget.addTab(tab1, "1. Seçenek")
tab_widget.addTab(tab2, "2. Seçenek")

label1 = QLabel("Bu 1")
label2 = QLabel("Bu 2")

tab1.layout = QVBoxLayout()
tab1.layout.addWidget(label1)
tab1.setLayout(tab1.layout)

tab2.layout = QVBoxLayout()
tab2.layout.addWidget(label2)
tab2.setLayout(tab2.layout)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())