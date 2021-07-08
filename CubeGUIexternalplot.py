# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 15:30:39 2021

@author: 44781
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 20:18:51 2021

@author: TH Simm
"""
#Initialises
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *#ttk, Frame
from ClassPlotCube import *
phi1=0.0
PHI=30.0
phi2=30.0  
        
class FitPeakGUI(Frame):#tk.Tk):
    
    def __init__(self,master=None):#*args,**kwargs):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()#window within frame

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Fit a peak")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)


        
       # creating a button instance
        quitButton = Button(self, text="Quit",font=20,command=self.client_exit)

        # placing the button on my window
        quitButton.pack(side='left')

        
        # creating a button instance
        elseButton = Button(self, text="Something else",font=20,command=self.client_exit)

        # placing the button on my window
        elseButton.pack(side='left')
        
        
 
        
        
        #text box
        self.text_phi1 = Text(self, height=1,width=6,font=14)
        self.text_phi1.pack(side='left')
        self.text_phi1.insert('1.0', 'phi1')
    
        #text box
        self.text_PHI = Text(self, height=1,width=6,font=14)
        self.text_PHI.pack(side='left')
        self.text_PHI.insert('1.0', 'PHI')
        
        #text box
        self.text_phi2 = Text(self, height=1,width=6,font=14)
        self.text_phi2.pack(side='left')
        self.text_phi2.insert('1.0', 'phi2')   
        
        # creating a button instance
                   
        plotButton = Button(self, text="Plot",font=20,command=self.plot_cuba)
        # placing the button on my window
        plotButton.pack(side='left')
        
    #Close window on button press    
    def client_exit(self):
        self.master.destroy()
        
    def get_phi1(self):
        try:
            phi1=float( self.text_phi1.get('1.0','end'))
        except:
            phi1=0.0
        print(phi1)
            
    def plot_cuba(self):
        
        try:
            phi1=float( self.text_phi1.get('1.0','end'))
        except:
            phi1=0.9
        try:
            phi2=float( self.text_phi2.get('1.0','end'))
        except:
            phi2=0.9
        try:
            PHI=float( self.text_PHI.get('1.0','end'))
        except:
            PHI=0.9
        print(phi1,PHI,phi2)
           
        g=gmatrix(phi1,PHI,phi2)     
        XYZ2=rotateG(g)
        # figa=self.fig
        plotCube(XYZ2,self)
        
        
        
root = Tk()
#size of the window
root.geometry("800x60")

app = FitPeakGUI(root)
root.mainloop()