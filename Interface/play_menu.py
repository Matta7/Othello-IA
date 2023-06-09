import arcade
import arcade.gui as gui

import os
import sys
from Interface.OthelloBoardView import OthelloBoardView
from Interface.ia_choice_menu import IAMenu

from IA import heuristic
from IA import aStar as aS


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PlayMenu(arcade.View):

    def __init__(self):
        super().__init__()
        self.window = arcade.get_window()
        self.manager = gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.WHITE)

        self.box = gui.UIBoxLayout(vertical=False, space_between=20)

        PvP_button = gui.UIFlatButton(text="Joueur contre Joueur", width=180)
        self.box.add(PvP_button)

        PvIA_button = gui.UIFlatButton(text="Joueur contre IA", width=180)
        self.box.add(PvIA_button)

        IAvIA_button = gui.UIFlatButton(text="IA contre IA", width=180)
        self.box.add(IAvIA_button)

        Test_button = gui.UIFlatButton(text="A*", width=180)
        self.box.add(Test_button)

        PvP_button.on_click = self.on_click_PvP_button
        PvIA_button.on_click = self.on_click_PvIA_button
        IAvIA_button.on_click = self.on_click_IAvIA_button
        Test_button.on_click = self.on_click_Test_button

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
    def on_click_PvP_button(self, event):
        self.window.show_view(OthelloBoardView())
        self.manager.disable()

    def on_click_PvIA_button(self, event):
        self.window.show_view(IAMenu())
        self.manager.disable()

    def on_click_IAvIA_button(self, event):
        self.window.show_view(IAMenu(IAvIA=True))
        self.manager.disable()

    def on_click_Test_button(self, event):
        ia1 = aS.AStar(p = 3, h = heuristic.mobility)
        ia2 = aS.AStar(p = 3, h = heuristic.occupation)
        self.window.show_view(OthelloBoardView(ia1, ia2, firstPlayer = ia1))
        self.manager.disable()

    def on_draw(self):
        self.clear()
        self.manager.draw()