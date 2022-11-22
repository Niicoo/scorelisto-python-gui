# -*- coding: utf-8 -*-

# Widgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
# Layouts
from PyQt5.QtWidgets import QVBoxLayout

            
class InputInfoStep3Widget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        # Attributes
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        # Widgets
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(6)
        self.tableWidget.setVerticalHeaderLabels(('Type', 'Length [ms]', 'f0 [Hz]','Pitch [st]','Energy [dB]','Linked',))
        # Layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.tableWidget)
        self.setLayout(mainLayout)
        # Initialization
        self.resetView()
    
    def resetView(self):
        nbColumn = self.tableWidget.columnCount()
        for k in range(nbColumn):
            self.tableWidget.removeColumn(0)
        
    
    def InitView(self,OutputStep2):
        self.resetView()
        nbColumn = len(OutputStep2)
        self.tableWidget.setColumnCount(nbColumn)
        for ind,note in enumerate(OutputStep2):
            self.tableWidget.setItem(0,ind, QTableWidgetItem("%r"%note['type_b']))
            self.tableWidget.setItem(1,ind, QTableWidgetItem("%.2f"%(note['length_s']*1e3)))
            if(note['type_b']):
                self.tableWidget.setItem(2,ind, QTableWidgetItem("%.1f"%note['f0_hz']))
                self.tableWidget.setItem(3,ind, QTableWidgetItem("%.1f"%note['pitch_st']))
                self.tableWidget.setItem(4,ind, QTableWidgetItem("%.1f"%note['energy_db']))
                self.tableWidget.setItem(5,ind, QTableWidgetItem("%r"%note['linked_b']))
            else:
                self.tableWidget.setItem(2,ind, QTableWidgetItem("None"))
                self.tableWidget.setItem(3,ind, QTableWidgetItem("None"))
                self.tableWidget.setItem(4,ind, QTableWidgetItem("None"))
                self.tableWidget.setItem(5,ind, QTableWidgetItem("None"))
    

