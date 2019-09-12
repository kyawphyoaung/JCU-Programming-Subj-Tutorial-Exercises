from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty
from kivy.core.window import Window

M_TO_KM = 1.60934

class TEMP_converter(App):
    message = StringProperty()

    def build(self):
        Window.size = (500, 200)
        self.title = "Convert Temperature Values"
        self.root = Builder.load_file('temp_converter.kv')
        return self.root

    def to_fahrenheit(self):
        tempature = self.temperature_valid()
        fahrenheit = tempature * 9.0 / 5 + 32
        self.root.ids.output_value.text = str(fahrenheit)
        self.message = str(fahrenheit)

    def to_celsius(self):
        tempature = self.temperature_valid()
        celsius = 5 / 9 * (tempature - 32)
        self.root.ids.output_value.text = str(celsius)
        self.message = str(celsius)

    def temperature_valid(self):
        try:
            temp = float(self.root.ids.input_value.text)
            return temp
        except ValueError:
            return 0


TEMP_converter().run()
