from kivy.lang import Builder
# from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy import require
from kivy.animation import Animation
from kivy.graphics import Rectangle
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout
# Imports kivy sub-modules

from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
# Imports kivymd sub-modules

from kivy_gradient import Gradient

from files import get_path
from concurrency import run_concurrent

import audio
import game_setup
import game_logic

require('2.3.1')

Builder.load_file("app.kv")  # Loads kivy file


class BackgroundManager(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.rect = Rectangle(
                size=self.size,
                pos=self.pos,
                texture=Gradient.vertical(
                    get_color_from_hex("000505"),
                    get_color_from_hex("202020"),
                    get_color_from_hex("000505"),
                )
            )
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


class LoginScreen(MDScreen, Screen):
    gradient = Gradient
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")
    press_font = get_path("assets", "fonts", "PressStart2P-Regular.ttf")

    def account(self):
        print("Pressed")
        popup = MDDialog(
            title='Error',
            text="Account creation is currently unavailable."
        )
        popup.open()
    # Creates a popup window to show account creation is unavaiable

    def hover_on(self, widget):
        widget.bold = True

    def hover_off(self, widget):
        widget.bold = False

    def click(self):
        run_concurrent(audio.playAudio, audio.UI_CLICK)


class SetupScreen(MDScreen, Screen):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")
    plr_num = StringProperty("4")
    maf_num = StringProperty("1")
    max_maf = StringProperty("1")

    def hover_on(self, widget):
        widget.bold = True

    def hover_off(self, widget):
        widget.bold = False

    def slide(self):
        run_concurrent(audio.playAudio, audio.UI_POP)

    def toggle(self, widget):
        if widget.active:
            run_concurrent(audio.playAudio, audio.UI_ENABLE)
        else:
            run_concurrent(audio.playAudio, audio.UI_DISABLE)

    def on_plr_slider_value(self, widget):
        self.plr_num = str(int(widget.value))
        game_setup.plr_num = int(widget.value)

        self.max_maf = str((game_setup.plr_num // 2) - 1)  # Sets max mafia val
        print(self.max_maf)

    def on_maf_slider_value(self, widget):
        self.maf_num = str(int(widget.value))
        game_setup.maf_num = int(widget.value)
        print(str(game_setup.maf_num))

    def on_include_doc_switch_active(self, widget):
        game_setup.maf_num = widget.active
        print(str(game_setup.include_doc))

    def on_include_det_switch_active(self, widget):
        game_setup.maf_num = widget.active
        print(str(game_setup.include_det))

    def on_continue(self, widget):
        print(self.ids)
        print(game_setup.plr_num)

    def click(self):
        run_concurrent(audio.playAudio, audio.UI_CLICK)


class PlayerScreen(MDScreen, Screen):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")

    def on_enter(self):
        print(self.ids)
        fadein = Animation(opacity=1)
        for i in range(game_setup.plr_num):
            text_field = self.ids["name" + str(i+1)]
            text_field.disabled = False
            fadein.start(text_field)
            # self.ids["name" + str(i+1)].opacity = 1

    def create_players(self):
        pass

    def on_leave(self):
        for i in range(game_setup.plr_num):
            plr_name = self.ids["name" + str(i+1)].text
            print(plr_name)
            game_logic.create_player(plr_name)
            print(game_setup.players)
        game_logic.assign_roles()

        for plr in game_setup.players:
            print(plr.name + "|" + plr.role)

        for i in range(16):
            self.ids["name" + str(i+1)].disabled = True
            self.ids["name" + str(i+1)].opacity = 0

    def click(self):
        run_concurrent(audio.playAudio, audio.UI_CLICK)


class RoleScreen(MDScreen, Screen):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")

    def on_enter(self):
        player_screen = self.manager.get_screen('player')
        print(game_setup.players)
        for i in range(game_setup.plr_num):
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            n = str(i+1)
            initial = player_screen.ids["name" + n].text[0].lower()
            icon = self.ids["icon" + n]

            self.ids["name" + n].text = player_screen.ids["name" + n].text
            if initial in alphabet:
                icon.icon = "alpha-" + initial + "-circle-outline"
        # for i in range(game_setup.plr_num):
        #     self.ids["name" + str(i+1)].disabled = False

    def show_role(self, card):
        print("Pressed")
        print(card.value)
        close_btn = MDFlatButton(
            text="Finish",
            theme_text_color="Custom",
            text_color=self.theme_cls.primary_color,
        )

        popup = MDDialog(
            title='You are ' + game_setup.players[int(card.value) - 1].role,
            text="[Desc.]. Once this tab closes it won't open again.",
            auto_dismiss=False,
            buttons=[close_btn],

        )

        close_btn.bind(on_release=popup.dismiss)

        popup.open()
        card.disabled = True
    # Creates a popup window to show account creation is unavaiable

    def click(self):
        run_concurrent(audio.playAudio, audio.UI_CLICK)


class GameScreen(MDScreen, Screen):
    rye_font = get_path("assets", "fonts", "Rye-Regular.ttf")

    def click(self):
        run_concurrent(audio.playAudio, audio.UI_CLICK)


class MafiaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = 'Dark'  # Creates red/dark theme
        Window.size = (360, 640)

        root = BackgroundManager()
        sm = ScreenManager()

        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SetupScreen(name='setup'))
        sm.add_widget(PlayerScreen(name='player'))
        sm.add_widget(RoleScreen(name='role'))
        sm.add_widget(GameScreen(name='game'))
        # Sets up kivy screen manager

        root.add_widget(sm)

        return root


MafiaApp().run()
# Runs application GUI
