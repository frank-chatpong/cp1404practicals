from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic labels creation."""
    status_text = StringProperty()

    def __init__(self):
        """Construct main app."""
        super().__init__()
        self.names = ["Chatpong", "Henry", "Frank", "James", "Edward"]

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

