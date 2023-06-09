import arcade
import arcade.gui as gui

import os
import sys
from Interface.OthelloBoardView import OthelloBoardView
from Interface.first_player_choice_menu import MinMaxMenu

from IA import easyIA as eIA
from IA import mediumIA as mIA
from IA import hardIA as hIA
from IA import veryHardIA as vhIA

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class IAMenu(arcade.View):

    def __init__(self, ia1 = None, IAvIA: bool = False):
        super().__init__()

        self.ia1 = ia1
        self.IAvIA = IAvIA

        self.window = arcade.get_window()
        self.manager = gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.WHITE)

        self.box = gui.UIBoxLayout(vertical=False, space_between=20)

        iaNb = 1
        if ia1 is not None and IAvIA:
            iaNb = 2

        easyIA1_button = gui.UIFlatButton(text="IA" + str(iaNb) + "Facile", width=100)
        self.box.add(easyIA1_button)

        mediumIA1_button = gui.UIFlatButton(text="IA" + str(iaNb) + "Medium", width=100)
        self.box.add(mediumIA1_button)

        hardIA1_button = gui.UIFlatButton(text="IA" + str(iaNb) + "Difficile", width=100)
        self.box.add(hardIA1_button)

        veryHardIA1_button = gui.UIFlatButton(text="IA" + str(iaNb) + "Très difficile", width=100)
        self.box.add(veryHardIA1_button)

        easyIA1_button.on_click = self.on_click_easyIA_button
        mediumIA1_button.on_click = self.on_click_mediumIA_button
        hardIA1_button.on_click = self.on_click_hardIA_button
        veryHardIA1_button.on_click = self.on_click_veryHardIA_button       

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.box)
        )

    # Buttons method.
    def on_click_easyIA_button(self, event):
        if self.IAvIA:
            if self.ia1 is None:
                self.window.show_view(IAMenu(ia1=eIA.EasyIA(), IAvIA=self.IAvIA))
            else:
                self.window.show_view(OthelloBoardView(ia1=self.ia1, ia2=eIA.EasyIA()))
        else:
            self.window.show_view(MinMaxMenu(eIA.EasyIA()))
        self.manager.disable()


    def on_click_mediumIA_button(self, event):
        if self.IAvIA:
            if self.ia1 is None:
                self.window.show_view(IAMenu(ia1=mIA.MediumIA(), IAvIA=self.IAvIA))
            else:
                self.window.show_view(OthelloBoardView(ia1=self.ia1, ia2=mIA.MediumIA()))
        else:
            self.window.show_view(MinMaxMenu(mIA.MediumIA()))
        self.manager.disable()

    def on_click_hardIA_button(self, event):
        if self.IAvIA:
            if self.ia1 is None:
                self.window.show_view(IAMenu(ia1=hIA.HardIA(), IAvIA=self.IAvIA))
            else:
                self.window.show_view(OthelloBoardView(ia1=self.ia1, ia2=hIA.HardIA()))
        else:
            self.window.show_view(MinMaxMenu(hIA.HardIA()))
        self.manager.disable()

    def on_click_veryHardIA_button(self, event):
        if self.IAvIA:
            if self.ia1 is None:
                self.window.show_view(IAMenu(ia1=vhIA.VeryHardIA(), IAvIA=self.IAvIA))
            else:
                self.window.show_view(OthelloBoardView(ia1=self.ia1, ia2=vhIA.VeryHardIA()))
        else:
            self.window.show_view(MinMaxMenu(vhIA.VeryHardIA()))
        self.manager.disable()


    def on_draw(self):
        self.clear()
        self.manager.draw()