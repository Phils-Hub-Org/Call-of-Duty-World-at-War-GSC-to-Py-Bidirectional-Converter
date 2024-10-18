from Utils.qt_utility import displayMessageBox
from Core.lexer import GscToPyLexer, PyToGscLexer
from Core.parser import parseGscToPython, parsePythonToGsc

class Converter:

    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

        from Resources.UI.ui_main_window import Ui_MainWindow
        self.ui: Ui_MainWindow = self.mainWindow.ui

        self.ui.convert_gsc_to_py_btn.clicked.connect(self.convertGscToPy)
        self.ui.convert_py_to_gsc_btn.clicked.connect(self.convertPyToGsc)
    
    def convertGscToPy(self):
        gsc_code = self.ui.gsc_code_input_area.toPlainText()

        if not gsc_code:
            displayMessageBox("Paste GSC code on the left to convert to Python")
            return

        # print(gsc_code)

        # print(True if '\n' in gsc_code else False)

        # 1. Tokenize the GSC code
        tokens = GscToPyLexer.tokenize(gsc_code)

        # # 2. Parse the tokens into Python code
        # python_code = parseGscToPython(tokens)

        # # 3. Display Python code
        # self.ui.python_code_input_area.setPlainText(python_code)

        # Optionally display success in status bar instead of popup
        self.ui.statusBar.showMessage("Successfully converted GSC to Python", 5000)  # 5000 ms duration

    def convertPyToGsc(self):
        py_code = self.ui.python_code_input_area.toPlainText()

        # TODO: Implement logic for 'Python to GSC' in lexer.py and parser.py
        displayMessageBox("Not Implemented")
        return

        if not py_code:
            displayMessageBox("Paste Python code on the right to convert to GSC")
            return

        # 1. Tokenize the Python code
        tokens = PyToGscLexer.tokenize(py_code)

        # 2. Parse the tokens into GSC code
        gsc_code = parsePythonToGsc(tokens)

        # 3. Display GSC code
        self.ui.gsc_code_input_area.setPlainText(gsc_code)

        # Optionally display success in status bar instead of popup
        self.ui.statusBar.showMessage("Successfully converted Python to GSC", 5000)  # 5000 ms duration
