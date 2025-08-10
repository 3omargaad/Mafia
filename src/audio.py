import tempfile
import os
import subprocess

temp_dir = "C:/Mafia/temp"
os.makedirs(temp_dir, exist_ok=True)
tempfile.tempdir = temp_dir

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play 
from pathlib import Path


def convertToWav(inputFile):
    #audio = AudioSegment.from_mp3(inputFile)
    #audio.export("MAFIA", format="wav")

    subprocess.call(['ffmpeg', '-i', f'{inputFile}_tts.mp3', f'{inputFile}_tts.wav'])



def playAudio(audioFile):
    file = AudioSegment.from_file(file = audioFile, format = "wav")
    play(file)
    


def textToSpeech(text, filename):
    tss = gTTS(text, lang='en', tld="co.uk")
    return tss.save(str(Path(f'assets\\plrNames\\{filename}.mp3')))

# Module Functions

WELCOME = str(Path("assets\\audio\\welcome.wav"))
INTRO = str(Path("assets\\audio\\intro.wav"))
POP = str(Path("assets\\audio\\pop.wav"))
MORNING = str(Path("assets\\audio\\morning.wav"))
GOODNIGHT = str(Path("assets\\audio\\goodnight.wav"))
GOODMORNING = str(Path("assets\\audio\\goodmorning.wav"))
ANNOUNCEMENT = str(Path("assets\\audio\\announcement.wav"))
DISCUSS = str(Path("assets\\audio\\discuss.wav"))
VOTE = str(Path("assets\\audio\\vote.wav"))
EXECUTION = str(Path("assets\\audio\\execution.wav"))
GAMECONTINUES = str(Path("assets\\audio\\gamecontinues.wav"))
GAMEOVER = str(Path("assets\\audio\\gameover.wav"))

MAFIA = str(Path("assets\\audio\\mafia.wav"))
MAFIA_SLEEP = str(Path("assets\\audio\\mafia_sleep.wav"))

DOCTOR = str(Path("assets\\audio\\doctor.wav"))
DOCTOR_SLEEP = str(Path("assets\\audio\\doctor_sleep.wav"))

DETECTIVE = str(Path("assets\\audio\\detective.wav"))
DETECTIVE_SLEEP = str(Path("assets\\audio\\detective_sleep.wav"))
# Audio Constants
