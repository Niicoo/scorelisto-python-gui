# -*- coding: utf-8 -*-

# Widget
from PyQt5.QtWidgets import QWidget
# Layout
from PyQt5.QtWidgets import QVBoxLayout

from parameters.gui_parameters_common_widgets import QTabWidgetExpandable
from parameters.gui_parameters_tabGlobal_widget import TabGlobalParameterWidget
from parameters.gui_parameters_tabStep1_widget import TabStepOneParameterWidget
from parameters.gui_parameters_tabStep2_widget import TabStepTwoParameterWidget
from parameters.gui_parameters_tabStep3_widget import TabStepThreeParameterWidget

from gui_common_widgets import headerWidget


class MainParametersWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self,parent)
        self.parent = parent
        self.ParametersManager = parent.ParametersManager
        self.Header = headerWidget(self)
        mainLayout = QVBoxLayout()
        tab = QTabWidgetExpandable(self)
        self.tab0 = TabGlobalParameterWidget(self)
        self.tab1 = TabStepOneParameterWidget(self)
        self.tab2 = TabStepTwoParameterWidget(self)
        self.tab3 = TabStepThreeParameterWidget(self)
        tab.addTab(self.tab0,"Global")
        tab.addTab(self.tab1,"Step 1")
        tab.addTab(self.tab2,"Step 2")
        tab.addTab(self.tab3,"Step 3")
        mainLayout.addWidget(self.Header)
        mainLayout.addWidget(tab)
        self.setLayout(mainLayout)
        # Design
        mainLayout.setContentsMargins(0, 0, 0, 0)
        # Initialization
        self.Header.updateViewName("Parameters - step 1")
        # Connexions
        tab.currentChanged.connect(self.UpdateNameView)
    
    def UpdateNameView(self,NumTab):
        if(NumTab==0):
            self.Header.updateViewName("Parameters - step 1")
        elif(NumTab==1):
            self.Header.updateViewName("Parameters - step 2")
        elif(NumTab==2):
            self.Header.updateViewName("Parameters - step 3")
        elif(NumTab==3):
            self.Header.updateViewName("Parameters - step 4")