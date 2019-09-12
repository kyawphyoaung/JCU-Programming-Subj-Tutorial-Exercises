from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class BoxLayoutDemo(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('greet.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear(self):
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
