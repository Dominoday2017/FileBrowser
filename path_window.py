import kivy
from kivy.app import App
from kivy.uix.widget import Widget


class SettingWindow(Widget):
    pass


class SecondApp(App):
    def build(self):
        return SettingWindow()


SecondApp().run()
