from kivy.core.audio import SoundLoader
from time import sleep
sound = SoundLoader.load('assets/audio/preset/common/test.ogg')

if sound:
    # print("Sound found at %s" % sound.source)
    # print("Sound is %.3f seconds" % sound.length)
    sleep(2)
    sound.play()
