from PySide6.QtWidgets import(QWidget,QMainWindow,QGridLayout,QPushButton,
    )
from display import LineEdit,ResultLabel
from variables import BORDERRADIUS, BUTTONFONTSIZE,OPBUTTONSCOLOR, BUTTONSCOLOR
class Window(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.c_widget = QWidget()
        self.setCentralWidget(self.c_widget)
        self.setWindowTitle("Calculator")
        self.grid_layout:QGridLayout = QGridLayout()
        self.c_widget.setLayout(self.grid_layout)
    def addWidgetToGLayout(self, widget, _row=0, _column=0, textconnect:LineEdit=None):
        """addToGLayout checks the widget's instance, and related on this, it places on
        different grid_layout's row and column. On the buttons, it place on the grid
          and add the command functions. These functions set the button's operation
          on textconnect"""
        if isinstance(widget, LineEdit):
            self.grid_layout.addWidget(widget, 3, 2)
        elif isinstance(widget, ResultLabel):
             self.grid_layout.addWidget(widget, 5, 2)
        elif isinstance(widget, QPushButton):
            self.op_button_id = ["plus","minus","mult","div","del",'equal']
            self.op_button_sing = ["+","-","*","/","C","="]
            _buttonLayout = [
                '7','8','9',
                '4','5','6',
                '1','2','3',
                ".",'0',]
            _text_index = 0
            _button_name_index = 0
            for _row in range(3,9):
                _button_sing = self.op_button_sing[_button_name_index]
                _buttonid = self.op_button_id[_button_name_index]
                self.op_button = QPushButton(_button_sing)
                self.op_button.setObjectName(_buttonid)
                self.op_button.clicked.connect(
                    lambda checked, button=self.op_button:
                    self._operationButton(button,toconnect=textconnect))
                if self._isId(self.op_button, "del"):
                    self.grid_layout.addWidget(self.op_button, 6,5,1,1)
                    self.op_button.setStyleSheet(f"font-size:{BUTTONFONTSIZE}; background: red; border-radius:{BORDERRADIUS}")
                elif self._isId(self.op_button, "equal"):
                    self.grid_layout.addWidget(self.op_button, 7,3,1,4)
                    self.op_button.setStyleSheet(f"font-size:{BUTTONFONTSIZE}; background: {OPBUTTONSCOLOR}; border-radius:{BORDERRADIUS}")
                else:
                    self.grid_layout.addWidget(self.op_button, _row,6,1,1)
                    self.op_button.setStyleSheet(f"font-size:{BUTTONFONTSIZE}; background:{OPBUTTONSCOLOR}; border-radius:{BORDERRADIUS}")
                _button_name_index += 1
                for _column in range(3,6):
                    if _text_index < len(_buttonLayout):
                        if _text_index == _buttonLayout.index('0'):
                            _column = 4
                        self.number_text = _buttonLayout[_text_index]    
                        self.button = QPushButton(self.number_text)
                        self.button.setStyleSheet(
                            f"font-size:{BUTTONFONTSIZE}; background:{BUTTONSCOLOR}; border-radius:{BORDERRADIUS}")
                        self.button.clicked.connect(
                            lambda checked, nt=self.number_text:self._buttonClick(textconnect,nt))
                        self.grid_layout.addWidget(self.button, _row, _column, 1 ,1)
                        _text_index += 1
        else:
            self.grid_layout.addWidget(widget, _row,_column)
    def _operationButton(self, button:QPushButton,toconnect:LineEdit):
        """_operationButton gets the button's Object name in paramter and checks if
        are equals plus/minus/mult/div/del. After that, the function insert or remove the button's sing
        at toconnect paramter
        """
        for i in range(0,len(self.op_button_id)):
            if button.objectName() == self.op_button_id[i]:
                toconnect.insert(self.op_button_sing[i])
            elif button.objectName() == "del":
                toconnect.setText("")
            elif button.objectName() == "equal":
                toconnect.setText(str(eval(toconnect.text())))
    def _buttonClick(self,toconnect:LineEdit|ResultLabel, nt):
        """_buttonClick insert nt's text at toconnect"""
        toconnect.insert(nt)
    def _isId(self, button: QPushButton, nameid):
        """_IsId returns True or False if the button's ObjectName() is equals nameid"""
        if button.objectName() == nameid:
            return True
        return False
    def adjustFixedSize(self):
        """adjustFixedSize adjusts the window in relation of icons on it. Also fixes to the final
        resolution state"""
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    
