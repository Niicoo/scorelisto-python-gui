#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def UpdateSVGIcons(DATAPATH,ThemeColorPrimary,ThemeColorSecondary,TextColorEnabled):
    os.makedirs(DATAPATH, exist_ok=True)
    StringToWrite = CreateStringSvg_appname(ThemeColorPrimary,ThemeColorSecondary)
    with open(os.path.join(DATAPATH, "appname.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvg_favicon(ThemeColorPrimary,ThemeColorSecondary)
    with open(os.path.join(DATAPATH, "favicon.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvg_check(TextColorEnabled)
    with open(os.path.join(DATAPATH, "check.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvg_cross(TextColorEnabled)
    with open(os.path.join(DATAPATH, "cross.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvg_warning(ThemeColorPrimary,ThemeColorSecondary)
    with open(os.path.join(DATAPATH, "warning.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvg_questionmark(ThemeColorPrimary,ThemeColorSecondary)
    with open(os.path.join(DATAPATH, "questionmark.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvg_edit(ThemeColorPrimary,ThemeColorSecondary)
    with open(os.path.join(DATAPATH, "edit.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvgMPL_move(TextColorEnabled)
    with open(os.path.join(DATAPATH, "move.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvgMPL_subplots(TextColorEnabled)
    with open(os.path.join(DATAPATH, "subplots.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvgMPL_filesave(TextColorEnabled)
    with open(os.path.join(DATAPATH, "filesave.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvgMPL_home(TextColorEnabled)
    with open(os.path.join(DATAPATH, "home.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvgMPL_forward(TextColorEnabled)
    with open(os.path.join(DATAPATH, "forward.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvgMPL_zoom_to_rect(TextColorEnabled)
    with open(os.path.join(DATAPATH, "zoom_to_rect.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvgMPL_qt4_editor_options(TextColorEnabled)
    with open(os.path.join(DATAPATH, "qt4_editor_options.svg"),'w') as fileout:
        fileout.write(StringToWrite)
    
    StringToWrite = CreateStringSvgMPL_back(TextColorEnabled)
    with open(os.path.join(DATAPATH, "back.svg"),'w') as fileout:
        fileout.write(StringToWrite)


def CreateStringSvg_check(TextColor):
    StringSVG = """<svg
xmlns="http://www.w3.org/2000/svg" 
width="24" 
height="24" 
viewBox="0 0 24 24" 
fill="none" 
stroke="%s" 
stroke-width="2" 
stroke-linecap="round" 
stroke-linejoin="round" 
class="feather 
feather-check">
<polyline points="20 6 9 17 4 12"></polyline>
</svg>
    """%TextColor
    return(StringSVG)

def CreateStringSvg_cross(TextColor):
    StringSVG = """<svg
xmlns="http://www.w3.org/2000/svg" 
width="24" 
height="24" 
viewBox="0 0 24 24" 
fill="none" 
stroke="%s" 
stroke-width="2" 
stroke-linecap="round" 
stroke-linejoin="round" 
class="feather feather-x">
<line x1="18" y1="6" x2="6" y2="18"></line>
<line x1="6" y1="6" x2="18" y2="18"></line>
</svg>
    """%TextColor
    return(StringSVG)


def CreateStringSvg_appname(ThemeColorPrimary,ThemeColorSecondary):
    StringSVG = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   id="svg4190"
   version="1.1"
   inkscape:version="0.91 r13725"
   width="500"
   height="80"
   viewBox="0 0 500 80"
   sodipodi:docname="appname.svg">
  <metadata
     id="metadata4196">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <defs
     id="defs4194">
    <linearGradient
       inkscape:collect="always"
       id="linearGradient4208">
      <stop
         style="stop-color:%s;stop-opacity:1;"
         offset="0"
         id="stop4210" />
      <stop
         style="stop-color:%s;stop-opacity:1;"
         offset="1"
         id="stop4212" />
    </linearGradient>
    <linearGradient
       inkscape:collect="always"
       xlink:href="#linearGradient4208"
       id="linearGradient4214"
       x1="0"
       y1="40.000001"
       x2="500"
       y2="40.000001"
       gradientUnits="userSpaceOnUse" />
  </defs>
  <sodipodi:namedview
     pagecolor="#888888"
     bordercolor="#666666"
     borderopacity="1"
     objecttolerance="10"
     gridtolerance="10"
     guidetolerance="10"
     inkscape:pageopacity="1"
     inkscape:pageshadow="2"
     inkscape:window-width="1920"
     inkscape:window-height="1023"
     id="namedview4192"
     showgrid="false"
     inkscape:zoom="2.167876"
     inkscape:cx="227.52825"
     inkscape:cy="60.669725"
     inkscape:window-x="0"
     inkscape:window-y="0"
     inkscape:window-maximized="1"
     inkscape:current-layer="svg4190" />
  <path
     style="fill:url(#linearGradient4214);fill-opacity:1;stroke:none"
     d="m 0.058541,70.998652 0,-9.001348 14.557463,-0.211609 14.557465,-0.211612 -6.388593,-9.21296 -6.388593,-9.21295 -8.168871,0 -8.168871,0 0,-9.01694 0,-9.01695 11.283401,0.0489 11.2834,0.0489 13.277418,18.4514 13.277419,18.451382 -4.505181,8.942558 -4.50518,8.942547 -20.055639,0 -20.055638,0 0,-9.001338 z m 53.465962,-18.049459 0,-27.05082 7.985176,0 7.985176,0 0,18.03388 0,18.033872 16.265932,0 16.265923,0 -4.54264,9.016939 L 92.94141,80 l -19.708452,0 -19.708455,0 0,-27.050807 z m 53.465947,0 0,-27.05082 7.98518,0 7.98518,0 0,18.03388 0,18.033872 8.33236,0 8.33235,0 0,-21.940092 0,-21.94009 -16.23353,-0.21022 -16.2335,-0.21019 4.48809,-8.8209303 4.48808,-8.82092 19.7306,0 19.73061,0 0,30.8732103 0,30.873214 -3.79279,9.114942 L 148.01029,80 l -20.50992,0 -20.50992,0 0,-27.050807 z m 54.16032,0 0,-27.05082 16.31755,0 16.31753,0 0,-3.90622 0,-3.90621 -16.23352,-0.21022 -16.23353,-0.21019 4.48811,-8.8209303 4.48808,-8.82092 19.73059,0 19.73062,0 0,12.9504103 0,12.95041 -3.81899,8.59876 c -2.10046,4.72933 -3.819,8.78108 -3.819,9.00389 0,0.2228 1.71854,0.4051 3.819,0.4051 l 3.81899,0 0,18.033872 0,18.033875 -7.98518,0 -7.98517,0 0,-18.033875 0,-18.033872 -8.33237,0 -8.33235,0 0,18.033872 0,18.033875 -7.98517,0 -7.98519,0 0,-27.050817 z m 53.46598,-0.39205 0,-27.44286 24.64988,0 24.64989,0 0,9.01695 0,9.01694 -16.66471,0 -16.66471,0 0,9.40897 0,9.408982 16.66471,0 16.66471,0 0,9.016939 0,9.016936 -24.64989,0 -24.64988,0 0,-27.442857 z m 54.16032,-12.54531 0,-39.9881503 7.98518,0 7.98517,0 0,30.9712203 0,30.971222 15.97035,0 c 8.78369,0 15.97036,0.219372 15.97036,0.487485 0,0.268125 -1.93854,4.325747 -4.30786,9.016939 L 308.07243,80 l -19.64768,0 -19.64768,0 0,-39.988167 z m 53.46597,0 0,-39.9881503 7.98516,0 7.98518,0 0,39.9881503 0,39.988167 -7.98518,0 -7.98516,0 0,-39.988167 z m 21.52525,30.986819 0,-9.001348 14.55746,-0.211609 14.55747,-0.211622 -6.3886,-9.21295 -6.3886,-9.21295 -8.16886,0 -8.16887,0 0,-9.01694 0,-9.01695 11.2834,0.0489 11.2834,0.0489 13.27741,18.4514 13.27742,18.451382 -4.50518,8.942558 -4.50517,8.942547 -20.05565,0 -20.05563,0 0,-9.001348 z m 70.13067,-21.945749 0,-30.94707 -8.25468,-0.22015 -8.2547,-0.22015 4.34078,-8.6249203 4.34078,-8.62489 20.23144,-0.20787 20.23145,-0.20785 0,9.02878 0,9.0287703 -8.33236,0 -8.33236,0 0,30.97122 0,30.971227 -7.98517,0 -7.98518,0 0,-30.947097 z m 37.49562,3.89628 0,-27.05081 7.98516,0 7.98518,0 0,18.03388 0,18.033872 8.33236,0 8.33235,0 0,-21.940092 0,-21.94009 -16.2335,-0.21022 -16.23353,-0.21019 4.48809,-8.8209303 4.48809,-8.82092 19.73061,0 19.73061,0 0,30.8732103 0,30.873214 -3.79281,9.114942 L 492.41441,80 l -20.50993,0 -20.5099,0 0,-27.050817 z M 1.681255,14.725213 c 0.92469,-1.83279 2.982657,-5.8904003 4.573258,-9.0169403 l 2.892005,-5.68459 20.105903,0 20.105902,0 0,9.01693 0,9.0169403 -24.679161,0 -24.679162,0 1.681255,-3.33234 z m 53.465962,0 c 0.92469,-1.83279 2.982656,-5.8904003 4.573259,-9.0169403 l 2.892003,-5.68459 19.758721,0 19.75872,0 0,9.01693 0,9.0169403 -24.331976,0 -24.331983,0 1.681256,-3.33234 z m 161.092243,0 c 0.92468,-1.83279 2.98266,-5.8904003 4.57326,-9.0169403 l 2.892,-5.68459 20.1059,0 20.1059,0 0,9.01693 0,9.0169403 -24.67915,0 -24.67917,0 1.68126,-3.33234 z m 129.15154,0 c 0.92469,-1.83279 2.98266,-5.8904003 4.57327,-9.0169403 l 2.89199,-5.68459 20.10591,0 20.1059,0 0,9.01693 0,9.0169403 -24.67916,0 -24.67917,0 1.68126,-3.33234 z"
     id="path4200"
     inkscape:connector-curvature="0" />
</svg>
    """%(ThemeColorPrimary,ThemeColorSecondary)
    
    return(StringSVG)


def CreateStringSvg_favicon(ThemeColorPrimary,ThemeColorSecondary):
    StringSVG = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:osb="http://www.openswatchbook.org/uri/2009/osb"
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   id="svg3527"
   version="1.1"
   inkscape:version="0.91 r13725"
   width="512"
   height="512"
   viewBox="0 0 512 512"
   sodipodi:docname="favicon.svg">
  <metadata
     id="metadata3533">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <defs
     id="defs3531">
    <linearGradient
       inkscape:collect="always"
       id="linearGradient6659">
      <stop
         style="stop-color:%s;stop-opacity:1"
         offset="0"
         id="stop6661" />
      <stop
         style="stop-color:%s;stop-opacity:1"
         offset="1"
         id="stop6663" />
    </linearGradient>
    <linearGradient
       id="linearGradient6552"
       osb:paint="solid">
      <stop
         style="stop-color:#000000;stop-opacity:1;"
         offset="0"
         id="stop6554" />
    </linearGradient>
    <inkscape:perspective
       sodipodi:type="inkscape:persp3d"
       inkscape:vp_x="0 : 256 : 1"
       inkscape:vp_y="0 : 1000 : 0"
       inkscape:vp_z="512 : 256 : 1"
       inkscape:persp3d-origin="256 : 170.66667 : 1"
       id="perspective5066" />
    <linearGradient
       inkscape:collect="always"
       xlink:href="#linearGradient6659"
       id="linearGradient6669"
       x1="502.34714"
       y1="150.26886"
       x2="8.5668478"
       y2="272.01358"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(1.0021384,0,0,1.0021384,-0.01283011,-1.082006)" />
  </defs>
  <sodipodi:namedview
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1"
     objecttolerance="10"
     gridtolerance="10"
     guidetolerance="10"
     inkscape:pageopacity="0"
     inkscape:pageshadow="2"
     inkscape:window-width="1920"
     inkscape:window-height="1023"
     id="namedview3529"
     showgrid="false"
     inkscape:zoom="1"
     inkscape:cx="49.47412"
     inkscape:cy="253.30339"
     inkscape:window-x="0"
     inkscape:window-y="0"
     inkscape:window-maximized="1"
     inkscape:current-layer="layer3" />
  <g
     inkscape:groupmode="layer"
     id="layer3"
     inkscape:label="Contour">
    <rect
       style="opacity:1;fill:url(#linearGradient6669);fill-opacity:1;stroke:none;stroke-width:5;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       id="rect6562"
       width="500"
       height="500"
       x="6"
       y="6"
       ry="98" />
  </g>
  <path
     style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-opacity:1"
     d="m 230.50303,66.004115 c -1.25423,-0.03682 -2.53632,0.172798 -3.73999,0.656756 -3.85067,1.548963 -5.42872,5.328503 -3.52017,8.442601 l 12.94727,21.125057 c 3.83927,6.264411 4.43169,13.364521 1.67016,19.994911 -2.76146,6.63037 -8.54627,11.99612 -16.29045,15.10987 l -93.90551,37.75733 c -11.46827,4.61126 -20.03709,12.55997 -24.12734,22.38054 -4.090197,9.82058 -3.21251,20.33694 2.47241,29.61407 l 0.35686,0.58248 c 9.60259,15.66678 30.62483,23.75598 50.91833,20.97422 l 10.57764,50.81571 15.58812,74.88108 -3.76569,-2.32532 c -8.58143,-5.2971 -17.31933,-7.9798 -26.81099,-8.23143 -4.7061,-0.12475 -12.48866,1.08061 -16.94994,2.62469 -30.28346,10.48135 -38.848069,45.46413 -17.027,69.55743 3.60541,3.98089 13.50996,10.6027 18.76569,12.54553 6.50739,2.40557 12.99864,3.4998 20.71847,3.4903 3.14618,-0.004 12.08497,-1.91254 15.53101,-3.31622 15.93553,-6.49116 25.40353,-18.65769 27.36486,-35.1628 l 0.53958,-4.53922 -13.90368,-66.91653 -18.36029,-86.65149 146.45114,-29.74636 c 2.09544,10.18538 7.86221,38.72966 10.91173,53.9347 l 9.9838,47.54356 -4.61078,-2.8289 c -10.55831,-6.47868 -21.74623,-8.82334 -33.9912,-7.12445 -9.0632,1.25743 -16.26501,4.30313 -23.50779,9.94406 -4.19194,3.26484 -10.377,11.99805 -12.29063,17.35166 -7.82113,21.8806 3.75916,46.05864 26.86524,56.09291 22.51594,9.77805 49.44716,1.54526 60.41676,-18.47019 2.99689,-5.46827 4.12841,-9.37807 4.96479,-17.18225 l 0.38544,-3.60633 -19.47375,-93.51604 -22.02318,-100.24831 C 210.89529,198.25207 209.92518,198.02711 152.277,218.57892 l 2.42383,11.64048 c -13.70339,1.88095 -27.90227,-3.57929 -34.3852,-14.1561 l -0.354,-0.58248 c -3.84185,-6.26862 -4.43737,-13.36918 -1.67588,-19.99952 2.76148,-6.63044 8.54917,-11.99609 16.29331,-15.1099 l 93.90552,-37.75731 c 11.46831,-4.61124 20.03711,-12.55995 24.12732,-22.38053 4.09025,-9.82058 3.21097,-20.337421 -2.47525,-29.614091 L 237.19221,69.496733 c -1.31164,-2.14207 -3.92981,-3.411535 -6.68918,-3.492618 z m 131.92801,77.494155 c -3.36909,-0.0219 -6.80173,0.21956 -10.26077,0.74263 -0.76167,0.11512 -1.51567,0.24298 -2.264,0.38289 -0.25829,0.0483 -0.51183,0.1041 -0.76797,0.15548 -0.486,0.0969 -0.97095,0.19442 -1.45032,0.30169 -0.30721,0.0693 -0.61075,0.14507 -0.91644,0.21816 -0.41859,0.10042 -0.83643,0.20076 -1.25048,0.30866 -0.33115,0.0861 -0.65786,0.17561 -0.98499,0.26687 -0.37826,0.10526 -0.75366,0.21345 -1.12768,0.32489 -0.34537,0.10313 -0.68876,0.20895 -1.03064,0.31793 -0.34138,0.10824 -0.68195,0.21851 -1.01924,0.33185 -0.36081,0.12143 -0.72039,0.24427 -1.07631,0.37132 -0.30345,0.10871 -0.60254,0.22141 -0.90215,0.33416 -0.37934,0.14309 -0.75988,0.28723 -1.13344,0.43629 -0.24758,0.0993 -0.4911,0.20172 -0.73658,0.304 -0.41545,0.17202 -0.83059,0.34378 -1.23907,0.52448 -0.12477,0.0555 -0.24586,0.1156 -0.37112,0.17173 -2.26993,1.02405 -4.43137,2.17014 -6.46078,3.42993 -0.0382,0.024 -0.0769,0.0463 -0.11424,0.0695 -0.48862,0.30428 -0.96844,0.61786 -1.44174,0.93523 -0.0619,0.0408 -0.12177,0.0818 -0.18272,0.12299 -0.46494,0.31498 -0.92258,0.63655 -1.37324,0.96309 -0.0607,0.0435 -0.12053,0.0868 -0.17986,0.12995 -0.45523,0.33294 -0.90173,0.67151 -1.34183,1.01647 -0.0401,0.0317 -0.0792,0.0636 -0.11991,0.0952 -0.45746,0.36128 -0.90741,0.7288 -1.34757,1.10232 -0.87063,0.73934 -1.71419,1.4963 -2.51234,2.28122 l 12.03367,57.58978 c 1.0672,0.50296 2.16455,0.96716 3.2832,1.404 0.56553,0.22322 1.13835,0.43689 1.71586,0.64283 0.0478,0.0165 0.0976,0.0345 0.14557,0.0512 0.55544,0.19618 1.11686,0.38342 1.68158,0.56393 0.0692,0.0219 0.13857,0.0437 0.20844,0.065 0.55863,0.17619 1.1221,0.34542 1.69013,0.50587 0.0694,0.0193 0.13928,0.036 0.2084,0.056 0.57685,0.16034 1.15562,0.31587 1.74152,0.45946 0.0401,0.0106 0.083,0.0182 0.12277,0.0277 2.42565,0.59029 4.92601,1.03608 7.48289,1.33207 0.13301,0.0142 0.26665,0.0334 0.3997,0.0486 0.46057,0.051 0.92607,0.0899 1.39037,0.12996 0.26649,0.0232 0.53209,0.0502 0.79936,0.0695 0.41561,0.031 0.83277,0.0534 1.2505,0.0764 0.3232,0.0181 0.64543,0.0362 0.97069,0.0488 0.38783,0.0155 0.77827,0.0264 1.16768,0.0349 0.36109,0.008 0.72208,0.012 1.08489,0.014 0.36507,0.002 0.7317,1.3e-4 1.09914,-0.006 0.39481,-0.005 0.79134,-0.0136 1.18768,-0.0256 0.3446,-0.0106 0.69062,-0.0207 1.03637,-0.0369 0.43091,-0.0199 0.86332,-0.0479 1.29613,-0.0767 0.31716,-0.0217 0.63363,-0.0393 0.95072,-0.065 0.49206,-0.0393 0.98759,-0.0903 1.48171,-0.14155 0.26181,-0.0276 0.52323,-0.0508 0.7851,-0.0813 0.75827,-0.0886 1.51666,-0.18642 2.27828,-0.30167 27.67112,-4.18359 46.48743,-24.87482 42.02796,-46.21616 -0.55749,-2.6678 -1.45054,-5.2205 -2.64371,-7.63501 -0.89428,-1.8108 -1.95813,-3.54603 -3.17185,-5.19365 -1.21318,-1.64824 -2.57968,-3.21079 -4.07976,-4.67847 -6.00036,-5.8707 -14.16018,-10.22752 -23.425,-12.50843 -2.31618,-0.57026 -4.69926,-1.00864 -7.13743,-1.31119 -2.43728,-0.30208 -4.93062,-0.46664 -7.45713,-0.48267 z"
     id="path3771"
     inkscape:connector-curvature="0" />
  <g
     id="g3697"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3699"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3701"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3703"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3705"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3707"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3709"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3711"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3713"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3715"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3717"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3719"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3721"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3723"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3725"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
</svg>
    """%(ThemeColorPrimary,ThemeColorSecondary)
    return(StringSVG)


def CreateStringSvgMPL_move(TextColor):
    StringSVG = """<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Created with matplotlib (http://matplotlib.org/) -->
<svg height="72pt" fill="%s" version="1.1" viewBox="0 0 72 72" width="72pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <defs>
  <style type="text/css">
*{stroke-linecap:butt;stroke-linejoin:round;}
  </style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 72 
L 72 72 
L 72 0 
L 0 0 
z
" style="fill:none;opacity:0;"/>
  </g>
  <g id="text_1">
   <path d="M 70 37.44 
C 70 36.8025 69.734375 36.18625 69.2775 35.74 
L 59.56625 26.018125 
C 59.109375 25.56125 58.50375 25.295625 57.855625 25.295625 
C 56.5275 25.295625 55.433125 26.400625 55.433125 27.72875 
L 55.433125 32.584375 
L 40.855625 32.584375 
L 40.855625 18.0175 
L 45.71125 18.0175 
C 47.039375 18.0175 48.144375 16.9125 48.144375 15.584375 
C 48.144375 14.93625 47.87875 14.330625 47.421875 13.87375 
L 37.710625 4.1625 
C 37.25375 3.705625 36.648125 3.44 36 3.44 
C 35.351875 3.44 34.74625 3.705625 34.289375 4.1625 
L 24.578125 13.87375 
C 24.12125 14.330625 23.855625 14.93625 23.855625 15.584375 
C 23.855625 16.9125 24.960625 18.0175 26.28875 18.0175 
L 31.144375 18.0175 
L 31.144375 32.584375 
L 16.566875 32.584375 
L 16.566875 27.72875 
C 16.566875 26.400625 15.4725 25.295625 14.144375 25.295625 
C 13.49625 25.295625 12.890625 25.56125 12.43375 26.018125 
L 2.7225 35.74 
C 2.265625 36.18625 2 36.8025 2 37.44 
C 2 38.088125 2.265625 38.69375 2.7225 39.150625 
L 12.43375 48.861875 
C 12.890625 49.31875 13.49625 49.584375 14.144375 49.584375 
C 15.4725 49.584375 16.566875 48.49 16.566875 47.161875 
L 16.566875 42.295625 
L 31.144375 42.295625 
L 31.144375 56.873125 
L 26.28875 56.873125 
C 24.960625 56.873125 23.855625 57.9675 23.855625 59.295625 
C 23.855625 59.94375 24.12125 60.549375 24.578125 61.00625 
L 34.289375 70.7175 
C 34.74625 71.174375 35.351875 71.44 36 71.44 
C 36.648125 71.44 37.25375 71.174375 37.710625 70.7175 
L 47.421875 61.00625 
C 47.87875 60.549375 48.144375 59.94375 48.144375 59.295625 
C 48.144375 57.9675 47.039375 56.873125 45.71125 56.873125 
L 40.855625 56.873125 
L 40.855625 42.295625 
L 55.433125 42.295625 
L 55.433125 47.161875 
C 55.433125 48.49 56.5275 49.584375 57.855625 49.584375 
C 58.50375 49.584375 59.109375 49.31875 59.56625 48.861875 
L 69.2775 39.150625 
C 69.734375 38.69375 70 38.088125 70 37.44 
"/>
  </g>
 </g>
</svg>
    """%(TextColor)
    return(StringSVG)





def CreateStringSvgMPL_subplots(TextColor):
    StringSVG = """<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Created with matplotlib (http://matplotlib.org/) -->
<svg height="72pt" fill="%s" version="1.1" viewBox="0 0 72 72" width="72pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <defs>
  <style type="text/css">
*{stroke-linecap:butt;stroke-linejoin:round;}
  </style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 72 
L 72 72 
L 72 0 
L 0 0 
z
" style="fill:none;opacity:0;"/>
  </g>
  <g id="text_1">
   <path d="M 20.21125 56.873125 
L 6.855625 56.873125 
L 6.855625 61.72875 
L 20.21125 61.72875 
z
M 33.566875 52.0175 
L 23.855625 52.0175 
C 22.5275 52.0175 21.4225 53.111875 21.4225 54.44 
L 21.4225 64.161875 
C 21.4225 65.49 22.5275 66.584375 23.855625 66.584375 
L 33.566875 66.584375 
C 34.895 66.584375 36 65.49 36 64.161875 
L 36 54.44 
C 36 53.111875 34.895 52.0175 33.566875 52.0175 
M 39.644375 37.44 
L 6.855625 37.44 
L 6.855625 42.295625 
L 39.644375 42.295625 
z
M 15.355625 18.0175 
L 6.855625 18.0175 
L 6.855625 22.873125 
L 15.355625 22.873125 
z
M 65.144375 56.873125 
L 37.21125 56.873125 
L 37.21125 61.72875 
L 65.144375 61.72875 
z
M 28.71125 13.161875 
L 19 13.161875 
C 17.671875 13.161875 16.566875 14.25625 16.566875 15.584375 
L 16.566875 25.295625 
C 16.566875 26.62375 17.671875 27.72875 19 27.72875 
L 28.71125 27.72875 
C 30.039375 27.72875 31.144375 26.62375 31.144375 25.295625 
L 31.144375 15.584375 
C 31.144375 14.25625 30.039375 13.161875 28.71125 13.161875 
M 53 32.584375 
L 43.28875 32.584375 
C 41.960625 32.584375 40.855625 33.689375 40.855625 35.0175 
L 40.855625 44.72875 
C 40.855625 46.056875 41.960625 47.161875 43.28875 47.161875 
L 53 47.161875 
C 54.328125 47.161875 55.4225 46.056875 55.4225 44.72875 
L 55.4225 35.0175 
C 55.4225 33.689375 54.328125 32.584375 53 32.584375 
M 65.144375 37.44 
L 56.644375 37.44 
L 56.644375 42.295625 
L 65.144375 42.295625 
z
M 65.144375 18.0175 
L 32.355625 18.0175 
L 32.355625 22.873125 
L 65.144375 22.873125 
z
"/>
  </g>
 </g>
</svg>
    """%(TextColor)
    return(StringSVG)




def CreateStringSvgMPL_filesave(TextColor):
    StringSVG = """<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Created with matplotlib (http://matplotlib.org/) -->
<svg height="72pt" fill="%s" version="1.1" viewBox="0 0 72 72" width="72pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <defs>
  <style type="text/css">
*{stroke-linecap:butt;stroke-linejoin:round;}
  </style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 72 
L 72 72 
L 72 0 
L 0 0 
z
" style="fill:none;opacity:0;"/>
  </g>
  <g id="text_1">
   <path d="M 21.4225 61.72875 
L 21.4225 47.161875 
L 50.566875 47.161875 
L 50.566875 61.72875 
z
M 55.4225 61.72875 
L 55.4225 45.94 
C 55.4225 43.931875 53.796875 42.295625 51.78875 42.295625 
L 20.21125 42.295625 
C 18.203125 42.295625 16.566875 43.931875 16.566875 45.94 
L 16.566875 61.72875 
L 11.71125 61.72875 
L 11.71125 13.161875 
L 16.566875 13.161875 
L 16.566875 28.94 
C 16.566875 30.95875 18.203125 32.584375 20.21125 32.584375 
L 42.066875 32.584375 
C 44.085625 32.584375 45.71125 30.95875 45.71125 28.94 
L 45.71125 13.161875 
C 46.47625 13.161875 47.953125 13.7675 48.484375 14.29875 
L 59.14125 24.955625 
C 59.640625 25.455 60.28875 27.00625 60.28875 27.72875 
L 60.28875 61.72875 
z
M 40.855625 26.5175 
C 40.855625 27.155 40.281875 27.72875 39.644375 27.72875 
L 32.355625 27.72875 
C 31.7075 27.72875 31.144375 27.155 31.144375 26.5175 
L 31.144375 14.373125 
C 31.144375 13.725 31.7075 13.161875 32.355625 13.161875 
L 39.644375 13.161875 
C 40.281875 13.161875 40.855625 13.725 40.855625 14.373125 
z
M 65.144375 27.72875 
C 65.144375 25.720625 64.0075 22.9475 62.5625 21.5025 
L 51.9375 10.8775 
C 50.4925 9.443125 47.719375 8.295625 45.71125 8.295625 
L 10.5 8.295625 
C 8.491875 8.295625 6.855625 9.931875 6.855625 11.94 
L 6.855625 62.94 
C 6.855625 64.95875 8.491875 66.584375 10.5 66.584375 
L 61.5 66.584375 
C 63.508125 66.584375 65.144375 64.95875 65.144375 62.94 
z
"/>
  </g>
 </g>
</svg>
    """%(TextColor)
    return(StringSVG)

def CreateStringSvgMPL_home(TextColor):
    StringSVG = """<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Created with matplotlib (http://matplotlib.org/) -->
<svg height="72pt" fill="%s" version="1.1" viewBox="0 0 72 72" width="72pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <defs>
  <style type="text/css">
*{stroke-linecap:butt;stroke-linejoin:round;}
  </style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 72 
L 72 72 
L 72 0 
L 0 0 
z
" style="fill:none;opacity:0;"/>
  </g>
  <g id="text_1">
   <path d="M 57.860938 45.94 
C 57.860938 45.865625 57.860938 45.79125 57.818438 45.716875 
L 35.994687 27.72875 
L 14.181562 45.716875 
C 14.181562 45.79125 14.139062 45.865625 14.139062 45.94 
L 14.139062 64.15125 
C 14.139062 65.479375 15.244062 66.584375 16.572187 66.584375 
L 31.139063 66.584375 
L 31.139063 52.0175 
L 40.860938 52.0175 
L 40.860938 66.584375 
L 55.427813 66.584375 
C 56.755938 66.584375 57.860938 65.479375 57.860938 64.15125 
z
M 66.318438 43.32625 
C 66.732813 42.826875 66.658438 42.03 66.169688 41.615625 
L 57.860938 34.709375 
L 57.860938 19.22875 
C 57.860938 18.54875 57.329688 18.0175 56.639063 18.0175 
L 49.360938 18.0175 
C 48.670312 18.0175 48.139062 18.54875 48.139062 19.22875 
L 48.139062 26.62375 
L 38.884687 18.88875 
C 37.290937 17.560625 34.709063 17.560625 33.115313 18.88875 
L 5.830312 41.615625 
C 5.341562 42.03 5.267187 42.826875 5.681562 43.32625 
L 8.029687 46.13125 
C 8.220937 46.354375 8.529062 46.51375 8.826562 46.545625 
C 9.166562 46.588125 9.474687 46.47125 9.740312 46.28 
L 35.994687 24.3925 
L 62.259687 46.28 
C 62.482813 46.47125 62.748438 46.545625 63.056562 46.545625 
C 63.088437 46.545625 63.130938 46.545625 63.173438 46.545625 
C 63.470938 46.51375 63.779063 46.354375 63.970313 46.13125 
z
"/>
  </g>
 </g>
</svg>
    """%(TextColor)
    return(StringSVG)

def CreateStringSvgMPL_forward(TextColor):
    StringSVG = """<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Created with matplotlib (http://matplotlib.org/) -->
<svg height="72pt" fill="%s" version="1.1" viewBox="0 0 72 72" width="72pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <defs>
  <style type="text/css">
*{stroke-linecap:butt;stroke-linejoin:round;}
  </style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 72 
L 72 72 
L 72 0 
L 0 0 
z
" style="fill:none;opacity:0;"/>
  </g>
  <g id="text_1">
   <path d="M 62.71125 37.44 
C 62.71125 36.14375 62.2225 34.900625 61.30875 34.01875 
L 36.605625 9.315625 
C 35.691875 8.4125 34.438125 7.88125 33.1525 7.88125 
C 31.866875 7.88125 30.645 8.4125 29.741875 9.315625 
L 26.894375 12.163125 
C 25.980625 13.034375 25.449375 14.288125 25.449375 15.584375 
C 25.449375 16.87 25.980625 18.12375 26.894375 18.995 
L 38.008125 30.15125 
L 11.296875 30.15125 
C 8.56625 30.15125 6.855625 32.425 6.855625 35.006875 
L 6.855625 39.8625 
C 6.855625 42.444375 8.56625 44.72875 11.296875 44.72875 
L 38.008125 44.72875 
L 26.894375 55.8425 
C 25.980625 56.75625 25.449375 58.01 25.449375 59.295625 
C 25.449375 60.58125 25.980625 61.835 26.894375 62.74875 
L 29.741875 65.59625 
C 30.645 66.4675 31.866875 66.99875 33.1525 66.99875 
C 34.438125 66.99875 35.691875 66.4675 36.605625 65.59625 
L 61.30875 40.893125 
C 62.2225 39.979375 62.71125 38.725625 62.71125 37.44 
"/>
  </g>
 </g>
</svg>
    """%(TextColor)
    return(StringSVG)

def CreateStringSvgMPL_zoom_to_rect(TextColor):
    StringSVG = """<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Created with matplotlib (http://matplotlib.org/) -->
<svg height="72pt" fill="%s" version="1.1" viewBox="0 0 72 72" width="72pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <defs>
  <style type="text/css">
*{stroke-linecap:butt;stroke-linejoin:round;}
  </style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 72 
L 72 72 
L 72 0 
L 0 0 
z
" style="fill:none;opacity:0;"/>
  </g>
  <g id="text_1">
   <path d="M 48.139062 32.589687 
C 48.139062 41.960938 40.510312 49.589687 31.139063 49.589687 
C 21.767812 49.589687 14.139062 41.960938 14.139062 32.589687 
C 14.139062 23.218437 21.767812 15.589687 31.139063 15.589687 
C 40.510312 15.589687 48.139062 23.218437 48.139062 32.589687 
M 67.572187 64.156562 
C 67.572187 62.870937 67.040937 61.617188 66.169688 60.745937 
L 53.154062 47.730312 
C 56.224688 43.289062 57.860938 37.976562 57.860938 32.589687 
C 57.860938 17.820937 45.907813 5.867812 31.139063 5.867812 
C 16.380937 5.867812 4.427812 17.820937 4.427812 32.589687 
C 4.427812 47.347812 16.380937 59.300937 31.139063 59.300937 
C 36.525937 59.300937 41.838437 57.664687 46.279687 54.594062 
L 59.295313 67.577812 
C 60.166562 68.480937 61.420313 69.012187 62.716563 69.012187 
C 65.372813 69.012187 67.572187 66.812812 67.572187 64.156562 
"/>
  </g>
 </g>
</svg>
    """%(TextColor)
    return(StringSVG)

def CreateStringSvgMPL_qt4_editor_options(TextColor):
    StringSVG = """<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Created with matplotlib (http://matplotlib.org/) -->
<svg height="72pt" fill="%s" version="1.1" viewBox="0 0 72 72" width="72pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <defs>
  <style type="text/css">
*{stroke-linecap:butt;stroke-linejoin:round;}
  </style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 72 
L 72 72 
L 72 0 
L 0 0 
z
" style="fill:none;opacity:0;"/>
  </g>
  <g id="text_1">
   <path d="M 74.855625 61.72875 
L 2 61.72875 
L 2 8.295625 
L -2.855625 8.295625 
L -2.855625 66.584375 
L 74.855625 66.584375 
z
M 70 14.373125 
C 70 13.693125 69.46875 13.161875 68.78875 13.161875 
L 52.2775 13.161875 
C 51.215 13.161875 50.651875 14.4475 51.44875 15.244375 
L 56.03875 19.834375 
L 38.433125 37.44 
L 29.593125 28.6 
C 29.09375 28.11125 28.339375 28.11125 27.84 28.6 
L 5.644375 50.795625 
L 12.933125 58.084375 
L 28.71125 42.295625 
L 37.561875 51.14625 
C 38.050625 51.635 38.805 51.635 39.304375 51.14625 
L 63.3275 27.123125 
L 67.9175 31.713125 
C 68.714375 32.51 70 31.93625 70 30.87375 
z
"/>
  </g>
 </g>
</svg>
    """%(TextColor)
    return(StringSVG)

def CreateStringSvgMPL_back(TextColor):
    StringSVG = """<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Created with matplotlib (http://matplotlib.org/) -->
<svg height="72pt" fill="%s" version="1.1" viewBox="0 0 72 72" width="72pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <defs>
  <style type="text/css">
*{stroke-linecap:butt;stroke-linejoin:round;}
  </style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 72 
L 72 72 
L 72 0 
L 0 0 
z
" style="fill:none;opacity:0;"/>
  </g>
  <g id="text_1">
   <path d="M 65.144375 35.006875 
C 65.144375 32.425 63.43375 30.15125 60.703125 30.15125 
L 33.991875 30.15125 
L 45.105625 19.0375 
C 46.019375 18.12375 46.550625 16.87 46.550625 15.584375 
C 46.550625 14.288125 46.019375 13.034375 45.105625 12.13125 
L 42.258125 9.315625 
C 41.344375 8.4125 40.133125 7.88125 38.8475 7.88125 
C 37.55125 7.88125 36.2975 8.4125 35.394375 9.315625 
L 10.69125 33.986875 
C 9.82 34.900625 9.28875 36.14375 9.28875 37.44 
C 9.28875 38.725625 9.82 39.979375 10.69125 40.850625 
L 35.394375 65.59625 
C 36.2975 66.4675 37.55125 66.99875 38.8475 66.99875 
C 40.133125 66.99875 41.386875 66.4675 42.258125 65.59625 
L 45.105625 62.70625 
C 46.019375 61.835 46.550625 60.58125 46.550625 59.295625 
C 46.550625 58.01 46.019375 56.75625 45.105625 55.885 
L 33.991875 44.72875 
L 60.703125 44.72875 
C 63.43375 44.72875 65.144375 42.444375 65.144375 39.8625 
z
"/>
  </g>
 </g>
</svg>
    """%(TextColor)
    return(StringSVG)

def CreateStringSvg_warning(ThemeColorPrimary,ThemeColorSecondary):
    StringSVG = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:osb="http://www.openswatchbook.org/uri/2009/osb"
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   id="svg3527"
   version="1.1"
   inkscape:version="0.92.3 (d244b95, 2018-08-02)"
   width="512"
   height="512"
   viewBox="0 0 512 512"
   sodipodi:docname="warning.svg">
  <metadata
     id="metadata3533">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <defs
     id="defs3531">
    <linearGradient
       inkscape:collect="always"
       id="linearGradient6659">
      <stop
         style="stop-color:%s;stop-opacity:1"
         offset="0"
         id="stop6661" />
      <stop
         style="stop-color:%s;stop-opacity:1"
         offset="1"
         id="stop6663" />
    </linearGradient>
    <linearGradient
       id="linearGradient6552"
       osb:paint="solid">
      <stop
         style="stop-color:#000000;stop-opacity:1;"
         offset="0"
         id="stop6554" />
    </linearGradient>
    <inkscape:perspective
       sodipodi:type="inkscape:persp3d"
       inkscape:vp_x="0 : 256 : 1"
       inkscape:vp_y="0 : 1000 : 0"
       inkscape:vp_z="512 : 256 : 1"
       inkscape:persp3d-origin="256 : 170.66667 : 1"
       id="perspective5066" />
    <linearGradient
       inkscape:collect="always"
       xlink:href="#linearGradient6659"
       id="linearGradient6669"
       x1="502.34714"
       y1="150.26886"
       x2="8.5668478"
       y2="272.01358"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(1.0021384,0,0,1.0021384,-587.01283,347.91799)" />
    <linearGradient
       inkscape:collect="always"
       xlink:href="#linearGradient6659"
       id="linearGradient4575"
       x1="-482.85242"
       y1="188.95137"
       x2="-343.85135"
       y2="188.95137"
       gradientUnits="userSpaceOnUse" />
    <linearGradient
       inkscape:collect="always"
       xlink:href="#linearGradient6659"
       id="linearGradient4593"
       x1="-708.78619"
       y1="349"
       x2="-159.21379"
       y2="349"
       gradientUnits="userSpaceOnUse" />
  </defs>
  <sodipodi:namedview
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1"
     objecttolerance="10"
     gridtolerance="10"
     guidetolerance="10"
     inkscape:pageopacity="0"
     inkscape:pageshadow="2"
     inkscape:window-width="1920"
     inkscape:window-height="1025"
     id="namedview3529"
     showgrid="false"
     inkscape:zoom="1"
     inkscape:cx="-7"
     inkscape:cy="187.52722"
     inkscape:window-x="0"
     inkscape:window-y="0"
     inkscape:window-maximized="1"
     inkscape:current-layer="layer3"
     inkscape:snap-bbox="false"
     inkscape:snap-global="false" />
  <g
     inkscape:groupmode="layer"
     id="layer3"
     inkscape:label="Contour">
    <path
       sodipodi:type="star"
       style="fill:url(#linearGradient4593);fill-opacity:1"
       id="path4583"
       sodipodi:sides="6"
       sodipodi:cx="-434"
       sodipodi:cy="349"
       sodipodi:r1="274.96362"
       sodipodi:r2="137.48183"
       sodipodi:arg1="-1.0110405"
       sodipodi:arg2="-0.48744172"
       inkscape:flatsided="true"
       inkscape:rounded="0.06"
       inkscape:randomized="1.25247e-15"
       d="m -288.00001,116.00001 c 13.98,8.76 129.3803,226.45266 128.78392,242.9397 -0.59638,16.48703 -131.42361,225.27295 -146,232.99999 -14.57638,7.72703 -260.8039,-1.17971 -274.7839,-9.93971 -13.98,-8.76 -129.3803,-226.45266 -128.78392,-242.9397 0.59638,-16.48703 131.42361,-225.27295 146,-232.99999 14.57638,-7.727034 260.8039,1.17971 274.7839,9.93971 z"
       inkscape:transform-center-x="50.285775"
       inkscape:transform-center-y="6.9986864"
       transform="matrix(0.9082854,-0.03839025,0.04201662,1.0225495,635.53207,-117.53113)" />
  </g>
  <g
     id="g3697"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3699"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3701"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3703"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3705"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3707"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3709"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3711"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3713"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3715"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3717"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3719"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3721"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3723"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3725"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <rect
     style="fill:#ffffff;fill-opacity:1;stroke-width:1.1803571"
     id="rect4577"
     width="80"
     height="200"
     x="216"
     y="77"
     ry="5.6999998" />
  <circle
     style="fill:#ffffff;fill-opacity:1;stroke-width:1.06818688"
     id="path4579"
     cx="256"
     cy="375"
     r="40" />
</svg>
    """%(ThemeColorSecondary,ThemeColorPrimary)
    
    return(StringSVG)

def CreateStringSvg_questionmark(ThemeColorPrimary,ThemeColorSecondary):
    StringSVG = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:osb="http://www.openswatchbook.org/uri/2009/osb"
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   id="svg3527"
   version="1.1"
   inkscape:version="0.92.3 (d244b95, 2018-08-02)"
   width="512"
   height="512"
   viewBox="0 0 512 512"
   sodipodi:docname="questionmark2.svg">
  <metadata
     id="metadata3533">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <defs
     id="defs3531">
    <linearGradient
       inkscape:collect="always"
       id="linearGradient6659">
      <stop
         style="stop-color:%s;stop-opacity:1"
         offset="0"
         id="stop6661" />
      <stop
         style="stop-color:%s;stop-opacity:1"
         offset="1"
         id="stop6663" />
    </linearGradient>
    <linearGradient
       id="linearGradient6552"
       osb:paint="solid">
      <stop
         style="stop-color:#000000;stop-opacity:1;"
         offset="0"
         id="stop6554" />
    </linearGradient>
    <inkscape:perspective
       sodipodi:type="inkscape:persp3d"
       inkscape:vp_x="0 : 256 : 1"
       inkscape:vp_y="0 : 1000 : 0"
       inkscape:vp_z="512 : 256 : 1"
       inkscape:persp3d-origin="256 : 170.66667 : 1"
       id="perspective5066" />
    <linearGradient
       inkscape:collect="always"
       xlink:href="#linearGradient6659"
       id="linearGradient844"
       x1="-736.67792"
       y1="258.63815"
       x2="-448.4935"
       y2="16.962605"
       gradientUnits="userSpaceOnUse" />
  </defs>
  <sodipodi:namedview
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1"
     objecttolerance="10"
     gridtolerance="10"
     guidetolerance="10"
     inkscape:pageopacity="0"
     inkscape:pageshadow="2"
     inkscape:window-width="1920"
     inkscape:window-height="1025"
     id="namedview3529"
     showgrid="false"
     inkscape:zoom="1"
     inkscape:cx="31"
     inkscape:cy="253.30339"
     inkscape:window-x="0"
     inkscape:window-y="0"
     inkscape:window-maximized="1"
     inkscape:current-layer="layer3" />
  <g
     inkscape:groupmode="layer"
     id="layer3"
     inkscape:label="Contour">
    <path
       sodipodi:type="star"
       style="fill:url(#linearGradient844);fill-opacity:1"
       id="path836"
       sodipodi:sides="5"
       sodipodi:cx="-632"
       sodipodi:cy="125"
       sodipodi:r1="192.02344"
       sodipodi:r2="166.29716"
       sodipodi:arg1="-0.015623729"
       sodipodi:arg2="0.6126948"
       inkscape:flatsided="true"
       inkscape:rounded="0.07"
       inkscape:randomized="0"
       d="m -440,122 c 0.24687,15.79967 -114.86548,179.55865 -129.81557,184.6758 -14.95009,5.11715 -206.2658,-53.75689 -215.75234,-66.39398 -9.48653,-12.63709 -12.6138,-212.782232 -3.52671,-225.709538 9.08709,-12.9273063 198.47005,-77.749764 213.57271,-73.102186 C -560.41924,-53.882325 -440.24687,106.20033 -440,122 Z"
       transform="matrix(1.3267063,-0.41310207,0.33546455,1.3492458,1048.5906,-152.77806)" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:483.27114868px;line-height:1.25;font-family:'Liberation Serif';-inkscape-font-specification:'Liberation Serif';letter-spacing:0px;word-spacing:0px;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:12.08178043"
       x="113.93684"
       y="435.45535"
       id="text868"
       transform="scale(1.0894053,0.91793203)"><tspan
         sodipodi:role="line"
         id="tspan866"
         x="113.93684"
         y="435.45535"
         style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-family:'Liberation Serif';-inkscape-font-specification:'Liberation Serif Bold';fill:#ffffff;fill-opacity:1;stroke-width:12.08178043">?</tspan></text>
  </g>
  <g
     id="g3697"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3699"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3701"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3703"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3705"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3707"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3709"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3711"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3713"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3715"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3717"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3719"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3721"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3723"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3725"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
</svg>
    """%(ThemeColorSecondary,ThemeColorPrimary)
    
    return(StringSVG)




def CreateStringSvg_edit(ThemeColorPrimary,ThemeColorSecondary):
    StringSVG = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:osb="http://www.openswatchbook.org/uri/2009/osb"
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   id="svg3527"
   version="1.1"
   inkscape:version="0.92.3 (d244b95, 2018-08-02)"
   width="512"
   height="512"
   viewBox="0 0 512 512"
   sodipodi:docname="edit.svg">
  <metadata
     id="metadata3533">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <defs
     id="defs3531">
    <linearGradient
       inkscape:collect="always"
       id="linearGradient6659">
      <stop
         style="stop-color:%s;stop-opacity:1"
         offset="0"
         id="stop6661" />
      <stop
         style="stop-color:%s;stop-opacity:1"
         offset="1"
         id="stop6663" />
    </linearGradient>
    <linearGradient
       id="linearGradient6552"
       osb:paint="solid">
      <stop
         style="stop-color:#000000;stop-opacity:1;"
         offset="0"
         id="stop6554" />
    </linearGradient>
    <inkscape:perspective
       sodipodi:type="inkscape:persp3d"
       inkscape:vp_x="0 : 256 : 1"
       inkscape:vp_y="0 : 1000 : 0"
       inkscape:vp_z="512 : 256 : 1"
       inkscape:persp3d-origin="256 : 170.66667 : 1"
       id="perspective5066" />
    <linearGradient
       inkscape:collect="always"
       xlink:href="#linearGradient6659"
       id="linearGradient6669"
       x1="502.34714"
       y1="150.26886"
       x2="8.5668478"
       y2="272.01358"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(1.0021384,0,0,1.0021384,-0.01283011,-1.082006)" />
  </defs>
  <sodipodi:namedview
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1"
     objecttolerance="10"
     gridtolerance="10"
     guidetolerance="10"
     inkscape:pageopacity="0"
     inkscape:pageshadow="2"
     inkscape:window-width="1920"
     inkscape:window-height="1025"
     id="namedview3529"
     showgrid="false"
     inkscape:zoom="1"
     inkscape:cx="-116.52588"
     inkscape:cy="253.30339"
     inkscape:window-x="0"
     inkscape:window-y="0"
     inkscape:window-maximized="1"
     inkscape:current-layer="g962"
     inkscape:object-nodes="false" />
  <g
     inkscape:groupmode="layer"
     id="layer3"
     inkscape:label="Contour">
    <rect
       style="opacity:1;fill:url(#linearGradient6669);fill-opacity:1;stroke:none;stroke-width:5;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       id="rect6562"
       width="500"
       height="500"
       x="6"
       y="6"
       ry="98" />
    <rect
       style="fill:#ffffff;fill-opacity:1"
       id="rect844"
       width="350"
       height="45"
       x="81"
       y="404"
       ry="10.4" />
    <g
       style="fill:none;stroke:#ffffff;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1"
       id="g962"
       transform="matrix(18.215283,0,0,18.418367,-508.43056,83.478294)">
      <polygon
         id="polygon948"
         points="7,17 3,17 3,13 14,2 18,6 "
         transform="translate(30.359122,-3.2576178)"
         style="stroke:#ffffff;stroke-opacity:1" />
    </g>
  </g>
  <g
     id="g3697"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3699"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3701"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3703"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3705"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3707"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3709"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3711"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3713"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3715"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3717"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3719"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3721"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3723"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
  <g
     id="g3725"
     transform="matrix(0,0.85377419,-0.8998903,0,291.17374,96.976102)" />
</svg>
    """%(ThemeColorSecondary,ThemeColorPrimary)
    
    return(StringSVG)