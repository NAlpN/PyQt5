import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("HastaArama.ui", self) 
        self.btnara.clicked.connect(self.button_clicked)

    def button_clicked(self):
        try:
            with open("HastaVerisi.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(", ")
                    if len(data) >= 4:
                        ad = data[0]
                        soyad = data[1]
                        yas = data[2]
                        il = data[3]

                        row_position = self.tblsonuc.rowCount()
                        self.tblsonuc.insertRow(row_position)
                        self.tblsonuc.setItem(row_position, 0, QTableWidgetItem(ad))
                        self.tblsonuc.setItem(row_position, 1, QTableWidgetItem(soyad))
                        self.tblsonuc.setItem(row_position, 2, QTableWidgetItem(yas))
                        self.tblsonuc.setItem(row_position, 3, QTableWidgetItem(il))
                print("Veriler tabloya eklendi!")
        except Exception as e:
            print(f"Dosya okuma hatası: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
