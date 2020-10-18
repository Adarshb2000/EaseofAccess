from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from jnius import autoclass

notification_reader = autoclass('getActiveNotifications')


class EaseofAccess(MDApp):
    def build(self):
        return MDLabel(text="Hello World")

if __name__ == "__main__":
    app = EaseofAccess()
    app.run()