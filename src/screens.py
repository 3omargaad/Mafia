from gui.python_gui.login_screen import LoginScreen
from gui.python_gui.setup_screen import SetupScreen
from gui.python_gui.player_screen import PlayerScreen
from gui.python_gui.role_screen import RoleScreen
from gui.python_gui.game_screen import GameScreen
from gui.python_gui.end_screen import EndScreen

from screen_manager import sm


def setup_screens():
    sm.add_widget(LoginScreen(name='login'))
    sm.add_widget(PlayerScreen(name='player'))
    sm.add_widget(RoleScreen(name='role'))
    sm.add_widget(GameScreen(name='game'))
    sm.add_widget(EndScreen(name='end'))
    sm.add_widget(SetupScreen(name='setup'))
