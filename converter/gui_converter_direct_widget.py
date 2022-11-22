# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSpacerItem
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QStackedWidget
# Layout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5 import QtCore,QtGui

from converter.gui_converter_common_widgets import TooRestrictivesParametersDialog
from converter.gui_converter_common_widgets import ResultConversionWidget

from gui_process_steps import RunStep_One
from gui_process_steps import RunStep_Two
from gui_process_steps import RunStep_Three

from PyQt5.QtCore import pyqtSignal

import multiprocessing
import ctypes

from gui_common_widgets import headerWidget


### direct convertion
###############################################################################
class DirectConversionWidget(QWidget):
    ConversionFailed = pyqtSignal()
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        self.parametersStep1 = None
        self.parametersStep2 = None
        self.parametersStep3 = None
        self.filename = None
        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.setInterval(100)
        # Widgets
        self.stack = QStackedWidget()
        self.pbar = QProgressBar(self)
        self.cancelButton = QPushButton("Cancel")
        self.MainStepName = QLabel()
        self.SubStepName = QLabel()
        self.Header = headerWidget()
        self.ResultWidget = ResultConversionWidget(self,EnableBackButton=False)
        # Layout
        progLayout = QVBoxLayout()
        progLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding))
        progLayout.addWidget(self.MainStepName)
        progLayout.addItem(QSpacerItem(20, 30, QSizePolicy.Maximum, QSizePolicy.Maximum))
        progLayout.addWidget(self.SubStepName)
        progLayout.addWidget(self.pbar)
        progLayout.addItem(QSpacerItem(20, 30, QSizePolicy.Maximum, QSizePolicy.Maximum))
        progLayout.addWidget(self.cancelButton)
        progLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding))
        mainWidget = QWidget()
        mainWidget.setLayout(progLayout)
        
        self.stack.addWidget(mainWidget)
        self.stack.addWidget(self.ResultWidget)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.Header)
        mainLayout.addWidget(self.stack)
        self.setLayout(mainLayout)
        
        # Initialization
        self.Header.updateViewName("Direct Conversion")
        # Connexions
        self.checkThreadTimer.timeout.connect(self.CheckProcessState)
        self.cancelButton.clicked.connect(self.CancelButtonClicked)
        self.cancelButton.setDisabled(True)
        # Initialization
        self.InitView()
        # Design
        self.MainStepName.setAlignment(QtCore.Qt.AlignCenter)
        myfont = QtGui.QFont()
        myfont.setBold(True)
        myfont.setPixelSize(30)
        self.MainStepName.setFont(myfont)
        self.cancelButton.setFixedSize(100,50)
        progLayout.setAlignment(self.cancelButton,QtCore.Qt.AlignCenter)
        
    
    def InitView(self):
        self.pbar.setRange(0, 100)
        self.pbar.setValue(0)
        self.pbar.resetFormat()
        self.MainStepName.setText("")
        self.SubStepName.setText("")
    
    def InitConversion(self,filename,GlobalParameterName):
        self.stack.setCurrentIndex(0)
        self.filename = filename
        StepParametersNames = self.ParametersManager.GetGlobalParameter(GlobalParameterName)
        self.parametersStep1 = self.ParametersManager.GetStep1Parameter(StepParametersNames['step1'])
        self.parametersStep1['TimeStart_s'] = None
        self.parametersStep1['TimeStop_s'] = None
        self.parametersStep2 = self.ParametersManager.GetStep2Parameter(StepParametersNames['step2'])
        self.parametersStep3 = self.ParametersManager.GetStep3Parameter(StepParametersNames['step3'])
        self.RunConversion()
    
    def CancelButtonClicked(self):
        if(self.t.is_alive()):
            self.t.terminate()
            self.result.put(b'')
    
    def ProcessFinished(self):
        self.checkThreadTimer.stop()
        self.cancelButton.setDisabled(True)
        self.SubStepName.setText("Finished")
        self.t.join()
        XMLByteString,MidiString,MidiString_norythm = self.result.get()
        if(XMLByteString != None):
            self.ResultWidget.InitView(XMLByteString,MidiString,MidiString_norythm)
            self.stack.setCurrentIndex(1)
        else:
            dialog = TooRestrictivesParametersDialog(self)
            dialog.exec_()
            self.ConversionFailed.emit()
    
    def UpdateProgression(self):
        if(self.mainstep.value==1):
            if(self.MainStepName.text()[0:6] != "Step 1"):
                self.pbar.setRange(0, 100)
                self.pbar.setFormat("%p%")
                self.MainStepName.setText("Step 1 : Pitch detection")
            self.SubStepName.setText(self.substep.value.decode("utf-8"))
            self.pbar.setValue(self.progression.value)
        elif(self.mainstep.value==2):
            if(self.MainStepName.text()[0:6] != "Step 2"):
                self.pbar.setRange(0, 8)
                self.pbar.setFormat("%v/%m")
                self.MainStepName.setText("Step 2 : Step detection")
            self.SubStepName.setText(self.substep.value.decode("utf-8"))
            self.pbar.setValue(self.progression.value)
        elif(self.mainstep.value==3):
            if(self.MainStepName.text()[0:6] != "Step 3"):
                self.pbar.setRange(0, 6)
                self.pbar.setFormat("%v/%m")
                self.MainStepName.setText("Step 3 : Notes detection")
            self.SubStepName.setText(self.substep.value.decode("utf-8"))
            self.pbar.setValue(self.progression.value)
    
    def CheckProcessState(self):
        if(self.t.is_alive()):
            self.UpdateProgression()
        else:
            self.ProcessFinished()
        
    def RunConversion(self):
        self.progression = multiprocessing.Value('d', 0.0)
        self.mainstep = multiprocessing.Value('i',0)
        self.substep = multiprocessing.Value(ctypes.c_char_p,b"")
        self.result = multiprocessing.Queue()
        self.t = multiprocessing.Process(target=self.Convert, args=(self.progression,self.mainstep,self.substep,self.result,))
        self.t.start()
        self.cancelButton.setEnabled(True)
        self.checkThreadTimer.start()
    
    def Convert(self,ProgressionValue,MainStepValue,SubStepValue,ResultQueue):
        MainStepValue.value = 1
        OUTPUT_STEP_1 = RunStep_One(self.filename,self.parametersStep1,ProgressionValue,SubStepValue)
        MainStepValue.value = 2
        OUTPUT_STEP_2,_ = RunStep_Two(OUTPUT_STEP_1,self.parametersStep2,ProgressionValue,SubStepValue)
        MainStepValue.value = 3
        XMLByteString,MidiString,MidiString_norythm,_ = RunStep_Three(OUTPUT_STEP_2,self.parametersStep3,ProgressionValue,SubStepValue)
        ResultQueue.put([XMLByteString,MidiString,MidiString_norythm])
###############################################################################





 