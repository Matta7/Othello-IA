import arcade
import arcade.gui as gui

import os
import sys
from Interface.OthelloBoardView import OthelloBoardView
from Interface.difficulty_menu import DifficultyMenu
from Model.Color import Color
from IA.AbstractIA import AbstractIA

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class MinMaxMenu(arcade.View):

    def __init__(self, ia: AbstractIA):
        super().__init__()
        self.window = arcade.get_window()
        self.manager = gui.UIManager()
        self.manager.enable()

        self.ia = ia

        arcade.set_background_color(arcade.color.WHITE)

        self.box = gui.UIBoxLayout(vertical=False, space_between=20)

        max_button = gui.UIFlatButton(text="Vous jouez en premier", width=200)
        self.box.add(max_button)

        min_button = gui.UIFlatButton(text="Vous jouez en second", width=200)
        self.box.add(min_button)

        max_button.on_click = self.on_click_max_button
        min_button.on_click = self.on_click_min_button

        """@PvP_button.event("on_click")
        def on_click_settings(event):
            print("Settings:", event)

        @PvIA_button.event("on_click")
        def on_click_settings(event):
            print("Settings:", event)

        @IAvIA_button.event("on_click")
        def on_click_settings(event):
            print("Settings:", event)"""

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.box)
        )

    # Buttons method.
    def on_click_max_button(self, event):
        self.window.show_view(OthelloBoardView(ia1=self.ia))
        self.manager.disable()

    def on_click_min_button(self, event):
        self.window.show_view(OthelloBoardView(ia1=self.ia, firstPlayer=self.ia))
        self.manager.disable()


    def on_draw(self):
        self.clear()
        self.manager.draw()