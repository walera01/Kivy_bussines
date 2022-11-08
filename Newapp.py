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
import os.path
import numpy as np
from kivy.garden.matplotlib import FigureCanvasKivyAgg

from kivy.app import App
import matplotlib as mpl




import json

class Test1(Screen):
   def __init__(self,**kwargs):
        super(Test1, self).__init__(**kwargs)

        with open('data.json', 'r') as f:
            templates = json.load(f)
        salary = []
        month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        for i in month:
            salary.append(templates[i][1])
        month = ['Jan','Feb','Mar', 'Apr',  'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        signal = np.array(salary)
        # print(signal)
        # this will plot the signal on graph
        plt.style.use('dark_background')
        plt.bar(month, signal, width=0.5, color = 'purple')


        # setting x label
        plt.xlabel('Month')
        plt.ylabel('salary')

        plt.colorbar(mpl.cm.ScalarMappable())



        # adding plot to kivy boxlayout
        self.ids.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))




class Shedule(Screen):
    def __init__(self, **kwargs):
        super(Shedule, self).__init__(**kwargs)
    def show(self):
        with open('data.json', 'r') as f:
            templates = json.load(f)
        salary = []
        month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        for i in month:
            salary.append(templates[i][1])

        signal = np.array(salary)
        print(salary)
        plt.style.use('dark_background')
        plt.bar(month, salary, width=0.4, color='purple')


        # setting x label
        plt.xlabel('Month')
        plt.ylabel('salary')

        plt.colorbar(mpl.cm.ScalarMappable())

        # adding plot to kivy boxlayout
        self.ids.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class Menu(Screen):
    pass

class Window1(Screen):

    def save(self, inp1,inp2,inp3):
        if inp1.text != 'Month':
            with open('data.json', 'r') as f:
                file = json.load(f)
            file[inp1.text] = [int(inp2.text), int(inp3.text)]
            with open('data.json', 'w') as f:
                json.dump(file, f)
            self.ids.Err_mess.text = "Successfull"
            with open('data.json', 'r') as f:
                print(json.load(f))
        else:
            self.ids.Err_mess.text = "False"


    def spinner_clicked(self, values):
        self.ids.inp1.text = values


class MyApp(App):
    def build(self):
        if os.path.exists('data.json') == False:
            with open('data.json', 'a') as f:
                month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
                data = {}
                for m in month:
                    data.update({m:[0,0]})
                json.dump(data,f)
        sm = ScreenManager()
        sm.add_widget(Menu(name = "menu"))
        sm.add_widget(Window1(name = "window1"))
        sm.add_widget((Shedule(name = 'shedule')))
        sm.add_widget(Test1(name = "test1"))
        return sm

if __name__ == "__main__":
    MyApp().run()
