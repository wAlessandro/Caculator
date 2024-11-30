from PySide6.QtWidgets import QMainWindow

class Window(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculator")
        self.configStyle()
    def adjustFixedSize(self):
        """adjustFixedSize adjusts the window in relation of icons on it. Also fixes to the final
        resolution state"""
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    def configStyle(self):
        self.setStyleSheet("background-color: #7F7F7F;")
