# -*- coding: utf-8 -*-
import copy
import pickle
import os

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject


class ManageParameters(QObject):
    ParamStep1Changed = pyqtSignal()
    ParamStep2Changed = pyqtSignal()
    ParamStep3Changed = pyqtSignal()
    ParamGlobalChanged = pyqtSignal()
    ParamStep1Renamed = pyqtSignal(str,str)
    ParamStep2Renamed = pyqtSignal(str,str)
    ParamStep3Renamed = pyqtSignal(str,str)
    ParamGlobalRenamed = pyqtSignal(str,str)
    def __init__(self,pathfile,parent=None):
        QObject.__init__(self)
        self.pathfile = pathfile
        self.parameters = self.LoadParameters()
        self.UpdateParametersFile()
    
    def LoadParameters(self):
        if(os.path.isfile(self.pathfile)):
            with open(self.pathfile, "rb") as fp:
                parameters = pickle.load(fp)
        else:
            parameters = self.DefaultParameters()
        return(parameters)
    
    def UpdateParametersFile(self):
        with open(self.pathfile, "wb") as fp:
            pickle.dump(self.parameters,fp)
    
    
    def GetGlobalParameter(self,paramKey):
        if not (paramKey in self.parameters['global']):
            return(None)
        parameters = copy.deepcopy(self.parameters['global'][paramKey])
        return(parameters)
    
    def GetStep1Parameter(self,paramKey):
        if not (paramKey in self.parameters['step1']):
            return(None)
        parameters = copy.deepcopy(self.parameters['step1'][paramKey])
        return(parameters)
    
    def GetStep2Parameter(self,paramKey):
        if not (paramKey in self.parameters['step2']):
            return(None)
        parameters = copy.deepcopy(self.parameters['step2'][paramKey])
        return(parameters)
    
    def GetStep3Parameter(self,paramKey):
        if not (paramKey in self.parameters['step3']):
            return(None)
        parameters = copy.deepcopy(self.parameters['step3'][paramKey])
        return(parameters)
    
    def GetListOfGlobalParameters(self):
        listParam = list(self.parameters['global'].keys())
        return(listParam)
    
    def GetListOfStep1Parameters(self):
        listParam = list(self.parameters['step1'].keys())
        return(listParam)
    
    def GetListOfStep2Parameters(self):
        listParam = list(self.parameters['step2'].keys())
        return(listParam)
    
    def GetListOfStep3Parameters(self):
        listParam = list(self.parameters['step3'].keys())
        return(listParam)

    def DelGlobalParameter(self,key):
        if not (key in self.parameters['global']):
            raise ValueError("This global parameter does not exists")
        if(key == 'default'):
            raise ValueError("Cannot delete 'default' parameter")
        
        del self.parameters['global'][key]
        self.UpdateParametersFile()
        self.ParamGlobalChanged.emit()
    
    def DelStep1Parameter(self,key):
        if not (key in self.parameters['step1']):
            raise ValueError("This global parameter does not exists")
        if(key == 'default'):
            raise ValueError("Cannot delete 'default' parameter")
        
        del self.parameters['step1'][key]
        
        for globalparam in self.parameters['global']:
            if(self.parameters['global'][globalparam]['step1'] == key):
                self.parameters['global'][globalparam]['step1'] = 'default'
        
        self.UpdateParametersFile()
        self.ParamStep1Changed.emit()
    
    def DelStep2Parameter(self,key):
        if not (key in self.parameters['step2']):
            raise ValueError("This global parameter does not exists")
        if(key == 'default'):
            raise ValueError("Cannot delete 'default' parameter")
        
        del self.parameters['step2'][key]
        
        for globalparam in self.parameters['global']:
            if(self.parameters['global'][globalparam]['step2'] == key):
                self.parameters['global'][globalparam]['step2'] = 'default'
        self.UpdateParametersFile()
        self.ParamStep2Changed.emit()
    
    def DelStep3Parameter(self,key):
        if not (key in self.parameters['step3']):
            raise ValueError("This global parameter does not exists")
        if(key == 'default'):
            raise ValueError("Cannot delete 'default' parameter")
        
        del self.parameters['step3'][key]
        
        for globalparam in self.parameters['global']:
            if(self.parameters['global'][globalparam]['step3'] == key):
                self.parameters['global'][globalparam]['step3'] = 'default'
        self.UpdateParametersFile()
        self.ParamStep3Changed.emit()
    
    def UpdateNameParameterGlobal(self,OldKey,NewKey):
        if not (OldKey in self.parameters['global']):
            raise ValueError("This global parameter does not exists")
        if(OldKey == 'default'):
            raise ValueError("Cannot modify 'default' parameter")
        
        self.parameters['global'][NewKey] = self.parameters['global'].pop(OldKey)
        self.UpdateParametersFile()
        self.ParamGlobalRenamed.emit(OldKey,NewKey)
        
    def UpdateNameParameterStep1(self,OldKey,NewKey):
        if not (OldKey in self.parameters['step1']):
            raise ValueError("This step1 parameter does not exists")
        if(OldKey == 'default'):
            raise ValueError("Cannot modify 'default' parameter")
        
        self.parameters['step1'][NewKey] = self.parameters['step1'].pop(OldKey)
        self.UpdateParametersFile()
        self.ParamStep1Renamed.emit(OldKey,NewKey)
    
    def UpdateNameParameterStep2(self,OldKey,NewKey):
        if not (OldKey in self.parameters['step2']):
            raise ValueError("This step2 parameter does not exists")
        if(OldKey == 'default'):
            raise ValueError("Cannot modify 'default' parameter")
        
        self.parameters['step2'][NewKey] = self.parameters['step2'].pop(OldKey)
        self.UpdateParametersFile()
        self.ParamStep2Renamed.emit(OldKey,NewKey)
    
    def UpdateNameParameterStep3(self,OldKey,NewKey):
        if not (OldKey in self.parameters['step3']):
            raise ValueError("This step1 parameter does not exists")
        if(OldKey == 'default'):
            raise ValueError("Cannot modify 'default' parameter")
        
        self.parameters['step3'][NewKey] = self.parameters['step3'].pop(OldKey)
        self.UpdateParametersFile()
        self.ParamStep3Renamed.emit(OldKey,NewKey)
    
    
    def GlobalNameExists(self,name):
        return(name in self.parameters['global'])
    def Step1NameExists(self,name):
        return(name in self.parameters['step1'])
    def Step2NameExists(self,name):
        return(name in self.parameters['step2'])
    def Step3NameExists(self,name):
        return(name in self.parameters['step3'])
    
    def IsGlobalParameterOk(self,parameter):
        # Check if all the necessary keys are here
        if not ('step1' in parameter):
            return(False)
        if not ('step2' in parameter):
            return(False)
        if not ('step3' in parameter):
            return(False)
        
        # Check if the step parameters exists in the database
        if not (parameter['step1'] in self.parameters['step1']):
            return(False)
        if not (parameter['step2'] in self.parameters['step2']):
            return(False)
        if not (parameter['step3'] in self.parameters['step3']):
            return(False)
        
        return(True)
    
    def IsParametersStep1Ok(self,parameter):
        if not ('WindowTimeSize_s' in parameter):
            return(False)
        if not ('SonogramPeriod_s' in parameter):
            return(False)
        if not ('f0_hz' in parameter):
            return(False)
        if not ('FreqMin_hz' in parameter):
            return(False)
        if not ('FreqMax_hz' in parameter):
            return(False)
        if not ('CutOff' in parameter):
            return(False)
        if not ('SmallCutOff' in parameter):
            return(False)
        return(True)
    
    def IsParametersStep2Ok(self,parameter):
        if not ('MedianFilterSize_s' in parameter):
            return(False)
        if not ('ThresholdEnergyON_dB' in parameter):
            return(False)
        if not ('ThresholdEnergyOFF_dB' in parameter):
            return(False)
        if not ('MaxPitchVariation_st' in parameter):
            return(False)
        if not ('MinimumTimeSize_s' in parameter):
            return(False)
        if not ('MinNoteSize_s' in parameter):
            return(False)
        if not ('MinNoteDiff_st' in parameter):
            return(False)
        if not ('LMHGaussian_st' in parameter):
            return(False)
        return(True)
    
    def IsParametersStep3Ok(self,parameter):
        if not ('DelayMin_s' in parameter):
            return(False)
        if not ('DelayMax_s' in parameter):
            return(False)
        if not ('MaxDelayVar' in parameter):
            return(False)
        if not ('ErrorMax' in parameter):
            return(False)
        if not ('CombinationToMask' in parameter):
            return(False)
         ########  1 NOTES #########
        if not ('1NOTE_1BEAT' in parameter['CombinationToMask']):
            return(False)
        if not ('1REST_1BEAT' in parameter['CombinationToMask']):
            return(False)
        if not ('1NOTE_2BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1REST_2BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1NOTE_3BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1REST_3BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1NOTE_4BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1REST_4BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1NOTE_5BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1REST_5BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1NOTE_6BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1REST_6BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1NOTE_7BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1REST_7BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1NOTE_8BEATS' in parameter['CombinationToMask']):
            return(False)
        if not ('1REST_8BEATS' in parameter['CombinationToMask']):
            return(False)
        ########  2 NOTES #########
        ### 1 BEAT
        if not ('EN_EN' in parameter['CombinationToMask']):
            return(False)
        if not ('ER_EN' in parameter['CombinationToMask']):
            return(False)
        if not ('EN_ER' in parameter['CombinationToMask']):
            return(False)
        if not ('DEN_SN' in parameter['CombinationToMask']):
            return(False)
        if not ('SN_DEN' in parameter['CombinationToMask']):
            return(False)
        ### 2 BEATS
        if not ('DQN_EN' in parameter['CombinationToMask']):
            return(False)
        if not ('QR-ER_EN' in parameter['CombinationToMask']):
            return(False)
        if not ('DQN_ER' in parameter['CombinationToMask']):
            return(False)
        if not ('EN_EN-QN' in parameter['CombinationToMask']):
            return(False)
        ### 3 BEATS
        if not ('QN-DQN_EN' in parameter['CombinationToMask']):
            return(False)
        if not ('QR-QR-ER_EN' in parameter['CombinationToMask']):
            return(False)
        if not ('QN-DQN_ER' in parameter['CombinationToMask']):
            return(False)
        if not ('EN_EN-HN' in parameter['CombinationToMask']):
            return(False)
        ### 4 BEATS
        if not ('HN-DQN_EN' in parameter['CombinationToMask']):
            return(False)
        if not ('QR-QR-QR-ER_EN' in parameter['CombinationToMask']):
            return(False)
        if not ('HN-DQN_ER' in parameter['CombinationToMask']):
            return(False)
        if not ('EN_EN-DHN' in parameter['CombinationToMask']):
            return(False)
        
        ######### 3 NOTES ##########
        ### 1 BEAT
        if not ('EN_SN_SN' in parameter['CombinationToMask']):
            return(False)
        if not ('ER_SN_SN' in parameter['CombinationToMask']):
            return(False)
        if not ('SN_SN_EN' in parameter['CombinationToMask']):
            return(False)
        if not ('SN_SN_ER' in parameter['CombinationToMask']):
            return(False)
        if not ('SN_EN_SN' in parameter['CombinationToMask']):
            return(False)
        if not ('T_EN_EN_EN' in parameter['CombinationToMask']):
            return(False)
        if not ('T_EN_DEN_SN' in parameter['CombinationToMask']):
            return(False)
        if not ('T_EN_SN_DEN' in parameter['CombinationToMask']):
            return(False)
        if not ('T_SN_EN_DEN' in parameter['CombinationToMask']):
            return(False)
        if not ('T_SN_DEN_EN' in parameter['CombinationToMask']):
            return(False)
        if not ('T_DEN_EN_SN' in parameter['CombinationToMask']):
            return(False)
        if not ('T_DEN_SN_EN' in parameter['CombinationToMask']):
            return(False)
        ### 2 BEATS
        if not ('EN_QN_EN' in parameter['CombinationToMask']):
            return(False)
        if not ('DQN_SN_SN' in parameter['CombinationToMask']):
            return(False)
        ### 3 BEATS
        if not ('QN-DQN_SN_SN' in parameter['CombinationToMask']):
            return(False)
        ### 4 BEATS
        if not ('HN-DQN_SN_SN' in parameter['CombinationToMask']):
            return(False)
        ######### 4 NOTES ##########
        if not ('SN_SN_SN_SN' in parameter['CombinationToMask']):
            return(False)
        return(True)
    
    def ModifyGlobalParameter(self,KeyName,parameters):
        if self.GlobalNameExists(KeyName):
            if(self.IsGlobalParameterOk(parameters)):
                self.parameters['global'][KeyName] = copy.deepcopy(parameters)
                self.UpdateParametersFile()
    
    def ModifyStep1Parameter(self,KeyName,parameters):
        if self.Step1NameExists(KeyName):
            if(self.IsParametersStep1Ok(parameters)):
                self.parameters['step1'][KeyName] = copy.deepcopy(parameters)
                self.UpdateParametersFile()
    
    def ModifyStep2Parameter(self,KeyName,parameters):
        if self.Step2NameExists(KeyName):
            if(self.IsParametersStep2Ok(parameters)):
                self.parameters['step2'][KeyName] = copy.deepcopy(parameters)
                self.UpdateParametersFile()
    
    def ModifyStep3Parameter(self,KeyName,parameters):
        if self.Step3NameExists(KeyName):
            if(self.IsParametersStep3Ok(parameters)):
                self.parameters['step3'][KeyName] = copy.deepcopy(parameters)
                self.UpdateParametersFile()
    
    def AddGlobalParameter(self,KeyName,parameters=None):
        if not self.GlobalNameExists(KeyName):
            if(parameters==None):
                self.parameters['global'][KeyName] = self.DefaultGlobalParameters()
                self.UpdateParametersFile()
                self.ParamGlobalChanged.emit()
            elif(self.IsGlobalParameterOk(parameters)):
                self.parameters['global'][KeyName] = copy.deepcopy(parameters)
                self.UpdateParametersFile()
                self.ParamGlobalChanged.emit()
    
    def AddStep1Parameter(self,KeyName,parameters=None):
        if not self.Step1NameExists(KeyName):
            if(parameters==None):
                self.parameters['step1'][KeyName] = self.DefaultStep1Parameters()
                self.UpdateParametersFile()
                self.ParamStep1Changed.emit()
            elif(self.IsStep1ParameterOk(parameters)):
                self.parameters['step1'][KeyName] = copy.deepcopy(parameters)
                self.UpdateParametersFile()
                self.ParamStep1Changed.emit()
    
    def AddStep2Parameter(self,KeyName,parameters=None):
        if not self.Step2NameExists(KeyName):
            if(parameters==None):
                self.parameters['step2'][KeyName] = self.DefaultStep2Parameters()
                self.UpdateParametersFile()
                self.ParamStep2Changed.emit()
            elif(self.IsStep2ParameterOk(parameters)):
                self.parameters['step2'][KeyName] = copy.deepcopy(parameters)
                self.UpdateParametersFile()
                self.ParamStep2Changed.emit()
    
    def AddStep3Parameter(self,KeyName,parameters=None):
        if not self.Step3NameExists(KeyName):
            if(parameters==None):
                self.parameters['step3'][KeyName] = self.DefaultStep3Parameters()
                self.UpdateParametersFile()
                self.ParamStep3Changed.emit()
            elif(self.IsStep3ParameterOk(parameters)):
                self.parameters['step3'][KeyName] = copy.deepcopy(parameters)
                self.UpdateParametersFile()
                self.ParamStep3Changed.emit()
    
    
    def DefaultStep1Parameters(self):
        parameters = {
            'WindowTimeSize_s':20e-3,
            'SonogramPeriod_s':1e-3,
            'f0_hz':32.7032,
            'FreqMin_hz':50.0,
            'FreqMax_hz':5000.0,
            'CutOff':0.97,
            'SmallCutOff':0.5
        }
        return(parameters)
    
    def DefaultStep2Parameters(self):
        parameters = {
            'MedianFilterSize_s': 20e-3,
            'ThresholdEnergyON_dB': 25.0,
            'ThresholdEnergyOFF_dB': 30.0,
            'MaxPitchVariation_st': 1.0,
            'MinimumTimeSize_s': 50e-3,
            'MinNoteSize_s': 100e-3,
            'MinNoteDiff_st': 0.5,
            'LMHGaussian_st': 0.5
        }
        return(parameters)
    
    def DefaultStep3Parameters(self):
        CombinationToMask = {
             ########  1 NOTES #########
            '1NOTE_1BEAT': False,
            '1REST_1BEAT': False,
            '1NOTE_2BEATS': False,
            '1REST_2BEATS': False,
            '1NOTE_3BEATS': False,
            '1REST_3BEATS': False,
            '1NOTE_4BEATS': False,
            '1REST_4BEATS': False,
            '1NOTE_5BEATS': False,
            '1REST_5BEATS': False,
            '1NOTE_6BEATS': False,
            '1REST_6BEATS': False,
            '1NOTE_7BEATS': False,
            '1REST_7BEATS': False,
            '1NOTE_8BEATS': False,
            '1REST_8BEATS': False,
            ########  2 NOTES #########
            ### 1 BEAT
            'EN_EN': False,
            'ER_EN': False,
            'EN_ER': False,
            'DEN_SN': False,
            'SN_DEN': False,
            ### 2 BEATS
            'DQN_EN': False,
            'QR-ER_EN': False,
            'DQN_ER': False,
            'EN_EN-QN': False,
            ### 3 BEATS
            'QN-DQN_EN': False,
            'QR-QR-ER_EN': False,
            'QN-DQN_ER': False,
            'EN_EN-HN': False,
            ### 4 BEATS
            'HN-DQN_EN': False,
            'QR-QR-QR-ER_EN': False,
            'HN-DQN_ER': False,
            'EN_EN-DHN': False,
            
            ######### 3 NOTES ##########
            ### 1 BEAT
            'EN_SN_SN': False,
            'ER_SN_SN': False,
            'SN_SN_EN': False,
            'SN_SN_ER': False,
            'SN_EN_SN': False,
            'T_EN_EN_EN': False,
            'T_EN_DEN_SN': False,
            'T_EN_SN_DEN': False,
            'T_SN_EN_DEN': False,
            'T_SN_DEN_EN': False,
            'T_DEN_EN_SN': False,
            'T_DEN_SN_EN': False,
            ### 2 BEATS
            'EN_QN_EN': False,
            'DQN_SN_SN': False,
            ### 3 BEATS
            'QN-DQN_SN_SN': False,
            ### 4 BEATS
            'HN-DQN_SN_SN': False,
            ######### 4 NOTES ##########
            'SN_SN_SN_SN': False
        }
        parameters = {
            'DelayMin_s': 0.3,
            'DelayMax_s': 1.5,
            'MaxDelayVar': 0.5,
            'ErrorMax': 10.0,
            'CombinationToMask':CombinationToMask

        }
        return(parameters)
    
    def DefaultGlobalParameters(self):
        parameters = {'step1':'default','step2':'default','step3':'default'}
        return(parameters)
    
    def DefaultParameters(self):
        parameters = {}
        parameters['global'] = {'default':self.DefaultGlobalParameters()}
        parameters['step1'] = {'default':self.DefaultStep1Parameters()}
        parameters['step2'] = {'default':self.DefaultStep2Parameters()}
        parameters['step3'] = {'default':self.DefaultStep3Parameters()}
        return(parameters)
        
