#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QWidget
# Layouts
from PyQt5.QtWidgets import QVBoxLayout

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from converter.gui_converter_common_widgets import MyNavigationToolbar2QT

import wave
import numpy as np
from gui_common_widgets import MultiprocessingQTimer


def GetSignalTempToPlot(filename,SubSamplingRate=8000.0):
    with wave.open(filename,mode='rb') as wavefile:
        Fe = wavefile.getframerate()
        Te = 1.0/Fe
        NbSamples = wavefile.getnframes()
        nb_channels = wavefile.getnchannels()
        
        sampwidth = wavefile.getsampwidth()
        temp = wavefile.readframes(NbSamples)
        
        if sampwidth == 1:
            temp = np.fromstring(temp,dtype=np.int8)
        elif sampwidth == 2:
            temp = np.fromstring(temp,dtype=np.int16)
        elif sampwidth == 4:
            temp = np.fromstring(temp,dtype=np.int32)
        elif sampwidth == 8:
            temp = np.fromstring(temp,dtype=np.int64)
        else:
            print("The sampled width is not compatible: number of Bytes= %d"%sampwidth)
            raise ValueError("The sample width of the wav file is not compatible with the application")
        
        if(Fe>SubSamplingRate):
            BestError = np.inf
            BestInd = 1
            for div in range(2,10):
                error = np.abs(SubSamplingRate - 1.0/(Te*div))
                if(error < BestError):
                    BestError = error
                    BestInd = div
            
            NbSampFinal = int(NbSamples/(nb_channels*BestInd))
            xData = np.arange(0,NbSampFinal)*(Te*BestInd)
            yData = np.zeros(NbSampFinal,dtype=temp.dtype)
            for k in range(0,NbSampFinal):
                samps = temp[k*BestInd*nb_channels:(k*BestInd+1)*nb_channels].astype(np.float)
                yData[k] = np.round(np.mean(samps)).astype(temp.dtype)
        else:
            NbSampFinal = int(NbSamples/nb_channels)
            xData = np.arange(0,NbSampFinal)*Te
            yData = np.zeros(NbSampFinal,dtype=temp.dtype)
            for k in range(0,NbSampFinal):
                samps = temp[k*nb_channels:(k+1)*nb_channels].astype(np.float)
                yData[k] = np.round(np.mean(samps)).astype(temp.dtype)
        return({'x':xData,'y':yData})
        

class PlotStep1Widget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = MyNavigationToolbar2QT(self.canvas, self)
        # set the layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.toolbar)
        mainLayout.addWidget(self.canvas)
        self.setLayout(mainLayout)
        # Initialization
        self.resetView()
        self.ProcessForPlotting = MultiprocessingQTimer(500)
        self.ProcessForPlotting.finished.connect(self.plotSignalTemp)
    
    def resetView(self):
        self.figure.clf()
        self.ax1 = self.figure.add_subplot(211)
        self.ax1.set_ylabel("Amplitude")
        self.lineStart = self.ax1.axvline(0,linestyle='--',color='r')
        self.lineEnd = self.ax1.axvline(0,linestyle='--',color='r')
        self.lineStart.set_visible(False)
        self.lineEnd.set_visible(False)
        self.ax2 = self.figure.add_subplot(212,sharex=self.ax1)
        self.ax2.set_ylabel("Pitch")
        self.ax2.set_xlabel("Time [s]")
        self.ax1.grid()
        self.ax2.grid()
        self.resultPlot = self.ax2.plot([],[])[0]
        self.figure.set_tight_layout('tight')
    
    def UpdateVlineStart(self,x_lineStart):
        if(x_lineStart is not None):
            self.lineStart.set_xdata(x_lineStart)
            self.lineStart.set_visible(True)
            self.canvas.draw_idle()
        else:
            self.lineStart.set_visible(False)
    
    def UpdateVlineEnd(self,x_lineEnd):
        if(x_lineEnd is not None):
            self.lineEnd.set_xdata(x_lineEnd)
            self.lineEnd.set_visible(True)
            self.canvas.draw_idle()
        else:
            self.lineEnd.set_visible(False)
    
    def plotSignalTemp(self):
        x = self.ProcessForPlotting.results['x']
        y = self.ProcessForPlotting.results['y']
        self.ax1.plot(x,y)
        self.canvas.draw_idle()
    
    def plotResults(self,OutputStep1):
        x = np.arange(len(OutputStep1['pitch_st']))*OutputStep1['te_s']
        y = OutputStep1['pitch_st']
        self.resultPlot.set_data(x,y)
        self.ax2.relim()
        self.ax2.autoscale_view()
        self.canvas.draw_idle()
    
    def InitView(self,filename):
        self.ProcessForPlotting.start(GetSignalTempToPlot,(filename,))
            
