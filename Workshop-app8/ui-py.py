from PyQt5 import uic

with open ('HastaKaydıUI.py', "w", encoding="utf-8") as fout:
    uic.compileUi('HastaKaydı.ui', fout)