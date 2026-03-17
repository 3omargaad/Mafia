from pydub import AudioSegment
from pydub.playback import play
from threading import Thread

from files import get_path


def play_audio(audioFile):
    file = AudioSegment.from_file(file=audioFile, format="wav")
    play(file)


def play_audio_in_parallel(audioFile):
    thread = Thread(target=play_audio(audioFile))
    thread.start()


def get_sound(sound):
    get_path("assets", "audio", "preset", "common", sound)


UI_CLICK = get_sound("ui_click.wav")
UI_ENABLE = get_sound("ui_enable.wav")
UI_DISABLE = get_sound("ui_disable.wav")
UI_POP = get_sound("ui_pop.wav")

WELCOME = get_path("assets", "audio", "preset", "uk", "welcome.wav")
INTRO = get_path("assets", "audio", "preset", "uk", "intro.wav")
