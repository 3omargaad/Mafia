from pathlib import Path
from glob import glob
from os import remove

def get_path(*parts) -> Path:
    """
    Build a cross-platform file path relative to the script's directory.

    Example:
        get_path("assets", "fonts", "myfont.ttf")
    """
    base_dir = Path(__file__).parent.parent  # main directory
    return str(base_dir.joinpath(*parts))

def clearAudioFiles():
    files = glob(str(get_path("assets", "audio", "player_names", "*")))
    for f in files:
        remove(f)

# Example usage:
#font_file = get_path("assets", "fonts", "Rye-Regular.ttf")
#audio_file = get_path("assets", "audio", "preset", "welcome.wav")

#print(font_file)
#print(audio_file)
