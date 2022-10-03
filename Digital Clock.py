# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:10:12 2022
@author: Pooja
"""

#Importing library
from tkinter import Label, Tk
import time
#Title and Size of thr digitalClock application.
app_window = Tk()
app_window.title("Digital CLock")
app_window.geometry("420x150")
app_window.resizable(1,1)

#font of time and its color, border width and background color.
text_font =("Boulder", 70, "bold")
background = "#f2e750" 
foreground = "#363529" 
border_Width = 25

#Combination of all and label of clock
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_Width) 
label.grid(row=1, column=1)

#main function of our digital clock - real time.
def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)
    
digital_clock()
app_window.mainloop()


