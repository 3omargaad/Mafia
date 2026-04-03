from screen_manager import sm

game_screen = sm.get_screen('game')
dialogue = game_screen.ids["dialogue"]


def display(text, *args):
    dialogue.text = text
