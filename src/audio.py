from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play 
from pathlib import Path
import files

import glob

import tempfile
import os
import subprocess

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
    return tss.save(str(Path(f'assets\\audio\\player_names\\{filename}.mp3')))

# Module Functions
files.get_path("assets", "audio", "preset", "welcome.wav")
WELCOME = files.get_path("assets", "audio", "preset", "welcome.wav")
INTRO = files.get_path("assets", "audio", "preset", "intro.wav")
POP = files.get_path("assets", "audio", "preset", "pop.wav")
MORNING = files.get_path("assets", "audio", "preset", "morning.wav")
GOODNIGHT = files.get_path("assets", "audio", "preset", "goodnight.wav")
GOODMORNING = files.get_path("assets", "audio", "preset", "goodmorning.wav")
ANNOUNCEMENT = files.get_path("assets", "audio", "preset", "announcement.wav")
FORTUNATELY = files.get_path("assets", "audio", "preset", "fortunately.wav")
DISCUSS = files.get_path("assets", "audio", "preset", "discuss.wav")
VOTE = files.get_path("assets", "audio", "preset", "vote.wav")
EXECUTION = files.get_path("assets", "audio", "preset", "execution.wav")
REVEAL = files.get_path("assets", "audio", "preset", "reveal.wav")
GAMECONTINUES = files.get_path("assets", "audio", "preset", "gamecontinues.wav")
GAMEOVER = files.get_path("assets", "audio", "preset", "gameover.wav")

MAFIA = files.get_path("assets", "audio", "preset", "mafia.wav")
MAFIA_SLEEP = files.get_path("assets", "audio", "preset", "mafia_sleep.wav")

DOCTOR = files.get_path("assets", "audio", "preset", "doctor.wav")
DOCTOR_SLEEP = files.get_path("assets", "audio", "preset", "doctor_sleep.wav")

DETECTIVE = files.get_path("assets", "audio", "preset", "detective.wav")
DETECTIVE_SLEEP = files.get_path("assets", "audio", "preset", "detective_sleep.wav")
# Audio Constants
