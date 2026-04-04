from files import get_path


def get_sound(name):
    return get_path("assets", "audio", "preset", "uk", name)


RYE = get_path("assets", "fonts", "Rye-Regular.ttf")
ROBOTO = get_path("assets", "fonts", "RobotoSlab-Medium.ttf")

WIN_IMG = get_path("assets", "images", "win_img.png")
LOSE_IMG = get_path("assets", "images", "lose_img.png")

UI_CLICK = get_path("assets", "audio", "preset", "common", "ui_click.ogg")
UI_ENABLE = get_path("assets", "audio", "preset", "common", "ui_enable.ogg")
UI_DISABLE = get_path("assets", "audio", "preset", "common", "ui_disable.ogg")
UI_POP = get_path("assets", "audio", "preset", "common", "ui_pop.ogg")
WIN = get_path("assets", "audio", "preset", "common", "win.ogg")
LOSE = get_path("assets", "audio", "preset", "common", "lose.ogg")

WELCOME = get_sound("welcome.ogg")
INTRO = get_sound("intro.ogg")
NIGHT = get_sound("night.ogg")
MAFIA = get_sound("mafia.ogg")
MAFIA_SLEEP = get_sound("mafia_sleep.ogg")
DOCTOR = get_sound("doctor.ogg")
DOCTOR_SLEEP = get_sound("doctor_sleep.ogg")
DETECTIVE = get_sound("detective.ogg")
DETECTIVE_SLEEP = get_sound("detective_sleep.ogg")
MORNING = get_sound("morning.ogg")
FORTUNATELY = get_sound("fortunately.ogg")
UNFORTUNATELY = get_sound("unfortunately.ogg")
DISCUSS = get_sound("discuss.ogg")
VOTE = get_sound("vote.ogg")
REVEAL = get_sound("reveal.ogg")
EXECUTION = get_sound("execution.ogg")
GAME_OVER = get_sound("game_over.ogg")
GAME_CONTINUES = get_sound("game_continues.ogg")
