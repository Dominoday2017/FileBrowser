import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class WindowElements(Widget):
    btn = ObjectProperty(None)

    def btn_touch_up(self):
        print('Touch Up')
        from subprocess import Popen, PIPE
        process = Popen(['python3', 'path_window.py'], stdout=PIPE, stderr=PIPE)


class WindowApp(App):
    def build(self):
        return WindowElements()


WindowApp().run()
