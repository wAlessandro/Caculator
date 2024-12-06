from PySide6.QtWidgets import QLineEdit,QLabel
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from styling import *

class LineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        self.textChanged.connect(self._alllowedChars)
        self.setReadOnly(True)
    Slot()
    def _alllowedChars(self):
        alltext = self.text()
        for i in alltext:
            if i not in ALLOWEDCHARS:
                self.setText(alltext.replace(i, ""))
        if alltext.count(".") > 1:
            self.setText(alltext.replace(".", ""))
    def configStyle(self) -> None:
        self.setStyleSheet(
            f"font-size: {BIG_FONT_SIZE}px; color: white; background:black"
            )
        self.setFont("Roboto Condensed")
        self.setMinimumHeight(MEDIUM_FONT_SIZE * 1.2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for i in range(4)])
        self.setMinimumWidth(MINIMIUM_WIDTH)
        self.setMaximumWidth(MAXIMUM_WIDHT)
        self.setMaximumHeight(MAXIMUM_HEIGHT)



class ResultLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    def configStyle(self):
        self.setStyleSheet(
            f"font-size: {MEDIUM_FONT_SIZE}px;"
            )
        self.setAlignment(Qt.AlignmentFlag.AlignRight)