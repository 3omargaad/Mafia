from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play 
from pathlib import Path
import glob

import tempfile
import os
import subprocess

temp_dir = "C:/Mafia/temp"
os.makedirs(temp_dir, exist_ok=True)
tempfile.tempdir = temp_dir


def clearAudioFiles():
    files = glob.glob('assets\\audio\\player_names\\*')
    for f in files:
        os.remove(f)

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

WELCOME = str(Path("assets\\audio\\preset\\welcome.wav"))
INTRO = str(Path("assets\\audio\\preset\\intro.wav"))
POP = str(Path("assets\\audio\\preset\\pop.wav"))
MORNING = str(Path("assets\\audio\\preset\\morning.wav"))
GOODNIGHT = str(Path("assets\\audio\\preset\\goodnight.wav"))
GOODMORNING = str(Path("assets\\audio\\preset\\goodmorning.wav"))
ANNOUNCEMENT = str(Path("assets\\audio\\preset\\announcement.wav"))
FORTUNATELY = str(Path("assets\\audio\\preset\\fortunately.wav"))
DISCUSS = str(Path("assets\\audio\\preset\\discuss.wav"))
VOTE = str(Path("assets\\audio\\preset\\vote.wav"))
EXECUTION = str(Path("assets\\audio\\preset\\execution.wav"))
REVEAL = str(Path("assets\\audio\\preset\\reveal.wav"))
GAMECONTINUES = str(Path("assets\\audio\\preset\\gamecontinues.wav"))
GAMEOVER = str(Path("assets\\audio\\preset\\gameover.wav"))

MAFIA = str(Path("assets\\audio\\preset\\mafia.wav"))
MAFIA_SLEEP = str(Path("assets\\audio\\preset\\mafia_sleep.wav"))

DOCTOR = str(Path("assets\\audio\\preset\\doctor.wav"))
DOCTOR_SLEEP = str(Path("assets\\audio\\preset\\doctor_sleep.wav"))

DETECTIVE = str(Path("assets\\audio\\preset\\detective.wav"))
DETECTIVE_SLEEP = str(Path("assets\\audio\\preset\\detective_sleep.wav"))
# Audio Constants
