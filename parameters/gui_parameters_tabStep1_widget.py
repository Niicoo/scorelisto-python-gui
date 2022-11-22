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
from gui_common_widgets import ParametersStepOneWidget
from PyQt5 import QtCore


class TabStepOneParameterWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self,parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        # Widgets
        self.ParametersList = ListParametersWidget(self)
        self.ParametersWidget = ParametersStepOneWidget(self,editingMode = True)
        self.buttonSave = QPushButton("save")
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
        self.ParametersList.itemAdded.connect(self.ParametersManager.AddStep1Parameter)
        self.ParametersList.itemDeleted.connect(self.ParametersManager.DelStep1Parameter)
        self.ParametersList.listParameters.currentItemChanged.connect(self.CurrentItemChanged)
        self.buttonSave.clicked.connect(self.buttonSaveClicked)
        self.ParametersManager.ParamStep1Renamed.connect(self.ParametersList.UpdateANameParameter)
        self.ParametersWidget.ParametersNotReady.connect(self.DisabledSaveButton)
        self.ParametersWidget.ParametersReady.connect(self.EnabledSaveButton)
        # Initialisation
        listParameters = self.ParametersManager.GetListOfStep1Parameters()
        self.ParametersList.UpdateList(listParameters)
        self.ParametersList.listParameters.setCurrentItem(self.ParametersList.listParameters.item(0))
        self.UpdateRegExValidator()
        # Design
        self.buttonSave.setFixedSize(100,50)
        rightLayout.setAlignment(self.buttonSave,QtCore.Qt.AlignHCenter)
        rightWidget.setSizePolicy(QSizePolicy(QSizePolicy.Maximum,QSizePolicy.Preferred))
    
    def UpdateRegExValidator(self):
        ListName = self.ParametersList.GetListNameWithoutSelectedOne()
        self.ParametersWidget.NameValidator.UpdateForbiddenWords(ListName)
    
    def DisabledSaveButton(self):
        self.buttonSave.setDisabled(True)
    
    def EnabledSaveButton(self):
        self.buttonSave.setEnabled(True)
    
    def CurrentItemChanged(self,item):
        self.UpdateRegExValidator()
        self.ParametersWidget.SetValuesFromName(item.text())
    
    def buttonSaveClicked(self):
        NewParameters = self.ParametersWidget.GenerateDictonaryParameter()
        NewKey = self.ParametersWidget.GetNewParameterName()
        CurrentItem = self.ParametersList.GetCurrentItem()
        if(CurrentItem is not None):
            OldKey = CurrentItem.text()
            if(NewKey != OldKey):
                self.ParametersManager.UpdateNameParameterStep1(OldKey,NewKey)
            self.ParametersManager.ModifyStep1Parameter(NewKey,NewParameters)
