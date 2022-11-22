# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QWidget
# Layouts
from PyQt5.QtWidgets import QVBoxLayout

import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from converter.gui_converter_common_widgets import MyNavigationToolbar2QT
     
import numpy as np

def GetListConfigsPerNote(DigitalPartition):
    ListConfigs = []
    for note in DigitalPartition.NotesChrono:
        KeyNote = note[0][0]
        TempList = DigitalPartition.NotesDico[KeyNote].GetListValidConfRef()
        if(len(note)==2):
            KeyNote = note[1][0]
            TempList = TempList + DigitalPartition.NotesDico[KeyNote].GetListValidConfRef()
        ListConfigs.append(TempList)
        if(len(note[0])==2):
            KeyNote = note[0][1]
            TempList = DigitalPartition.NotesDico[KeyNote].GetListValidConfRef()
            ListConfigs.append(TempList)
    return(ListConfigs)


def GetListNotesType(DigitalPartition):
    ListType = []
    for note in DigitalPartition.NotesChrono:
        KeyNote = note[0][0]
        TempType = DigitalPartition.NotesDico[KeyNote].GetType()
        ListType.append(TempType)
        if(len(note[0])==2):
            KeyNote = note[0][1]
            TempType = DigitalPartition.NotesDico[KeyNote].GetType()
            ListType.append(TempType)
    return(ListType)


def GetListNotesLength(DigitalPartition):
    ListLength = []
    ListRef =[]
    for note in DigitalPartition.NotesChrono:
        KeyNote = note[0][0]
        TempLength = DigitalPartition.NotesDico[KeyNote].GetAnalogLength()
        ListLength.append(TempLength)
        ListRef.append(KeyNote)
        if(len(note[0])==2):
            KeyNote = note[0][1]
            TempLength = DigitalPartition.NotesDico[KeyNote].GetAnalogLength()
            ListLength.append(TempLength)
            ListRef.append(KeyNote)
    return(ListLength,ListRef)

def GetListXticksPosPerNote(DigitalPartition):
    ListLength,_ = GetListNotesLength(DigitalPartition)
    ListXPos = [0.0]
    PastPos = 0.0
    for k in range(0,len(ListLength)-1):
        ListXPos.append(ListLength[k] + PastPos)
        PastPos = ListLength[k] + PastPos
    return(ListXPos)

def GetXPosFromKeyNote(DigitalPartition,KeyNote):
    XNotePos = 0.0
    for note in DigitalPartition.NotesChrono:
        if(note[0][0]==KeyNote):
            break;
        if(len(note)==2):
            if(note[1][0]==KeyNote):
                break;
        XNotePos += DigitalPartition.NotesDico[note[0][0]].GetAnalogLength()
        if(len(note[0])==2):
            if(note[0][1]==KeyNote):
                break;
            XNotePos += DigitalPartition.NotesDico[note[0][1]].GetAnalogLength()
    return(XNotePos)



def GetDelayFromConfRefs(DigitalPartition,ListRefs):
    DelayList = []
    ErrorList = []
    for confref in ListRefs:
        conf = DigitalPartition._GetConfFromConfRef(confref)
        DelayList.append(conf.get_delay())
        ErrorList.append(conf.get_besterror())
    return(DelayList,ErrorList)

def Convert_Delay_to_BPM(Delay):
    return(60.0/Delay)

def Convert_Delay_to_LOG10Delay(Delay):
    return(10.0*np.log10(Delay))

def Convert_LOG10Delay_to_BPM(Delay):
    return(60.0/np.power(10.0,Delay/10.0))





class PlotStep3Widget(QWidget):
    def __init__(self, parent,echelle='log'):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = MyNavigationToolbar2QT(self.canvas, self)
        self.echelle = echelle
        # Layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.toolbar)
        mainLayout.addWidget(self.canvas)
        self.setLayout(mainLayout)

    ###########################################################################
    def resetView(self):
        self.figure.clf()
    
    def InitView(self):
        self.resetView()
        # Creating Axes
        self.gs = gridspec.GridSpec(2, 1, width_ratios=[1], height_ratios=[4,20])
        self.axInput = self.figure.add_subplot(self.gs[0])
        self.axField = self.figure.add_subplot(self.gs[1],sharex=self.axInput)
        # Updating canvas
        self.figure.set_tight_layout('tight')
        self.canvas.draw_idle()
    
    def plotResults(self,OutputStep3,DigitalPartition,parameters):
        self.Generate_axInput(DigitalPartition)
        self.Generate_axOutput(DigitalPartition)
        # Updating canvas
        self.canvas.draw_idle()
    
    def UpdateResults(self,OutputStep3,DigitalPartition,parameters):
        self.Update_axInput_axOutput(DigitalPartition)
        # Updating canvas
        self.canvas.draw_idle()
    ###########################################################################
    
    def Generate_axInput(self,DigitalPartition):
        ListLength,_ = GetListNotesLength(DigitalPartition)
        ListType = GetListNotesType(DigitalPartition)
        TpsNoteDeb = 0
        for Ind,length in enumerate(ListLength):
            if(ListType[Ind]=='rest'):
                Couleur = 'k'
            elif(Ind%2):
                Couleur = 'g'
            else:
                Couleur = 'b'
            rect = mpatches.Rectangle([TpsNoteDeb, -1], ListLength[Ind] , 2,color=Couleur, ec="none")
            self.axInput.add_patch(rect)
            TpsNoteDeb += ListLength[Ind]
        
        self.axInput.axes.get_yaxis().set_visible(False)
        self.axInput.axes.get_xaxis().set_visible(False)
        self.axInput.set_xlim([-0.1,TpsNoteDeb+0.1])
        self.axInput.set_xlabel("Time [s]")
    
    
    def _ConvertDelay(self,DelayVector):
        if(self.echelle=='log'):
            return(Convert_Delay_to_LOG10Delay(DelayVector))
        elif(self.echelle=='bpm'):
            return(Convert_Delay_to_BPM(DelayVector))
        else:
            return(DelayVector)
    
    def Update_axInput_axOutput(self,DigitalPartition):
        self.PlotBestPath(DigitalPartition)
    
    def PlotBestPath(self,DigitalPartition):
        ListDelay = []
        ListXPosNote = []
        for ConfRef in DigitalPartition.BestPathFound:
            conf = DigitalPartition._GetConfFromConfRef(ConfRef)
            KeyNote = conf.get_keynotes()[0]
            XPosTemp = GetXPosFromKeyNote(DigitalPartition,KeyNote)
            ListXPosNote.append(XPosTemp)
            ListDelay.append(conf.get_delay())
        DelayVector = np.array(ListDelay)
        XPosVector = np.array(ListXPosNote)
        self.plotBP.set_data(XPosVector,self._ConvertDelay(DelayVector))
        
    
    def Generate_axOutput(self,DigitalPartition):
        self.axField.set_xlabel("Notes [count]")
        
        if(self.echelle=='log'):
            self.axField.set_ylabel("10xLOG10(1/BPM)")
            self.axField.set_ylim([2,-5.5])
        elif(self.echelle=='bpm'):
            self.axField.set_ylabel("BPM")
            self.axField.set_ylim([35,205])
        else:
            self.axField.set_ylabel("delay")
            self.axField.set_ylim([1.714285,0.292683])
        
        ListConfigs = GetListConfigsPerNote(DigitalPartition)
        ListXticksPos = GetListXticksPosPerNote(DigitalPartition)
        # Set X parameters Ticks
        self.axField.set_xticks(ListXticksPos)
        self.axField.grid(b=True, which='major', color='k', axis='x', linestyle='--')
        
        # Plot points for each notes
        self.ListConfScatter = []
        for IndNote in range(len(ListConfigs)):
            DelayList, ErrorList = GetDelayFromConfRefs(DigitalPartition,ListConfigs[IndNote])
            DelayVector = np.array(DelayList)
            ErrorVector = np.array(ErrorList)
            
            XPosNote = np.ones(len(DelayVector))*ListXticksPos[IndNote]
            Tempcomb = self.axField.scatter(XPosNote,self._ConvertDelay(DelayVector),c='red', picker=10)
            self.ListConfScatter.append(Tempcomb)
            for IndConf in range(0,len(DelayVector)):
                if((DelayVector[IndConf] > 0.3) and (DelayVector[IndConf] < 1.5)):
                    self.axField.text(ListXticksPos[IndNote]+0.1,self._ConvertDelay(DelayVector[IndConf]),'%.3f'%ErrorVector[IndConf], fontsize=6)
        
        # Change Y ticks labels
        self.canvas.draw()
        labels = [item.get_text() for item in self.axField.get_yticklabels()]
        newlabels = []
        for label in labels:
            if(label != ''):
                if(self.echelle=='log'):
                    temp = float(label.replace(u"\u2212","-"))
                    BPM = Convert_LOG10Delay_to_BPM(temp)
                    newlabels.append(label+ '(BPM %d) '%BPM)
                elif(self.echelle=='bpm'):
                    temp = float(label)
                    Delay = 60.0/temp
                    newlabels.append(label+ '(delay %.2f) '%Delay)
                else:
                    temp = float(label)
                    BPM = 60.0/temp
                    newlabels.append(label+ '(BPM %.1f) '%BPM)
            else:
                newlabels.append('')
        self.axField.set_yticklabels(newlabels)
        
        # Change X ticks labels
        labels = [item.get_text() for item in self.axField.get_xticklabels()]
        newlabels = []
        for k in range(1,len(labels)+1):
            newlabels.append(k)
        self.axField.set_xticklabels(newlabels)

        # Plot of the best path found
        self.plotBP, = self.axField.plot([0],[0],'-x',color='r')
        self.PlotBestPath(DigitalPartition)
        #self.plotbestpath.set_visible('False')
        
        # Information on the selected note
        self.annot = self.axField.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"),
                            arrowprops=dict(arrowstyle="->"))
        self.annot.set_backgroundcolor('red')
        self.annot.set_color('white')
        self.annot.get_bbox_patch().set_alpha(1)
        self.annot.set_visible(False)
        

