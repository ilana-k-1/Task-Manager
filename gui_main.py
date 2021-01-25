from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock

import list_and_card_def as List
import list_support

class Card_graphics(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class list_graphics(BoxLayout):
    #initialize and delay, maybe pass data to attribute
    cards = ObjectProperty([])
    view = ObjectProperty(None)
    title = StringProperty('')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.view.data = [{'text':str(x)} for x in range(5)]
        Clock.schedule_once(self.delayed_init,0)

    def delayed_init(self, arg):
        self.view.data = [{'text': card.text} for card in self.cards]



class Layout_of_lists(BoxLayout):
    view = ObjectProperty(None)
    def __init__(self, list_array, **kwargs):
        super().__init__(**kwargs)
        self.view.data = [{'title':list.title, 'cards':list.cards} for list in list_array]

    pass

class MainApp(App):
    def build(self):
        list_array = list_support.get_all_lists()
        print(list_array)
        lists = Layout_of_lists(list_array)
        # lists = list_graphics()
        return lists

if __name__ == "__main__":
    MainApp().run()
