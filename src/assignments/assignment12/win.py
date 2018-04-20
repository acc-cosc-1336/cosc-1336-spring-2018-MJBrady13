from tkinter import Tk, Label
from converter import Converter

class Win(Tk):

    def __init__(self):

        self.converter = Converter()
        self.km = 100
        self.miles = self.converter.get_miles_from_km(self.km)
        

        
        Tk.__init__(self, None, None)
        self.geometry("640x480")
        self.label1 = Label(self, text='Km: '+str(self.km))
        self.label2 = Label(self, text='Miles: '+str(self.miles))

        self.label1.pack()
        self.label2.pack()
