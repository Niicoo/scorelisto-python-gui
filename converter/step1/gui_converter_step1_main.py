#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QScrollArea
# Design
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QSpacerItem
# Layouts
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from converter.step1.gui_plot_step1_widget import PlotStep1Widget
from converter.step1.gui_info_step1_widget import InputInfoStep1Widget
from converter.step1.gui_parameters_step1_widget import ParametersStep1InputWidget
from converter.gui_converter_common_widgets import ConfirmCancelDialog,ConfirmAbortDialog,NoResultFoundDialog,ConfirmBackDialog
from converter.gui_converter_common_widgets import ProcessAlreadyRunningDialog
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal

from gui_process_steps import RunStep_One
from gui_common_widgets import MultiprocessingQTimerInterResults

class Step1ConversionWidget(QWidget):
    GoBackToMainMenu = pyqtSignal()
    GoBack = pyqtSignal()
    GoForward = pyqtSignal()
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        self.rangePbar = 100
        # Widgets
        self.paramWidget = ParametersStep1InputWidget(self)
        self.plotWidget = PlotStep1Widget(self)
        self.infoWidget = InputInfoStep1Widget(self)
        self.SubSteps = QLabel("")
        self.cancelButton = QPushButton("cancel")
        self.runButton = QPushButton("run")
        self.abortButton = QPushButton("abort")
        self.backButton = QPushButton("back")
        self.nextButton = QPushButton("next")
        self.pbar = QProgressBar(self)
        self.pbar.setRange(0, self.rangePbar)

        # Layout
            # Section Parameters
        scrollParam = QScrollArea()
        scrollParam.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scrollParam.setWidget(self.paramWidget)
        scrollParam.setWidgetResizable(True)
        
        dataParamLayout = QVBoxLayout()
        dataParamLayout.addWidget(scrollParam)
        dataParamLayout.addWidget(self.runButton)
        dataParamLayout.addWidget(QWidget())
        dataParamWidget = QWidget()
        dataParamWidget.setLayout(dataParamLayout)
            # Section info
        dataInfoWidget = QWidget()
        dataInfoLayout = QVBoxLayout()
        dataInfoLayout.addWidget(self.infoWidget)
        dataInfoLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Preferred, QSizePolicy.Expanding))
        dataInfoWidget.setLayout(dataInfoLayout)
            # united sections
        dataWidget = QWidget()
        dataLayout = QHBoxLayout()
        dataLayout.addWidget(dataParamWidget)
        dataLayout.addWidget(self.plotWidget)
        dataLayout.addWidget(dataInfoWidget)
        dataWidget.setLayout(dataLayout)
            # Progression bar
        bottonWidget = QWidget()
        BottomLayout = QVBoxLayout()
        pbarWidget = QWidget()
        pbarLayout = QHBoxLayout()
        pbarLayout.addWidget(self.pbar)
        pbarLayout.addWidget(self.cancelButton)
        pbarWidget.setLayout(pbarLayout)
        buttonsWidget = QWidget()
        botbutLayout = QHBoxLayout()
        botbutLayout.addWidget(self.abortButton)
        botbutLayout.addWidget(self.backButton)
        botbutLayout.addWidget(self.nextButton)
        buttonsWidget.setLayout(botbutLayout)
        BottomLayout.addWidget(self.SubSteps)
        BottomLayout.addWidget(pbarWidget)
        BottomLayout.addWidget(buttonsWidget)
        bottonWidget.setLayout(BottomLayout)
            # Main Layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(dataWidget)
        mainLayout.addWidget(bottonWidget)
        self.setLayout(mainLayout)
        # Connexions
        self.paramWidget.TimeStartChanged.connect(self.plotWidget.UpdateVlineStart)
        self.paramWidget.TimeEndChanged.connect(self.plotWidget.UpdateVlineEnd)
        self.paramWidget.DefaultTimeStart.connect(self.infoWidget.EmitDefaultTimeStart)
        self.paramWidget.DefaultTimeEnd.connect(self.infoWidget.EmitDefaultTimeEnd)
        self.infoWidget.setDefaultTimeStart.connect(self.plotWidget.UpdateVlineStart)
        self.infoWidget.setDefaultTimeEnd.connect(self.plotWidget.UpdateVlineEnd)
        self.paramWidget.ParametersNotReady.connect(self.DisableRunButton)
        self.paramWidget.ParametersReady.connect(self.EnableRunButton)
        
        self.abortButton.clicked.connect(self.AbortClicked)
        self.runButton.clicked.connect(self.RunButtonClicked)
        self.cancelButton.clicked.connect(self.CancelButtonClicked)
        self.nextButton.clicked.connect(self.NextButtonClicked)
        self.backButton.clicked.connect(self.BackButtonClicked)
        
        self.MainProcess = MultiprocessingQTimerInterResults()
        self.MainProcess.finished.connect(self.MainProcessFinished)
        self.MainProcess.started.connect(self.MainProcessStarted)
        self.MainProcess.stopped.connect(self.MainProcessStopped)
        self.MainProcess.stepnamechanged.connect(self.UpdateStepName)
        self.MainProcess.progressionchanged.connect(self.UpdateProgression)
        # Design
        dataParamLayout.setContentsMargins(0, 0, 0, 0)
        dataInfoLayout.setContentsMargins(0, 0, 0, 0)
        dataLayout.setContentsMargins(0, 0, 0, 0)
        BottomLayout.setContentsMargins(0, 0, 0, 0)
        pbarLayout.setContentsMargins(0, 0, 0, 0)
        botbutLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        
        dataParamWidget.setFixedWidth(self.paramWidget.width()+30)
        self.runButton.setFixedSize(100,50)
        self.cancelButton.setFixedSize(100,30)
        self.abortButton.setFixedSize(100,30)
        self.backButton.setFixedSize(100,30)
        self.nextButton.setFixedSize(100,30)
        self.paramWidget.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed))
        scrollParam.setMaximumHeight(self.paramWidget.height()+30)
        bottonWidget.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum))
        dataParamWidget.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding))
        scrollParam.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding))
        dataParamLayout.setAlignment(self.runButton,QtCore.Qt.AlignHCenter)
        botbutLayout.setAlignment(self.abortButton,QtCore.Qt.AlignHCenter)
        botbutLayout.setAlignment(self.backButton,QtCore.Qt.AlignHCenter)
        botbutLayout.setAlignment(self.nextButton,QtCore.Qt.AlignHCenter)
    
    # Enable or Disable buttons
    ###########################################################################
    def DisableRunButton(self):
        self.runButton.setDisabled(True)
    def EnableRunButton(self):
        self.runButton.setEnabled(True)
    def DisableCancelButton(self):
        self.cancelButton.setDisabled(True)
    def EnableCancelButton(self):
        self.cancelButton.setEnabled(True)
    def DisableNextButton(self):
        self.nextButton.setDisabled(True)
    def EnableNextButton(self):
        self.nextButton.setEnabled(True)
    ###########################################################################
    
    def resetView(self):
        # Attributes
        self.inputs = None
        self.result = None
        # Sub views
        self.paramWidget.resetView()
        self.plotWidget.resetView()
        self.infoWidget.resetView()
        # initialization
        self.DisableNextButton()
        self.DisableCancelButton()
        self.SubSteps.setText("")
        self.paramWidget.timeStartEdit.setText('')
        self.paramWidget.timeEndEdit.setText('')
        self.pbar.setValue(0)

    
    def InitView(self,inputs):
        self.resetView()
        self.inputs = inputs
        self.infoWidget.InitView(inputs)
        self.plotWidget.InitView(inputs)
        self.paramWidget.timeStartEdit.setText("0.0")
        self.paramWidget.timeEndEdit.setText("%.5f"%self.infoWidget.Length)
    
    
    def GetResults(self):
        return(self.result)
    
    # Buttons clicked
    ###########################################################################
    def AbortClicked(self):
        my_dialog = ConfirmAbortDialog(self) 
        if(my_dialog.exec_()):
            self.DisableCancelButton()
            self.MainProcess.stop()
            self.resetView()
            self.GoBackToMainMenu.emit()
        
    def CancelButtonClicked(self):
        my_dialog = ConfirmCancelDialog(self) 
        if(my_dialog.exec_()):
            self.DisableCancelButton()
            self.MainProcess.stop()
    
    def RunButtonClicked(self):
        if(not self.MainProcess.processRunning):
            parameters = self.paramWidget.GetParameters()
            self.MainProcess.start(RunStep_One,(self.inputs,parameters))
        else:
            my_dialog = ProcessAlreadyRunningDialog(self) 
            my_dialog.exec_()
    
    def NextButtonClicked(self):
        if(not self.MainProcess.processRunning):
            if(self.result is None):
                my_dialog = NoResultFoundDialog(self)
                my_dialog.exec_()
            else:
                self.GoForward.emit()
        else:
            my_dialog = ProcessAlreadyRunningDialog()
            my_dialog.exec_()
    
    def BackButtonClicked(self):
        my_dialog = ConfirmBackDialog(self) 
        if(my_dialog.exec_()):
            self.MainProcess.stop()
            self.resetView()
            self.GoBack.emit()
    ###########################################################################
    
    # Signals
    ###########################################################################
    def MainProcessStarted(self):
        self.result = None
        self.DisableNextButton()
        self.EnableCancelButton()
    
    def MainProcessStopped(self):
        self.UpdateProgression(0)
        self.DisableCancelButton()
    
    def MainProcessFinished(self):
        self.pbar.setValue(self.rangePbar)
        self.SubSteps.setText("Finished")
        self.EnableNextButton()
        self.DisableCancelButton()
        self.result = self.MainProcess.GetResults()
        self.plotWidget.plotResults(self.result)
    
    def UpdateStepName(self,NewName):
        self.SubSteps.setText(NewName)
    
    def UpdateProgression(self,NewProgress):
        self.pbar.setValue(NewProgress)
###############################################################################


