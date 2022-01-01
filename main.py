# Import kyvi app and label, from uix
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text='Tech with Tim')

###
if __name__=="__main__":
    MyApp().run()