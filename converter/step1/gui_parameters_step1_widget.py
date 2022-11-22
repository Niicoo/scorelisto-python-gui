#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLabel
# Layouts
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtGui import QDoubleValidator

from gui_common_widgets import ParametersStepOneWidget,QLineEditWithCheck
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui


class ParametersStep1InputWidget(QWidget):
    TimeStartChanged = pyqtSignal(float)
    TimeEndChanged = pyqtSignal(float)
    DefaultTimeStart = pyqtSignal()
    DefaultTimeEnd = pyqtSignal()
    ParametersReady = pyqtSignal()
    ParametersNotReady = pyqtSignal()
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        # Validators
        self.Validator_TStart = QDoubleValidator()
        self.Validator_TStart.setRange(0,10000,5)
        self.Validator_TEnd = QDoubleValidator()
        self.Validator_TEnd.setRange(0,10000,5)
        # Widgets
        TimeStartLabel = QLabel("Time start")
        TimeEndLabel = QLabel("Time end")
        self.timeStartEdit = QLineEditWithCheck(self,self.Validator_TStart)
        self.timeEndEdit = QLineEditWithCheck(self,self.Validator_TEnd)
        self.parameterComboName = QComboBox()
        self.ParametersWidget = ParametersStepOneWidget(self)
        # Layouts
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(TimeStartLabel)
        mainLayout.addWidget(self.timeStartEdit)
        mainLayout.addWidget(TimeEndLabel)
        mainLayout.addWidget(self.timeEndEdit)
        mainLayout.addWidget(self.parameterComboName)
        mainLayout.addWidget(self.ParametersWidget)
        self.setLayout(mainLayout)
        # Connexions
        self.timeStartEdit.textChanged.connect(self.EmitTimeStartChanged)
        self.timeEndEdit.textChanged.connect(self.EmitTimeEndChanged)
        self.timeStartEdit.textChanged.connect(self.CheckIfAllParametersAreReady)
        self.timeEndEdit.textChanged.connect(self.CheckIfAllParametersAreReady)
        self.ParametersManager.ParamStep1Changed.connect(self.updateComboParametersNames)
        self.parameterComboName.currentIndexChanged.connect(self.setParametersValueFromCombo)
        self.ParametersWidget.ParametersReady.connect(self.CheckIfAllParametersAreReady)
        self.ParametersWidget.ParametersNotReady.connect(self.CheckIfAllParametersAreReady)
        # Initialization
        self.resetView()
        # Design
        self.setFixedWidth(self.ParametersWidget.width())
    
    def resetView(self):
        self.updateComboParametersNames()
        self.timeStartEdit.setText('')
        self.timeEndEdit.setText('')
    
    def updateComboParametersNames(self):
        listParameters = self.ParametersManager.GetListOfStep1Parameters()
        self.parameterComboName.clear()
        self.parameterComboName.addItems(listParameters)
        self.parameterComboName.setCurrentIndex(0)
    
    def EmitTimeStartChanged(self,newvalue):
        try:
            TimeStart = float(newvalue)
            self.TimeStartChanged.emit(TimeStart)
        except ValueError:
            self.DefaultTimeStart.emit()
    
    def EmitTimeEndChanged(self,newvalue):
        try:
            TimeEnd = float(newvalue)
            self.TimeEndChanged.emit(TimeEnd)
        except ValueError:
            self.DefaultTimeEnd.emit()
    
    def CheckIfAllParametersAreReady(self):
        if(not self.ParametersWidget.AreParametersReady()):
            self.ParametersNotReady.emit()
            return(False)
        VtStart = self.timeStartEdit.validator()
        state = VtStart.validate(self.timeStartEdit.text(), 0)[0]
        if(state != QtGui.QValidator.Acceptable):
            self.ParametersNotReady.emit()
            return(False)
        VtStart = self.timeEndEdit.validator()
        state = VtStart.validate(self.timeEndEdit.text(), 0)[0]
        if(state != QtGui.QValidator.Acceptable):
            self.ParametersNotReady.emit()
            return(False)
        self.ParametersReady.emit()
        return(True)
    
    def setParametersValueFromCombo(self,ind):
        if(ind != -1):
            paramName = self.parameterComboName.currentText()
            self.ParametersWidget.SetValuesFromName(paramName)
        

    
    def GetTimeStart(self):
        try:
            TimeStart = float(self.timeStartEdit.text())
        except ValueError:
            TimeStart = None
        return(TimeStart)
    
    def GetTimeEnd(self):
        try:
            TimeEnd = float(self.timeEndEdit.text())
        except ValueError:
            TimeEnd = None
        return(TimeEnd)
    
    def GetParameters(self):
        Parameters = self.ParametersWidget.GenerateDictonaryParameter()
        TimeStart = self.GetTimeStart()
        TimeEnd = self.GetTimeEnd()
        Parameters["TimeStart_s"] = TimeStart
        Parameters["TimeStop_s"] = TimeEnd
        return(Parameters)


