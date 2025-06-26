from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton,
QFileDialog, QMessageBox)
from PySide6.QtCore import QSize
import sys, pathlib, os

def bootstrap_graphviz():
    if hasattr(sys, "_MEIPASS"):
        root = pathlib.Path(sys._MEIPASS)
    else:
        root = pathlib.Path(__file__).parent / "resources"
    
    gv_bin = root / "graphviz" / "bin"
    os.environ["PATH"] = str(gv_bin) + os.pathsep + os.environ.get("PATH", "")
    os.environ["GRAPHVIZ_DOT"] = str(gv_bin / "dot.exe")

bootstrap_graphviz()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Top Down Builder")
        self.setMinimumSize(QSize(480,520))

        central = QWidget()
        layout = QVBoxLayout(central)
        self.setCentralWidget(central)

        import_btn = QPushButton("Importar .txt")
        import_btn.clicked.connect(self.import_txt)
        layout.addWidget(import_btn)

    def import_txt(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo .txt",
            str(pathlib.Path.home()),
            "Archivos de texto (*.txt);;Todos los archivos (*)"
        )

        if ruta:
            try:
                with open(ruta,"r", encoding="utf-8") as f:
                    contenido = f.read()
                    QMessageBox.information(
                        self,
                        "Archivo importado",
                        f"Ruta: \n{ruta}\n\nPrimeros caracteres:\n{contenido[:120]}..."
                    )
            except Exception as e:
                QMessageBox.critical(
                self,
                "Error al leer",
                f"No se pudo abrir el archivo:\n{e}"
            )

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()