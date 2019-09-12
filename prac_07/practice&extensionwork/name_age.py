from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicName(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names_ages = {"Kyaw Phyo Aung": "20", "Chaw Ei Phyu": "21", "Sai Aung Myat": "21"}

    def build(self):
        self.title = "Name Lists"
        self.root = Builder.load_file('name_age.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names_ages:
            temp_button = Button(text=name, id=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.names_box.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.id
        self.status_text = "{}'s age is {}".format(name, self.names_ages[name])


DynamicName().run()
