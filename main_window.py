import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

"""
TODO:
-add button Cancel
-add button Serach
-add labels with resutls
-add windows for search results
-change layout for current labels and text inputs
"""

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        """
        Creating label and text input
        :param kwargs:
        """
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 3

        """rows with path"""
        self.add_widget(Label(text="Path: "))  # Add a label widget
        self.pathInput = TextInput(hint_text="example", multiline=False)  # Create a Text input box stored in the name variable
        self.add_widget(self.pathInput)  # Add the text input widget to the GUI

        """rows with key words"""
        self.add_widget(Label(text="Key words"))
        self.kwInput = TextInput(hint_text="example", multiline=True)
        self.add_widget(self.kwInput)

        """rows with number of results"""
        self.add_widget(Label(text="Number of results"))
        self.numberInput = TextInput(hint_text="example", multiline=False)
        self.add_widget(self.numberInput)

class MyApp(App):
    def build(self):
        """building app"""
        return MyGrid()

MyApp().run()