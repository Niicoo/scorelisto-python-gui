# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QWidget
# Layouts
from PyQt5.QtWidgets import QVBoxLayout


from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from converter.gui_converter_common_widgets import MyNavigationToolbar2QT

import numpy as np


class PlotStep2ResultWidget(QWidget):
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
    
    def resetView(self):
        self.figure.clf()
        self.ax1 = self.figure.add_subplot(111)
        self.ax1.set_ylabel("Pitch [st]")
        self.ax1.set_xlabel("Time [s]")
        self.ax1.grid()
        self.originalplot = self.ax1.plot([],[])[0]
        self.listPlots = []
        self.figure.set_tight_layout('tight')
    
    def InitView(self,OutputStep1):
        self.resetView()
        x = np.arange(len(OutputStep1['pitch_st']))*OutputStep1['te_s']
        y = OutputStep1['pitch_st']
        self.originalplot.set_data(x,y)
        self.ax1.relim()
        self.ax1.autoscale_view()
        self.canvas.draw_idle()
    
    def plotResults(self,OutputStep2,offset):
        for plot in self.listPlots:
            plot.remove()
        self.listPlots = []
        OffsetTime = 0
        for note in OutputStep2:
            if(note['type_b']):
                TimeStart = OffsetTime
                TimeEnd = OffsetTime + note['length_s']
                tempPlot = self.ax1.plot([TimeStart+offset,TimeEnd+offset],[note['pitch_st'],note['pitch_st']],color='r',linewidth=2.0)[0]
                self.listPlots.append(tempPlot)
            OffsetTime += note['length_s']
        self.ax1.relim()
        self.ax1.autoscale_view()
        self.canvas.draw_idle()


class PlotStep2EnergyWidget(QWidget):
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
    
    def resetView(self):
        self.figure.clf()
        self.ax1 = self.figure.add_subplot(111)
        self.ax1.set_ylabel("Energy [dB]")
        self.ax1.set_xlabel("Time [s]")
        self.ax1.grid()
        self.originalplot = self.ax1.plot([],[])[0]
        self.listPlots = []
        self.figure.set_tight_layout('tight')
    
    def InitView(self,OutputStep1):
        self.resetView()
        x = np.arange(len(OutputStep1['energy_db']))*OutputStep1['te_s']
        y = OutputStep1['energy_db']
        self.originalplot.set_data(x,y)
        self.ax1.relim()
        self.ax1.autoscale_view()
        self.canvas.draw_idle()
    
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
