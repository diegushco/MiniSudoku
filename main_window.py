# .*. coding: utf-8
from PyQt4.QtGui import (
    QMainWindow,
    QAction,
    QMessageBox,
    QPushButton,
    QWidget,
    QGridLayout,
    QLineEdit
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

        lineEdit = QLineEdit()
        lineEdit.setAlignment(Qt.AlignCenter)
        lineEdit1 = QLineEdit()
        lineEdit1.setAlignment(Qt.AlignCenter)
        lineEdit2 = QLineEdit()
        lineEdit2.setAlignment(Qt.AlignCenter)
        lineEdit3 = QLineEdit()
        lineEdit3.setAlignment(Qt.AlignCenter)
        lineEdit4 = QLineEdit()
        lineEdit4.setAlignment(Qt.AlignCenter)
        lineEdit5 = QLineEdit()
        lineEdit5.setAlignment(Qt.AlignCenter)
        lineEdit6 = QLineEdit()
        lineEdit6.setAlignment(Qt.AlignCenter)
        lineEdit7 = QLineEdit()
        lineEdit7.setAlignment(Qt.AlignCenter)
        lineEdit8 = QLineEdit()
        lineEdit8.setAlignment(Qt.AlignCenter)
        lineEdit9 = QLineEdit()
        lineEdit9.setAlignment(Qt.AlignCenter)
        lineEdit10 = QLineEdit()
        lineEdit10.setAlignment(Qt.AlignCenter)
        lineEdit11 = QLineEdit()
        lineEdit11.setAlignment(Qt.AlignCenter)
        lineEdit12 = QLineEdit()
        lineEdit12.setAlignment(Qt.AlignCenter)
        lineEdit13 = QLineEdit()
        lineEdit13.setAlignment(Qt.AlignCenter)
        lineEdit14 = QLineEdit()
        lineEdit14.setAlignment(Qt.AlignCenter)
        lineEdit15 = QLineEdit()
        lineEdit15.setAlignment(Qt.AlignCenter)

        #longitid de textEdit a 1
        lineEdit.setMaxLength(1)
        lineEdit1.setMaxLength(1)
        lineEdit2.setMaxLength(1)
        lineEdit3.setMaxLength(1)
        lineEdit4.setMaxLength(1)
        lineEdit5.setMaxLength(1)
        lineEdit6.setMaxLength(1)
        lineEdit7.setMaxLength(1)
        lineEdit8.setMaxLength(1)
        lineEdit9.setMaxLength(1)
        lineEdit10.setMaxLength(1)
        lineEdit11.setMaxLength(1)
        lineEdit12.setMaxLength(1)
        lineEdit13.setMaxLength(1)
        lineEdit14.setMaxLength(1)
        lineEdit15.setMaxLength(1)


        #Creando la grilla
        gridLayout = QGridLayout()

        #Creando el centralWidget
        centralWidget = QWidget()

        #agregando elementos a la grilla
        gridLayout.addWidget(lineEdit, 0, 0)
        gridLayout.addWidget(lineEdit1, 0, 1)
        gridLayout.addWidget(lineEdit2, 0, 2)
        gridLayout.addWidget(lineEdit3, 0, 3)
        gridLayout.addWidget(lineEdit4, 1, 0)
        gridLayout.addWidget(lineEdit5, 1, 1)
        gridLayout.addWidget(lineEdit6, 1, 2)
        gridLayout.addWidget(lineEdit7, 1, 3)
        gridLayout.addWidget(lineEdit8, 2, 0)
        gridLayout.addWidget(lineEdit9, 2, 1)
        gridLayout.addWidget(lineEdit10, 2, 2)
        gridLayout.addWidget(lineEdit11, 2, 3)
        gridLayout.addWidget(lineEdit12, 3, 0)
        gridLayout.addWidget(lineEdit13, 3, 1)
        gridLayout.addWidget(lineEdit14, 3, 2)
        gridLayout.addWidget(lineEdit15, 3, 3)


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

