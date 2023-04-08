import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Mi ventana principal')

        # Creación de un botón
        self.button = QPushButton('Mi botón', self)
        self.button.move(150, 150)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print('¡El botón fue clickeado!')

if __name__ == '__main__':
    # Creación de la aplicación
    app = QApplication(sys.argv)

    # Creación de la ventana principal
    main_window = MainWindow()
    main_window.show()

    # Inicio del bucle de eventos de la aplicación
    sys.exit(app.exec_())
