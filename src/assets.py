from kivy.resources import resource_find
from files import get_path
 
 
def get_sound(name):
    return get_path("assets", "audio", "preset", "uk", name)


# RYE = get_path("assets", "fonts", "RobotoSlab-Medium.ttf")
# ROBOTO = get_path("assets", "fonts", "RobotoSlab-Medium.ttf")

WIN_IMG = resource_find(get_path("assets", "images", "win_img.png"))
LOSE_IMG = resource_find(get_path("assets", "images", "lose_img.png"))

UI_CLICK = resource_find(get_path("assets", "audio", "preset", "common", "ui_click.ogg"))
UI_ENABLE = resource_find(get_path("assets", "audio", "preset", "common", "ui_enable.ogg"))
UI_DISABLE = resource_find(get_path("assets", "audio", "preset", "common", "ui_disable.ogg"))
UI_POP = resource_find(get_path("assets", "audio", "preset", "common", "ui_pop.ogg"))
WIN = resource_find(get_path("assets", "audio", "preset", "common", "win.ogg"))
LOSE = resource_find(get_path("assets", "audio", "preset", "common", "lose.ogg"))

WELCOME = resource_find(get_sound("welcome.ogg"))
INTRO = resource_find(get_sound("intro.ogg"))
NIGHT = resource_find(get_sound("night.ogg"))
MAFIA = resource_find(get_sound("mafia.ogg"))
MAFIA_SLEEP = resource_find(get_sound("mafia_sleep.ogg"))
DOCTOR = resource_find(get_sound("doctor.ogg"))
DOCTOR_SLEEP = resource_find(get_sound("doctor_sleep.ogg"))
DETECTIVE = resource_find(get_sound("detective.ogg"))
DETECTIVE_SLEEP = resource_find(get_sound("detective_sleep.ogg"))
MORNING = resource_find(get_sound("morning.ogg"))
FORTUNATELY = resource_find(get_sound("fortunately.ogg"))
UNFORTUNATELY = resource_find(get_sound("unfortunately.ogg"))
DISCUSS = resource_find(get_sound("discuss.ogg"))
VOTE = resource_find(get_sound("vote.ogg"))
REVEAL = resource_find(get_sound("reveal.ogg"))
EXECUTION = resource_find(get_sound("execution.ogg"))
GAME_OVER = resource_find(get_sound("game_over.ogg"))
GAME_CONTINUES = resource_find(get_sound("game_continues.ogg"))
