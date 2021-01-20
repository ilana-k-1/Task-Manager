from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

import list_and_card_def as List
import list_support

class add_new_card(Button):
    pass

class Card(Button): #this visualizes a single card
    pass

class CardLayout(BoxLayout): #this the cards in a list
    def __init__(self, card_array, **kwargs):
        super().__init__(orientation = 'vertical', **kwargs)
        for card in card_array:
            new_card = Card(text = card.text)
            self.add_widget(new_card)

class ListBox(BoxLayout): #this visualizes a single list
    def __init__(self, list, **kwargs):
        super().__init__(orientation = 'vertical', **kwargs)
        title = Label(text = list.title)
        cards = CardLayout(list.cards)
        button = add_new_card( text = 'add a new card!')
        self.add_widget(title)
        self.add_widget(cards)
        self.add_widget(button)


class ListLayout(GridLayout): #this is the layout for all the lists
    title = StringProperty('')
    def __init__(self, list_array, **kwargs):
        super(ListLayout, self).__init__(cols = len(list_array), **kwargs)
        for list in list_array:
            list_layout = ListBox(list)
            self.add_widget(list_layout)

class MainApp(App):
    def build(self):
        list_array = list_support.get_all_lists()
        lists = ListLayout(list_array)
        return lists

if __name__ == "__main__":
    MainApp().run()
