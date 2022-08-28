from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


Window.size = (800, 600)
Window.clearcolor = (1, .5, 0, 1)


class Container(GridLayout):
    pass


class PlanshetApp(App):
    def build(self):

        return Container()



if __name__ == '__main__':
     PlanshetApp().run()
