"""
CP1404/CP5632 Practical
Convert miles to km program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CALCULATE_MILE_TO_KM = 1.60934


class ConvertMilesToKmApp(App):
    """Convert miles to km is a Kivy App for converting miles to km."""
    output_label = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres."
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call)."""
        try:
            result = float(value) * CALCULATE_MILE_TO_KM
        except ValueError:
            result = 0

        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value, change):
        """Handle increment when press Up/Down."""
        try:
            miles = int(value) + change
        except ValueError:
            miles = change

        self.root.ids.input_number.text = str(miles)
        self.handle_calculate(str(miles))





ConvertMilesToKmApp().run()
