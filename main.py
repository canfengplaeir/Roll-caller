import random
import configparser
import os
from tkinter import filedialog
import pandas
import xlrd
import configparser


class Operation(object):
    # 写入数据
    def wconfig(self,section,key,value,inipath):
        conf = configparser.ConfigParser()
        conf[section]={key:value}
        with open(inipath,'w') as cfg:
            conf.write(cfg)
    def close_window(self):
    # 终止所有进程
        os._exit(0)
    def RandomPeople(self):
        pass
    def ReadExcel(self):
        pass
    def ReadText(self):
        pass
    def GetUpdates(self):
        pass
    def PreservationPlacement(self):
        pass
    def CreateADefaultProfile(self):
        '''
        配置文件内容：
        1.文件路径 file_path
        2.循序或随机抽人 Drawout Random Introduction
        3.主界面文本内容 MainInterfaceMainText
        4.是否语音播报 YNVoiceBroadcast
        5.如果文件为excel文件，那么读取的列  Columns
        6.是否连抽，以及连抽的个数 Drawn NumberOfDraws
        7.应用主题 Theme
        '''
        config = configparser.ConfigParser()
        config["Path"] = {              
        'file_path': "",
        }

        config['Drawout'] = {
            "mode": 'Random',
        }

        config['Theme'] = {
            "theme": 'litera'
        }
        config['MainInterfaceMainText'] = {
            "text1": '让我看看，躲起来的人都在哪？'
        }
        config['VoiceBroadcast'] = {
            "mode": '0'
        }
        config['Excel'] = {
            "columns": '0'
        }
        config['Drawn'] = {
            "mode": "0",
            "number": "2"
        }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        
