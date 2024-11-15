import sys

from PyQt6.QtCore import QStringListModel
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QWidget,
                             QStackedLayout, QComboBox, QTabWidget, QListView)

from CajaColor import CajaColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo de Qtab")
        self.setFixedSize(400, 400)

        self.tab_widget = QTabWidget(self)

        self.list_view = QListView(self)

        modelo = QStringListModel()
        elementos = ["elemento 1", "elemento 2", "elemento 3", "elemento 4", "elemento 5", "elemento 6", "elemento 7", "elemento 8", "elemento 9", "elemento 10", "elemento 11", "elemento 12", "elemento 13", "elemento 14", "elemento 15"]
        modelo.setStringList(elementos)

        self.list_view.setModel(modelo)

        centralLayout = QVBoxLayout()

        combo_colores = QComboBox()
        combo_colores.addItems(["red","blue","green","yellow"])
        combo_colores.setCurrentIndex(0)

        combo_colores.currentIndexChanged.connect(self.cambioTabs)

        tab1 = CajaColor("red")
        tab2 = CajaColor("blue")
        tab3 = CajaColor("green")
        tab4 = CajaColor("yellow")

        self.tab_widget.addTab(tab1, "Tab 1")
        self.tab_widget.addTab(tab2, "Tab 2")
        self.tab_widget.addTab(tab3, "Tab 3")
        self.tab_widget.addTab(tab4, "Tab 4")

        centralLayout.addWidget(self.tab_widget)
        centralLayout.addWidget(combo_colores)
        centralLayout.addWidget(self.list_view)
        container = QWidget()
        container.setLayout(centralLayout)
        self.setCentralWidget(container)

        self.show()

    def cambioTabs(self, indice):
        self.tab_widget.setCurrentIndex(indice)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()





