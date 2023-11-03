from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TipCalculatorApp(App):
    def build(self):
        self.title = "Tip Calculator"
        self.bill_input = TextInput(hint_text="Enter total bill", multiline=False)
        self.tip_input = TextInput(hint_text="Enter tip percentage (10, 12, or 15)", multiline=False)
        self.split_input = TextInput(hint_text="Enter number of people", multiline=False)
        self.result_label = Label()

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.bill_input)
        layout.add_widget(self.tip_input)
        layout.add_widget(self.split_input)
        layout.add_widget(self.result_label)

        calculate_button = Button(text="Calculate")
        calculate_button.bind(on_press=self.calculate_tip)
        layout.add_widget(calculate_button)

        return layout

    def calculate_tip(self, instance):
        bill = float(self.bill_input.text)
        amount_of_tip = self.tip_input.text
        number_of_people = int(self.split_input.text)

        if amount_of_tip == "10":
            ten_percent_tip = ((bill * 1.10) - bill) / number_of_people
            tip_per_person = round(ten_percent_tip, 2)
            bill_per_person = (bill / number_of_people) + tip_per_person
            self.result_label.text = f"Each person should leave a {tip_per_person:.2f} $ tip, and pay {bill_per_person:.2f} $ in total."
        elif amount_of_tip == "12":
            twelve_percent_tip = ((bill * 1.12) - bill) / number_of_people
            tip_per_person = round(twelve_percent_tip, 2)
            bill_per_person = (bill / number_of_people) + tip_per_person
            self.result_label.text = f"Each person should leave a {tip_per_person:.2f} $ tip, and pay {bill_per_person:.2f} $ in total."
        else:
            fifteen_percent_tip = ((bill * 1.15) - bill) / number_of_people
            tip_per_person = round(fifteen_percent_tip, 2)
            bill_per_person = (bill / number_of_people) + tip_per_person
            self.result_label.text = f"Each person should leave a {tip_per_person:.2f} $ tip, and pay {bill_per_person:.2f} $ in total."

if __name__ == '__main__':
    TipCalculatorApp().run()
