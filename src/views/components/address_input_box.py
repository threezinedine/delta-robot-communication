from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class IPInput(TextInput):
    def __init__(self, **kwargs):
        TextInput.__init__(self, **kwargs)
        self.size_hint = (0.2, 1)
        self.multiline = False

    def get_value(self):
        return self.text


class PortInput(IPInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_value(self):
        return int(self.text)


class IPDelimiter(Label):
    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.size_hint = (0.1, 1.)
        self.bold = True
        self.font_size = 25
    
    def get_value(self):
        return self.text


class AddressInputBox(BoxLayout):
    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)

        self.widgets_dict = {
            'ip_input_1': IPInput(text='127'),
            'delimiter_1': IPDelimiter(text='.'),
            'ip_input_2': IPInput(text='0'),
            'delimiter_2': IPDelimiter(text='.'),
            'ip_input_3': IPInput(text='0'),
            'delimiter_3': IPDelimiter(text='.'),
            'ip_input_4': IPInput(text='1'),
            'delimiter_4': IPDelimiter(text=':'),
            'port_input': PortInput(text='1234')

        }

        self.intial()
        self.draw()
        print(self.get_value())

    def intial(self):
        self.orientation = 'horizontal'
        self.size_hint = (1., .05)

    def draw(self):
        for _, widget in self.widgets_dict.items():
            self.add_widget(widget)
        self.add_widget(Label(text=''))

    def get_value(self):
        result = ""
        for widget_id, widget in self.widgets_dict.items():
            if widget_id is not 'delimiter_4' and widget_id is not 'port_input':
                result += widget.get_value()

        return result, self.widgets_dict['port_input'].get_value()
