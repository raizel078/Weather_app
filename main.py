from PySide6.QtWidgets import QApplication
import sys
from ui import Mainwindow

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())

