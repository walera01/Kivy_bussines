from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Rectangle,Triangle, Line
from kivy.clock import Clock
from kivy.config import Config
from random import randint
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 800)



class Game(Widget):
    def __init__(self,**kwargs):
        super(Game, self).__init__(**kwargs)


    def go(self):
        self.remove_widget(self.ids['go'])
        self.width = 800
        self.top = 800
        self.downv = True  # положение персонажа внизу
        self.click = 0
        Clock.schedule_interval(self.move, 1.0 / 60.0)

    # движение карты
    def move(self,fps):
        person = self.ids["person"]
        stons = [self.ids["stone"],self.ids["stone2"],self.ids["stone3"],self.ids["stone4"],self.ids["stone5"],self.ids["stone6"],self.ids["polka"]]

        for i in stons:
            i.pos[0] -= 5

            if i.pos[0] < -1000:
                i.pos[0] = randint(800,1500)
            if person.collide_widget(i):
                print("11111")
                print(i.pos)
                self.ids['mess'].text = "Провал"
                Clock.schedule_interval(self.die, 1.0 / 60.0)
                self.add_widget(Button(text = "Return", on_press = self.repet))
                return False
        # print(self.ids["stone"].pos,"  ",self.ids["person"].pos) #позиции объектов

    # По нажатию на экран персонаж начинает движение
    def press(self):
        self.click +=1
        if self.downv:
            Clock.schedule_interval(self.up, 1.0 / 60.0)
        else:
            Clock.schedule_interval(self.down, 1.0 / 60.0)

    # движение персонажа вверх
    def up(self, fps):
        if self.ids["person"].pos[1] >= 500:
            return False
        if self.click % 2 == 0:
            return False
        self.downv = False
        if self.ids["person"].rotate <360:
            self.ids["person"].rotate += 5
        self.ids["person"].pos[1] += 5



    # движение персонажа вниз
    def down(self, fps):
        if self.click % 2 == 1:
            return False
        if self.ids["person"].pos[1] <= 50:
            return False
        if self.ids["person"].rotate >0:
            self.ids["person"].rotate -= 5
        self.downv = True
        self.ids["person"].pos[1] -= 5

    # смерть игрока
    def die(self, fps):
        if self.ids['person'].pos[1]<0:
            return False
        self.ids["person"].pos[1] -= 15
        self.ids["person"].rotate -= 20

    def repet(self):
        self.go()

class ProvercaApp(App):
    def __init__(self,**kwargs):
        super(ProvercaApp, self).__init__(**kwargs)
        self.w = Widget(size_hint=[800, 800])

    def build(self):

        self.w.add_widget(Game())
        return self.w
    #
    # def clear_widget_main(self):
    #     self.w.clear_widgets()



ProvercaApp().run()