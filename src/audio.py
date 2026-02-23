from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

import tempfile
import os
import subprocess

import game_setup
from files import get_path

temp_dir = "C:/Mafia/temp"
os.makedirs(temp_dir, exist_ok=True)
tempfile.tempdir = temp_dir


def convertToWav(inputFile):
    # audio = AudioSegment.from_mp3(inputFile)
    # audio.export("MAFIA", format="wav")

    subprocess.call(
        ['ffmpeg', '-i', f'{inputFile}_tts.mp3', f'{inputFile}_tts.wav']
    )


def playAudio(audioFile):
    file = AudioSegment.from_file(file=audioFile, format="wav")
    play(file)


def textToSpeech(text, filename):
    tss = gTTS(text, lang='en', tld="co.uk")
    return tss.save(get_path(
        "assets",
        "audio",
        "player_names",
        f"{filename}.mp3"
        )
    )
# Module Functions


PRESET = ("assets", "audio", "preset")

WELCOME = get_path(PRESET, game_setup.host_accent, "welcome.wav")
INTRO = get_path(PRESET, game_setup.host_accent, "intro.wav")
POP = get_path(PRESET, game_setup.host_accent, "pop.wav")
MORNING = get_path(PRESET, game_setup.host_accent, "morning.wav")
GOODNIGHT = get_path(PRESET, game_setup.host_accent, "goodnight.wav")
GOODMORNING = get_path(PRESET, game_setup.host_accent, "goodmorning.wav")
ANNOUNCEMENT = get_path(PRESET, game_setup.host_accent, "announcement.wav")
FORTUNATELY = get_path(PRESET, game_setup.host_accent, "fortunately.wav")
DISCUSS = get_path(PRESET, game_setup.host_accent, "discuss.wav")
VOTE = get_path(PRESET, game_setup.host_accent, "vote.wav")
EXECUTION = get_path(PRESET, game_setup.host_accent, "execution.wav")
REVEAL = get_path(PRESET, game_setup.host_accent, "reveal.wav")
GAMECONTINUES = get_path(PRESET, game_setup.host_accent, "gamecontinues.wav")
GAMEOVER = get_path(PRESET, game_setup.host_accent, "gameover.wav")

MAFIA = get_path(PRESET, game_setup.host_accent, "mafia.wav")
MAFIA_SLEEP = get_path(PRESET, game_setup.host_accent, "mafia_sleep.wav")

DOCTOR = get_path(PRESET, game_setup.host_accent, "doctor.wav")
DOCTOR_SLEEP = get_path(PRESET, game_setup.host_accent, "doctor_sleep.wav")

DETECTIVE = get_path(PRESET, game_setup.host_accent, "detective.wav")
DETECTIVE_SLEEP = get_path(
    PRESET,
    game_setup.host_accent,
    "detective_sleep.wav"
)
# Audio Constants
