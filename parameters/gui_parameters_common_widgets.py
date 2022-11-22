#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Layouts
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
# Widgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QListWidgetItem

from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QTabBar

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtSvg
from PyQt5.QtCore import QSize
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt

from gui_common_widgets import QLineEditWithCheck,MyQRegularExpressionValidator
import gui_settings
import os

# Expandable QtabWidget
###############################################################################
class QTabWidgetExpandable(QTabWidget):
    def __init__(self, parent=None, expanded=-1):
        super(QTabWidget, self).__init__(parent)
        tabbar = QTabBar(self)
        tabbar.setDrawBase(False)
        self.setTabBar(tabbar)

    def resizeEvent(self, event):
        self.tabBar().setMinimumWidth(self.width())
        super(QTabWidget, self).resizeEvent(event)
###############################################################################


# Dialog to ask for a new parameter name
###############################################################################
class EnterNewNameDialog(QDialog):
    def __init__(self,parent, ExistingNAMES):
        QDialog.__init__(self,parent,QtCore.Qt.FramelessWindowHint)
        mainLayout = QFormLayout()
        iconSvgWidget = QtSvg.QSvgWidget(os.path.join(gui_settings.DATA_PATH_ICONS, 'edit.svg'))
        label = QLabel("Enter newparameter name:")
        RegExParamName = QtCore.QRegularExpression("^(?!^$)(.{3,128})$")
        self.validator = MyQRegularExpressionValidator(RegExParamName)
        self.lineEdit = QLineEditWithCheck(self,self.validator)
        self.validator.UpdateForbiddenWords(ExistingNAMES)
        self.enterButton = QPushButton("Enter")
        self.cancelButton = QPushButton("Cancel")
        secondLayout = QHBoxLayout()
        secondLayout.addWidget(self.cancelButton)
        secondLayout.addWidget(self.enterButton)
        buttonWidget = QWidget()
        buttonWidget.setLayout(secondLayout)
        mainLayout.addWidget(iconSvgWidget)
        mainLayout.addWidget(label)
        mainLayout.addWidget(self.lineEdit)
        mainLayout.addWidget(buttonWidget)
        self.setLayout(mainLayout)
        self.lineEdit.textValid.connect(self.DesignNameOk)
        self.lineEdit.textUnvalid.connect(self.DesignNameNotOk)
        self.enterButton.clicked.connect(self.AcceptIfReady)
        self.cancelButton.clicked.connect(self.close)
        self.lineEdit.returnPressed.connect(self.AcceptIfReady)
        self.DesignNameNotOk()
        # Design
        self.enterButton.setFixedSize(100,30)
        self.cancelButton.setFixedSize(100,30)
        iconSvgWidget.setFixedSize(30,30)
        mainLayout.setAlignment(label,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(iconSvgWidget,QtCore.Qt.AlignCenter)
    
    def DesignNameOk(self):
        self.enterButton.setEnabled(True)
    
    def DesignNameNotOk(self):
        self.enterButton.setDisabled(True)
    
    def keyPressEvent(self,evt):
        if((evt.key() != Qt.Key_Enter) and (evt.key() != Qt.Key_Return)):
            super(EnterNewNameDialog, self).keyPressEvent(evt)
    
    def AcceptIfReady(self):
        if(self.lineEdit.IsValid()):
            self.accept()
###############################################################################



# Dialog to confirm the suppression of a parameter
###############################################################################
class DeleteConfirmationDialog(QDialog):
    def __init__(self, parent, paramname):
        QDialog.__init__(self,parent,QtCore.Qt.FramelessWindowHint)
        self.paramname = paramname
        mainLayout = QGridLayout()
        iconSvgWidget = QtSvg.QSvgWidget(os.path.join(gui_settings.DATA_PATH_ICONS, 'questionmark.svg'))
        self.label = QLabel("Are you sure you want to delete the parameter: '%s'"%self.paramname)
        self.CancelButton = QPushButton("No/Cancel")
        self.YesButton = QPushButton("Yes")
        
        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(self.CancelButton)
        buttonsLayout.addWidget(self.YesButton)
        buttonsWidget = QWidget()
        buttonsWidget.setLayout(buttonsLayout)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(iconSvgWidget)
        mainLayout.addWidget(self.label)
        mainLayout.addWidget(buttonsWidget)
        mainLayout.setAlignment(iconSvgWidget,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(self.label,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(buttonsWidget,QtCore.Qt.AlignCenter)
        buttonsLayout.setAlignment(self.CancelButton,QtCore.Qt.AlignCenter)
        buttonsLayout.setAlignment(self.YesButton,QtCore.Qt.AlignCenter)
        self.setLayout(mainLayout)
        self.YesButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)
        self.CancelButton.setFixedSize(100,30)
        self.YesButton.setFixedSize(100,30)
        iconSvgWidget.setFixedSize(30,30)
###############################################################################



# Dialog to inform that we cannot delete the default parameter
###############################################################################
class CannotDeleteDefaultParameterDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self,parent,QtCore.Qt.FramelessWindowHint)
        mainLayout = QVBoxLayout()
        iconSvgWidget = QtSvg.QSvgWidget(os.path.join(gui_settings.DATA_PATH_ICONS, 'warning.svg'))
        label = QLabel("You cannot delete the 'default' parameter")
        YesButton = QPushButton("Ok")
        YesButton.clicked.connect(self.accept)
        mainLayout.addWidget(iconSvgWidget)
        mainLayout.addWidget(label)
        mainLayout.addWidget(YesButton)
        mainLayout.setAlignment(label,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(YesButton,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(iconSvgWidget,QtCore.Qt.AlignCenter)
        self.setLayout(mainLayout)
        YesButton.setFixedSize(100,30)
        iconSvgWidget.setFixedSize(30,30)
###############################################################################


# List of parameters
###############################################################################
class ListParametersWidget(QWidget):
    itemDeleted = pyqtSignal(str)
    itemAdded = pyqtSignal(str)
    def __init__(self, parent):
        QWidget.__init__(self,parent)
        mainLayout = QHBoxLayout()
        buttonsWidget = QWidget()
        buttonsLayout = QVBoxLayout()
        self.buttonNew = QPushButton("+")
        self.buttonDel = QPushButton("-")
        buttonsLayout.addWidget(self.buttonNew)
        buttonsLayout.addWidget(self.buttonDel)
        self.buttonNew.clicked.connect(self.NewParameterClicked)
        self.buttonDel.clicked.connect(self.DelParameterClicked)
        buttonsWidget.setLayout(buttonsLayout)
        self.listParameters = QListWidget()
        mainLayout.addWidget(self.listParameters)
        mainLayout.addWidget(buttonsWidget)
        self.setLayout(mainLayout)
        # Design
        self.buttonNew.setFixedSize(50,50)
        self.buttonDel.setFixedSize(50,50)
    
    def GetListName(self):
        namelist = [self.listParameters.item(k).text() for k in range(self.listParameters.count())]
        return(namelist)
    
    def GetCurrentItem(self):
        CurrentName = self.listParameters.currentItem()
        return(CurrentName)
    
    def GetListNameWithoutSelectedOne(self):
        NameList = self.GetListName()
        CurrentItem = self.GetCurrentItem()
        if(CurrentItem is not None):
            NameList.remove(CurrentItem.text())
        return(NameList)
    
    def NameAlreadyExists(self,name):
        listname = self.GetListName()
        if(name in listname):
            return(True)
        return(False)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.DelParameterClicked()
    
    def NewParameterClicked(self):
        ListNames = self.GetListName()
        my_dialog = EnterNewNameDialog(self,ListNames)
        if(my_dialog.exec_()):
            itemToAdd = QListWidgetItem(my_dialog.lineEdit.text())
            itemToAdd.setSizeHint(QSize(itemToAdd.sizeHint().width(), 30))
            self.listParameters.addItem(itemToAdd)
            self.itemAdded.emit(my_dialog.lineEdit.text())
            self.listParameters.setCurrentItem(itemToAdd)
    
    def DelParameterClicked(self):
        SelectedItems = self.listParameters.selectedItems()
        if(SelectedItems!=[]):
            item = SelectedItems[0]
            if(item.text() == 'default'):
                dialogwarning = CannotDeleteDefaultParameterDialog(self)
                dialogwarning.exec_()
            else:
                my_dialog = DeleteConfirmationDialog(self,item.text()) 
                if(my_dialog.exec_()):
                    delitem = self.listParameters.takeItem(self.listParameters.row(item))
                    self.itemDeleted.emit(delitem.text())
    
    def UpdateANameParameter(self,OldKey,NewKey):
        for k in range(self.listParameters.count()):
            if(self.listParameters.item(k).text() == OldKey):
                self.listParameters.item(k).setText(NewKey)
            
    def UpdateList(self,namelist):
        self.listParameters.clear()
        for name in namelist:
            itemToAdd = QListWidgetItem(name)
            itemToAdd.setSizeHint(QSize(itemToAdd.sizeHint().width(), 30))
            self.listParameters.addItem(itemToAdd)
###############################################################################





