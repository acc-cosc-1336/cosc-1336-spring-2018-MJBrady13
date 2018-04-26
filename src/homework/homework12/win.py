from tkinter import Tk, Label, Button
from converter import Converter

class Win(Tk):

    def __init__(self):

        Tk.__init__(self, None, None)
                
        self.converter = Converter()
        self.km = 100
        self.miles = self.converter.get_miles_from_km(self.km)
        
        

        self.display_conversion_button = Button(self, text='Display Conversion',\
                                                command=self.display_labels)
        self.display_conversion_button.pack()
        
        self.quit_button = Button(self, text='Quit', command=self.destroy)

        self.quit_button.pack()
        
        
        
        
        


    def display_labels(self):
        self.label1 = Label(self, text='Km: '+str(self.km))
        self.label2 = Label(self, text='Miles: '+str(self.miles))

        self.label1.pack()
        self.label2.pack()

    
