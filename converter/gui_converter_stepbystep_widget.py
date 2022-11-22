# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStackedWidget
# Layouts
from PyQt5.QtWidgets import QVBoxLayout

from converter.step1.gui_converter_step1_main import Step1ConversionWidget
from converter.step2.gui_converter_step2_main import Step2ConversionWidget
from converter.step3.gui_converter_step3_main import Step3ConversionWidget

from converter.gui_converter_common_widgets import ResultConversionWidget

from gui_common_widgets import headerWidget

from PyQt5.QtCore import pyqtSignal

### 
###############################################################################
class StepByStepConversionWidget(QWidget):
    GoBackToMainMenu = pyqtSignal()
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        # Widgets
        self.Step1Widget = Step1ConversionWidget(self)
        self.Step2Widget = Step2ConversionWidget(self)
        self.Step3Widget = Step3ConversionWidget(self)
        self.ResultWidget = ResultConversionWidget(self)
        self.Header = headerWidget()
        # Layout
        mainLayout = QVBoxLayout()
        self.stack = QStackedWidget()
        self.stack.addWidget(self.Step1Widget)
        self.stack.addWidget(self.Step2Widget)
        self.stack.addWidget(self.Step3Widget)
        self.stack.addWidget(self.ResultWidget)
        mainLayout.addWidget(self.Header)
        mainLayout.addWidget(self.stack)
        self.setLayout(mainLayout)
        # Connexions
        self.Step1Widget.GoBackToMainMenu.connect(self.EmitGoBackToMainMenuFromStep1)
        self.Step2Widget.GoBackToMainMenu.connect(self.EmitGoBackToMainMenuFromStep2)
        self.Step3Widget.GoBackToMainMenu.connect(self.EmitGoBackToMainMenuFromStep3)
        self.ResultWidget.GoBackToMainMenu.connect(self.EmitGoBackToMainMenuFromStep3)
        self.Step1Widget.GoBack.connect(self.EmitGoBackToMainMenuFromStep1)
        self.Step2Widget.GoBack.connect(self.drawStep1ConversionWidget)
        self.Step3Widget.GoBack.connect(self.drawStep2ConversionWidget)
        self.ResultWidget.GoBack.connect(self.drawStep3ConversionWidget)
        self.Step1Widget.GoForward.connect(self.MoveToStep2)
        self.Step2Widget.GoForward.connect(self.MoveToStep3)
        self.Step3Widget.GoForward.connect(self.MoveToResult)
        # Design
        mainLayout.setContentsMargins(0, 0, 0, 0)
        # Initialization
        self.Header.updateViewName("Conversion step by step - STEP 1")
    
    def drawStep1ConversionWidget(self):
        self.stack.setCurrentIndex(0)
        self.Header.updateViewName("Conversion step by step - STEP 1")
    
    def drawStep2ConversionWidget(self):
        self.stack.setCurrentIndex(1)
        self.Header.updateViewName("Conversion step by step - STEP 2")
    
    def drawStep3ConversionWidget(self):
        self.stack.setCurrentIndex(2)
        self.Header.updateViewName("Conversion step by step - STEP 3")
    
    def drawResultConversionWidget(self):
        self.stack.setCurrentIndex(3)
        self.Header.updateViewName("Conversion step by step - RESULTS")
    
    # Back To main menu
    def EmitGoBackToMainMenuFromStep1(self):
        self.GoBackToMainMenu.emit()
    
    def EmitGoBackToMainMenuFromStep2(self):
        self.Step1Widget.resetView()
        self.GoBackToMainMenu.emit()
    
    def EmitGoBackToMainMenuFromStep3(self):
        self.Step1Widget.resetView()
        self.Step2Widget.resetView()
        self.GoBackToMainMenu.emit()
    
    # STEP 1
    def InitConversion(self,FileName):
        self.drawStep1ConversionWidget()
        self.Step1Widget.InitView(FileName)
    
    # STEP 2
    def MoveToStep2(self):
        self.drawStep2ConversionWidget()
        InputStep2 = self.Step1Widget.GetResults()
        self.Step2Widget.InitView(InputStep2)
    
    # STEP 3
    def MoveToStep3(self):
        self.drawStep3ConversionWidget()
        InputStep3 = self.Step2Widget.GetResults()
        self.Step3Widget.InitView(InputStep3)
    
    # RESULT
    def MoveToResult(self):
        self.drawResultConversionWidget()
        XMLByteString,MidiByteString,MidiNoRythmByteString = self.Step3Widget.GetResults()
        self.ResultWidget.InitView(XMLByteString,MidiByteString,MidiNoRythmByteString)

