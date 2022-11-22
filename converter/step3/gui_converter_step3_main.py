#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QScrollArea
# Design
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QSpacerItem
# Layouts
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5 import QtCore

from converter.gui_converter_common_widgets import GetXmlFileOutPath
from converter.step3.gui_plot_step3_widget import PlotStep3Widget
from converter.step3.gui_info_step3_widget import InputInfoStep3Widget
from converter.step3.gui_parameters_step3_widget import ParametersStep3InputWidget
from converter.gui_converter_common_widgets import ConfirmCancelDialog,ConfirmAbortDialog,NoResultFoundDialog,ConfirmBackDialog
from converter.gui_converter_common_widgets import ProcessAlreadyRunningDialog

from PyQt5.QtCore import pyqtSignal

from gui_process_steps import RunStep_Three,RunStep_Three_bis
from gui_common_widgets import MultiprocessingQTimerInterResults


class Step3ConversionWidget(QWidget):
    GoBackToMainMenu = pyqtSignal()
    GoBack = pyqtSignal()
    GoForward = pyqtSignal()
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        self.rangePbar = 6
        # Widgets
        self.paramWidget = ParametersStep3InputWidget(self)
        self.plotWidget = PlotStep3Widget(self)
        self.infoWidget = InputInfoStep3Widget(self)
        self.SubSteps = QLabel("")
        self.cancelButton = QPushButton("cancel")
        self.comboStackChoice = QComboBox()
        self.comboStackChoice.addItems(["Note Infos","Result Plot"])
        self.runButton = QPushButton("run")
        self.abortButton = QPushButton("abort")
        self.backButton = QPushButton("back")
        self.nextButton = QPushButton("next")
        self.pbar = QProgressBar(self)
        self.pbar.setFormat("%v/%m")
        self.pbar.setRange(0, 6)
        # Layout
            # Section Parameters
        scrollParam = QScrollArea()
        scrollParam.setWidget(self.paramWidget)
        scrollParam.setWidgetResizable(True)
        dataParamWidget = QWidget()
        dataParamLayout = QVBoxLayout()
        dataParamLayout.addWidget(scrollParam)
        dataParamLayout.addWidget(self.runButton)
        dataParamLayout.addWidget(QWidget())
        dataParamWidget.setLayout(dataParamLayout)
        self.stackInfoPlot = QStackedWidget()
        self.stackInfoPlot.addWidget(self.infoWidget)
        self.stackInfoPlot.addWidget(self.plotWidget)
        
        InfoPlotWidget = QWidget()
        InfoPlotLayout = QVBoxLayout()
        InfoPlotLayout.addWidget(self.comboStackChoice)
        InfoPlotLayout.addWidget(self.stackInfoPlot)
        InfoPlotWidget.setLayout(InfoPlotLayout)
        
            # united sections
        dataWidget = QWidget()
        dataLayout = QHBoxLayout()
        dataLayout.addWidget(dataParamWidget)
        dataLayout.addWidget(InfoPlotWidget)
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
        self.comboStackChoice.currentIndexChanged.connect(self.drawStackWidget)
        # Design
        dataParamLayout.setContentsMargins(0, 0, 0, 0)
        InfoPlotLayout.setContentsMargins(0, 0, 0, 0)
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
        #scrollParam.setMaximumHeight(self.paramWidget.height()+30)
        bottonWidget.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum))
        dataParamWidget.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding))
        scrollParam.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding))
        dataParamLayout.setAlignment(self.runButton,QtCore.Qt.AlignHCenter)
        botbutLayout.setAlignment(self.abortButton,QtCore.Qt.AlignHCenter)
        botbutLayout.setAlignment(self.backButton,QtCore.Qt.AlignHCenter)
        botbutLayout.setAlignment(self.nextButton,QtCore.Qt.AlignHCenter)
    
    def drawStackWidget(self,index):
        self.stackInfoPlot.setCurrentIndex(index)
    
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
        self.UsedParameters = None
        self.result = None
        self.FirstRun = True
        # Sub views
        self.paramWidget.resetView()
        self.plotWidget.resetView()
        self.infoWidget.resetView()
        # initialization
        self.DisableNextButton()
        self.DisableCancelButton()
        self.SubSteps.setText("")
        self.pbar.setValue(0)
        self.pbar.setRange(0, 6)
    
    def InitView(self,inputs):
        self.resetView()
        self.inputs = inputs
        self.infoWidget.InitView(inputs)
        self.plotWidget.InitView()
    
    
    def GetResults(self):
        return(self.result)
    
    def SaveFile(self):
        FilePath = GetXmlFileOutPath()
        if(FilePath):
            with open(FilePath,mode='wb') as FileOut:
                FileOut.write(self.result)
    
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
            self.UsedParameters = self.paramWidget.GetParameters()
            if(self.FirstRun):
                self.MainProcess.start(RunStep_Three,(self.inputs,self.UsedParameters))
                self.pbar.setRange(0, 6)
            else:
                self.MainProcess.start(RunStep_Three_bis,(self.DigitalPartition,self.UsedParameters))
                self.pbar.setRange(0, 4)
        else:
            my_dialog = ProcessAlreadyRunningDialog(self) 
            my_dialog.exec_()
    
    def NextButtonClicked(self):
        if(not self.MainProcess.processRunning):
            if(self.result is None):
                my_dialog = NoResultFoundDialog()
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
        self.SubSteps.setText("Finished")
        self.EnableNextButton()
        self.DisableCancelButton()
        if(self.FirstRun):
            self.pbar.setValue(6)
            self.FirstRun = False
            self.result = self.MainProcess.GetResults()[0:3]
            self.DigitalPartition = self.MainProcess.GetResults()[3]
            self.plotWidget.plotResults(self.result,self.DigitalPartition,self.UsedParameters)
            self.comboStackChoice.setCurrentIndex(1)
        else:
            self.pbar.setValue(4)
            self.result = self.MainProcess.GetResults()[0:3]
            self.DigitalPartition = self.MainProcess.GetResults()[3]
            self.plotWidget.UpdateResults(self.result,self.DigitalPartition,self.UsedParameters)
    
    def UpdateStepName(self,NewName):
        self.SubSteps.setText(NewName)
    
    def UpdateProgression(self,NewProgress):
        self.pbar.setValue(NewProgress)
    ###########################################################################
###############################################################################





