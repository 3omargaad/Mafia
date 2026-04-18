# from pydub import AudioSegment
# from pydub.playback import play
from kivy.core.audio import SoundLoader
from time import sleep
# from kivy.app import App

from threading import Lock
from kivy import Config

from concurrency import run_concurrent

Config.set('kivy', 'audio', 'sdl2')

_sound_cache = {}
_cache_lock = Lock()


def get_sound(path):
    with _cache_lock:
        s = _sound_cache.get(path)
        if s is None:
            s = SoundLoader.load(path)
            if s:
                _sound_cache[path] = s
        return s
# Loads sound from cache


def play_audio(path, *args):
    sound = get_sound(path)
    if not sound:
        return False
    # ensure safe restart instead of reloading
    if sound.state == 'play':
        sound.stop()
    sound.play()

    def unload():
        sleep(31)
        sound.unload()
    run_concurrent(unload)
    return True

# def play_audio(file):
#    file = get_sound(file)
#    audio = SoundLoader.load(file)
#    audio.stop()
#    audio.play()
#    # file = AudioSegment.from_file(file=audioFile, format="wav")
#    # play(file)
