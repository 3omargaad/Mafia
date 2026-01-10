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


def textToSpeech(text, filename, accent):
    tss = gTTS(text, lang='en', tld=accent)
    return tss.save(get_path("assets", "audio", "player_names", f"{filename}.mp3"))


textToSpeech("the quick brown fox jumps over the lazy dog", "uk", "co.uk")