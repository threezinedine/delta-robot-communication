from kivy.app import App
from kivy.uix.label import Label
from .components import AddressInputBox


class CommunicationApp(App):
    def build(self):
        return AddressInputBox()
