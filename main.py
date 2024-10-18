from PySide6.QtWidgets import QApplication
from Core.main_window import MainWindow

class Entry:

    @classmethod
    def init(cls):
        
        cls.mainWindow = MainWindow()
        cls.mainWindow.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    entry = Entry()
    entry.init()
    sys.exit(app.exec())