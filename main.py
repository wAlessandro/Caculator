from mainwindow import Window
from display import LineEdit, ResultLabel
from layout import Layout
from styling import ICONDIR
from PySide6.QtWidgets import (
    QApplication,QPushButton,
    )
from PySide6.QtGui import QIcon
#negative numbers implemention
if __name__ == "__main__":
    app = QApplication()
    window = Window()
    icon = QIcon(ICONDIR)
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    resultLabel = ResultLabel()
    textLine = LineEdit()
    buttons = QPushButton()
    grid = Layout(
        window,
        textLine,
        resultLabel)
    grid.insertToGLayout(textLine)
    grid.insertToGLayout(resultLabel)
    grid.insertToGLayout(buttons)
    window.adjustFixedSize()
    window.show()
    app.exec()