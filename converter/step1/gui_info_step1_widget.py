# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGroupBox
# Layouts
from PyQt5.QtWidgets import QVBoxLayout

import wave
from PyQt5.QtCore import pyqtSignal

class InputInfoStep1Widget(QGroupBox):
    setDefaultTimeStart = pyqtSignal(float)
    setDefaultTimeEnd = pyqtSignal(float)
    def __init__(self, parent):
        QGroupBox.__init__(self,"File information", parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        self.Fe = 0.0
        self.Te = 0.0
        self.NbSamples = 0.0
        self.nb_channels = 0.0
        self.sampwidth = 0.0
        self.Length = 0.0
        # Widgets
        self.frequencyLabel = QLabel()
        self.periodLabel = QLabel()
        self.nbsmplesLabel = QLabel()
        self.lengthLabel = QLabel()
        self.samplewidthLabel = QLabel()
        self.nbchannelsLabel = QLabel()
        # Layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.frequencyLabel)
        mainLayout.addWidget(self.periodLabel)
        mainLayout.addWidget(self.nbsmplesLabel)
        mainLayout.addWidget(self.lengthLabel)
        mainLayout.addWidget(self.samplewidthLabel)
        mainLayout.addWidget(self.nbchannelsLabel)
        self.setLayout(mainLayout)
        # Initialization
        self.resetView()
    
    def EmitDefaultTimeStart(self):
        self.setDefaultTimeStart.emit(0.0)
    
    def EmitDefaultTimeEnd(self):
        self.setDefaultTimeEnd.emit(self.Length)
    
    def resetView(self):
        self.frequencyLabel.setText("Framerate:")
        self.periodLabel.setText("Period:")
        self.nbsmplesLabel.setText("Nb Samples:")
        self.lengthLabel.setText("Length:")
        self.samplewidthLabel.setText("Sample width:")
        self.nbchannelsLabel.setText("Nb of channels:")
    
    def InitView(self,filename):
        with wave.open(filename,mode='rb') as wavefile:
            self.Fe = wavefile.getframerate()
            self.Te = 1.0/self.Fe
            self.NbSamples = wavefile.getnframes()
            self.nb_channels = wavefile.getnchannels()
            self.sampwidth = wavefile.getsampwidth()
            self.Length = self.NbSamples*self.Te
        self.frequencyLabel.setText("Framerate: %.1f hz"%self.Fe)
        self.periodLabel.setText("Period: %.3f ms"%(self.Te*1000.0))
        self.nbsmplesLabel.setText("Nb Samples: %d"%self.NbSamples)
        self.lengthLabel.setText("Length: %.3f s"%self.Length)
        self.samplewidthLabel.setText("Sample width: %d byte(s)"%self.sampwidth)
        self.nbchannelsLabel.setText("Nb of channels: %d"%self.nb_channels)
    

