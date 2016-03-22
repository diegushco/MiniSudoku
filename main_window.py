# .*. coding: utf-8
from PyQt4.QtGui import (
    QMainWindow,
    QAction,
    QMessageBox,
    QPushButton,
    QWidget,
    QGridLayout
    )
from PyQt4.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(self.tr("Juego Mini Sudoku"))
        self.setMinimumSize(400, 400)

        #creando menu
        menu = self.menuBar()
        self._crearAcciones()
        self._crearMenu(menu)

        btn = QPushButton("1", self)
        btn2 = QPushButton("2", self)
        btn3 = QPushButton("3", self)
        btn4 = QPushButton("4", self)
        btn5= QPushButton("5", self)
        btn6= QPushButton("6", self)

        #Creando la grilla
        gridLayout = QGridLayout()

        #Creando el centralWidget
        centralWidget = QWidget()

        #agregando elementos a la grilla
        gridLayout.addWidget(btn, 0, 0)
        gridLayout.addWidget(btn2, 0, 1)
        gridLayout.addWidget(btn3, 0, 2)
        gridLayout.addWidget(btn4, 1, 0)
        gridLayout.addWidget(btn5, 1, 1)
        gridLayout.addWidget(btn6, 1, 2)

        #asignando la grilla al central widget
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(gridLayout)


    def _crearAcciones(self):
        self.nuevo = QAction("Nuevo", self)
        self.nuevo.setShortcut("Ctrl+N")
        self.sugerencia = QAction("Sugerencia", self)
        self.sugerencia.setShortcut("Ctrl+S")
        self.salir = QAction("Salir", self)
        self.salir.setShortcut("Ctrl+Q")
        self.acerca = QAction("Acerca de", self)

    def _crearMenu(self, menu_bar):
        menu_archivo = menu_bar.addMenu("&Archivo")
        menu_archivo.addAction(self.nuevo)
        menu_archivo.addAction(self.sugerencia)
        menu_archivo.addAction(self.salir)
        menu_acerca = menu_bar.addMenu("A&cerca de")
        menu_acerca.addAction(self.acerca)

