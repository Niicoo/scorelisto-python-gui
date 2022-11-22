#!/home/ndejax/miniconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:52:08 2018

@author: ndejax
"""
import sys
import argparse
import os

# Layout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
# Widget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QLocale
from PyQt5 import QtSvg
 

from parameters.gui_parameters_main import MainParametersWidget
from converter.gui_converter_main import MainConverterWidget
from parameters_manager import ManageParameters
from SvgUpdate import UpdateSVGIcons
from gui_stylesheet import UpdateStyleSheet
import gui_settings

class MainScoreListo(QMainWindow):
    # root window
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.setWindowIcon(QtGui.QIcon(os.path.join(ICON_DATA_PATH, 'favicon.svg')))
        self.setWindowTitle('ScoreListo GUI')
        #self.setGeometry(10,10,1280,320)
        self.center()
        # Attributes
        self.ParametersManager = ManageParameters(PATH_PARAMETERS_FILE)
        # Widgets
        iconSvgWidget = QtSvg.QSvgWidget(os.path.join(ICON_DATA_PATH, 'favicon.svg'))
        self.pushButtonConverter = QPushButton("Converter")
        self.pushButtonParameters = QPushButton("Parameters")
        self.converter = MainConverterWidget(self)
        self.parameters = MainParametersWidget(self)
        # Layouts
        self.stack = QStackedWidget()
        self.stack.addWidget(self.converter)
        self.stack.addWidget(self.parameters)
        rootLayout = QHBoxLayout()
        self.root = QWidget()
        ButtonWidget = QWidget()
        buttonsLayout = QVBoxLayout()
        buttonsLayout.addWidget(iconSvgWidget)
        buttonsLayout.addWidget(self.pushButtonConverter)
        buttonsLayout.addWidget(self.pushButtonParameters)
        ButtonWidget.setLayout(buttonsLayout)
        rootLayout.addWidget(ButtonWidget)
        rootLayout.addWidget(self.stack)
        self.root.setLayout(rootLayout)
        self.setCentralWidget(self.root)
        # Connexions
        self.pushButtonConverter.clicked.connect(self.drawConverterWidget)
        self.pushButtonParameters.clicked.connect(self.drawParametersWidget)
        # Design
        buttonsLayout.setContentsMargins(0, 0, 10, 0)
        self.stack.setContentsMargins(0,0,0,0)
        buttonsLayout.setAlignment(QtCore.Qt.AlignTop)
        self.pushButtonConverter.setFixedSize(100,50)
        self.pushButtonParameters.setFixedSize(100,50)
        iconSvgWidget.setFixedSize(100,100)
        
    def SetPageName(self,NewText):
        self.viewLabel.setText(NewText)
    
    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
    
    def drawConverterWidget(self):
        self.stack.setCurrentIndex(0)
    
    def drawParametersWidget(self):
        self.stack.setCurrentIndex(1)



TextColorEnabled = "#ffffff"
TextColorDisabled = "#a3a3a3"
BackgroundColor = "#1c1c1c"
ThemeColorPrimary = "#fe215d"
ThemeColorSecondary = "#fd15d5"
ButtonColorEnabled = "#3c3c3c"
ButtonColorDisabled = "#2c2c2c"

DATA_PATH = './data'
ICON_DATA_PATH = os.path.join(DATA_PATH, "icons")
PARAMETERS_DATA_PATH = os.path.join(DATA_PATH, "parameters")
PATH_PARAMETERS_FILE = os.path.join(PARAMETERS_DATA_PATH,"savedparameters.scorelisto")




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-cp','--colorprimary', help='Primary color of the theme', required=False)
    parser.add_argument('-cs','--colorsecondary', help='Secondary color of the theme', required=False)
    parser.add_argument('-ssoff','--stylesheetoff', help='Option to unactive stylesheet', action='store_true', required=False)
    parser.add_argument('-p','--datapath', help='Path of the data',required=False)
    args = vars(parser.parse_args())
    
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('chip_icon_normal.png'))    
    QLocale.setDefault(QLocale(31))
    # Update colors if specified
    if(args['colorprimary'] is not None):
        ThemeColorPrimary = args['colorprimary']
    if(args['colorsecondary'] is not None):
        ThemeColorSecondary = args['colorsecondary']
    if(args['datapath'] is not None):
        DATA_PATH = args['datapath']
        PATH_PARAMETERS_FILE = os.path.join(DATA_PATH, "parameters", "savedparameters.scorelisto")
        ICON_DATA_PATH = os.path.join(DATA_PATH, "icons")
    gui_settings.init(ICON_DATA_PATH)
    os.makedirs(ICON_DATA_PATH, exist_ok=True)
    os.makedirs(PARAMETERS_DATA_PATH, exist_ok=True)
    if(args['stylesheetoff'] is False):
        MyStyleSheet = UpdateStyleSheet(TextColorEnabled, \
                                        TextColorDisabled, \
                                        BackgroundColor, \
                                        ThemeColorPrimary, \
                                        ThemeColorSecondary, \
                                        ButtonColorEnabled, \
                                        ButtonColorDisabled)
        UpdateSVGIcons(ICON_DATA_PATH, ThemeColorPrimary, ThemeColorSecondary, TextColorEnabled)
    else:
        # Default theme
        UpdateSVGIcons(ICON_DATA_PATH, ThemeColorPrimary, ThemeColorSecondary, "ffffff")
        MyStyleSheet = ""
    
    root = MainScoreListo()
    root.setStyleSheet(MyStyleSheet)
    root.show()
    root.center()
    sys.exit(app.exec())


