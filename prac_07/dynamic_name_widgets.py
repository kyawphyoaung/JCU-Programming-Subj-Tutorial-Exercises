from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicName(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Kyaw Phyo Aung", "Chaw Ei Phyu", "Sai Aung Myat"]

    def build(self):
        self.title = "Name Lists"
        self.root = Builder.load_file('dynamic_name_widgets.kv')
        self.create_widgets()   
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Button(text=name)
            self.root.ids.names_box.add_widget(temp_button)


DynamicName().run()
