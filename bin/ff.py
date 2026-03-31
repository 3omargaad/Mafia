from kivy.core.audio import SoundLoader
from kivy import Config
import time

Config.set('kivy', 'audio', 'ffpyplayer')
sound = SoundLoader.load('assets/audio/preset/common/test.ogg')
print('loaded', bool(sound))
if sound:
    sound.play()
    time.sleep(2)
    print('state', sound.state)
