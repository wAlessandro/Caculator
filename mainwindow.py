from PySide6.QtWidgets import QMainWindow,QWidget
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt, Signal

class Window(QMainWindow):
    resultRequested = Signal()
    deleteRequested = Signal()
    operationRequested = Signal(str)
    numericRequested = Signal(str)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculator")
        self.configStyle()
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        KEYS = Qt.Key
        key = event.key()
        text = event.text()
        # print(event)
        clickedEsc = (key == KEYS.Key_Escape)
        if clickedEsc:
            self.deleteRequested.emit()
            return event.ignore()
        
        clickedEnter = key in [
            KEYS.Key_Return, KEYS.Key_Enter
              ]
        if clickedEnter:
            self.resultRequested.emit()
            return event.ignore()
        clickedOperation = key in [
            KEYS.Key_Plus, KEYS.Key_Minus,
              KEYS.Key_division, KEYS.Key_multiply,
              KEYS.Key_Slash, KEYS.Key_Asterisk,
            ]
        if clickedOperation:
            self.operationRequested.emit(text)
            return event.ignore()
        
        clickedNumeric = [
            KEYS.Key_NumberSign,KEYS.Key_Period
        ]
        if clickedNumeric:
            self.numericRequested.emit(text)
            return event.ignore()
    def adjustFixedSize(self):
        """adjustFixedSize adjusts the window in relation of icons on it.
        Also fixes to the final resolution state"""
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    def configStyle(self):
        self.setStyleSheet("background-color: #7F7F7F;")
