# -*- coding: utf-8 -*-
import os
import tkinter, tkinter.filedialog,tkinter.messagebox
import sys


def config_pickup(start_value,end_value,base_dir,new_dir):
    file_list = os.listdir(base_dir)
    file_flag = 0

    for config_file in file_list:
        path = base_dir + "/" + config_file
        base_config = open(path)
        for config_name in base_config:
            if config_name.find("hostname") != -1:
                name_tmp = config_name.split(" ")
                hostname = name_tmp[1]
                file_flag = file_flag + 1
                break
        new_config = hostname[:-1] + ".txt"
        new_path = new_dir + "/" + new_config
        out_config = open(new_path, "w")
        flag = 0
        base_config.close()
        base_config = open(path)
    
        for config in base_config:
            if config.find(start_value) != -1:
                flag = 1
            elif config.find(end_value) == 0:
                flag = 2
            else:
                pass
        
            if flag == 1:
                out_config.write(config)
            elif flag == 2:
                out_config.write(config)
                flag = 3
            elif flag == 3:
                break
            else:
                pass
    
        base_config.close()
        out_config.close()
    if file_flag == 0:
        tkinter.messagebox.showinfo("end","ファイルがありません")
    else:
        tkinter.messagebox.showinfo("end", "終了")


def text_get():
    start_value = start_box.get()
    if start_value == "":
        tkinter.messagebox.showinfo("error", "startに値を入力してください")
        return
    end_value = end_box.get()
    if end_value == "":
        tkinter.messagebox.showinfo("error", "endに値を入力してください")
        return
    base_dir = base_box.get()
    if base_dir == "":
        tkinter.messagebox.showinfo("error", "変換元フォルダを指定してください")
        return
    out_dir = out_box.get()
    if out_dir == "":
        tkinter.messagebox.showinfo("error", "出力先フォルダを指定してください")
        return
    config_pickup(start_value,end_value,base_dir,out_dir)

def basedir_get():
    iDir = os.path.abspath(os.path.dirname(__file__))
    base_dir = tkinter.filedialog.askdirectory(initialdir = iDir)
    if base_dir != "":
        base_box.delete(0,tkinter.END)
        base_box.insert(tkinter.END,base_dir)

def outdir_get():
    iDir = os.path.abspath(os.path.dirname(__file__))
    new_dir = tkinter.filedialog.askdirectory(initialdir = iDir)
    if new_dir != "":
        out_box.delete(0,tkinter.END)
        out_box.insert(tkinter.END,new_dir)
    
root  = tkinter.Tk()
root.title("config_pickup")
root.geometry("300x200")
start_label = tkinter.Label(root,text="start")
start_label.place(x=10, y=10)
start_box = tkinter.Entry(root,width=20)
start_box.place(x=50, y=12)
end_label = tkinter.Label(text="end")
end_label.place(x=10, y=40)
end_box = tkinter.Entry(root,width=20)
end_box.place(x=50, y=42)
base_label = tkinter.Label(text="変換元フォルダ")
base_label.place(x=2, y=70)
base_box = tkinter.Entry(root,width=40)
base_box.place(x=5, y=90)
out_label = tkinter.Label(text="出力先フォルダ")
out_label.place(x=2, y=110)
out_box = tkinter.Entry(root,width=40)
out_box.place(x=5, y=130)
button = tkinter.Button(root,width=10,text="OK",command=text_get)
button.place(x=110, y=170)
base_button = tkinter.Button(root,text="参照",command=basedir_get)
base_button.place(x=258, y=86)
out_button = tkinter.Button(root,text="参照",command=outdir_get)
out_button.place(x=258, y=126)
root.mainloop()
