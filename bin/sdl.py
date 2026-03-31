from kivy.core.audio import SoundLoader
from kivy import Config
import time

Config.set('kivy', 'audio', 'sdl2')
sound = SoundLoader.load('assets/audio/preset/common/ui_enable.wav')
print('loaded', bool(sound))

if sound:
    sound.play()
    time.sleep(2)
    print(sound.state)
