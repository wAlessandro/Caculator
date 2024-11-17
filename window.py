from PySide6.QtWidgets import(QWidget,QMainWindow,QGridLayout,QPushButton,
    )
from display import LineEdit,ResultLabel

class Window(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.c_widget = QWidget()

        self.setCentralWidget(self.c_widget)
        self.setWindowTitle("Calculator")

        self.grid_layout:QGridLayout = QGridLayout()
        self.c_widget.setLayout(self.grid_layout)

    def addToGLayout(self,widget,buttonconnect:LineEdit|ResultLabel=None):
        if isinstance(widget, LineEdit):
            self.grid_layout.addWidget(widget, 3, 2)
        elif isinstance(widget, ResultLabel):
             self.grid_layout.addWidget(widget, 5, 2)
        elif isinstance(widget, QPushButton):
            self.op_button_id = ["plus","minus","mult","div","del"]
            self.op_button_sing = ["+","-","*","/","C"]
            buttonnameindex = 0
            for row in range(3,8):
                button_sing = self.op_button_sing[buttonnameindex]
                buttonid = self.op_button_id[buttonnameindex]
                self.op_button = QPushButton(button_sing)
                self.op_button.setObjectName(buttonid)
                self.op_button.clicked.connect(lambda checked, button=self.op_button: self._operationButton(button,toconnect=buttonconnect))
                self.op_button.setStyleSheet("font-size:40px;")
                # print(buttonid)
                if self.op_button.objectName() == "del":
                    self.grid_layout.addWidget(self.op_button, 6,5,1,1)
                else:
                    self.grid_layout.addWidget(self.op_button, row,6,1,1)
                buttonnameindex += 1
            buttonLayout = [
                '7','8','9',
                '4','5','6',
                '1','2','3',
                '0']
            text_index = 0
            self.text_memory = ""
            buttonconnect.textChanged.connect(lambda: self._textBoxConnect(buttonconnect))
            for row in range(3,7):
                for column in range(3,6):
                    if text_index < len(buttonLayout):
                        if text_index == buttonLayout.index('0'):
                            column = 4
                        self.number_text = buttonLayout[text_index]    
                        self.button = QPushButton()
                        self.button.setText(self.number_text)
                        self.button.setStyleSheet("font-size:40px;")
                        self.button.clicked.connect(lambda checked, nt=self.number_text:self._buttonClick(buttonconnect,nt))
                        self.grid_layout.addWidget(self.button, row, column, 1 ,1)
                        buttonconnect.setText(self.text_memory)
                        text_index += 1
    def _operationButton(self, button:QPushButton,toconnect:LineEdit|ResultLabel):
        if button.objectName() == "plus":
            self.text_memory += "+"
        if button.objectName() == "minus":
            self.text_memory += "-"
        if button.objectName() == "mult":
            self.text_memory += "*"
        if button.objectName() == "div":
            self.text_memory += '/'
        if button.objectName() == "del":
            self.text_memory = ""
        toconnect.setText(self.text_memory)
    def _textBoxConnect(self, toconnect:LineEdit|ResultLabel):
        self.text_memory = toconnect.text()
    def _buttonClick(self,toconnect:LineEdit|ResultLabel, nt):
        self.text_memory += nt
        toconnect.setText(self.text_memory)
    def adjustfixedsize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    
