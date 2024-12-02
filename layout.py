from styling import  (BUTTONSTYLESHEET,
                        OPERATORBUTTONSTYLESHEET,DELETEBUTTONSTYLESHEET,
                        EQUALSBUTTONSTYLESHEET,BUTTONFONTS, BACKBUTTONSTYLESHEET)

from PySide6.QtWidgets import QPushButton, QWidget, QGridLayout
from display import LineEdit,ResultLabel
from mainwindow import Window

class Layout(QPushButton):
    def __init__(
            self,window,display:LineEdit,
            label:ResultLabel,parent= None,):
        super().__init__(parent)
        self.window:Window = window
        centralWidget = QWidget()
        self.window.setCentralWidget(centralWidget)
        self.gridLayout:QGridLayout = QGridLayout()
        self.gridLayout.setSpacing(3)
        centralWidget.setLayout(self.gridLayout)
        self.display:LineEdit = display
        self.label = label
        self._opButtonId = [
            "plus","minus",
            "mult","div",
            "del",'equal',"back"
            ]
        self._opButtonSing = [
            "+","-",
            "*","/",
            "C","=",
            "<"
            ]
        self._buttonLayout = [
            '7','8','9',
            '4','5','6',
            '1','2','3',
            ".",'0',
            ]
        self._left = None
        self._right = None
        self._center = None
        self.equation = ""

    def insertToGLayout(
                        self, widget,
                        row=0, column=0,):
        """addToGLayout checks the widget's instance, and related on this, it places on
        different grid_layout's row and column. On the buttons, it place on the grid
        and add the command functions. These functions set the button's operation
        on textconnect"""
        if isinstance(
            widget, LineEdit):
            self.gridLayout.addWidget(
                widget,
                3, 2,
                1, 1,
                )
        elif isinstance(widget, ResultLabel):
            self.gridLayout.addWidget(
                widget,
                4, 2,
                1, 1
                )
        elif isinstance(widget, QPushButton):
            textIndex = 0
            buttonNameIndex = 0
            for row in range(3,len(self._opButtonId)+3):
                buttonSing = self._opButtonSing[buttonNameIndex]
                buttonId = self._opButtonId[buttonNameIndex]
                self.opButton = QPushButton(buttonSing)
                self.opButton.setObjectName(buttonId)
                self.opButton.clicked.connect(
                    lambda checked, button=self.opButton:
                    self._configOperationButton(button))
                self._configOpButtonStyle(self.opButton, row,)
                buttonNameIndex += 1
                for column in range(3,6):
                    if textIndex < len(self._buttonLayout):
                        if textIndex == self._buttonLayout.index('0'):
                            column = 4
                        self.number_text = self._buttonLayout[textIndex]
                        self.button = QPushButton(self.number_text)
                        self.button.setStyleSheet(BUTTONSTYLESHEET)
                        self.button.setFont(BUTTONFONTS)
                        self.button.clicked.connect(
                            lambda checked, nt=self.number_text:
                            self._buttonClick(nt),)
                        self.gridLayout.addWidget(
                                                self.button,
                                                row, column,
                                                1, 1,
                                                )
                        textIndex += 1
        else:
            self.gridLayout.addWidget(
                                    widget,
                                    row,column,
                                    )
    def _resulter(self):
        if (self._right is None and
        self._left is not None and
        self._center is not None):
            self._right = self.display.text()
        self.equation = f"{self._left} {self._center} {self._right}"
        result = str(
            eval(self.equation)
            )
        self._left = result
        self.label.setText(self.equation)
        self.display.setText(result)
        self._right = None
        print("result=",result)
    def _clear(self):
        
        self.display.clear()
        self._left = None
        self._center = None
        self._right = None
        self.equation = ""
        print("cleaning")
        print(self.equation)  
    def _buttonClick(self, numbertext,):
        """_buttonClick insert nt's text at display"""
        displayText = self.display.text()
        if numbertext == ".":
            if displayText == "":
                return
        self.display.insert(numbertext)
    def _leftSideText(self, text):
        if (self._left is None):
            self._left = text
            self.equation = f"{self._left} {self._center} {self._right}"
        self.label.setText(self.equation)
    def _configOperationButton(self, button:QPushButton,):
        """_operationButton gets the button's Object name
        in paramter and checks if are equals plus/minus/mult/div/del.
        After that, the function insert or remove the button's sing at display
        """
        displayText = self.display.text()
        for i in range(0,2):
            if (button.objectName() == "del"):
                self._clear()
                return
            if (button.objectName() == "equal"):
                self._resulter()
                return
            if (button.objectName() == "back"):
                self.display.backspace()
                return
        buttonIdList = [
                        idd for idd in self._opButtonId if idd != "del"
                        and idd != "equal" and idd != "back"
                         ]
        for a in range(0, len(buttonIdList)):
            buttonsing = self._opButtonSing[a]
            if button.objectName() == buttonIdList[a]:
                self._center = buttonsing
                self.equation = f"{self._left} {self._center} {self._right}"
                self.label.setText(self.equation)
            self.display.clear()
        self._leftSideText(displayText)
    def _configOpButtonStyle(self, button, row,):
        if self._isId(button, "del"):
            self.gridLayout.addWidget(
                                button, 6,5,
                                1,1
                )
            button.setStyleSheet(DELETEBUTTONSTYLESHEET)
            button.setFont(BUTTONFONTS)
        elif self._isId(button, "back"):
            self.gridLayout.addWidget(
                                    button,
                                    7,3,
                                    1,1
                                    )
            button.setFont(BUTTONFONTS)
            button.setStyleSheet(BACKBUTTONSTYLESHEET)
        elif self._isId(button, "equal"):
            self.gridLayout.addWidget(
                                    button,
                                    7,4,
                                    1,4
                                    )
            button.setStyleSheet(EQUALSBUTTONSTYLESHEET)
            button.setFont(BUTTONFONTS)
        
        else:
            self.gridLayout.addWidget(
                                    button,
                                    row,6, 
                                    1,1
                                    )
            button.setStyleSheet(OPERATORBUTTONSTYLESHEET)
            button.setFont(BUTTONFONTS)
    def _isId(self, button: QPushButton, nameid,):
        """_IsId returns True or False 
        if the button's ObjectName() is equals nameid"""
        if button.objectName() == nameid:
            return True
        return False