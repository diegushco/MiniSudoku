# .*. coding: utf-8
from PyQt4.QtGui import (
    QMainWindow,
    QAction,
    QMessageBox
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

