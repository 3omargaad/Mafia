from plyer import vibrator


def vibrate():
    try:
        vibrator.vibrate()
    except NotImplementedError:
        print("Vibrator not implemented on device.")
