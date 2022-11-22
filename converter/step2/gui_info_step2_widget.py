# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
# Layouts
from PyQt5.QtWidgets import QVBoxLayout

import numpy as np
       
class InputInfoStep2Widget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        self.Te = None
        self.f0 = None
        self.EnergyMax = None
        self.EnergyMin = None
        self.PitchMin = None
        self.PitchMax = None
        # Widgets
        self.TeLabel = QLabel()
        self.f0Label = QLabel()
        self.EnergyMaxLabel = QLabel()
        self.EnergyMinLabel = QLabel()
        self.PitchMaxLabel = QLabel()
        self.PitchMinLabel = QLabel()
        # Layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.TeLabel)
        mainLayout.addWidget(self.f0Label)
        mainLayout.addWidget(self.EnergyMinLabel)
        mainLayout.addWidget(self.EnergyMaxLabel)
        mainLayout.addWidget(self.PitchMinLabel)
        mainLayout.addWidget(self.PitchMaxLabel)
        self.setLayout(mainLayout)
        # Initialization
        self.resetView()
    
    def resetView(self):
        self.TeLabel.setText("Period:")
        self.f0Label.setText("f0:")
        self.EnergyMaxLabel.setText("Energy max:")
        self.EnergyMinLabel.setText("Energy min:")
        self.PitchMaxLabel.setText("Pitch max:")
        self.PitchMinLabel.setText("Pitch min:")
    
    def InitView(self,OutputStep1):
        self.Te = OutputStep1['te_s']
        self.f0 = OutputStep1['f0_hz']
        self.EnergyMax = np.max(np.ma.masked_invalid(OutputStep1['energy_db']))
        self.EnergyMin = np.min(np.ma.masked_invalid(OutputStep1['energy_db']))
        self.PitchMin = np.min(np.ma.masked_invalid(OutputStep1['pitch_st']))
        self.PitchMax = np.min(np.ma.masked_invalid(OutputStep1['pitch_st']))
        self.TeLabel.setText("Period: %.1f ms"%(self.Te*1000))
        self.f0Label.setText("f0: %.1f Hz"%self.f0)
        self.EnergyMaxLabel.setText("Energy max: %.1f dB"%self.EnergyMax)
        self.EnergyMinLabel.setText("Energy min: %.1f dB"%self.EnergyMin)
        self.PitchMaxLabel.setText("Pitch max: %.1f st"%self.PitchMax)
        self.PitchMinLabel.setText("Pitch min: %.1f st"%self.PitchMin)
    
