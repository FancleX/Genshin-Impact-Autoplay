import tkinter as tk
from tkinter.constants import HORIZONTAL, X
import tkinter.messagebox
import re
import Autoplay
from WindsongLyre import *
import time
from tkinter import Canvas, filedialog
from tkinter.ttk import *
import base64
import os

class MY_GUI():
    def __init__(self, init_window):
        self.init_window = init_window

    def set_window(self):
        self.init_window.title('Genshin Impact Autoplay')
        self.init_window.geometry('500x300')
        #Figure
        self.init_canvas = tk.Canvas(self.init_window, bg='DarkTurquoise', height=100, width=500)
        self.image_file = tk.PhotoImage(file='icon.gif')
        Canvas.create_image(self.init_canvas, 250, 50, image = self.image_file)
        self.init_canvas.pack(side='top')
        #Frame mainwindow
        self.init_frame = tk.Frame(self.init_window).pack()
        self.init_frame_l = tk.Frame(self.init_frame).pack(side='top')
        self.init_frame_r = tk.Frame(self.init_frame).pack(side='bottom')
        #Label mainwindow
        tk.Label(self.init_frame_l, text='Music name: ', bg=None, font=('Arial' ,14)).pack()
        self.name = tk.Entry(self.init_frame_r, show=None, font=('Arial', 14), highlightcolor='red', highlightthickness=1)
        self.name.pack()
        #Button
        self.btn_start = tk.Button(self.init_window, text='Start with default', command=self.mainStart).place(x=100, y=230)
        self.btn_go = tk.Button(self.init_window, text='Setting before start', command=self.jump).place(x=300, y=230)
        self.btn_import = tk.Button(self.init_window, text='...', command=self.getFile).place(x=370, y=133)
        #Status bar
        self.bar = tk.Label(self.init_window, bg='white', width=5)
        self.bar.place(x=138, y=180)
        #Progress bar
        self.pb = Progressbar(self.init_window, length=170, mode='determinate', orient=HORIZONTAL, cursor='star')
        self.pb.place(x=190, y=180)
        self.pb['value'] = 0
    
    def set_sub_window(self):
        #Set subwindow
        self.sub_window = tk.Toplevel(self.init_window)
        self.sub_window.geometry('500x300')
        self.sub_window.title('Parameters setting')
        #Label subwindow
        tk.Label(self.sub_window, text='Please set pause delay time(s): ', bg=None, font=('Arial' ,14)).pack(fill=X, pady=10)
        self.q1 = tk.Entry(self.sub_window, show=None, font=('Arial', 14), highlightcolor='red', highlightthickness=1)
        self.q1.pack()
        tk.Label(self.sub_window, text='Please set single key delay time(s): ', bg=None, font=('Arial' ,14)).pack(fill=X, pady=10)
        self.q2 = tk.Entry(self.sub_window, show=None, font=('Arial', 14), highlightcolor='red', highlightthickness=1)
        self.q2.pack()
        tk.Label(self.sub_window, text='Please set combo key delay time(s): ', bg=None, font=('Arial' ,14)).pack(fill=X, pady=10)
        self.q3 = tk.Entry(self.sub_window, show=None, font=('Arial', 14), highlightcolor='red', highlightthickness=1)
        self.q3.pack()
        #Button
        self.btn_run = tk.Button(self.sub_window, text='Run', command=self.subStart).place(x=240, y=250)

    #Function        
    #Import button
    def getFile(self):
        self.file_path = filedialog.askopenfilename()
        self.name.delete(0, 'end')
        self.name.insert(0, self.file_path)

    #Progress bar
    def progress(self, counter):
        self.pb['value'] = counter
        self.init_window.update()

    #Progress indicator
    def proIn(self):
        amount = self.pb['maximum']
        counter = self.counter
        percent = int ((counter / amount) * 100) 
        self.bar.config(text=str(percent) + '%')
        self.init_window.update()

    #Status bar initially display  
    def statusDisplay(self):
        t = [ '3', '2', '1','Start']
        for i in t:
            self.bar.config(text=i)
            self.init_window.update()
            time.sleep(1)
     
    #Get user's input
    def getName(self):
        name = self.name.get()
        try:
            with open(name, 'r') as f:
                lyrics = f.readlines()
            return lyrics
        except:
            return 1

    #Jump
    def jump(self):
        if (self.getName() != 1):
            self.set_sub_window()
        else:
            tkinter.messagebox.showerror(title='Error', message='Name input error, please retry')
            
    #Get settings
    def getSetting(self):
        t_pause = self.q1.get()
        t_single = self.q2.get()
        t_combo = self.q3.get()
        s = [t_pause, t_single, t_combo]
        return s
        
    #First filter lyrics with combo keys, single keys and space pause
    def lyricsfinder(self, lyrics):
        ls = []
        for rows in lyrics:
            rows = rows.replace('\n', ' ')
            ls.append(re.findall(r'[\w\s]+', rows))
        return ls

    #Start with default
    def mainStart(self):
        if (self.getName() != 1):
            self.lyricsget = self.getName()
        else:
            tkinter.messagebox.showerror(title='Error', message='Name input error, please retry')
            return None
        self.statusDisplay()
        self.counter = 0
        self.pb['maximum'] = len(self.lyricsfinder(self.lyricsget))
        for row in self.lyricsfinder(self.lyricsget):
            for keys in row:
                Autoplay.autoplay(keys, t_pause = 0.1, t_single = 0.07, t_combo = 0.08)
            self.counter += 1
            self.proIn()
            self.progress(self.counter)
        time.sleep(0.5)
        self.bar.config(text='End')
    
    #Start with new settings
    def subStart(self):
        self.lyricsget = self.getName()
        l = self.getSetting()
        t_pause = float(l[0])
        t_single = float(l[1])
        t_combo = float(l[2])
        self.statusDisplay()
        time.sleep(3)
        self.counter = 0
        self.pb['maximum'] = len(self.lyricsfinder(self.lyricsget))
        for row in self.lyricsfinder(self.lyricsget):
            for keys in row:
                Autoplay.autoplay(keys, t_pause, t_single, t_combo)
            self.counter += 1
            self.proIn()
            self.progress(self.counter)
        time.sleep(0.5)
        self.bar.config(text='End')

#Decode GUI picture
def pic():
    image = open('icon.gif', 'wb')
    image.write(base64.b64decode(WindsongLyre_gif))
    image.close()

#Start GUI
def GUI_Start():
    window = tk.Tk()
    pic()
    profile = MY_GUI(window)
    profile.set_window()
    os.remove('icon.gif')
    window.mainloop()

if __name__ == '__main__':
    GUI_Start()
