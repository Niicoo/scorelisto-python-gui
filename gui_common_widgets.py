# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QFrame
# Layouts
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QFormLayout

from PyQt5 import QtCore
from PyQt5.QtGui import QDoubleValidator
from PyQt5 import QtGui

from PyQt5.QtCore import pyqtSignal

from PyQt5.QtCore import QObject
from PyQt5 import QtSvg

import gui_settings

import os

import multiprocessing
import ctypes

# A class that proceed to a multiprocessing task with a QTimer and signals
###############################################################################
class MultiprocessingQTimer(QObject):
    finished = pyqtSignal()
    started = pyqtSignal()
    def __init__(self,IntervalTimer=100):
        QObject.__init__(self)
        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.setInterval(IntervalTimer)
        self.checkThreadTimer.timeout.connect(self.CheckProcessState)
        # Value to check if the process if finished
        self.V_isProcessFinished = multiprocessing.Value(ctypes.c_bool,False)
        self.Q_results = multiprocessing.Queue()
        self.results = None
        self.p = None
        self.processRunning = False
    
    def stop(self):
        if(self.p is not None):
            self.p.terminate()
            self.p = None
            self.processRunning = False
    
    def CheckProcessState(self):
        if(self.processRunning):
            if(self.V_isProcessFinished.value):
                self.results = self.Q_results.get()
                self.p.join()
                self.p = None
                self.checkThreadTimer.stop()
                self.processRunning = False
                self.finished.emit()
    
    def start(self,fonction,arguments):
        self.fonction = fonction
        self.arguments = arguments
        self.p = multiprocessing.Process(target=self.Process, args=(self.V_isProcessFinished,self.Q_results,))
        self.V_isProcessFinished.value = False
        self.p.start()
        self.processRunning = True
        self.started.emit()
        self.checkThreadTimer.start()
    
    def Process(self,processfinished,results):
        output = self.fonction(*self.arguments)
        processfinished.value = True
        results.put(output)
###############################################################################



# A class that proceed to a multiprocessing task with a QTimer and signals and intermediate results
###############################################################################
class MultiprocessingQTimerInterResults(QObject):
    finished = pyqtSignal()
    started = pyqtSignal()
    stopped = pyqtSignal()
    stepnamechanged = pyqtSignal(str)
    progressionchanged = pyqtSignal(int)
    def __init__(self,IntervalTimer=100):
        QObject.__init__(self)
        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.setInterval(IntervalTimer)
        self.checkThreadTimer.timeout.connect(self.CheckProcessState)
        # Value to check if the process if finished
        self.V_isProcessFinished = multiprocessing.Value(ctypes.c_bool,False)
        self.Q_results = multiprocessing.Queue()
        self.results = None
        self.p = None
        self.processRunning = False
        ### Added ###
        self.V_progression = multiprocessing.Value('d', 0.0)
        self.V_substep = multiprocessing.Value(ctypes.c_char_p,b"")
        self.progression = 0
        self.stepname = ""
        ###
    
    def stop(self):
        if(self.p is not None):
            self.p.terminate()
        self.p = None
        self.processRunning = False
        self.stopped.emit()
    
    def GetResults(self):
        return(self.results)
    
    def CheckProcessState(self):
        if(self.processRunning):
            if(self.V_isProcessFinished.value):
                self.results = self.Q_results.get()
                self.p.join()
                self.p = None
                self.checkThreadTimer.stop()
                self.processRunning = False
                self.finished.emit()
            elif(self.p.is_alive()):
                tempProgress = int(self.V_progression.value)
                if(tempProgress != self.progression):
                    self.progression = tempProgress
                    self.progressionchanged.emit(self.progression)
                tempStepname = self.V_substep.value.decode("utf-8")
                if(tempStepname != self.stepname):
                    self.stepname = tempStepname
                    self.stepnamechanged.emit(self.stepname)
                
    
    def start(self,fonction,arguments):
        self.fonction = fonction
        self.arguments = arguments
        self.progression = 0
        self.stepname = ""
        self.p = multiprocessing.Process(target=self.Process, args=(self.V_isProcessFinished,self.Q_results,self.V_progression,self.V_substep))
        self.V_isProcessFinished.value = False
        self.p.start()
        self.processRunning = True
        self.started.emit()
        self.checkThreadTimer.start()
    
    def Process(self,processfinished,results,progression,stepname):
        output = self.fonction(*self.arguments,progression,stepname)
        processfinished.value = True
        results.put(output)
###############################################################################


        
class headerWidget(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        # Widgets
        #self.appnameWidget = QtSvg.QSvgWidget(os.path.join(ICON_DATA_PATH, 'appname.svg'))
        self.viewname = QLabel("Parameters")
        HLineRight = QFrame()
        HLineLeft = QFrame()
        # Layout
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(HLineLeft)
        mainLayout.addWidget(self.viewname)
        mainLayout.addWidget(HLineRight)
        self.setLayout(mainLayout)
        # Design
        #self.appnameWidget.setFixedSize(90,15)
        HLineRight.setFrameShape(QFrame.HLine)
        HLineRight.setLineWidth(1)
        HLineLeft.setFrameShape(QFrame.HLine)
        HLineLeft.setLineWidth(1)
        HLineRight.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Maximum))
        HLineLeft.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Maximum))
        myfont = QtGui.QFont()
        myfont.setItalic(True)
        self.viewname.setFont(myfont)
        self.viewname.setAlignment(QtCore.Qt.AlignCenter)
    
    def updateViewName(self,NewText):
        self.viewname.setText(NewText)



class QLineEditWithCheck(QWidget):
    textChanged = pyqtSignal(str)
    returnPressed = pyqtSignal()
    textValid = pyqtSignal()
    textUnvalid = pyqtSignal()
    def __init__(self,parent,Validator):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        # Widgets
        self.lineEdit = QLineEdit()
        self.lineEdit.setValidator(Validator)
        self.iconSvgWidgetOk = QtSvg.QSvgWidget(os.path.join(gui_settings.DATA_PATH_ICONS, 'check.svg'))
        self.iconSvgWidgetNotOk = QtSvg.QSvgWidget(os.path.join(gui_settings.DATA_PATH_ICONS, 'cross.svg'))
        # Layout
        iconWidget = QWidget()
        iconLayout = QHBoxLayout()
        iconLayout.addWidget(self.iconSvgWidgetOk)
        iconLayout.addWidget(self.iconSvgWidgetNotOk)
        iconWidget.setLayout(iconLayout)
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.lineEdit)
        mainLayout.addWidget(iconWidget)
        self.setLayout(mainLayout)
        # Connexions
        self.lineEdit.textChanged.connect(self.EmittextChanged)
        self.lineEdit.returnPressed.connect(self.EmitreturnPressed)
        self.lineEdit.textChanged.connect(self.check_field_state)
        # Design
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        iconLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit.setFixedHeight(25)
        iconWidget.setFixedSize(20,20)
        self.SetInvalidIcon()
        
    
    def text(self):
        return(self.lineEdit.text())
    
    def setText(self,*args, **kwargs):
        self.lineEdit.setText(*args, **kwargs)
    
    def setEnabled(self,*args, **kwargs):
        self.lineEdit.setEnabled(*args, **kwargs)
    
    def setDisabled(self,*args, **kwargs):
        self.lineEdit.setDisabled(*args, **kwargs)
    
    def setValidator(self,*args, **kwargs):
        self.lineEdit.setValidator(*args, **kwargs)
    
    def validator(self):
        return(self.lineEdit.validator())
    
    def setNewPattern(self,RegEx):
        RegExParamName = QtCore.QRegularExpression(RegEx)
        validator = MyQRegularExpressionValidator(RegExParamName)
        self.lineEdit.setValidator(validator)
        
    def EmittextChanged(self,string):
        self.textChanged.emit(string)
    
    def EmitreturnPressed(self):
        self.returnPressed.emit()
    
    def SetValidIcon(self):
        self.iconSvgWidgetOk.setVisible(True)
        self.iconSvgWidgetNotOk.setVisible(False)
    
    def SetInvalidIcon(self):
        self.iconSvgWidgetOk.setVisible(False)
        self.iconSvgWidgetNotOk.setVisible(True)
    
    def IsValid(self):
        state = self.lineEdit.validator().validate(self.lineEdit.text(), 0)[0]
        if(state == QtGui.QValidator.Acceptable):
            return(True)
        else:
            return(False)
    
    def check_field_state(self, *args, **kwargs):
        state = self.validator().validate(self.text(), 0)[0]
        if state == QtGui.QValidator.Acceptable:
            self.SetValidIcon()
            self.textValid.emit()
        else:
            self.SetInvalidIcon()
            self.textUnvalid.emit()


class MyQRegularExpressionValidator(QtGui.QRegularExpressionValidator):
    def __init__(self,RegularExpression,parent=None):
        QtGui.QRegularExpressionValidator.__init__(self, RegularExpression,parent)
    
    def validate(self,*args, **kwargs):
        output = super(MyQRegularExpressionValidator, self).validate(*args, **kwargs)
        if(output[0]==QtGui.QValidator.Invalid):
            output = list(output)
            output[0] = QtGui.QValidator.Intermediate
            output = tuple(output)
        return(output)
    
    def UpdateForbiddenWords(self,ListForbiddenWords):
        WordToExclude = ""
        for word in ListForbiddenWords:
            WordToExclude += "|%s"%word
        RegExString = "^(?!^$%s)(.{3,128})$"%WordToExclude
        RegEx = QtCore.QRegularExpression(RegExString)
        self.setRegularExpression(RegEx)

# Parameters abstract widget
###############################################################################
class ParametersAbstractWidget(QWidget):
    ParametersReady = pyqtSignal()
    ParametersNotReady = pyqtSignal()
    def __init__(self,parent,editingMode):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        self.editingMode = editingMode
        # Widgets
        RegExParamName = QtCore.QRegularExpression("^(?!^$)(.{3,128})$")
        self.NameValidator = MyQRegularExpressionValidator(RegExParamName)
        self.nameParam = QLineEditWithCheck(self,self.NameValidator)
        self.mainWidget = QWidget()
        # Layout
        self.mainLayout = QVBoxLayout()
        if(self.editingMode == True):
            name_label = QLabel("Name")
            nameLayout = QVBoxLayout()
            nameLayout.addWidget(name_label)
            name_label.setStyleSheet("font-weight: bold;");
            nameLayout.addWidget(self.nameParam)
            NameParamWidget = QWidget()
            NameParamWidget.setLayout(nameLayout)
            self.mainLayout.addWidget(NameParamWidget)
            nameLayout.setContentsMargins(0, 0, 0, 10)
        self.mainLayout.addWidget(self.mainWidget)
        self.setLayout(self.mainLayout)
        # Connexions
        self.nameParam.textChanged.connect(self.CheckIfParametersAreready)
        # Design
        self.setFixedWidth(300)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        
    def CheckIfParametersAreready(self):
        if(self.AreParametersReady() and self.nameParam.IsValid()):
            self.ParametersReady.emit()
        else:
            self.ParametersNotReady.emit()
    
    def setMainWidgetLayout(self,mainLayout):
        self.mainWidget.setLayout(mainLayout)
    
    def GetNewParameterName(self):
        NewName = self.nameParam.text()
        return(NewName)
    
    def setNewParamName(self,name):
        self.nameParam.setText(name)
        if((name=='default') or (not self.editingMode)):
            self.nameParam.setDisabled(True)
        else:
            self.nameParam.setEnabled(True)
    
    ### Fonctions to define !
    def AreParametersReady(self):
        return(True)
    
    def SetValuesFromName(self,name):
        return(True)
    
    def GenerateDictonaryParameter(self):
        return(True)
    ###
###############################################################################


# A widget with all the parameters relative to step 1
###############################################################################
class ParametersStepOneWidget(ParametersAbstractWidget):
    def __init__(self,parent,editingMode = False):
        ParametersAbstractWidget.__init__(self,parent,editingMode)
        # Validators
        self.Validator_WS = QDoubleValidator()
        self.Validator_WS.setRange(1,10000,5)
        self.Validator_Te = QDoubleValidator()
        self.Validator_Te.setRange(1,1000,5)
        self.Validator_f0 = QDoubleValidator()
        self.Validator_f0.setRange(1e-3,1e6,5)
        self.Validator_FMin = QDoubleValidator()
        self.Validator_FMin.setRange(0,10000,5)
        self.Validator_FMax = QDoubleValidator()
        self.Validator_FMax.setRange(0,10000,5)
        self.Validator_CO = QDoubleValidator()
        self.Validator_CO.setRange(0,1,5)
        self.Validator_SCO = QDoubleValidator()
        self.Validator_SCO.setRange(0,1,5)
        # Widgets
        GroupGeneralParam = QGroupBox("General")
        WS_label = QLabel("Window size [ms]")
        Te_label = QLabel("Period [ms]")
        f0_label = QLabel("f0 [Hz]")
        GroupMcLeodParam = QGroupBox("Mc Leod pitch detection")
        FMin_label = QLabel("Minimum frequency [Hz]")
        FMax_label = QLabel("Maximum frequency [Hz]")
        CO_label = QLabel("CutOff [ms]")
        SCO_label = QLabel("Small CutOff [ms]")
        self.WS_edit = QLineEditWithCheck(self,self.Validator_WS)
        self.Te_edit = QLineEditWithCheck(self,self.Validator_Te)
        self.f0_edit = QLineEditWithCheck(self,self.Validator_f0)
        self.FMin_edit = QLineEditWithCheck(self,self.Validator_FMin)
        self.FMax_edit = QLineEditWithCheck(self,self.Validator_FMax)
        self.CO_edit = QLineEditWithCheck(self,self.Validator_CO)
        self.SCO_edit = QLineEditWithCheck(self,self.Validator_SCO)
        # Layouts
        layoutGeneral = QFormLayout()
        layoutGeneral.addWidget(WS_label)
        layoutGeneral.addWidget(self.WS_edit)
        layoutGeneral.addWidget(f0_label)
        layoutGeneral.addWidget(self.f0_edit)
        layoutGeneral.addWidget(Te_label)
        layoutGeneral.addWidget(self.Te_edit)
        GroupGeneralParam.setLayout(layoutGeneral)
        layoutMcLeod = QFormLayout()
        layoutMcLeod.addWidget(FMin_label)
        layoutMcLeod.addWidget(self.FMin_edit)
        layoutMcLeod.addWidget(FMax_label)
        layoutMcLeod.addWidget(self.FMax_edit)
        layoutMcLeod.addWidget(CO_label)
        layoutMcLeod.addWidget(self.CO_edit)
        layoutMcLeod.addWidget(SCO_label)
        layoutMcLeod.addWidget(self.SCO_edit)
        GroupMcLeodParam.setLayout(layoutMcLeod)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(GroupGeneralParam)
        mainLayout.addWidget(GroupMcLeodParam)
        self.setMainWidgetLayout(mainLayout)
        # Design
        GroupGeneralParam.setContentsMargins(0, 0, 0, 0)
        #GroupMcLeodParam.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum))
        #GroupGeneralParam.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum))
        
        # Connexions
        self.WS_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.Te_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.f0_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.FMin_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.FMax_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.CO_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.SCO_edit.textChanged.connect(self.CheckIfParametersAreready)
            
    
    def AreParametersReady(self):
        for LineEdit in [self.WS_edit,
                         self.Te_edit,
                         self.f0_edit,
                         self.FMin_edit,
                         self.FMax_edit,
                         self.CO_edit,
                         self.SCO_edit]:
            if(not LineEdit.IsValid()):
                return(False)
        return(True)
    
    def SetValuesFromName(self,name):
        params = self.ParametersManager.GetStep1Parameter(name)
        self.setNewParamName(name)
        self.WS_edit.setText("%.2f"%(params['WindowTimeSize_s']*1e3))
        self.Te_edit.setText("%.2f"%(params['SonogramPeriod_s']*1e3))
        self.f0_edit.setText("%.2f"%params['f0_hz'])
        self.FMin_edit.setText("%.2f"%params['FreqMin_hz'])
        self.FMax_edit.setText("%.2f"%params['FreqMax_hz'])
        self.CO_edit.setText("%.2f"%params['CutOff'])
        self.SCO_edit.setText("%.2f"%params['SmallCutOff'])
    
    def GenerateDictonaryParameter(self):
        ParamOut = {}
        ParamOut['WindowTimeSize_s'] = float(self.WS_edit.text())/1e3
        ParamOut['SonogramPeriod_s'] = float(self.Te_edit.text())/1e3
        ParamOut['f0_hz'] = float(self.f0_edit.text())
        ParamOut['FreqMin_hz'] = float(self.FMin_edit.text())
        ParamOut['FreqMax_hz'] = float(self.FMax_edit.text())
        ParamOut['CutOff'] = float(self.CO_edit.text())
        ParamOut['SmallCutOff'] = float(self.SCO_edit.text())
        return(ParamOut)
###############################################################################


# A widget with all the parameters relative to step 2
###############################################################################
class ParametersStepTwoWidget(ParametersAbstractWidget):
    def __init__(self,parent,editingMode = False):
        ParametersAbstractWidget.__init__(self, parent,editingMode)
        # Validators
        self.Validator_MF = QDoubleValidator()
        self.Validator_MF.setRange(1,1000,5)
        self.Validator_TEOn = QDoubleValidator()
        self.Validator_TEOn.setRange(1,150,5)
        self.Validator_TEOff = QDoubleValidator()
        self.Validator_TEOff.setRange(1,150,5)
        self.Validator_MPV = QDoubleValidator()
        self.Validator_MPV.setRange(0.01,100,5)
        self.Validator_MTS = QDoubleValidator()
        self.Validator_MTS.setRange(1,10000,5)
        self.Validator_MNS = QDoubleValidator()
        self.Validator_MNS.setRange(0,10000,5)
        self.Validator_MND = QDoubleValidator()
        self.Validator_MND.setRange(0,1,5)
        self.Validator_LMHG = QDoubleValidator()
        self.Validator_LMHG.setRange(0,2,5)
        # Widgets
        MF_label = QLabel("Median Filter window size [ms]")
        TEOn_label = QLabel("Threshold energy ON [dB]")
        TEOff_label = QLabel("Threshold energy OFF [dB]")
        MPV_label = QLabel("Max Pitch Variation [semitone]")
        MTS_label = QLabel("Minimum length of a detection [ms]")
        MNS_label = QLabel("Minimum length of a note [ms]")
        MND_label = QLabel("Minimum gap between 2 notes [semitone]")
        LMHG_label = QLabel("Width at mid height gaussian [semitone]")
        self.MF_edit = QLineEditWithCheck(self,self.Validator_MF)
        self.TEOn_edit = QLineEditWithCheck(self,self.Validator_TEOn)
        self.TEOff_edit = QLineEditWithCheck(self,self.Validator_TEOff)
        self.MPV_edit = QLineEditWithCheck(self,self.Validator_MPV)
        self.MTS_edit = QLineEditWithCheck(self,self.Validator_MTS)
        self.MNS_edit = QLineEditWithCheck(self,self.Validator_MNS)
        self.MND_edit = QLineEditWithCheck(self,self.Validator_MND)
        self.LMHG_edit = QLineEditWithCheck(self,self.Validator_LMHG)
        # Layout
        mainLayout = QFormLayout()
        mainLayout.addWidget(MF_label)
        mainLayout.addWidget(self.MF_edit)
        mainLayout.addWidget(TEOn_label)
        mainLayout.addWidget(self.TEOn_edit)
        mainLayout.addWidget(TEOff_label)
        mainLayout.addWidget(self.TEOff_edit)
        mainLayout.addWidget(MPV_label)
        mainLayout.addWidget(self.MPV_edit)
        mainLayout.addWidget(MTS_label)
        mainLayout.addWidget(self.MTS_edit)
        mainLayout.addWidget(MNS_label)
        mainLayout.addWidget(self.MNS_edit)
        mainLayout.addWidget(MND_label)
        mainLayout.addWidget(self.MND_edit)
        mainLayout.addWidget(LMHG_label)
        mainLayout.addWidget(self.LMHG_edit)
        # Design
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setMainWidgetLayout(mainLayout)
        
        # Connexions
        self.MF_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.TEOn_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.TEOff_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.MPV_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.MTS_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.MNS_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.MND_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.LMHG_edit.textChanged.connect(self.CheckIfParametersAreready)

        
    def AreParametersReady(self):
        for LineEdit in [self.MF_edit,
                         self.TEOn_edit,
                         self.TEOff_edit,
                         self.MPV_edit,
                         self.MTS_edit,
                         self.MNS_edit,
                         self.MND_edit,
                         self.LMHG_edit]:
            if(not LineEdit.IsValid()):
                return(False)
        return(True)
    
    def SetValuesFromName(self,name):
        params = self.ParametersManager.GetStep2Parameter(name)
        self.setNewParamName(name)
        self.MF_edit.setText("%.2f"%(params['MedianFilterSize_s']*1e3))
        self.TEOn_edit.setText("%.2f"%params['ThresholdEnergyON_dB'])
        self.TEOff_edit.setText("%.2f"%params['ThresholdEnergyOFF_dB'])
        self.MPV_edit.setText("%.2f"%params['MaxPitchVariation_st'])
        self.MTS_edit.setText("%.2f"%(params['MinimumTimeSize_s']*1e3))
        self.MNS_edit.setText("%.2f"%(params['MinNoteSize_s']*1e3))
        self.MND_edit.setText("%.2f"%params['MinNoteDiff_st'])
        self.LMHG_edit.setText("%.2f"%params['LMHGaussian_st'])
    
    def GenerateDictonaryParameter(self):
        ParamOut = {}
        ParamOut['MedianFilterSize_s'] = float(self.MF_edit.text())/1e3
        ParamOut['ThresholdEnergyON_dB'] = float(self.TEOn_edit.text())
        ParamOut['ThresholdEnergyOFF_dB'] = float(self.TEOff_edit.text())
        ParamOut['MaxPitchVariation_st'] = float(self.MPV_edit.text())
        ParamOut['MinimumTimeSize_s'] = float(self.MTS_edit.text())/1e3
        ParamOut['MinNoteSize_s'] = float(self.MNS_edit.text())/1e3
        ParamOut['MinNoteDiff_st'] = float(self.MND_edit.text())
        ParamOut['LMHGaussian_st'] = float(self.LMHG_edit.text())
        return(ParamOut)
###############################################################################



# A widget with all the parameters relative to step 3
###############################################################################
class ParametersStepThreeWidget(ParametersAbstractWidget):
    def __init__(self,parent,editingMode = False):
        ParametersAbstractWidget.__init__(self, parent,editingMode)
        # Validators
        self.Validator_BPM_Min = QDoubleValidator()
        self.Validator_BPM_Min.setRange(0,200,5)
        self.Validator_BPM_Max = QDoubleValidator()
        self.Validator_BPM_Max.setRange(0,200,5)
        self.Validator_MDV = QDoubleValidator()
        self.Validator_MDV.setRange(1e-3,1,5)
        self.Validator_EM = QDoubleValidator()
        self.Validator_EM.setRange(0,100,5)
        # Widgets
        BPM_Min_label = QLabel("BPM Min")
        BPM_Max_label = QLabel("BPM Max")
        MaxDelayVar_label = QLabel("Max BPM variation")
        ErrorMax_label = QLabel("Error Max")
        self.BPM_Min_edit = QLineEditWithCheck(self,self.Validator_BPM_Min)
        self.BPM_Max_edit = QLineEditWithCheck(self,self.Validator_BPM_Max)
        self.MaxDelayVar_edit = QLineEditWithCheck(self,self.Validator_MDV)
        self.ErrorMax_edit = QLineEditWithCheck(self,self.Validator_EM)
        self.OneNoteOneBeat = QCheckBox("1 note - 1 beat")
        self.OneNoteTwoBeat = QCheckBox("1 note - 2 beat")
        self.OneNoteThreeBeat = QCheckBox("1 note - 3 beat")
        self.OneNoteFourBeat = QCheckBox("1 note - 4 beat")
        self.OneNoteFiveBeat = QCheckBox("1 note - 5 beat")
        self.OneNoteSixBeat = QCheckBox("1 note - 6 beat")
        self.OneNoteSevenBeat = QCheckBox("1 note - 7 beat")
        self.OneNoteEightBeat = QCheckBox("1 note - 8 beat")
        self.OneRestOneBeat = QCheckBox("1 rest - 1 beat")
        self.OneRestTwoBeat = QCheckBox("1 rest - 2 beat")
        self.OneRestThreeBeat = QCheckBox("1 rest - 3 beat")
        self.OneRestFourBeat = QCheckBox("1 rest - 4 beat")
        self.OneRestFiveBeat = QCheckBox("1 rest - 5 beat")
        self.OneRestSixBeat = QCheckBox("1 rest - 6 beat")
        self.OneRestSevenBeat = QCheckBox("1 rest - 7 beat")
        self.OneRestEightBeat = QCheckBox("1 rest - 8 beat")
        self.EN_EN = QCheckBox("EN_EN")
        self.ER_EN = QCheckBox("ER_EN")
        self.EN_ER = QCheckBox("EN_ER")
        self.DEN_SN = QCheckBox("DEN_SN")
        self.SN_DEN = QCheckBox("SN_DEN")
        self.DQN_EN = QCheckBox("DQN_EN")
        self.QR_ER_EN = QCheckBox("QR-ER_EN")
        self.DQN_ER = QCheckBox("DQN_ER")
        self.EN_EN_QN = QCheckBox("EN_EN-QN")
        self.QN_DQN_EN = QCheckBox("QN-DQN_EN")
        self.QR_QR_ER_EN = QCheckBox("QR-QR-ER_EN")
        self.QN_DQN_ER = QCheckBox("QN-DQN_ER")
        self.EN_EN_HN = QCheckBox("EN_EN-HN")
        self.HN_DQN_EN = QCheckBox("HN-DQN_EN")
        self.QR_QR_QR_ER_EN = QCheckBox("QR-QR-QR-ER_EN")
        self.HN_DQN_ER = QCheckBox("HN-DQN_ER")
        self.EN_EN_DHN = QCheckBox("EN_EN-DHN")
        self.EN_SN_SN = QCheckBox("EN_SN_SN")
        self.ER_SN_SN = QCheckBox("ER_SN_SN")
        self.SN_SN_EN = QCheckBox("SN_SN_EN")
        self.SN_SN_ER = QCheckBox("SN_SN_ER")
        self.SN_EN_SN = QCheckBox("SN_EN_SN")
        self.T_EN_EN_EN = QCheckBox("T_EN_EN_EN")
        self.T_EN_DEN_SN = QCheckBox("T_EN_DEN_SN")
        self.T_EN_SN_DEN = QCheckBox("T_EN_SN_DEN")
        self.T_SN_EN_DEN = QCheckBox("T_SN_EN_DEN")
        self.T_SN_DEN_EN = QCheckBox("T_SN_DEN_EN")
        self.T_DEN_EN_SN = QCheckBox("T_DEN_EN_SN")
        self.T_DEN_SN_EN = QCheckBox("T_DEN_SN_EN")
        self.EN_QN_EN = QCheckBox("EN_QN_EN")
        self.DQN_SN_SN = QCheckBox("DQN_SN_SN")
        self.QN_DQN_SN_SN = QCheckBox("QN-DQN_SN_SN")
        self.HN_DQN_SN_SN = QCheckBox("HN-DQN_SN_SN")
        self.SN_SN_SN_SN = QCheckBox("SN_SN_SN_SN")
        # Layout
        paramLayout = QFormLayout()
        paramLayout.addWidget(BPM_Min_label)
        paramLayout.addWidget(self.BPM_Min_edit)
        paramLayout.addWidget(BPM_Max_label)
        paramLayout.addWidget(self.BPM_Max_edit)
        paramLayout.addWidget(MaxDelayVar_label)
        paramLayout.addWidget(self.MaxDelayVar_edit)
        paramLayout.addWidget(ErrorMax_label)
        paramLayout.addWidget(self.ErrorMax_edit)
        GeneralParams = QWidget()
        GeneralParams.setLayout(paramLayout)
        
        OneNoteParam = QGroupBox("Combinations of 1 note/rest")
        layoutOneNote = QFormLayout()
        layoutOneNote.addWidget(self.OneNoteOneBeat)
        layoutOneNote.addWidget(self.OneNoteTwoBeat)
        layoutOneNote.addWidget(self.OneNoteThreeBeat)
        layoutOneNote.addWidget(self.OneNoteFourBeat)
        layoutOneNote.addWidget(self.OneNoteFiveBeat)
        layoutOneNote.addWidget(self.OneNoteSixBeat)
        layoutOneNote.addWidget(self.OneNoteSevenBeat)
        layoutOneNote.addWidget(self.OneNoteEightBeat)
        layoutOneNote.addWidget(self.OneRestOneBeat)
        layoutOneNote.addWidget(self.OneRestTwoBeat)
        layoutOneNote.addWidget(self.OneRestThreeBeat)
        layoutOneNote.addWidget(self.OneRestFourBeat)
        layoutOneNote.addWidget(self.OneRestFiveBeat)
        layoutOneNote.addWidget(self.OneRestSixBeat)
        layoutOneNote.addWidget(self.OneRestSevenBeat)
        layoutOneNote.addWidget(self.OneRestEightBeat)
        OneNoteParam.setLayout(layoutOneNote)
        TwoNoteParam = QGroupBox("Combinations of 2 notes/rests")
        layoutTwoNote = QFormLayout()
        layoutTwoNote.addWidget(self.EN_EN)
        layoutTwoNote.addWidget(self.ER_EN)
        layoutTwoNote.addWidget(self.EN_ER)
        layoutTwoNote.addWidget(self.DEN_SN)
        layoutTwoNote.addWidget(self.SN_DEN)
        layoutTwoNote.addWidget(self.DQN_EN)
        layoutTwoNote.addWidget(self.QR_ER_EN)
        layoutTwoNote.addWidget(self.DQN_ER)
        layoutTwoNote.addWidget(self.EN_EN_QN)
        layoutTwoNote.addWidget(self.QN_DQN_EN)
        layoutTwoNote.addWidget(self.QR_QR_ER_EN)
        layoutTwoNote.addWidget(self.QN_DQN_ER)
        layoutTwoNote.addWidget(self.EN_EN_HN)
        layoutTwoNote.addWidget(self.HN_DQN_EN)
        layoutTwoNote.addWidget(self.QR_QR_QR_ER_EN)
        layoutTwoNote.addWidget(self.HN_DQN_ER)
        layoutTwoNote.addWidget(self.EN_EN_DHN)
        TwoNoteParam.setLayout(layoutTwoNote)
        ThreeNoteParam = QGroupBox("Combinations of 3 notes/rests")
        layoutThreeNote = QFormLayout()
        layoutThreeNote.addWidget(self.EN_SN_SN)
        layoutThreeNote.addWidget(self.ER_SN_SN)
        layoutThreeNote.addWidget(self.SN_SN_EN)
        layoutThreeNote.addWidget(self.SN_SN_ER)
        layoutThreeNote.addWidget(self.SN_EN_SN)
        layoutThreeNote.addWidget(self.T_EN_EN_EN)
        layoutThreeNote.addWidget(self.T_EN_DEN_SN)
        layoutThreeNote.addWidget(self.T_EN_SN_DEN)
        layoutThreeNote.addWidget(self.T_SN_EN_DEN)
        layoutThreeNote.addWidget(self.T_SN_DEN_EN)
        layoutThreeNote.addWidget(self.T_DEN_EN_SN)
        layoutThreeNote.addWidget(self.T_DEN_SN_EN)
        layoutThreeNote.addWidget(self.EN_QN_EN)
        layoutThreeNote.addWidget(self.DQN_SN_SN)
        layoutThreeNote.addWidget(self.QN_DQN_SN_SN)
        layoutThreeNote.addWidget(self.HN_DQN_SN_SN)
        ThreeNoteParam.setLayout(layoutThreeNote)
        FourNoteParam = QGroupBox("Combinations of 4 notes/rests")
        layoutFourNote = QFormLayout()
        layoutFourNote.addWidget(self.SN_SN_SN_SN)
        FourNoteParam.setLayout(layoutFourNote)
        
        combLayout = QVBoxLayout()
        combLayout.addWidget(OneNoteParam)
        combLayout.addWidget(TwoNoteParam)
        combLayout.addWidget(ThreeNoteParam)
        combLayout.addWidget(FourNoteParam)
        combsWidgets = QWidget()
        combsWidgets.setLayout(combLayout)
        
        scrollCombs = QScrollArea()
        scrollCombs.setWidget(combsWidgets)
        scrollCombs.setWidgetResizable(True)
        scrollCombs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(GeneralParams)
        mainLayout.addWidget(scrollCombs)
        self.setMainWidgetLayout(mainLayout)
        
        # Connexions
        self.BPM_Min_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.BPM_Max_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.MaxDelayVar_edit.textChanged.connect(self.CheckIfParametersAreready)
        self.ErrorMax_edit.textChanged.connect(self.CheckIfParametersAreready)
        # Design
        mainLayout.setContentsMargins(0, 0, 0, 0)
        paramLayout.setContentsMargins(0, 0, 0, 0)
    
    def AreParametersReady(self):
        for LineEdit in [self.BPM_Min_edit,
                         self.BPM_Max_edit,
                         self.MaxDelayVar_edit,
                         self.ErrorMax_edit]:
            if(not LineEdit.IsValid()):
                return(False)
        return(True)
    
    def SetValuesFromName(self,name):
        params = self.ParametersManager.GetStep3Parameter(name)
        self.setNewParamName(name)
        self.BPM_Max_edit.setText("%.2f"%(60.0/params['DelayMin_s']))
        self.BPM_Min_edit.setText("%.2f"%(60.0/params['DelayMax_s']))
        self.MaxDelayVar_edit.setText("%.2f"%(params['MaxDelayVar']))
        self.ErrorMax_edit.setText("%.2f"%(params['ErrorMax']))
         ########  1 NOTES #########
        self.OneNoteOneBeat.setChecked(not params['CombinationToMask']['1NOTE_1BEAT'])
        self.OneRestOneBeat.setChecked(not params['CombinationToMask']['1REST_1BEAT'])
        self.OneNoteTwoBeat.setChecked(not params['CombinationToMask']['1NOTE_2BEATS'])
        self.OneRestTwoBeat.setChecked(not params['CombinationToMask']['1REST_2BEATS'])
        self.OneNoteThreeBeat.setChecked(not params['CombinationToMask']['1NOTE_3BEATS'])
        self.OneRestThreeBeat.setChecked(not params['CombinationToMask']['1REST_3BEATS'])
        self.OneNoteFourBeat.setChecked(not params['CombinationToMask']['1NOTE_4BEATS'])
        self.OneRestFourBeat.setChecked(not params['CombinationToMask']['1REST_4BEATS'])
        self.OneNoteFiveBeat.setChecked(not params['CombinationToMask']['1NOTE_5BEATS'])
        self.OneRestFiveBeat.setChecked(not params['CombinationToMask']['1REST_5BEATS'])
        self.OneNoteSixBeat.setChecked(not params['CombinationToMask']['1NOTE_6BEATS'])
        self.OneRestSixBeat.setChecked(not params['CombinationToMask']['1REST_6BEATS'])
        self.OneNoteSevenBeat.setChecked(not params['CombinationToMask']['1NOTE_7BEATS'])
        self.OneRestSevenBeat.setChecked(not params['CombinationToMask']['1REST_7BEATS'])
        self.OneNoteEightBeat.setChecked(not params['CombinationToMask']['1NOTE_8BEATS'])
        self.OneRestEightBeat.setChecked(not params['CombinationToMask']['1REST_8BEATS'])
        ########  2 NOTES #########
        ### 1 BEAT
        self.EN_EN.setChecked(not params['CombinationToMask']['EN_EN'])
        self.ER_EN.setChecked(not params['CombinationToMask']['ER_EN'])
        self.EN_ER.setChecked(not params['CombinationToMask']['EN_ER'])
        self.DEN_SN.setChecked(not params['CombinationToMask']['DEN_SN'])
        self.SN_DEN.setChecked(not params['CombinationToMask']['SN_DEN'])
        ### 2 BEATS
        self.DQN_EN.setChecked(not params['CombinationToMask']['DQN_EN'])
        self.QR_ER_EN.setChecked(not params['CombinationToMask']['QR-ER_EN'])
        self.DQN_ER.setChecked(not params['CombinationToMask']['DQN_ER'])
        self.EN_EN_QN.setChecked(not params['CombinationToMask']['EN_EN-QN'])
        ### 3 BEATS
        self.QN_DQN_EN.setChecked(not params['CombinationToMask']['QN-DQN_EN'])
        self.QR_QR_ER_EN.setChecked(not params['CombinationToMask']['QR-QR-ER_EN'])
        self.QN_DQN_ER.setChecked(not params['CombinationToMask']['QN-DQN_ER'])
        self.EN_EN_HN.setChecked(not params['CombinationToMask']['EN_EN-HN'])
        ### 4 BEATS
        self.HN_DQN_EN.setChecked(not params['CombinationToMask']['HN-DQN_EN'])
        self.QR_QR_QR_ER_EN.setChecked(not params['CombinationToMask']['QR-QR-QR-ER_EN'])
        self.HN_DQN_ER.setChecked(not params['CombinationToMask']['HN-DQN_ER'])
        self.EN_EN_DHN.setChecked(not params['CombinationToMask']['EN_EN-DHN'])
        
        ######### 3 NOTES ##########
        ### 1 BEAT
        self.EN_SN_SN.setChecked(not params['CombinationToMask']['EN_SN_SN'])
        self.ER_SN_SN.setChecked(not params['CombinationToMask']['ER_SN_SN'])
        self.SN_SN_EN.setChecked(not params['CombinationToMask']['SN_SN_EN'])
        self.SN_SN_ER.setChecked(not params['CombinationToMask']['SN_SN_ER'])
        self.SN_EN_SN.setChecked(not params['CombinationToMask']['SN_EN_SN'])
        self.T_EN_EN_EN.setChecked(not params['CombinationToMask']['T_EN_EN_EN'])
        self.T_EN_DEN_SN.setChecked(not params['CombinationToMask']['T_EN_DEN_SN'])
        self.T_EN_SN_DEN.setChecked(not params['CombinationToMask']['T_EN_SN_DEN'])
        self.T_SN_EN_DEN.setChecked(not params['CombinationToMask']['T_SN_EN_DEN'])
        self.T_SN_DEN_EN.setChecked(not params['CombinationToMask']['T_SN_DEN_EN'])
        self.T_DEN_EN_SN.setChecked(not params['CombinationToMask']['T_DEN_EN_SN'])
        self.T_DEN_SN_EN.setChecked(not params['CombinationToMask']['T_DEN_SN_EN'])
        ### 2 BEATS
        self.EN_QN_EN.setChecked(not params['CombinationToMask']['EN_QN_EN'])
        self.DQN_SN_SN.setChecked(not params['CombinationToMask']['DQN_SN_SN'])
        ### 3 BEATS
        self.QN_DQN_SN_SN.setChecked(not params['CombinationToMask']['QN-DQN_SN_SN'])
        ### 4 BEATS
        self.HN_DQN_SN_SN.setChecked(not params['CombinationToMask']['HN-DQN_SN_SN'])
        ######### 4 NOTES ##########
        self.SN_SN_SN_SN.setChecked(not params['CombinationToMask']['SN_SN_SN_SN'])
    
    def GenerateDictonaryParameter(self):
        ParamOut = {}
        ParamOut['DelayMin_s'] =  60.0/float(self.BPM_Max_edit.text())
        ParamOut['DelayMax_s'] =  60.0/float(self.BPM_Min_edit.text())
        ParamOut['MaxDelayVar'] =  float(self.MaxDelayVar_edit.text())
        ParamOut['ErrorMax'] =  float(self.ErrorMax_edit.text())
        ParamOut['CombinationToMask'] = {}
         ########  1 NOTES #########
        ParamOut['CombinationToMask']['1NOTE_1BEAT'] =  not self.OneNoteOneBeat.isChecked()
        ParamOut['CombinationToMask']['1REST_1BEAT'] =  not self.OneRestOneBeat.isChecked()
        ParamOut['CombinationToMask']['1NOTE_2BEATS'] = not self.OneNoteTwoBeat.isChecked()
        ParamOut['CombinationToMask']['1REST_2BEATS'] = not self.OneRestTwoBeat.isChecked()
        ParamOut['CombinationToMask']['1NOTE_3BEATS'] = not self.OneNoteThreeBeat.isChecked()
        ParamOut['CombinationToMask']['1REST_3BEATS'] = not self.OneRestThreeBeat.isChecked()
        ParamOut['CombinationToMask']['1NOTE_4BEATS'] = not self.OneNoteFourBeat.isChecked()
        ParamOut['CombinationToMask']['1REST_4BEATS'] = not self.OneRestFourBeat.isChecked()
        ParamOut['CombinationToMask']['1NOTE_5BEATS'] = not self.OneNoteFiveBeat.isChecked()
        ParamOut['CombinationToMask']['1REST_5BEATS'] = not self.OneRestFiveBeat.isChecked()
        ParamOut['CombinationToMask']['1NOTE_6BEATS'] = not self.OneNoteSixBeat.isChecked()
        ParamOut['CombinationToMask']['1REST_6BEATS'] = not self.OneRestSixBeat.isChecked()
        ParamOut['CombinationToMask']['1NOTE_7BEATS'] = not self.OneNoteSevenBeat.isChecked()
        ParamOut['CombinationToMask']['1REST_7BEATS'] = not self.OneRestSevenBeat.isChecked()
        ParamOut['CombinationToMask']['1NOTE_8BEATS'] = not self.OneNoteEightBeat.isChecked()
        ParamOut['CombinationToMask']['1REST_8BEATS'] = not self.OneRestEightBeat.isChecked()
        ########  2 NOTES #########
        ### 1 BEAT
        ParamOut['CombinationToMask']['EN_EN'] =  not self.EN_EN.isChecked()
        ParamOut['CombinationToMask']['ER_EN'] =  not self.ER_EN.isChecked()
        ParamOut['CombinationToMask']['EN_ER'] =  not self.EN_ER.isChecked()
        ParamOut['CombinationToMask']['DEN_SN'] =  not self.DEN_SN.isChecked()
        ParamOut['CombinationToMask']['SN_DEN'] =  not self.SN_DEN.isChecked()
        ### 2 BEATS
        ParamOut['CombinationToMask']['DQN_EN'] =  not self.DQN_EN.isChecked()
        ParamOut['CombinationToMask']['QR-ER_EN'] =  not self.QR_ER_EN.isChecked()
        ParamOut['CombinationToMask']['DQN_ER'] =  not self.DQN_ER.isChecked()
        ParamOut['CombinationToMask']['EN_EN-QN'] =  not self.EN_EN_QN.isChecked()
        ### 3 BEATS
        ParamOut['CombinationToMask']['QN-DQN_EN'] =  not self.QN_DQN_EN.isChecked()
        ParamOut['CombinationToMask']['QR-QR-ER_EN'] =  not self.QR_QR_ER_EN.isChecked()
        ParamOut['CombinationToMask']['QN-DQN_ER'] =  not self.QN_DQN_ER.isChecked()
        ParamOut['CombinationToMask']['EN_EN-HN'] =  not self.EN_EN_HN.isChecked()
        ### 4 BEATS
        ParamOut['CombinationToMask']['HN-DQN_EN'] =  not self.HN_DQN_EN.isChecked()
        ParamOut['CombinationToMask']['QR-QR-QR-ER_EN'] =  not self.QR_QR_QR_ER_EN.isChecked()
        ParamOut['CombinationToMask']['HN-DQN_ER'] =  not self.HN_DQN_ER.isChecked()
        ParamOut['CombinationToMask']['EN_EN-DHN'] =  not self.EN_EN_DHN.isChecked()
        
        ######### 3 NOTES ##########
        ### 1 BEAT
        ParamOut['CombinationToMask']['EN_SN_SN'] =  not self.EN_SN_SN.isChecked()
        ParamOut['CombinationToMask']['ER_SN_SN'] =  not self.ER_SN_SN.isChecked()
        ParamOut['CombinationToMask']['SN_SN_EN'] =  not self.SN_SN_EN.isChecked()
        ParamOut['CombinationToMask']['SN_SN_ER'] =  not self.SN_SN_ER.isChecked()
        ParamOut['CombinationToMask']['SN_EN_SN'] =  not self.SN_EN_SN.isChecked()
        ParamOut['CombinationToMask']['T_EN_EN_EN'] =  not self.T_EN_EN_EN.isChecked()
        ParamOut['CombinationToMask']['T_EN_DEN_SN'] =  not self.T_EN_DEN_SN.isChecked()
        ParamOut['CombinationToMask']['T_EN_SN_DEN'] =  not self.T_EN_SN_DEN.isChecked()
        ParamOut['CombinationToMask']['T_SN_EN_DEN'] =  not self.T_SN_EN_DEN.isChecked()
        ParamOut['CombinationToMask']['T_SN_DEN_EN'] =  not self.T_SN_DEN_EN.isChecked()
        ParamOut['CombinationToMask']['T_DEN_EN_SN'] =  not self.T_DEN_EN_SN.isChecked()
        ParamOut['CombinationToMask']['T_DEN_SN_EN'] =  not self.T_DEN_SN_EN.isChecked()
        ### 2 BEATS
        ParamOut['CombinationToMask']['EN_QN_EN'] =  not self.EN_QN_EN.isChecked()
        ParamOut['CombinationToMask']['DQN_SN_SN'] =  not self.DQN_SN_SN.isChecked()
        ### 3 BEATS
        ParamOut['CombinationToMask']['QN-DQN_SN_SN'] =  not self.QN_DQN_SN_SN.isChecked()
        ### 4 BEATS
        ParamOut['CombinationToMask']['HN-DQN_SN_SN'] =  not self.HN_DQN_SN_SN.isChecked()
        ######### 4 NOTES ##########
        ParamOut['CombinationToMask']['SN_SN_SN_SN'] =  not self.SN_SN_SN_SN.isChecked()
        return(ParamOut)
###############################################################################




# A widget with all the parameters relative to the global param
###############################################################################
class ParametersGlobalWidget(ParametersAbstractWidget):
    def __init__(self,parent,editingMode = False):
        ParametersAbstractWidget.__init__(self, parent, editingMode)
        # Widgets
        step1_label = QLabel("Step 1")
        step2_label = QLabel("Step 2")
        step3_label = QLabel("Step 3")
        self.choiceStep1 = QComboBox()
        self.choiceStep2 = QComboBox()
        self.choiceStep3 = QComboBox()
        mainLayout = QFormLayout()
        mainLayout.addRow(step1_label,self.choiceStep1)
        mainLayout.addRow(step2_label,self.choiceStep2)
        mainLayout.addRow(step3_label,self.choiceStep3)
        self.setMainWidgetLayout(mainLayout)
        # Initialisation
        self.UpdateListCombo1()
        self.UpdateListCombo2()
        self.UpdateListCombo3()
        # Design
        mainLayout.setContentsMargins(0, 0, 0, 0)
    
    def UpdateListCombo1(self):
        liststep1 = self.ParametersManager.GetListOfStep1Parameters()
        self.choiceStep1.clear()
        self.choiceStep1.addItems(liststep1)
    
    def UpdateListCombo2(self):
        liststep2 = self.ParametersManager.GetListOfStep2Parameters()
        self.choiceStep2.clear()
        self.choiceStep2.addItems(liststep2)
    
    def UpdateListCombo3(self):
        liststep3 = self.ParametersManager.GetListOfStep3Parameters()
        self.choiceStep3.clear()
        self.choiceStep3.addItems(liststep3)
    
    def SetValueCombo1(self,namestep1):
        index = self.choiceStep1.findText(namestep1, QtCore.Qt.MatchFixedString)
        if index >= 0:
             self.choiceStep1.setCurrentIndex(index)
    
    def SetValueCombo2(self,namestep2):
        index = self.choiceStep2.findText(namestep2, QtCore.Qt.MatchFixedString)
        if index >= 0:
             self.choiceStep2.setCurrentIndex(index)
    
    def SetValueCombo3(self,namestep3):
        index = self.choiceStep3.findText(namestep3, QtCore.Qt.MatchFixedString)
        if index >= 0:
             self.choiceStep3.setCurrentIndex(index)
    
    def SetGlobalName(self,NameGlobal):
        self.nameParam.setText(NameGlobal)
    
    def SetValuesFromName(self,name):
        self.setNewParamName(name)
        params = self.ParametersManager.GetGlobalParameter(name)
        self.SetGlobalName(name)
        self.SetValueCombo1(params['step1'])
        self.SetValueCombo2(params['step2'])
        self.SetValueCombo3(params['step3'])

    def GenerateDictonaryParameter(self):
        step1 = self.choiceStep1.currentText()
        step2 = self.choiceStep2.currentText()
        step3 = self.choiceStep3.currentText()
        ParamOut = {'step1':step1,'step2':step2,'step3':step3}
        return(ParamOut)
###############################################################################


