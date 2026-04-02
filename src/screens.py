from login_screen import LoginScreen
from setup_screen import SetupScreen
from player_screen import PlayerScreen
from role_screen import RoleScreen
from game_screen import GameScreen

from screen_manager import sm


def setup_screens():
    sm.add_widget(LoginScreen(name='login'))
    sm.add_widget(SetupScreen(name='setup'))
    sm.add_widget(PlayerScreen(name='player'))
    sm.add_widget(RoleScreen(name='role'))
    sm.add_widget(GameScreen(name='game'))
