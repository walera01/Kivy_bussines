from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.graphics import Line, Point
from matplotlib import pyplot as plt

import numpy as np
from kivy.garden.matplotlib import FigureCanvasKivyAgg

from kivy.app import App
import matplotlib as mpl




import json

class Test1(Screen):
   def __init__(self,**kwargs):
        super(Test1, self).__init__(**kwargs)


        signal = [0, 1350, 850, 1000,1000, 980, 1100, 1000,1000, 980, 1100, 1000,]
        month = ['Jan','Feb','Mar', 'Apr',  'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        signal = np.array(signal)
        # print(signal)
        # this will plot the signal on graph
        plt.plot(month, signal, color = 'red')


        # setting x label
        plt.xlabel('Month')
        plt.ylabel('salary')

        plt.colorbar(mpl.cm.ScalarMappable())
        plt.grid(True, color = 'green')

        # adding plot to kivy boxlayout
        self.ids.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))




class Shedule(Screen):
    def __init__(self, **kwargs):
        super(Shedule, self).__init__(**kwargs)
        width = self.right-30-self.right*0.01
        print(width)
        with self.canvas:
            for i in range(1, 13):
                Point(points = ((width*0.99/12 + 30)*i*2, self.y +30), pointsize = 5)
            for i in range(1, 13):
                Point(points = (self.x +30, (((self.top*0.8)/12)+30)*i), pointsize = 5)

class Menu(Screen):
    pass

class Window1(Screen):

    def save(self, inp1,inp2,inp3):
        if inp1.text != 'Month':

            with open('data.json', 'a') as f:
                data = {inp1.text:[inp2.text, inp3.text]}
                json.dump(data, f)
            self.ids.Err_mess.text = "Successfull"
        else:
            self.ids.Err_mess.text = "False"

    def spinner_clicked(self, values):
        self.ids.inp1.text = values


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name = "menu"))
        sm.add_widget(Window1(name = "window1"))
        sm.add_widget((Shedule(name = 'shedule')))
        sm.add_widget(Test1(name = "test1"))
        return sm

if __name__ == "__main__":
    MyApp().run()
