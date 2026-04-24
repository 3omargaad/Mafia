from jnius import autoclass

def do_vibrate(self):
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Context = autoclass('android.content.Context')
    activity = PythonActivity.mActivity
    vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
    if vibrator.hasVibrator():
        vibrator.vibrate([0, 500, 1000, 500])
    else:
        print("Your device does not have a vibration motor.")