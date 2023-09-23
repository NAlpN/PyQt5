from PyQt5 import uic

with open ('hakkinda.py', "w", encoding="utf-8") as fout:
    uic.compileUi('hakkinda.ui', fout)