# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
# Layouts
from PyQt5.QtWidgets import QVBoxLayout


from gui_common_widgets import ParametersStepThreeWidget
from PyQt5.QtCore import pyqtSignal


class ParametersStep3InputWidget(QWidget):
    ParametersReady = pyqtSignal()
    ParametersNotReady = pyqtSignal()
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        # Widgets
        self.parameterComboName = QComboBox()
        self.ParametersWidget = ParametersStepThreeWidget(self)
        # Layouts
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.parameterComboName)
        mainLayout.addWidget(self.ParametersWidget)
        self.setLayout(mainLayout)
        # Connexions
        self.ParametersManager.ParamStep1Changed.connect(self.resetView)
        self.parameterComboName.currentIndexChanged.connect(self.setParametersValueFromCombo)
        self.ParametersWidget.ParametersReady.connect(self.EmitParametersReady)
        self.ParametersWidget.ParametersNotReady.connect(self.EmitParametersNotReady)
        # Initialization
        self.resetView()
        # Design
        self.setFixedWidth(self.ParametersWidget.width())
    
    def resetView(self):
        listParameters = self.ParametersManager.GetListOfStep3Parameters()
        self.parameterComboName.clear()
        self.parameterComboName.addItems(listParameters)
        self.parameterComboName.setCurrentIndex(0)
    
    def EmitParametersReady(self):
        self.ParametersReady.emit()
    
    def EmitParametersNotReady(self):
        self.ParametersNotReady.emit()
    
    def setParametersValueFromCombo(self,ind):
        if(ind != -1):
            paramName = self.parameterComboName.currentText()
            self.ParametersWidget.SetValuesFromName(paramName)
    
    def GetParameters(self):
        Parameters = self.ParametersWidget.GenerateDictonaryParameter()
        return(Parameters)


