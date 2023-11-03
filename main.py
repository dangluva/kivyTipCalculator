from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class TipCalculatorApp(App):
    def build(self):
        self.title = "Tip Calculator"

        layout = GridLayout(cols=2, spacing=10, padding=10)

        layout.add_widget(Label(text="Total Bill:"))
        self.bill_input = TextInput(hint_text="Enter total bill", multiline=False)
        layout.add_widget(self.bill_input)

        layout.add_widget(Label(text="Tip Percentage:"))
        self.tip_input = TextInput(hint_text="Enter tip percentage", multiline=False)
        layout.add_widget(self.tip_input)

        layout.add_widget(Label(text="Number of People:"))
        self.split_input = TextInput(hint_text="Enter number of people", multiline=False)
        layout.add_widget(self.split_input)

        calculate_button = Button(text="Calculate")
        calculate_button.bind(on_press=self.calculate_tip)
        layout.add_widget(calculate_button)

        self.result_label = Label()
        layout.add_widget(self.result_label)

        return layout

    def calculate_tip(self, instance):
        try:
            bill = float(self.bill_input.text)
            tip_percentage = float(self.tip_input.text)
            number_of_people = int(self.split_input.text)

            tip_amount = (bill * tip_percentage / 100) / number_of_people
            total_per_person = (bill / number_of_people) + tip_amount

            self.result_label.text = f"Each person should leave a ${tip_amount:.2f} tip, and pay ${total_per_person:.2f} in total."

        except (ValueError, ZeroDivisionError):
            self.result_label.text = "Please enter valid values."


if __name__ == '__main__':
    TipCalculatorApp().run()
