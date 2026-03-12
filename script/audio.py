from pydub import AudioSegment
from pydub.playback import play
from threading import Thread

from files import get_path


def playAudio(audioFile):
    file = AudioSegment.from_file(file=audioFile, format="wav")
    play(file)


def playAudioInParallel(audioFile):
    thread = Thread(target=playAudio(audioFile))
    thread.start()


UI_CLICK = get_path("assets", "audio", "preset", "common", "ui_click.wav")
UI_ENABLE = get_path("assets", "audio", "preset", "common", "ui_enable.wav")
UI_DISABLE = get_path("assets", "audio", "preset", "common", "ui_disable.wav")
UI_POP = get_path("assets", "audio", "preset", "common", "ui_pop.wav")
