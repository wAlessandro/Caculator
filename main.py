from mainwindow import Window
from display import LineEdit, ResultLabel, resulter,Layout
from variables import ICONDIR
from PySide6.QtWidgets import(
    QApplication,QPushButton,
    )
from PySide6.QtGui import QIcon

if __name__ == "__main__":
    app = QApplication()
    window = Window()
    icon = QIcon(ICONDIR)
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    grid = Layout(window)
    text_box = LineEdit()
    grid.insertToGLayout(text_box)
    text_box.textChanged.connect(lambda: resulter(text_box, result_label))
    result_label = ResultLabel()
    grid.insertToGLayout(result_label)
    
    buttons = QPushButton()
    grid.insertToGLayout(buttons, textconnect=text_box)
    window.adjustFixedSize()
    window.show()
    app.exec()