from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from variables import ALLOWEDCHARS
from variables import *

class LineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    def configStyle(self,):
        self.setStyleSheet(f"font-size: {MEDIUM_FONT_SIZE}px;")
        self.setMinimumHeight(MEDIUM_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for i in range(4)])
        self.setMinimumWidth(MINIMIUM_WIDTH)
class ResultLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    def configStyle(self):
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px")

def resulter(display:LineEdit,label:QLabel):
    """resulter sets the display's result on label"""
    try:
       result = eval(display.text())
       label.setText(str(result))
    except (NameError,SyntaxError,ValueError):
        alltext = display.text()
        for i in alltext:
            if i not in ALLOWEDCHARS:
                display.setText(alltext.replace(i, ""))
