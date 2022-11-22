# -*- coding: utf-8 -*-


# Layouts
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
# Widgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSpacerItem
from PyQt5.QtWidgets import QSizePolicy

from parameters.gui_parameters_common_widgets import ListParametersWidget
from gui_common_widgets import ParametersGlobalWidget

from PyQt5 import QtCore

class TabGlobalParameterWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self,parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        # Widgets
        self.ParametersList = ListParametersWidget(self)
        self.buttonSave = QPushButton("save")
        self.ParametersWidget = ParametersGlobalWidget(self,editingMode = True)
        # Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.ParametersWidget)
        rightLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Preferred, QSizePolicy.Expanding))
        rightLayout.addWidget(self.buttonSave)
        rightWidget = QWidget()
        rightWidget.setLayout(rightLayout)
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.ParametersList)
        mainLayout.addWidget(rightWidget)
        self.setLayout(mainLayout)
        # Connexions
        self.ParametersList.itemAdded.connect(self.ParametersManager.AddGlobalParameter)
        self.ParametersList.itemDeleted.connect(self.ParametersManager.DelGlobalParameter)
        self.ParametersList.listParameters.currentItemChanged.connect(self.SetValuesFromName)
        self.ParametersManager.ParamStep1Changed.connect(self.ParametersWidget.UpdateListCombo1)
        self.ParametersManager.ParamStep2Changed.connect(self.ParametersWidget.UpdateListCombo2)
        self.ParametersManager.ParamStep3Changed.connect(self.ParametersWidget.UpdateListCombo3)
        self.buttonSave.clicked.connect(self.buttonSaveClicked)
        self.ParametersManager.ParamGlobalRenamed.connect(self.ParametersList.UpdateANameParameter)
        self.ParametersWidget.ParametersNotReady.connect(self.DisabledSaveButton)
        self.ParametersWidget.ParametersReady.connect(self.EnabledSaveButton)
        # Initialisation
        listParameters = self.ParametersManager.GetListOfGlobalParameters()
        self.ParametersList.UpdateList(listParameters)
        self.ParametersList.listParameters.setCurrentItem(self.ParametersList.listParameters.item(0))
        self.UpdateRegExValidator()
        # Design
        self.buttonSave.setFixedSize(100,50)
        rightLayout.setAlignment(self.buttonSave,QtCore.Qt.AlignHCenter)
        rightWidget.setSizePolicy(QSizePolicy(QSizePolicy.Maximum,QSizePolicy.Expanding))
        self.buttonSave.setSizePolicy(QSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum))
    
    def UpdateRegExValidator(self):
        ListName = self.ParametersList.GetListNameWithoutSelectedOne()
        NameToExclude = ""
        for name in ListName:
            NameToExclude += "|%s"%name
        RegEx = "^(?!^$%s)(.{3,128})$"%NameToExclude
        self.ParametersWidget.nameParam.setNewPattern(RegEx)
    
    def SetValuesFromName(self,item):
        self.UpdateRegExValidator()
        self.ParametersWidget.SetValuesFromName(item.text())
    
    def DisabledSaveButton(self):
        self.buttonSave.setDisabled(True)
    
    def EnabledSaveButton(self):
        self.buttonSave.setEnabled(True)
    
    def buttonSaveClicked(self):
        NewParameters = self.ParametersWidget.GenerateDictonaryParameter()
        NewKey = self.ParametersWidget.GetNewParameterName()
        CurrentItem = self.ParametersList.GetCurrentItem()
        if(CurrentItem is not None):
            OldKey = CurrentItem.text()
            if(NewKey != OldKey):
                self.ParametersManager.UpdateNameParameterGlobal(OldKey,NewKey)
            self.ParametersManager.ModifyGlobalParameter(NewKey,NewParameters)
        
    
