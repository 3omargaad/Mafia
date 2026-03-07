from pathlib import Path

from glob import glob
from os import remove


def get_path(*parts) -> Path:
    base_dir = Path(__file__).parent.parent  # Main directory
    return str(base_dir.joinpath(*parts))  # Returns file path

    # Build a cross-platform file path relative to the script's directory.
    # This removes the need to know a specific Operating System's file path
    # syntax.


def clearAudioFiles():
    files = glob(str(get_path("assets", "audio", "player_names", "*")))
    for f in files:
        remove(f)
    # Removes all audio files for player names
    # Usage at the end of a game round

# Example usage:
# font_file = get_path("assets", "fonts", "Rye-Regular.ttf")
# audio_file = get_path("assets", "audio", "preset", "welcome.wav")
