# .*. coding: utf-8
from PyQt4.QtGui import (
    QMainWindow,
    QAction,
    QMessageBox,
    QPushButton,
    QWidget,
    QGridLayout,
    QLineEdit,
    QHBoxLayout,
    QLabel
    )
from PyQt4.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(self.tr("Juego Mini Sudoku"))
        self.setMinimumSize(400, 400)
        self.errorGrupo = False
        self.errorLineaH = False
        self.errorLineaV = False
        #creando menu
        menu = self.menuBar()
        self._crearAcciones()
        self._crearMenu(menu)

        #boton validar
        btn = QPushButton("Probar", self)

        #Labels
        self.label = QLabel("", self)

        #Edits del juego
        self.lineEdit = QLineEdit()
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setAlignment(Qt.AlignCenter)
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setAlignment(Qt.AlignCenter)
        self.lineEdit3 = QLineEdit()
        self.lineEdit3.setAlignment(Qt.AlignCenter)
        self.lineEdit4 = QLineEdit()
        self.lineEdit4.setAlignment(Qt.AlignCenter)
        self.lineEdit5 = QLineEdit()
        self.lineEdit5.setAlignment(Qt.AlignCenter)
        self.lineEdit6 = QLineEdit()
        self.lineEdit6.setAlignment(Qt.AlignCenter)
        self.lineEdit7 = QLineEdit()
        self.lineEdit7.setAlignment(Qt.AlignCenter)
        self.lineEdit8 = QLineEdit()
        self.lineEdit8.setAlignment(Qt.AlignCenter)
        self.lineEdit9 = QLineEdit()
        self.lineEdit9.setAlignment(Qt.AlignCenter)
        self.lineEdit10 = QLineEdit()
        self.lineEdit10.setAlignment(Qt.AlignCenter)
        self.lineEdit11 = QLineEdit()
        self.lineEdit11.setAlignment(Qt.AlignCenter)
        self.lineEdit12 = QLineEdit()
        self.lineEdit12.setAlignment(Qt.AlignCenter)
        self.lineEdit13 = QLineEdit()
        self.lineEdit13.setAlignment(Qt.AlignCenter)
        self.lineEdit14 = QLineEdit()
        self.lineEdit14.setAlignment(Qt.AlignCenter)
        self.lineEdit15 = QLineEdit()
        self.lineEdit15.setAlignment(Qt.AlignCenter)

        #longitid de textEdit a 1
        self.lineEdit.setMaxLength(1)
        self.lineEdit1.setMaxLength(1)
        self.lineEdit2.setMaxLength(1)
        self.lineEdit3.setMaxLength(1)
        self.lineEdit4.setMaxLength(1)
        self.lineEdit5.setMaxLength(1)
        self.lineEdit6.setMaxLength(1)
        self.lineEdit7.setMaxLength(1)
        self.lineEdit8.setMaxLength(1)
        self.lineEdit9.setMaxLength(1)
        self.lineEdit10.setMaxLength(1)
        self.lineEdit11.setMaxLength(1)
        self.lineEdit12.setMaxLength(1)
        self.lineEdit13.setMaxLength(1)
        self.lineEdit14.setMaxLength(1)
        self.lineEdit15.setMaxLength(1)


        #Creando la grilla
        gridLayout = QGridLayout()
        layout_horizontal = QHBoxLayout(self)

        #Creando el centralWidget
        centralWidget = QWidget()

        #agregando elementos a la grilla
        gridLayout.addWidget(self.lineEdit, 0, 0)
        gridLayout.addWidget(self.lineEdit1, 0, 1)
        gridLayout.addWidget(self.lineEdit2, 0, 2)
        gridLayout.addWidget(self.lineEdit3, 0, 3)
        gridLayout.addWidget(self.lineEdit4, 1, 0)
        gridLayout.addWidget(self.lineEdit5, 1, 1)
        gridLayout.addWidget(self.lineEdit6, 1, 2)
        gridLayout.addWidget(self.lineEdit7, 1, 3)
        gridLayout.addWidget(self.lineEdit8, 2, 0)
        gridLayout.addWidget(self.lineEdit9, 2, 1)
        gridLayout.addWidget(self.lineEdit10, 2, 2)
        gridLayout.addWidget(self.lineEdit11, 2, 3)
        gridLayout.addWidget(self.lineEdit12, 3, 0)
        gridLayout.addWidget(self.lineEdit13, 3, 1)
        gridLayout.addWidget(self.lineEdit14, 3, 2)
        gridLayout.addWidget(self.lineEdit15, 3, 3)
        gridLayout.addWidget(self.label, 4, 0, 1, 4)

        #agregando boton a layout horizontal a la grilla
        layout_horizontal.addWidget(btn)
        #layout_horizontal.addWidget(label)

        gridLayout.addLayout(layout_horizontal, 5, 0, 1, 4)

        #asignando la grilla al central widget
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(gridLayout)

        #Conexiones
        btn.clicked.connect(self._valida)


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

    def _valida(self):
        c00 = self.lineEdit.text()
        c01 = self.lineEdit1.text()
        c02 = self.lineEdit2.text()
        c03 = self.lineEdit3.text()
        c10 = self.lineEdit4.text()
        c11 = self.lineEdit5.text()
        c12 = self.lineEdit6.text()
        c13 = self.lineEdit7.text()
        c20 = self.lineEdit8.text()
        c21 = self.lineEdit9.text()
        c22 = self.lineEdit10.text()
        c23 = self.lineEdit11.text()
        c30 = self.lineEdit12.text()
        c31 = self.lineEdit13.text()
        c32 = self.lineEdit14.text()
        c33 = self.lineEdit15.text()
        print ""
        print (c00 +"-"+ c01 + "-" +c02 + "-" +c03)
        print (c10 +"-"+ c11 + "-" +c12 + "-" +c13)
        print (c20 +"-"+ c21 + "-" +c22 + "-" +c23)
        print (c30 +"-"+ c31 + "-" +c32 + "-" +c33)

        #Validando primer grupo diferentes numeros
        if (c00 == c01):
            print "rojo"
        if (c00 == c10):
            print "rojo"
            self.errorGrupo = True
        if (c00 == c11):
            print "rojo"
            self.errorGrupo = True
        if (c01 == c10):
            print "rojo"
            self.errorGrupo = True
        if (c01 == c11):
            print "rojo"
            self.errorGrupo = True
        if (c10 == c11):
            print "rojo"
            self.errorGrupo = True

        #Validando segundo grupo diferentes numeros
        if (c02 == c03):
            print "rojo"
        if (c02 == c12):
            print "rojo"
            self.errorGrupo = True
        if (c02 == c13):
            print "rojo"
            self.errorGrupo = True
        if (c03 == c12):
            print "rojo"
            self.errorGrupo = True
        if (c03 == c13):
            print "rojo"
            self.errorGrupo = True
        if (c12 == c13):
            print "rojo"
            self.errorGrupo = True

        #Validando tercer grupo diferentes numeros
        if (c20 == c21):
            print "rojo"
        if (c20 == c30):
            print "rojo"
            self.errorGrupo = True
        if (c20 == c31):
            print "rojo"
            self.errorGrupo = True
        if (c21 == c30):
            print "rojo"
            self.errorGrupo = True
        if (c21 == c31):
            print "rojo"
            self.errorGrupo = True
        if (c30 == c31):
            print "rojo"
            self.errorGrupo = True

        #Validando cuarto grupo diferentes numeros
        if (c22 == c23):
            print "rojo"
        if (c22 == c32):
            print "rojo"
            self.errorGrupo = True
        if (c22 == c33):
            print "rojo"
            self.errorGrupo = True
        if (c23 == c32):
            print "rojo"
            self.errorGrupo = True
        if (c23 == c33):
            print "rojo"
            self.errorGrupo = True
        if (c32 == c33):
            print "rojo"
            self.errorGrupo = True

        #validando primera linea horizontal
        if (c00 == c01):
            print "rojo"
            self.errorLineaH = True
        if (c00 == c02):
            print "rojo"
            self.errorLineaH = True
        if (c00 == c03):
            print "rojo"
            self.errorLineaH = True
        if (c01 == c02):
            print "rojo"
            self.errorLineaH = True
        if (c01 == c03):
            print "rojo"
            self.errorLineaH = True
        if (c02 == c03):
            print "rojo"
            self.errorLineaH = True

        #validando segunda linea horizontal
        if (c10 == c11):
            print "rojo"
            self.errorLineaH = True
        if (c10 == c12):
            print "rojo"
            self.errorLineaH = True
        if (c10 == c13):
            print "rojo"
            self.errorLineaH = True
        if (c11 == c12):
            print "rojo"
            self.errorLineaH = True
        if (c11 == c13):
            print "rojo"
            self.errorLineaH = True
        if (c12 == c13):
            print "rojo"
            self.errorLineaH = True

        #validando tercera linea horizontal
        if (c20 == c21):
            print "rojo"
            self.errorLineaH = True
        if (c20 == c22):
            print "rojo"
            self.errorLineaH = True
        if (c20 == c23):
            print "rojo"
            self.errorLineaH = True
        if (c21 == c22):
            print "rojo"
            self.errorLineaH = True
        if (c21 == c23):
            print "rojo"
            self.errorLineaH = True
        if (c22 == c23):
            print "rojo"
            self.errorLineaH = True

        #validando cuarta linea horizontal
        if (c30 == c31):
            print "rojo"
            self.errorLineaH = True
        if (c30 == c32):
            print "rojo"
            self.errorLineaH = True
        if (c30 == c33):
            print "rojo"
            self.errorLineaH = True
        if (c31 == c32):
            print "rojo"
            self.errorLineaH = True
        if (c31 == c33):
            print "rojo"
            self.errorLineaH = True
        if (c32 == c33):
            print "rojo"
            self.errorLineaH = True

        #validando primera linea vertical
        if (c00 == c10):
            print "rojo"
            self.errorLineaV = True
        if (c00 == c20):
            print "rojo"
            self.errorLineaV = True
        if (c00 == c30):
            print "rojo"
            self.errorLineaV = True
        if (c10 == c20):
            print "rojo"
            self.errorLineaV = True
        if (c10 == c30):
            print "rojo"
            self.errorLineaV = True
        if (c20 == c30):
            print "rojo"
            self.errorLineaV = True

        #validando segunda linea vertical
        if (c01 == c11):
            print "rojo"
            self.errorLineaV = True
        if (c01 == c21):
            print "rojo"
            self.errorLineaV = True
        if (c01 == c31):
            print "rojo"
            self.errorLineaV = True
        if (c11 == c21):
            print "rojo"
            self.errorLineaV = True
        if (c11 == c31):
            print "rojo"
            self.errorLineaV = True
        if (c21 == c31):
            print "rojo"
            self.errorLineaV = True

        #validando tercera linea vertical
        if (c02 == c12):
            print "rojo"
            self.errorLineaV = True
        if (c02 == c22):
            print "rojo"
            self.errorLineaV = True
        if (c02 == c32):
            print "rojo"
            self.errorLineaV = True
        if (c12 == c22):
            print "rojo"
            self.errorLineaV = True
        if (c12 == c32):
            print "rojo"
            self.errorLineaV = True
        if (c22 == c32):
            print "rojo"
            self.errorLineaV = True

        #validando cuarta linea vertical
        if (c03 == c13):
            print "rojo"
            self.errorLineaV = True
        if (c03 == c23):
            print "rojo"
            self.errorLineaV = True
        if (c03 == c33):
            print "rojo"
            self.errorLineaV = True
        if (c13 == c23):
            print "rojo"
            self.errorLineaV = True
        if (c13 == c33):
            print "rojo"
            self.errorLineaV = True
        if (c23 == c33):
            print "rojo"
            self.errorLineaV = True

        if(self.errorGrupo == False and self.errorLineaH == False and self.errorLineaV == False):
            QMessageBox.information(self, self.tr("Has terminado"), "<h3>Muy Bien!! felicidades, has completado el MiniSudoku.</h3>" )

        if (self.errorGrupo):
            self.label.setText("Tiene error en uno o mas grupos")
            self.errorGrupo = False

        if (self.errorLineaH):
            self.label.setText("Tiene error en una linea horizontal")
            self.errorLineaH = False

        if (self.errorLineaV):
            self.label.setText("Tiene error en una linea vertical")
            self.errorLineaV = False