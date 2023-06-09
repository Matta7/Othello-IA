import arcade
import arcade.gui as gui

import os
import sys
from Interface.OthelloBoardView import OthelloBoardView
from Model.Color import Color

from IA import easyIA as eIA
from IA import mediumIA as mIA
from IA import hardIA as hIA
from IA import veryHardIA as vhIA


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DifficultyMenu(arcade.View):
    def __init__(self, firstPlayer: Color = Color.BLACK):
        super().__init__()
        
        self.startingPlayer = firstPlayer

        self.window = arcade.get_window()
        self.manager = gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.WHITE)

        self.box = gui.UIBoxLayout(vertical=False, space_between=20)

        easy_button = gui.UIFlatButton(text="Facile", width=200)
        self.box.add(easy_button)

        medium_button = gui.UIFlatButton(text="Moyen", width=200)
        self.box.add(medium_button)

        hard_button = gui.UIFlatButton(text="Difficile", width=200)
        self.box.add(hard_button)

        vhard_button = gui.UIFlatButton(text="Très difficile", width=200)
        self.box.add(vhard_button)

        easy_button.on_click = self.on_click_easy_button
        medium_button.on_click = self.on_click_medium_button
        hard_button.on_click = self.on_click_hard_button
        vhard_button.on_click = self.on_click_vhard_button

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.box)
        )

    # Buttons method.
    # Easy IA
    def on_click_easy_button(self, event):
        self.window.show_view(OthelloBoardView(ia1=eIA.EasyIA(), firstPlayer=self.startingPlayer))
        self.manager.disable()
      
    # Medium IA
    def on_click_medium_button(self, event):
        self.window.show_view(OthelloBoardView(ia1=mIA.MediumIA(), firstPlayer=self.startingPlayer))
        self.manager.disable()
    
    # Hard IA
    def on_click_hard_button(self, event):
        self.window.show_view(OthelloBoardView(ia1=hIA.HardIA(), firstPlayer=self.startingPlayer))
        self.manager.disable()

    # Very hard IA
    def on_click_vhard_button(self, event):
        self.window.show_view(OthelloBoardView(ia1=vhIA.VeryHardIA(), firstPlayer=self.startingPlayer))
        self.manager.disable()
    
    def on_draw(self):
        self.clear()
        self.manager.draw()



