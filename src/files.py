from pathlib import Path

def get_path(*parts) -> Path:
    """
    Build a cross-platform file path relative to the script's directory.

    Example:
        get_path("assets", "fonts", "myfont.ttf")
    """
    base_dir = Path(__file__).parent.parent  # main directory
    return str(base_dir.joinpath(*parts))

# Example usage:
#font_file = get_path("assets", "fonts", "Rye-Regular.ttf")
#audio_file = get_path("assets", "audio", "preset", "welcome.wav")

#print(font_file)
#print(audio_file)
