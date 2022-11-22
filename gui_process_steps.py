#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:52:08 2018

@author: ndejax
"""

from scorelisto._1_wavfilereader import AudioWav
from scorelisto._2_sonogram import Sonogram
from scorelisto._3_digitalpartition import DigitalPartition

    
def RunStep_One(filename,PARAMETERS,MultiProcProgressValue = None,MultiprocSubStepNameValue = None):
    """
    Input:
        'filename': inpute wav file path '/path/to/wavfile.wav' (str)
        'PARAMETERS' : must be a dictionary containing the following keys:
            ['WindowTimeSize_s'] = size of the sliding windows float value [seconds]
            ['SonogramPeriod_s'] = period of the output signal [s]
            ['f0_hz'] = f0 used to convert frequency to pitch value [Hz] (recommended value: 32.7032 Hz)
            ['TimeStart_s'] = time to start the conversion (None = starting from 0) [s]
            ['TimeStop_s'] = time to end the conversion (None = until the end) [s]
            ['FreqMin_hz'] = Minimum frequency to detect (recommended value: 50 Hz) [Hz]
            ['FreqMax_hz'] = Maximum frequency to detect (recommended value: 5000 Hz) [Hz]
            ['CutOff'] = cutoff parameter of the McLeod pitch detection method
                        (recommended value: 0.97)
            ['SmallCutOff'] = small cutoff parameter of the McLeod pitch detection method 
                        (recommended value: 0.5)
    Output:
        dictionary containing the following keys
            ['pitch_st']  = numpy array of len N (dtype='double') [pitch]
            ['energy_db'] = numpy array of len N (dtype='double') [dB]
            ['te_s'] = period of the 2 numpy array above 'pitch' and 'energy' [s]
            ['f0_hz'] = f0 use for converting frequency to pitch value (default=32.7032 Hz) [Hz]
    """
    
    size = PARAMETERS['WindowTimeSize_s']
    te = PARAMETERS['SonogramPeriod_s']
    f0 = PARAMETERS['f0_hz']
    tStart = PARAMETERS['TimeStart_s']
    tEnd = PARAMETERS['TimeStop_s']
    f_min = PARAMETERS['FreqMin_hz']
    f_max = PARAMETERS['FreqMax_hz']
    cutoff = PARAMETERS['CutOff']
    sm_cutoff = PARAMETERS['SmallCutOff']
    MultiprocSubStepNameValue.value = b"Opening audio file"
    AUDIO = AudioWav(filename)
    AUDIO.A_DefineMcLeodParameters(f_min,f_max,cutoff,sm_cutoff)
    MultiprocSubStepNameValue.value = b"Running McLeod pitch detection"
    OUTPUT = AUDIO.B_ExtractSemitonegram(size,te,f0,tStart,tEnd,MultiProcProgressValue)
    return(OUTPUT)



def RunStep_Two(INPUT,PARAMETERS,MultiProcProgressValue = None,MultiprocSubStepNameValue = None):
    """
    Input(s):
        
        'INPUT' : must be a dictionary containing the following keys:
            ['pitch_st']  = numpy array of len N (dtype='double') [pitch]
            ['energy_db'] = numpy array of len N (dtype='double') [dB]
            ['te_s'] = period of the 2 numpy array above 'pitch' and 'energy' [s]
            ['f0_hz'] = f0 use for converting frequency to pitch value (default=32.7032 Hz) [Hz]
            
        'PARAMETERS' : must be a dictionary containing the following keys:
            ['MedianFilterSize_s'] = size of the sliding windows of the median filter [seconds]
            ['ThresholdEnergyON_dB'] = activation threshold on the energy [dB]
            ['ThresholdEnergyOFF_dB'] = deactivation threshold on the energy [dB]
            ['MaxPitchVariation_st'] = maximum pitch variation from a sample to another [pitch]
            ['MinimumTimeSize_s'] = minimum size of a pitch detection [s]
            ['MinNoteSize_s'] = minimum size of a note detection [s]
            ['MinNoteDiff_st'] = minimum gap of pitch between two notes [pitch]
            ['LMHGaussian_st'] = Width at mid height of the gaussian used to produced the smoothed histogram [pitch]
            
            
    Output(s):
        
        list of dictionary containing the following keys
            ['type_b']  = boolean corresponing to the note type ['note':True or 'rest':False]
            ['length_s'] = the notes length [s]
            ['f0_hz'] = f0 based pitch [hz]
            ['pitch_st'] = the pitch of the notes [pitch] (None for the rests)
            ['energy_db'] = the energy of the notes [dB] (None for the rests)
            ['linked_b'] = boolean, if the note is connected to the past one [bool] (None for the rests)
    """
        
    MedianFilterSize = PARAMETERS['MedianFilterSize_s']
    ThresholdEnergy_ON = PARAMETERS['ThresholdEnergyON_dB']
    ThresholdEnergy_OFF = PARAMETERS['ThresholdEnergyOFF_dB']
    MaxPitchVariation = PARAMETERS['MaxPitchVariation_st']
    MinimumTimeSize = PARAMETERS['MinimumTimeSize_s']
    MinNoteSize = PARAMETERS['MinNoteSize_s']
    MinNoteDiff = PARAMETERS['MinNoteDiff_st']
    LMHGaussian = PARAMETERS['LMHGaussian_st']
    ### TRAITEMENT
    FollowProgression = MultiProcProgressValue is not None
    if(FollowProgression):
        MultiProcProgressValue.value = 1
        MultiprocSubStepNameValue.value = b"Loading input data"
    SONO = Sonogram(INPUT['pitch_st'],INPUT['energy_db'],INPUT['te_s'],INPUT['f0_hz'])
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 2
        MultiprocSubStepNameValue.value = b"Applying median filter"
    SONO.A_ApplyMedianFilter(MedianFilterSize)
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 3
        MultiprocSubStepNameValue.value = b"Filter on the energy"
    SONO.B_Masked_AutoEnergy(ThresholdEnergy_ON,ThresholdEnergy_OFF)
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 4
        MultiprocSubStepNameValue.value = b"Filter on the maximum pitch variation"
    SONO.C_Masked_MaximumVariation(MaxPitchVariation)
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 5
        MultiprocSubStepNameValue.value = b"Filter on the minimum size of a note"
    SONO.D_Masked_MinimumTimeSize(MinimumTimeSize)
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 6
        MultiprocSubStepNameValue.value = b"Detecting groups of notes"
    SONO.E_DetectGroupsOfNotes()
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 7
        MultiprocSubStepNameValue.value = b"Detecting notes"
    SONO.F_Detectnotes(MinNoteSize,MinNoteDiff,LMHGaussian)
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 8
        MultiprocSubStepNameValue.value = b"Generating analog partition"
    OUTPUT = SONO.G_GenerateAnalogPartition()
    
    OffsetStartValue = SONO.TimeOffsetFirstGroup()
    
    return(OUTPUT,OffsetStartValue)

    
    
    
def RunStep_Three(INPUT,PARAMETERS,MultiProcProgressValue = None,MultiprocSubStepNameValue = None):
    """
    Input(s):
        
        'INPUT' : must be a list of dictionary containing the following keys
            ['type_b']  = string corresponing to the note type ['note' or 'rest']
            ['length_s'] = the notes length [s]
            ['f0_hz'] = f0 based pitch [hz]
            ['pitch_st'] = the pitch of the notes [pitch] (None for the rests)
            ['energy_db'] = the energy of the notes [dB] (None for the rests)
            ['linked_b'] = boolean, if the note is connected to the past one [bool] (None for the rests)
            
        'PARAMETERS' : must be a dictionary containing the following keys:
            ['DelayMin_s'] = 60.0/BPMmax (default=60.0/200 BPM = 0.3) [seconds]
            ['DelayMax_s'] = 60.0/BPMmin (default=60.0/40 BPM = 1.5) [seconds]
            ['MaxDelayVar'] = Max delay variation along the track (default = 0.5) (0=0% ; 1= 100%)
            ['ErrorMax'] = error max of the combinations to be considerate
            ['CombinationToMask'] = dictionary containing the combination to mask or unmask
            
            
    Output:
        
        The string of the XML score ready to write into a file 
    """
    FollowProgression = MultiProcProgressValue is not None
    if(FollowProgression):
        MultiProcProgressValue.value = 1
        MultiprocSubStepNameValue.value = b"Loading input data"
    
    DelayMin = PARAMETERS['DelayMin_s']
    DelayMax = PARAMETERS['DelayMax_s']
    MaxDelayVar = PARAMETERS['MaxDelayVar']
    ErrorMax = PARAMETERS['ErrorMax']
    CombsToMask = PARAMETERS['CombinationToMask']
    
    DigPart = DigitalPartition()
    for AnalogNote in INPUT:
        DigPart.AddNote(AnalogNote['type_b'],AnalogNote['length_s'],AnalogNote['pitch_st'])
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 2
        MultiprocSubStepNameValue.value = b"Auto Setting fifths and clef"
    DigPart.A_MinimizeHeightError()
    DigPart.B_AutoSetFifths()
    DigPart.C_AutoSetClef()
    DigPart.D_AutoTranslateOctave()
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 3
        MultiprocSubStepNameValue.value = b"Getting all possible combinations for each notes"
    DigPart.E_GetConfigurationsForAllNotes()
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 3
        MultiprocSubStepNameValue.value = b"Masking unchecked combinations"
    DigPart.F_MaskCOMBINATIONS(CombsToMask)
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 4
        MultiprocSubStepNameValue.value = b"Building graph"
    DigPart.G_BuildGraph(ErrorMax,DelayMin,DelayMax,MaxDelayVar)
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 5
        MultiprocSubStepNameValue.value = b"Searching best rythms"
    DigPart.H_GetOptimalPath()
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 6
        MultiprocSubStepNameValue.value = b"Generating XML File"
    DigPart.I_GetPathInfos()
    XMLString = DigPart.J_GenerateScore("musicxml")
    MidiString = DigPart.J_GenerateScore("midi")
    MidiString_norythm = DigPart.J_GenerateScore("midi_norythm")
    return(XMLString,MidiString,MidiString_norythm,DigPart)


def RunStep_Three_bis(DigitalPartition,PARAMETERS,MultiProcProgressValue = None,MultiprocSubStepNameValue = None):
    """
    Input(s):
        'DigitalPartition' : A 'DigitalPartition' class already processed until function 'E_GetConfigurationsForAllNotes()'
            
        'PARAMETERS' : must be a dictionary containing the following keys:
            ['DelayMin_s'] = 60.0/BPMmax (default=60.0/200 BPM = 0.3) [seconds]
            ['DelayMax_s'] = 60.0/BPMmin (default=60.0/40 BPM = 1.5) [seconds]
            ['MaxDelayVar'] = Max delay variation along the track (default = 0.5) (0=0% ; 1= 100%)
            ['ErrorMax'] = error max of the combinations to be considerate
            ['CombinationToMask'] = dictionary containing the combination to mask or unmask
            
            
    Output:
        
        The string of the XML score ready to write into a file 
    """
    FollowProgression = MultiProcProgressValue is not None
    if(FollowProgression):
        MultiProcProgressValue.value = 1
        MultiprocSubStepNameValue.value = b"Loading input data"
    
    DelayMin = PARAMETERS['DelayMin_s']
    DelayMax = PARAMETERS['DelayMax_s']
    MaxDelayVar = PARAMETERS['MaxDelayVar']
    ErrorMax = PARAMETERS['ErrorMax']
    CombsToMask = PARAMETERS['CombinationToMask']
    
    if(FollowProgression):
        MultiProcProgressValue.value = 1
        MultiprocSubStepNameValue.value = b"Masking unchecked combinations"
    DigitalPartition.F_MaskCOMBINATIONS(CombsToMask)
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 2
        MultiprocSubStepNameValue.value = b"Building graph"
    DigitalPartition.G_BuildGraph(ErrorMax,DelayMin,DelayMax,MaxDelayVar)
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 3
        MultiprocSubStepNameValue.value = b"Searching best rythms"
    DigitalPartition.H_GetOptimalPath()
    
    
    if(FollowProgression):
        MultiProcProgressValue.value = 4
        MultiprocSubStepNameValue.value = b"Generating XML File"
    DigitalPartition.I_GetPathInfos()
    XMLString = DigitalPartition.J_GenerateScore("musicxml")
    MidiString = DigitalPartition.J_GenerateScore("midi")
    MidiString_norythm = DigitalPartition.J_GenerateScore("midi_norythm")
    return(XMLString,MidiString,MidiString_norythm,DigitalPartition)



