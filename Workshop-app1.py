import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("İlk Uygulama")
window.setGeometry(200,200,400,400)
window.show()

sys.exit(app.exec_())