from Utils.qt_utility import displayMessageBox

class Converter:

    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

        # just so the signals change color (in vscode editor)
        from Resources.UI.ui_main_window import Ui_MainWindow
        self.ui: Ui_MainWindow = self.mainWindow.ui

        self.ui.convert_gsc_to_py_btn.clicked.connect(self.convertGscToPy)
        self.ui.convert_py_to_gsc_btn.clicked.connect(self.convertPyToGsc)
    
    def convertGscToPy(self):
        # grab gsc code
        gsc_code = self.ui.gsc_code_input_area.toPlainText()

        if not gsc_code:
            displayMessageBox("Paste gsc code on the left to convert to python")
            return

        # parse gsc code
        parsed_gsc_code = gsc_code

        # display python code
        self.ui.python_code_input_area.setPlainText(parsed_gsc_code)

    def convertPyToGsc(self):
        # grab py code
        py_code = self.ui.python_code_input_area.toPlainText()

        if not py_code:
            displayMessageBox("Paste python code on the right to convert to gsc")
            return

        # parse py code
        parsed_py_code = py_code

        # display gsc code
        self.ui.gsc_code_input_area.setPlainText(parsed_py_code)