from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty
from kivy.core.window import Window

M_TO_KM = 1.60934

class Mile_converter(App):
    message = StringProperty()

    def build(self):
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('miles_converter.kv')
        return self.root

    def handle_press(self, miles):
        miles = self.number_valid()
        kilometer = miles*M_TO_KM
        self.message = str(kilometer)
        return kilometer

    def handle_increment(self, value):
        miles = self.number_valid()+value
        kilometer = self.handle_press(miles)
        self.root.ids.miles_input.text = str(miles)
        self.message = str(kilometer)

    def number_valid(self):
        try:
            number = float(self.root.ids.miles_input.text)
            return number
        except ValueError:
            return 0


Mile_converter().run()
