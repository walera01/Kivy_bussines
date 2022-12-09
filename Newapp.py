import time
from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.graphics import Line, Point, RoundedRectangle, Ellipse,Rectangle, Triangle
import datetime
from kivy_gradient import Gradient
from kivy.utils import get_color_from_hex


from matplotlib import pyplot as plt
import os.path
import numpy as np
from kivy.garden.matplotlib import FigureCanvasKivyAgg

from kivy.app import App
import matplotlib as mpl




import json



class Test2(Screen):
    def __init__(self,**kwargs):
        super(Test2, self).__init__(**kwargs)
        self.vector = True
        self.stop = True
    def on_enter(self, *args):
        print(self.ids["three2"].pos[0])
        Clock.schedule_interval(self.move, 1.0 / 60.0)
    def move(self, fps):

        if self.ids['three2'].pos[0] <= -10:
            self.ids['three2'].pos[0] = randint(self.width,self.width+40)
        self.ids['three2'].pos[0] -= 1.5
        # if self.ids['person'].collide_widget(self.ids['three2']):
        #     self.buuff(self.ids['three2'])
        #     return self.stop

    def jump(self):
        if self.vector:
            Clock.schedule_interval(self.up, 1.0 / 60.0)
        else:
            Clock.schedule_interval(self.down, 1.0 / 60.0)

    def up(self, time):
        if self.ids['person'].pos[1] < 350:
            self.ids['person'].pos[1] += 5
        else:
            self.vector = False
            return False
    def down(self, time):
        if self.ids['person'].pos[1] >= 101:
            self.ids['person'].pos[1] -= 5
        else:
            self.vector = True
            return False
    def buuff(self, three):
        self.stop = False
        Clock.schedule_interval(self.fall, 1.0 / 60.0)
    def fall(self,fps):
        self.ids['person'].pos[1] -=5
        if self.ids['person'].pos[1] <= 0:
            print(self.ids['person'].pos, "   ", self.ids['three2'].pos)
            self.stop = True
            return False

class Test1(Screen):
    def on_enter(self, *args):
        plt.close()
        self.ids.year.text = '2022'
        self.ids.layout1.clear_widgets()
        self.enter_year()
    def enter_year(self, values = str(datetime.datetime.now().year)):
        plt.close()

        self.ids.layout1.clear_widgets()
        with open('data.json', 'r') as f:
            templates = json.load(f)
        self.salary = []
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        for i in self.month:
            if templates[values][i][0] != 0:
                self.salary.append(templates[values][i][1]/templates[values][i][0])
            else:
                self.salary.append(templates[values][i][1])
        signal = np.array(self.salary)

        plt.style.use('dark_background')
        plt.bar(self.month, signal, width=0.4, color='green')
        plt.colorbar(mpl.cm.ScalarMappable())
        plt.xlabel('Month')
        plt.ylabel('salary/hour')

        self.ids.layout1.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class Shedule(Screen):
    def on_enter(self, *args):
        plt.close()
        self.ids.year.text = '2022'
        self.ids.layout.clear_widgets()
        self.enter_year()
    def enter_year(self, values = '2022'):

        plt.close()
        self.ids.layout.clear_widgets()
        self.ids.year.text = values
        self.ids.layout.clear_widgets()
        with open('data.json', 'r') as f:
            templates = json.load(f)
        self.salary = []
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        for i in self.month:
            self.salary.append(templates[values][i][1])

        signal = np.array(self.salary)
        print(self.salary)
        plt.style.use('dark_background')
        plt.bar(self.month, self.salary, width=0.4, color='purple')
        plt.colorbar(mpl.cm.ScalarMappable())
        plt.xlabel('Month')
        plt.ylabel('salary')

        self.ids.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class Menu(Screen):
    pass

class Window1(Screen):

    def save(self, year, inp1,inp2,inp3):
        if inp1.text != 'Month' and year.text != 'Year' and inp2 and inp3:
            with open('data.json', 'r') as f:
                file = json.load(f)
            # inp1.text = [int(inp2.text), int(inp3.text)]
            file[year.text][inp1.text] = [float(inp2.text), float(inp3.text)]
            with open('data.json', 'w') as f:
                json.dump(file, f)
            self.ids.Err_mess.text = "Successfull"
            with open('data.json', 'r') as f:
                print(json.load(f))
        else:
            self.ids.Err_mess.text = "False"



    def spinner_clicked(self, values, id=None):
        if id == 'year':
            self.ids.year.text = values
        else:
            self.ids.inp1.text = values


class MyApp(App):
    def build(self):
        if os.path.exists('data.json') == False:
            with open('data.json', 'a') as f:
                year = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031']
                month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
                data = {}
                year_dict = {}
                for m in month:
                    year_dict.update({m: [0, 0]})
                for y in year:
                    data.update({y:year_dict})
                    # data.update({m:[0,0]})
                json.dump(data,f)
        sm = ScreenManager()
        sm.add_widget(Menu(name = "menu"))
        sm.add_widget(Window1(name = "window1"))
        sm.add_widget((Shedule(name = 'shedule')))
        sm.add_widget(Test1(name = "test1"))
        sm.add_widget(Test2(name = "test2"))

        return sm
    def change_screen(self, screen_name):
        self.root.current = screen_name
if __name__ == "__main__":
    MyApp().run()