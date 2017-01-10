'''
Created on Dec 28, 2016

@author: user
'''

from Tkinter import Frame, Tk, Label
import random
import time
from Tkconstants import GROOVE

class Window(Frame):

    
    def createWidgets(self):
        
        self.widList = []
        
        for i in range(50):
            self.widList.append([])
            self.widList[i] = Label(self, width = 1, height = self.List[i], bg ='#3B9C9C', borderwidth = 5, relief = GROOVE)
            self.widList[i].grid(row = 0, column = i)
        
        self.master.bind('<Left>', self.slower)
        self.master.bind('<Right>',self.faster)
        
        self.sort()    
    
    def refresh(self):
        
        for i in range(50):
            self.widList[i].configure(bg ='#3B9C9C')
    
    def slower(self, event):
        self.timer += 0.1
    
    def faster(self, event):
        if self.timer > 0.1:
            self.timer -= 0.1
        
    def sort(self):
        
        i, j, a = 1, 2, self.List              
        aux = 0
        
        while i < len(a):
            self.widList[i - 1].configure(bg = '#3B9C0F')
            
            try:
                self.widList[j - 1].configure(bg = '#3B9000')
            except IndexError:
                pass
            
            if a[i-1] < a[i]:      
                i,j = j, j+1                    
            else:
                
                aux = self.List[i]
                self.widList[i].configure(height = self.List[i - 1])
                self.widList[i - 1].configure(height = aux)
                
                a[i-1], a[i] = a[i], a[i-1]
               
                i -= 1
                if i == 0:
                    i,j = j, j+1
            
            self.master.update()
            time.sleep(self.timer)
            self.refresh()
            
    
    def __init__(self, List, master = None):
        Frame.__init__(self, master)
        self.timer = 1
        self.List = List
        self.master = master
        self.grid()
        self.createWidgets()
        
        
root = Tk()

List = random.sample(range(1, 100), 50)

win = Window(List, master = root)
win.mainloop()
root.destroy()