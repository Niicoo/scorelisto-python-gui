# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QDialog
# Widgets 
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSizePolicy

from PyQt5 import QtSvg
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
import os
import gui_settings

# Dialog to save the music xml file
###############################################################################
def GetXmlFileOutPath():
    SaveDialog = QFileDialog()
    SaveDialog.setNameFilter('XML files (*.xml)')
    SaveDialog.setDefaultSuffix('xml')
    SaveDialog.setAcceptMode(QFileDialog.AcceptSave)
    if SaveDialog.exec_():
        FilePath = SaveDialog.selectedFiles()[0]
        return(FilePath)
    else:
        return None
###############################################################################

# Dialog to save the midi file
###############################################################################
def GetMidiFileOutPath():
    SaveDialog = QFileDialog()
    SaveDialog.setNameFilter('Midi files (*.mid)')
    SaveDialog.setDefaultSuffix('mid')
    SaveDialog.setAcceptMode(QFileDialog.AcceptSave)
    if SaveDialog.exec_():
        FilePath = SaveDialog.selectedFiles()[0]
        return(FilePath)
    else:
        return None
###############################################################################


# Widget when a conversion is finished
###############################################################################
class ResultConversionWidget(QWidget):
    GoBack = pyqtSignal()
    GoBackToMainMenu = pyqtSignal()
    def __init__(self, parent,EnableBackButton=True):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        # Widgets
        self.XMLButton = QPushButton("XML File")
        self.MidiButton = QPushButton("Midi File")
        self.MidiNoRythmButton = QPushButton("Midi File (No Rythm)")
        self.BackButton = QPushButton("Back")
        self.HomeButton = QPushButton("Home")
        # Layout
        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(self.XMLButton)
        buttonsLayout.addWidget(self.MidiButton)
        buttonsLayout.addWidget(self.MidiNoRythmButton)
        buttonsWidget = QWidget()
        buttonsWidget.setLayout(buttonsLayout)
        backhomeLayout = QHBoxLayout()
        if(EnableBackButton):
            backhomeLayout.addWidget(self.BackButton)
        backhomeLayout.addWidget(self.HomeButton)
        backhomeWidget = QWidget()
        backhomeWidget.setLayout(backhomeLayout)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(buttonsWidget)
        mainLayout.addWidget(backhomeWidget)
        self.setLayout(mainLayout)
        # Connexions
        self.XMLButton.clicked.connect(self.SaveMusicXMLFile)
        self.MidiButton.clicked.connect(self.SaveMidiFile)
        self.MidiNoRythmButton.clicked.connect(self.SaveMidiNoRythmFile)
        if(EnableBackButton):
            self.BackButton.clicked.connect(self.BackButtonClicked)
        self.HomeButton.clicked.connect(self.HomeButtonClicked)
        # Design
        self.XMLButton.setFixedSize(150,150)
        self.MidiButton.setFixedSize(150,150)
        self.MidiNoRythmButton.setFixedSize(150,150)
        if(EnableBackButton):
            self.BackButton.setFixedSize(70,50)
        self.HomeButton.setFixedSize(70,50)
        backhomeWidget.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum))
        
    
    def InitView(self,XMLByteString,MidiByteString,MidiNoRythmByteString):
        self.XMLByteString = XMLByteString
        self.MidiByteString = MidiByteString
        self.MidiNoRythmByteString = MidiNoRythmByteString
    
    def BackButtonClicked(self):
        self.GoBack.emit()
    
    def HomeButtonClicked(self):
        self.GoBackToMainMenu.emit()
    
    def SaveMusicXMLFile(self):
        FilePath = GetXmlFileOutPath()
        if(FilePath):
            with open(FilePath,mode='wb') as FileOut:
                FileOut.write(self.XMLByteString)
    
    def SaveMidiFile(self):
        FilePath = GetMidiFileOutPath()
        if(FilePath):
            with open(FilePath,mode='wb') as FileOut:
                FileOut.write(self.MidiByteString)
    
    def SaveMidiNoRythmFile(self):
        FilePath = GetMidiFileOutPath()
        if(FilePath):
            with open(FilePath,mode='wb') as FileOut:
                FileOut.write(self.MidiNoRythmByteString)
###############################################################################


class MyNavigationToolbar2QT(NavigationToolbar2QT):
    def __init__(self, *args, **kwargs):
        NavigationToolbar2QT.__init__(self,*args, **kwargs)
    
    def _icon(self, name):
        name = name.replace('.png', '.svg')
        pm = QtGui.QPixmap(os.path.join(gui_settings.DATA_PATH_ICONS, name))
        if hasattr(pm, 'setDevicePixelRatio'):
            pm.setDevicePixelRatio(self.canvas._dpi_ratio)
        return QtGui.QIcon(pm)

# Dialog to confirm abort and come back to menu
###############################################################################
class ConfirmAbortDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self,parent,QtCore.Qt.FramelessWindowHint)
        mainLayout = QGridLayout()
        iconSvgWidget = QtSvg.QSvgWidget(os.path.join(gui_settings.DATA_PATH_ICONS, 'questionmark.svg'))
        label1 = QLabel("Are you sure you want to cancel and come back to the main menu ?")
        label2 = QLabel("All the work in progress will be lost")
        self.CancelButton = QPushButton("No (don't quit)")
        self.YesButton = QPushButton("Yes (quit)")
        responseLayout = QHBoxLayout()
        responseLayout.addWidget(self.CancelButton)
        responseLayout.addWidget(self.YesButton)
        responseWidget = QWidget()
        responseWidget.setLayout(responseLayout)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(iconSvgWidget)
        mainLayout.addWidget(label1)
        mainLayout.addWidget(label2)
        mainLayout.addWidget(responseWidget)
        self.setLayout(mainLayout)
        self.YesButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)
        self.CancelButton.setFixedSize(150,30)
        self.YesButton.setFixedSize(150,30)
        iconSvgWidget.setFixedSize(30,30)
        mainLayout.setAlignment(iconSvgWidget,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(responseWidget,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(label1,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(label2,QtCore.Qt.AlignCenter)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
###############################################################################

# Dialog to confirm cancel and come back to menu
###############################################################################
class ConfirmCancelDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self,parent,QtCore.Qt.FramelessWindowHint)
        iconSvgWidget = QtSvg.QSvgWidget(os.path.join(gui_settings.DATA_PATH_ICONS, 'questionmark.svg'))
        self.label = QLabel("Are you sure you want to cancel the current conversion ?")
        self.NoButton = QPushButton("No")
        self.YesButton = QPushButton("Yes")
        responseLayout = QHBoxLayout()
        responseLayout.addWidget(self.NoButton)
        responseLayout.addWidget(self.YesButton)
        responseWidget = QWidget()
        responseWidget.setLayout(responseLayout)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(iconSvgWidget)
        mainLayout.addWidget(self.label)
        mainLayout.addWidget(responseWidget)
        self.setLayout(mainLayout)
        self.YesButton.clicked.connect(self.accept)
        self.NoButton.clicked.connect(self.close)
        self.NoButton.setFixedSize(100,30)
        self.YesButton.setFixedSize(100,30)
        iconSvgWidget.setFixedSize(30,30)
        mainLayout.setAlignment(iconSvgWidget,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(responseWidget,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(self.label,QtCore.Qt.AlignCenter)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
###############################################################################


# No path found - parameters too restrictive
###############################################################################
class TooRestrictivesParametersDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self,parent,QtCore.Qt.FramelessWindowHint)
        iconSvgWidget = QtSvg.QSvgWidget(os.path.join(gui_settings.DATA_PATH_ICONS, 'warning.svg'))
        self.label = QLabel("The parameters you choose are too restrictives\nPlease choose different conversion parameters and restart the conversion.")
        self.OkButton = QPushButton("Ok")
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(iconSvgWidget)
        mainLayout.addWidget(self.label)
        mainLayout.addWidget(self.OkButton)
        self.setLayout(mainLayout)
        self.OkButton.clicked.connect(self.accept)
        self.OkButton.setFixedSize(100,30)
        iconSvgWidget.setFixedSize(30,30)
        mainLayout.setAlignment(iconSvgWidget,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(self.label,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(self.OkButton,QtCore.Qt.AlignCenter)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
###############################################################################


# Dialog process already running
###############################################################################
class ProcessAlreadyRunningDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self,parent,QtCore.Qt.FramelessWindowHint)
        iconSvgWidget = QtSvg.QSvgWidget(os.path.join(gui_settings.DATA_PATH_ICONS, 'warning.svg'))
        self.label = QLabel("A conversion is already running")
        self.OkButton = QPushButton("Ok")
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(iconSvgWidget)
        mainLayout.addWidget(self.label)
        mainLayout.addWidget(self.OkButton)
        self.setLayout(mainLayout)
        self.OkButton.clicked.connect(self.accept)
        self.OkButton.setFixedSize(100,30)
        iconSvgWidget.setFixedSize(30,30)
        mainLayout.setAlignment(iconSvgWidget,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(self.label,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(self.OkButton,QtCore.Qt.AlignCenter)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
###############################################################################

# Dialog no result found
###############################################################################
class NoResultFoundDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self,parent,QtCore.Qt.FramelessWindowHint)
        iconSvgWidget = QtSvg.QSvgWidget(os.path.join(gui_settings.DATA_PATH_ICONS, 'warning.svg'))
        self.label = QLabel("Please execute this conversion step before to move to the next one")
        self.OkButton = QPushButton("Ok")
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(iconSvgWidget)
        mainLayout.addWidget(self.label)
        mainLayout.addWidget(self.OkButton)
        self.setLayout(mainLayout)
        self.OkButton.clicked.connect(self.accept)
        self.OkButton.setFixedSize(100,30)
        iconSvgWidget.setFixedSize(30,30)
        mainLayout.setAlignment(iconSvgWidget,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(self.label,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(self.OkButton,QtCore.Qt.AlignCenter)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
###############################################################################


# Dialog to confirm back step
###############################################################################
class ConfirmBackDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self,parent,QtCore.Qt.FramelessWindowHint)
        mainLayout = QGridLayout()
        iconSvgWidget = QtSvg.QSvgWidget(os.path.join(gui_settings.DATA_PATH_ICONS, 'questionmark.svg'))
        self.label = QLabel("Are you sure you want to cancel the current step conversion ?")
        self.NoButton = QPushButton("No")
        self.YesButton = QPushButton("Yes")
        responseLayout = QHBoxLayout()
        responseLayout.addWidget(self.NoButton)
        responseLayout.addWidget(self.YesButton)
        responseWidget = QWidget()
        responseWidget.setLayout(responseLayout)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(iconSvgWidget)
        mainLayout.addWidget(self.label)
        mainLayout.addWidget(responseWidget)
        self.setLayout(mainLayout)
        self.YesButton.clicked.connect(self.accept)
        self.NoButton.clicked.connect(self.close)
        self.NoButton.setFixedSize(100,30)
        self.YesButton.setFixedSize(100,30)
        iconSvgWidget.setFixedSize(30,30)
        mainLayout.setAlignment(iconSvgWidget,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(responseWidget,QtCore.Qt.AlignCenter)
        mainLayout.setAlignment(self.label,QtCore.Qt.AlignCenter)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
###############################################################################




