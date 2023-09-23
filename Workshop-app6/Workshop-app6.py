import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from MainWindow import Ui_MainWindow

class NotDefteri(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushKaydetBtn.clicked.connect(self.save_text)
        self.pushTemizleBtn.clicked.connect(self.clear_text)
    def save_text(self):
        txt = self.pln_textedit.toPlainText()
        file_path , _ = QFileDialog.getSaveFileName(self, "Dosya Kaydet", "", "Metin Dosyası (*.txt);; Tüm Dosyalar (*)")
        if file_path:
            with open(file_path, "w") as file:
                file.write(txt)
    def clear_text(self):
        self.pln_textedit.clear()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotDefteri()
    window.show()
    sys.exit(app.exec_())        