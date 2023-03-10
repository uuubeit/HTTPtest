import requests

from kivy.app import App
from kivy.config import Config

from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def ledOn(self, instance):
        requests.get(f"http://192.168.31.10/ledOn")
        print("send")

    def ledOff(self, instance):
        requests.get(f"http://192.168.31.10/ledOff")
        print("send")

    def build(self):
        bl = BoxLayout(orientation="vertical")
        bl.add_widget(Button(text="On", on_press=self.ledOn))
        bl.add_widget(Button(text="Off", on_press=self.ledOff))

        return bl


if __name__ == "__main__":
    MyApp().run()
