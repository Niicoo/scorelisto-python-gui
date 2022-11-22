#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Layouts
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
# Widgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QPushButton
# Design
from PyQt5.QtWidgets import QSpacerItem
from PyQt5.QtWidgets import QSizePolicy

from PyQt5 import QtCore
from PyQt5 import QtSvg
from PyQt5.QtCore import pyqtSignal
import os


from converter.gui_converter_direct_widget import DirectConversionWidget
from converter.gui_converter_stepbystep_widget import StepByStepConversionWidget
import gui_settings

import os.path


### Home
###############################################################################
class HomeWidget(QWidget):
    DirectConversionSelected = pyqtSignal(str,str)
    StepByStepConversionSelected = pyqtSignal(str)
    def __init__(self, parent):
        QWidget.__init__(self,parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        # Widgets
        appNameSvgWidget = QtSvg.QSvgWidget(os.path.join(gui_settings.DATA_PATH_ICONS, 'appname.svg'))
        appNameSvgWidget.setFixedSize(300,50)
        button_sf = QPushButtonSelectFile('Select a file')
        self.filenameEdit = QLineEdit('')
        self.button_dc = QPushButton("Direct Conversion")
        paramLabel = QLabel("Parameters")
        self.combo_param = QComboBox(self)
        self.button_sbs = QPushButton("Step by Step Conversion")
        # Layout
        SelectFileLayout = QVBoxLayout()
        SelectFileLayout.addWidget(appNameSvgWidget)
        SelectFileLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding))
        SelectFileLayout.addWidget(button_sf)
        SelectFileLayout.addWidget(self.filenameEdit)
        SelectFileLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding))
        SelectFileWidget = QWidget()
        SelectFileWidget.setLayout(SelectFileLayout)
        DirectLayout = QVBoxLayout()
        DirectLayout.addWidget(self.button_dc)
        DirectLayout.addWidget(paramLabel)
        DirectLayout.addWidget(self.combo_param)
        DirectWidget = QWidget()
        DirectWidget.setLayout(DirectLayout)
        StepByStepLayout = QVBoxLayout()
        StepByStepLayout.addWidget(self.button_sbs)
        StepByStepLayout.addItem(QSpacerItem(20, 59, QSizePolicy.Minimum, QSizePolicy.Fixed))
        StepByStepWidget = QWidget()
        StepByStepWidget.setLayout(StepByStepLayout)
        ConversionChoiceLayout = QHBoxLayout()
        ConversionChoiceLayout.addWidget(DirectWidget)
        ConversionChoiceLayout.addWidget(StepByStepWidget)
        ConversionChoiceWidget = QWidget()
        ConversionChoiceWidget.setLayout(ConversionChoiceLayout)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(SelectFileWidget)
        mainLayout.addWidget(ConversionChoiceWidget)
        self.setLayout(mainLayout)
        # Connexions
        button_sf.clicked.connect(self.openFileNameDialog)
        self.button_dc.clicked.connect(self.ClickOnDirectConversion)
        self.button_sbs.clicked.connect(self.ClickOnStepByStepConversion)
        self.ParametersManager.ParamGlobalChanged.connect(self.updateComboGlobalParam)
        self.filenameEdit.textChanged.connect(self.FileNameChanged)
        # Initialisation
        self.updateComboGlobalParam()
        self.button_dc.setDisabled(True)
        self.button_sbs.setDisabled(True)
        self.filenameEdit.setDragEnabled(True)
        # Design
        self.filenameEdit.setFixedHeight(30)
        self.filenameEdit.setMinimumWidth(600)
        SelectFileLayout.setAlignment(self.filenameEdit,QtCore.Qt.AlignHCenter)
        SelectFileLayout.setAlignment(button_sf,QtCore.Qt.AlignHCenter)
        SelectFileLayout.setAlignment(appNameSvgWidget,QtCore.Qt.AlignHCenter)
        SelectFileLayout.setContentsMargins(0, 10, 0, 0)
        temp = QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
        temp.setVerticalStretch(1)
        SelectFileWidget.setSizePolicy(temp)
        temp2 = QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
        temp2.setVerticalStretch(1)
        ConversionChoiceWidget.setSizePolicy(temp2)
        ConversionChoiceLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        DirectLayout.setContentsMargins(0, 0, 0, 0)
        StepByStepWidget.setFixedWidth(200)
        self.button_sbs.setFixedHeight(50)
        DirectWidget.setFixedWidth(200)
        self.button_dc.setFixedHeight(50)
        paramLabel.setFixedHeight(20)
        self.combo_param.setFixedHeight(30)
        DirectWidget.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed))
        
    
    def FileNameChanged(self,NewText):
        if(self.IsFileNameOk(NewText)):
            self.button_dc.setEnabled(True)
            self.button_sbs.setEnabled(True)
        else:
            self.button_dc.setDisabled(True)
            self.button_sbs.setDisabled(True)

    def IsFileNameOk(self,FileName):
        if(not os.path.isfile(FileName)):
            return(False)
        else:
            return(True)
    
    
    def updateComboGlobalParam(self):
        listglobal = self.ParametersManager.GetListOfGlobalParameters()
        self.combo_param.clear()
        self.combo_param.addItems(listglobal)
    
    def openFileNameDialog(self):    
        fileName, _ = QFileDialog().getOpenFileName(None,"Select wav file to convert...", "","Wav Files (*.wav)")
        self.filenameEdit.setText(fileName)
    
    def ClickOnDirectConversion(self):
        fileName = self.filenameEdit.text()
        ParamName = self.combo_param.currentText()
        self.DirectConversionSelected.emit(fileName,ParamName)
            
    def ClickOnStepByStepConversion(self):
        fileName = self.filenameEdit.text()
        self.StepByStepConversionSelected.emit(fileName)
            
###############################################################################

class MainConverterWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        # Widgets
        self.home = HomeWidget(self)
        self.directconversion = DirectConversionWidget(self)
        self.stepbystep = StepByStepConversionWidget(self)
        # Layout
        mainLayout = QHBoxLayout()
        self.stack = QStackedWidget()
        self.stack.addWidget(self.home)
        self.stack.addWidget(self.directconversion)
        self.stack.addWidget(self.stepbystep)
        mainLayout.addWidget(self.stack)
        self.setLayout(mainLayout)
        # Connexions
        self.home.DirectConversionSelected.connect(self.drawDirectConversionWidget)
        self.home.StepByStepConversionSelected.connect(self.drawStepByStepWidget)
        self.directconversion.ConversionFailed.connect(self.drawHomeWidget)
        self.directconversion.ResultWidget.GoBackToMainMenu.connect(self.drawHomeWidget)
        self.stepbystep.GoBackToMainMenu.connect(self.drawHomeWidget)
        # Design
        mainLayout.setContentsMargins(0, 0, 0, 0)
    
    def drawHomeWidget(self):
        self.stack.setCurrentIndex(0)

    def drawDirectConversionWidget(self,FileName,GlobalParameterName):
        self.stack.setCurrentIndex(1)
        self.directconversion.InitConversion(FileName,GlobalParameterName)
        
    def drawStepByStepWidget(self,FileName):
        self.stack.setCurrentIndex(2)
        self.stepbystep.InitConversion(FileName)


class QPushButtonSelectFile(QPushButton):
    def __init__(self,initText,parent=None):
        QLineEdit.__init__(self,initText)
        



