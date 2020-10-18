from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

from jnius import autoclass

PythonActivity = autoclass('org.renpy.android.PythonActivity')
activity = PythonActivity.mActivity

Context = autoclass('android.content.Context')
vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)

class EaseofAccess(MDApp):
    def build(self):
        vibrator.vibrate(10000)   

if __name__ == "__main__":
    app = EaseofAccess()
    app.run()