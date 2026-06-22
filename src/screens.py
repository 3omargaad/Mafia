from gui.python_gui.start_screen import StartScreen
from gui.python_gui.tutorial_screen import TutorialScreen
from gui.python_gui.setup_screen import SetupScreen
from gui.python_gui.player_screen import PlayerScreen
from gui.python_gui.role_screen import RoleScreen
from gui.python_gui.game_screen import GameScreen
from gui.python_gui.end_screen import EndScreen

from screen_manager import sm


def setup_screens():
    sm.add_widget(StartScreen(name='start'))
    sm.add_widget(TutorialScreen(name='tutorial'))
    sm.add_widget(PlayerScreen(name='player'))
    sm.add_widget(RoleScreen(name='role'))
    sm.add_widget(GameScreen(name='game'))
    sm.add_widget(EndScreen(name='end'))
    sm.add_widget(SetupScreen(name='setup'))

# Sets up the screens for app.py

