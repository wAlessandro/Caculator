from PySide6.QtWidgets import QLineEdit,QLabel,QPushButton,QGridLayout,QWidget
from PySide6.QtCore import Qt

from variables import (
    BUTTONFONTSIZE,BUTTONSCOLOR,BORDERRADIUS,OPBUTTONSCOLOR,ALLOWEDCHARS,
    MEDIUM_FONT_SIZE,TEXT_MARGIN,MINIMIUM_WIDTH,BIG_FONT_SIZE,SMALL_FONT_SIZE
)
from mainwindow import Window

class LineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        self.textChanged.connect(self._alllowedChars)

    def _alllowedChars(self):
        alltext = self.text()
        for i in alltext:
            if i not in ALLOWEDCHARS:
                self.setText(alltext.replace(i, ""))
    def configStyle(self) -> None:
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
        self.setStyleSheet(
            f"font-size: {SMALL_FONT_SIZE}px;"
            )
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
