from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class TipCalculatorApp(App):
    def build(self):
        self.title = "Tip Calculator"
        self.calculate_pressed = 0  # Track the number of times "Calculate" button was pressed

        layout = GridLayout(cols=2, spacing=10, padding=10)

        layout.add_widget(Label(text="Total Bill:", color='green', bold=True))
        self.bill_input = TextInput(hint_text="Enter total bill", input_type='number', multiline=False, on_touch_down=self.clear_data)
        layout.add_widget(self.bill_input)

        layout.add_widget(Label(text="Tip Percentage:", color='pink', bold=True))
        self.tip_input = TextInput(hint_text="Enter tip percentage", input_type='number', multiline=False)
        layout.add_widget(self.tip_input)

        layout.add_widget(Label(text="Number of People:", color='red', bold=True))
        self.split_input = TextInput(hint_text="Enter number of people", input_type='number', multiline=False)
        layout.add_widget(self.split_input)

        calculate_button = Button(text="Calculate", color='yellow', bold=True, font_size=20, background_normal='', background_color='blue')
        calculate_button.bind(on_press=self.calculate_tip)
        layout.add_widget(calculate_button)

        self.result_label = TextInput(hint_text="Total to pay: ", readonly=True, multiline=True)
        layout.add_widget(self.result_label)

        return layout

    def calculate_tip(self, instance):
        try:
            bill = float(self.bill_input.text)
            tip_percentage = float(self.tip_input.text)
            number_of_people = int(self.split_input.text)

            tip_amount = (bill * tip_percentage / 100) / number_of_people
            total_per_person = (bill / number_of_people) + tip_amount

            result_text = f"Each person should leave a ${tip_amount:.2f} tip, and pay ${total_per_person:.2f} in total."
            self.result_label.text = result_text

        except (ValueError, ZeroDivisionError):
            self.result_label.text = "Please enter valid values."

    def clear_data(self, instance, touch):
        if self.bill_input.collide_point(*touch.pos):
            self.bill_input.text = ''
            self.tip_input.text = ''
            self.split_input.text = ''
            self.result_label.text = ''
            self.calculate_pressed = 0
        else:
            self.calculate_pressed += 1


if __name__ == '__main__':
    TipCalculatorApp().run()
