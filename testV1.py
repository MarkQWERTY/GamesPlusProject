import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWebEngineView, QDesktopWidget
from PyQt5.QtCore import QUrl


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Crear el componente de visualización web
        self.web_view = QWebEngineView(self)
        self.setCentralWidget(self.web_view)

        # Configurar la ventana principal
        self.setWindowTitle("Mi Navegador")
        self.resize(800, 600)  # Tamaño inicial de la ventana
        self.center_window()  # Centrar la ventana en la pantalla
        self.showFullScreen()  # Mostrar la ventana en pantalla completa

        # Cargar una página web inicial (por ejemplo, www.google.com)
        self.load_url("https://www.google.com")

    def load_url(self, url):
        self.web_view.setUrl(QUrl(url))

    def center_window(self):
        # Obtener la geometría de la pantalla
        screen_geo = QDesktopWidget().screenGeometry()
        # Centrar la ventana en la pantalla
        self.setGeometry(screen_geo.width() // 4, screen_geo.height() // 4,  # Ajustar la posición
                         screen_geo.width() // 2, screen_geo.height() // 2)  # Ajustar el tamaño


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    sys.exit(app.exec_())
