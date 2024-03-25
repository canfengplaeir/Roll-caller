# -*- coding: utf-8 -*
import configparser
import os
from tkinter import * 
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import main
import requests

def window_centered(name,width,height):
        swidth = name.winfo_screenwidth()
        sheight = name.winfo_screenheight()
        size_geo = '%dx%d+%d+%d' % (width, height, (swidth-width)/2, (sheight-height)/2)
        return size_geo


opera = main.Operation()
if os.path.exists("config.ini"):
    conf = configparser.ConfigParser()
    conf.read('config.ini') 
    Path = conf.items("Path")
    Drawout = conf.items("Drawout")
    Theme = conf.items("Theme")
    MainInterfaceMainText = conf.items("MainInterfaceMainText")
    VoiceBroadcast = conf.items("VoiceBroadcast")
    Excel = conf.items("VoiceBroadcast")
    Drawn = conf.items("Drawn")
else:
     opera.CreateADefaultProfile()

def GetFilePath():
    f_types = [('Text Files', '*.xls'), ('Text Files', '*.xlsx'),('Text Files','*.txt')]
    file_path = filedialog.askopenfilename(filetypes=f_types)
    if  len(file_path) == 0:
        print("未选择文件")
    else:
        choosefile_entry.delete(0,"end")
        choosefile_entry.insert(0,file_path)

# 写入数据
def saveset():
    file_path = choosefile_entry.get()
    theme = theme_combobox.get()
    conf["Path"]={"file_path":file_path}
    with open("config.ini",'w') as cfg:
        conf.write(cfg)


def settings_interface():
    
    SetWin = ttk.Toplevel(title="设置")
    # SetWin.lift()
    SetWin.wm_transient(app)
    SetWin.resizable(False,False)
    SetWin.geometry(window_centered(SetWin,300,480))
    if os.path.exists("resource\icon.ico"):
        SetWin.iconbitmap("resource\icon.ico")        

    # 选择文件
    file_frame = ttk.Frame(SetWin)
    file_frame.grid(column=0,row=0)
    fileaddress_label = ttk.Label(file_frame,text="文件路径")
    fileaddress_label.grid(column=0,row=0)
    global choosefile_entry
    choosefile_entry = ttk.Entry(file_frame)
    choosefile_entry.grid(column=0,row=1)
    # choosefile_entry.configure(state="readonly")
    file_button = tk.Button(file_frame,text="选项文件",command=lambda:GetFilePath())
    file_button.grid(column=1,row=1)


    # 连抽模式
    drawnframe = ttk.Frame(SetWin)
    drawnframe.grid(column=0,row=1)
    drawn_label = ttk.Label(drawnframe,text="连抽模式")
    drawn_label.pack()
    var_checkbox = StringVar()
    DrawnCheckBox = ttk.Checkbutton(drawnframe,text="开启",variable=var_checkbox,onvalue="开启",offvalue="关闭")
    var_checkbox.set("关闭")
    # DrawnCheckBox()
    DrawnCheckBox.pack()

    # 主题选择
    theme_frame = ttk.Frame(SetWin)
    theme_frame.grid(column=0,row=2)
    theme_label = ttk.Label(theme_frame,text="选择主题")
    theme_label.grid(column=0,row=0)    
    var_combobox=tk.StringVar()
    global theme_combobox
    theme_combobox = ttk.Combobox(theme_frame,textvariable=var_combobox,values=("litera","dark","blue"))
    theme_combobox.grid(column=0,row=1)

    # 主页面文字
    maintext_frame = ttk.Frame(SetWin)
    maintext_frame.grid(column=0,row=3)
    maintext_label = ttk.Label(maintext_frame,text="主页面文字")
    maintext_label.grid(column=0,row=0)
    maintext_entry = ttk.Entry(maintext_frame)
    maintext_entry.grid(column=0,row=1)


    # 重置配置文件
    bottom_frame = ttk.Frame(SetWin)
    bottom_frame.grid(column=0,row=4)
    reset_button = tk.Button(bottom_frame,text="重置设置",command=opera.CreateADefaultProfile)
    reset_button.grid(column=2,row=0)
    savesettings_button = tk.Button(bottom_frame,text="保存",command=saveset)
    savesettings_button.grid(column=0,row=0)
    cancel_button = tk.Button(bottom_frame,text="退出",command=SetWin.destroy)
    cancel_button.grid(column=3,row=0)


    if not MainInterfaceMainText[0][1] == "":
        maintext_entry.delete(0,"end")
        maintext_entry.insert(0,MainInterfaceMainText[0][1])
    if not Theme[0][1] == "":
         theme_combobox.set(Theme[0][1])
    if not Path[0][1] == "":
        choosefile_entry.delete(0,"end")
        choosefile_entry.insert(0,Path[0][1])
    SetWin.mainloop()


app = ttk.window.Window(title="点名器", themename=Theme[0][1])
app.resizable(False,False)
app.geometry(window_centered(app,550,350))
app.protocol("WM_DELETE_WINDOW", opera.close_window)
while True:
    if os.path.exists("resource\icon.ico"):
        app.iconbitmap("resource\icon.ico")
        break
    else:
        try:
            iconurl = requests.get("http://canfeng.serv00.net:34926/d/file/icon.ico?sign=gpLKxOj0kJ2IWrQhSBLOYW16vmmbLg_m9wkDXrcKHyk=:0",allow_redirects=True)
            open("resource/icon.ico","wb").write(iconurl.content)
        except:
            break
            
top_menu = Menu(app,tearoff=False)
menuMore = Menu(top_menu,tearoff=False)
top_menu.add_cascade(label="更多",menu=menuMore)
top_menu.add_cascade(label="设置",command=settings_interface)
menuMore.add_command(label="关于")
app.config(menu = top_menu)
# setting = tk.Button(app,text="设置",command=settings_interface).pack()
app.mainloop()
    


