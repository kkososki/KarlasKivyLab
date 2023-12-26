from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from navigation_screen_manager import NavigationScreenManager
from canvas_examples import *

class MyScreenManager(NavigationScreenManager):
    pass

class ThelabApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        

   
ThelabApp().run() 