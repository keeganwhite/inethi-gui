from kivy.app import App
from kivy.uix.label import Label


class InethiApp(App):
    def build(self):
        return Label(text="iNethi Installer")


if __name__ == "__main__":
    InethiApp().run()
