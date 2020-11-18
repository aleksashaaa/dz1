import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("cof.ui", self)
        self.con = sqlite3.connect('cof.db')
        self.pushButton.clicked.connect(self.do)

    def do(self):
        req = 'SELECT * FROM cof'
        print(req)
        cur = self.con.cursor()
        res = cur.execute(req).fetchall()
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(len(res[0]))
        for i, elem in enumerate(res):
            for j, value in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setHorizontalHeaderLabels(['ID:', 'Название:',
                                                    "Обжарка:", "мол./зерн.:", "Вкус:", "Цена:", "Объем:"])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())