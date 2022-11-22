# -*- coding: utf-8 -*-
import matplotlib


MyStyleSheet = """
QDFialog {
    border: 2px solid ThemeColorPrimary;
}
QWidget
{
    color:TextColorEnabled;
    background-color: BackgroundColor;
}

QWidget:item:hover
{
    background-color:ButtonColorEnabled;
}

QWidget:item:selected
{
    background-color: ThemeColorPrimary;
}


QPushButton {
	color:TextColorEnabled;
    font-weight: bold;
	background-color:ButtonColorEnabled;
    border: none;
}

QPushButton:hover {
    background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 ThemeColorPrimary, stop:1 ThemeColorSecondary);
}

QPushButton:disabled {
    color:BackgroundColor;
    border: 2px solid ButtonColorEnabled;
    background-color:ButtonColorDisabled;
}

QTabWidget {
    border:none;
}
 
QTabBar::tab {
    height: 40px;
    font-weight: bold;
    text-transform: uppercase;
    border: none;
}

QTabBar::tab::selected {
    border-bottom: 6px solid ThemeColorPrimary;
    color:ThemeColorPrimary;
}

QLineEdit {
    background-color:ButtonColorEnabled;
}

QSvgWidget {
    color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 ThemeColorPrimary, stop:1 ThemeColorSecondary);
}

QPushButtonSelectFile {
    border : 5px dotted ThemeColorPrimary;
    font-weight: bold;
    width: 400;
    height:200;
    margin-bottom: 15px;
}

QPushButtonSelectFile::hover {
    background-color:ButtonColorDisabled;
}

QProgressBar {
    border: 2px solid ButtonColorEnabled;
    text-align: center;
}

QProgressBar::chunk {
     background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 ThemeColorPrimary, stop:1 ThemeColorSecondary);
}

QScrollArea {
    border: none;
}

QGroupBox {
    font-weight: bold;
}

QScrollBar:vertical {
    background-color: ButtonColorDisabled;
    width: 20px;
    border: 1px solid ButtonColorEnabled;
    margin-top:10px;
    margin-bottom:10px;
}

QScrollBar::handle:vertical {
    border: none;
    min-height: 30px;
    background-color: ButtonColorEnabled;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    border: none;
    background: none;
}

QScrollBar::left-arrow:vertical, QScrollBar::right-arrow:vertical, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    border: none;
    background: none;
    color: none;
}

QScrollBar:horizontal {
    background-color: ButtonColorDisabled;
    width: 20px;
    border: 1px solid ButtonColorEnabled;
    margin-top:10px;
    margin-bottom:10px;
}

QScrollBar::handle:horizontal {
    border: none;
    min-height: 30px;
    background-color: ButtonColorEnabled;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    border: none;
    background: none;
}

QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal, QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    border: none;
    background: none;
    color: none;
}

"""


def UpdateStyleSheet(   TextColorEnabled, \
                        TextColorDisabled, \
                        BackgroundColor, \
                        ThemeColorPrimary, \
                        ThemeColorSecondary, \
                        ButtonColorEnabled, \
                        ButtonColorDisabled):
    
    matplotlib.rcParams['text.color'] = TextColorEnabled
    matplotlib.rcParams['axes.labelcolor'] = TextColorEnabled
    matplotlib.rcParams['xtick.color'] = TextColorEnabled
    matplotlib.rcParams['ytick.color'] = TextColorEnabled
    matplotlib.rcParams['patch.facecolor'] = BackgroundColor
    matplotlib.rcParams['figure.facecolor'] = BackgroundColor
    matplotlib.rcParams['axes.facecolor'] = BackgroundColor
    
    MyStyleSheetOut = MyStyleSheet.replace("BackgroundColor",BackgroundColor)
    MyStyleSheetOut = MyStyleSheetOut.replace("ThemeColorPrimary",ThemeColorPrimary)
    MyStyleSheetOut = MyStyleSheetOut.replace("ThemeColorSecondary",ThemeColorSecondary)
    MyStyleSheetOut = MyStyleSheetOut.replace("TextColorEnabled",TextColorEnabled)
    MyStyleSheetOut = MyStyleSheetOut.replace("TextColorDisabled",TextColorDisabled)
    MyStyleSheetOut = MyStyleSheetOut.replace("ButtonColorEnabled",ButtonColorEnabled)
    MyStyleSheetOut = MyStyleSheetOut.replace("ButtonColorDisabled",ButtonColorDisabled)
    return(MyStyleSheetOut)

