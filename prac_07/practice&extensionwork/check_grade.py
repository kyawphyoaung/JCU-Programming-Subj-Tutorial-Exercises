from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class CheckGrade(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Check Grade Program V1.0"
        self.root = Builder.load_file('check_grade.kv')
        return self.root

    def clear(self):
        self.root.ids.input_mark.text = ""

    def checkgrade(self):
        mark = self.valid_mark()
        if (mark >= 85 and mark <= 100):
            grade = "Pass with High Distinction"
        elif (mark >= 75 and mark < 85):
            grade = "Pass with Distinction"
        elif (mark >= 65 and mark < 75):
            grade = "Pass with Credit"
        elif (mark >= 50 and mark < 65):
            grade = "Pass"
        elif (mark < 50):
            grade = "Fail"
        else:
            grade = "Wrong Mark"
        return grade

    def handle_check(self):
        grade = self.checkgrade()
        self.root.ids.output_label.text = str(grade)

    def valid_mark(self):
        try:
            mark = int(self.root.ids.input_mark.text)
        except ValueError:
            self.root.ids.output_label.text = "Wrong Input"
        return mark


CheckGrade().run()
