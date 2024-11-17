from window import Window
from display import LineEdit, ResultLabel, resulter
from variables import ICONDIR

from PySide6.QtWidgets import(
    QApplication,QWidget,QMainWindow,QGridLayout,QPushButton, QLineEdit,QLabel
    )
from PySide6.QtGui import QIcon

if __name__ == "__main__":
    app = QApplication()
    window = Window()
    icon = QIcon(ICONDIR)
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    text_box = LineEdit()
    window.addToGLayout(text_box)
    text_box.textChanged.connect(lambda: resulter(text_box, result_label))

    result_label = ResultLabel()
    window.addToGLayout(result_label)

    buttons = QPushButton()
    window.addToGLayout(buttons, buttonconnect=text_box)
        
    window.adjustfixedsize()
    window.show()
    app.exec()