from PySide6.QtWidgets import QLineEdit,QLabel,QPushButton,QGridLayout,QWidget
from PySide6.QtCore import Qt

from variables import (
    BUTTONFONTSIZE,BUTTONSCOLOR,BORDERRADIUS,OPBUTTONSCOLOR,ALLOWEDCHARS,
    MEDIUM_FONT_SIZE,TEXT_MARGIN,MINIMIUM_WIDTH,BIG_FONT_SIZE
)
from mainwindow import Window

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


class Layout(QPushButton):
    def __init__(self,window,parent= None):
        super().__init__(parent)
        self.window:Window = window
        centralWidget = QWidget()
        self.window.setCentralWidget(centralWidget)
        self.gridLayout = QGridLayout()
        centralWidget.setLayout(self.gridLayout)

        self._opButtonId = ["plus","minus","mult","div","del",'equal']
        self._opButtonSing = ["+","-","*","/","C","="]
        self._buttonLayout = [
            '7','8','9',
            '4','5','6',
            '1','2','3',
            ".",'0',]
    def insertToGLayout(self,widget, _row=0, _column=0, textconnect:LineEdit=None):
        """addToGLayout checks the widget's instance, and related on this, it places on
        different grid_layout's row and column. On the buttons, it place on the grid
        and add the command functions. These functions set the button's operation
        on textconnect"""
        if isinstance(widget, LineEdit):
            self.gridLayout.addWidget(widget, 3, 2)
        elif isinstance(widget, ResultLabel):
            self.gridLayout.addWidget(widget, 5, 2)
        elif isinstance(widget, QPushButton):
            _text_index = 0
            _button_name_index = 0
            for _row in range(3,9):
                buttonSing = self._opButtonSing[_button_name_index]
                buttonId = self._opButtonId[_button_name_index]
                self.opButton = QPushButton(buttonSing)
                self.opButton.setObjectName(buttonId)
                self.opButton.clicked.connect(
                    lambda checked, button=self.opButton:
                    self._operationButton(button,toconnect=textconnect))
                if self._isId(self.opButton, "del"):
                    self.gridLayout.addWidget(self.opButton, 6,5,1,1)
                    self.opButton.setStyleSheet(
                        f"font-size:{BUTTONFONTSIZE}; background: red; border-radius:{BORDERRADIUS}")
                elif self._isId(self.opButton, "equal"):
                    self.gridLayout.addWidget(self.opButton, 7,3,1,4)
                    self.opButton.setStyleSheet(
                        f"font-size:{BUTTONFONTSIZE}; background: {OPBUTTONSCOLOR}; border-radius:{BORDERRADIUS}")
                else:
                    self.gridLayout.addWidget(self.opButton, _row,6,1,1)
                    self.opButton.setStyleSheet(
                        f"font-size:{BUTTONFONTSIZE}; background:{OPBUTTONSCOLOR}; border-radius:{BORDERRADIUS}")
                _button_name_index += 1
                for _column in range(3,6):
                    if _text_index < len(self._buttonLayout):
                        if _text_index == self._buttonLayout.index('0'):
                            _column = 4
                        self.number_text = self._buttonLayout[_text_index]    
                        self.button = QPushButton(self.number_text)
                        self.button.setStyleSheet(
                            f"font-size:{BUTTONFONTSIZE}; background:{BUTTONSCOLOR}; border-radius:{BORDERRADIUS}")
                        self.button.clicked.connect(
                            lambda checked, nt=self.number_text:self._buttonClick(textconnect,nt))
                        self.gridLayout.addWidget(self.button, _row, _column, 1 ,1)
                        _text_index += 1
        else:
            self.gridLayout.addWidget(widget, _row,_column)
    def _operationButton(self, button:QPushButton,toconnect:LineEdit):
        """_operationButton gets the button's Object name in paramter and checks if
        are equals plus/minus/mult/div/del. After that, the function insert or remove the button's sing
        at toconnect paramter
        """
        for i in range(0,len(self._opButtonId)):
            if button.objectName() == self._opButtonId[i]:
                toconnect.insert(self._opButtonSing[i])
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