from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play 
from pathlib import Path

import glob
import tempfile
import os
import subprocess

from files import get_path

temp_dir = "C:/Mafia/temp"
os.makedirs(temp_dir, exist_ok=True)
tempfile.tempdir = temp_dir

def convertToWav(inputFile):
    #audio = AudioSegment.from_mp3(inputFile)
    #audio.export("MAFIA", format="wav")

    subprocess.call(['ffmpeg', '-i', f'{inputFile}_tts.mp3', f'{inputFile}_tts.wav'])



def playAudio(audioFile):
    file = AudioSegment.from_file(file = audioFile, format = "wav")
    play(file)
    


def textToSpeech(text, filename):
    tss = gTTS(text, lang='en', tld="co.uk")
    return tss.save(get_path("assets", "audio", "player_names", f"{filename}.mp3"))

# Module Functions

WELCOME = get_path("assets", "audio", "preset", "welcome.wav")
INTRO = get_path("assets", "audio", "preset", "intro.wav")
POP = get_path("assets", "audio", "preset", "pop.wav")
MORNING = get_path("assets", "audio", "preset", "morning.wav")
GOODNIGHT = get_path("assets", "audio", "preset", "goodnight.wav")
GOODMORNING = get_path("assets", "audio", "preset", "goodmorning.wav")
ANNOUNCEMENT = get_path("assets", "audio", "preset", "announcement.wav")
FORTUNATELY = get_path("assets", "audio", "preset", "fortunately.wav")
DISCUSS = get_path("assets", "audio", "preset", "discuss.wav")
VOTE = get_path("assets", "audio", "preset", "vote.wav")
EXECUTION = get_path("assets", "audio", "preset", "execution.wav")
REVEAL = get_path("assets", "audio", "preset", "reveal.wav")
GAMECONTINUES = get_path("assets", "audio", "preset", "gamecontinues.wav")
GAMEOVER = get_path("assets", "audio", "preset", "gameover.wav")

MAFIA = get_path("assets", "audio", "preset", "mafia.wav")
MAFIA_SLEEP = get_path("assets", "audio", "preset", "mafia_sleep.wav")

DOCTOR = get_path("assets", "audio", "preset", "doctor.wav")
DOCTOR_SLEEP = get_path("assets", "audio", "preset", "doctor_sleep.wav")

DETECTIVE = get_path("assets", "audio", "preset", "detective.wav")
DETECTIVE_SLEEP = get_path("assets", "audio", "preset", "detective_sleep.wav")
# Audio Constants
