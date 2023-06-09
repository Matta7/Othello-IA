#On fera le même genre de menu que dans start_menu.py, mais avec des boutons, réparti en layout avec une seule colonne de la même manière que dans le fichier
#play_menu.py.

# On importe les modules nécessaires
import arcade
import arcade.gui as gui

import os
import sys

import Interface.rules_menu as rm
from Interface.play_menu import PlayMenu

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StartMenu(arcade.View):
    def __init__(self):
      super().__init__()
      self.window = arcade.get_window()
      self.manager = gui.UIManager()
      self.manager.enable()

      arcade.set_background_color(arcade.color.WHITE)

      self.box = gui.UIBoxLayout(vertical=True, space_between=20)

      Game_title = gui.UILabel(text="Othello", font_size=75, text_color=arcade.color.BLACK)
      self.box.add(Game_title)

      Play_button = gui.UIFlatButton(text="Jouer", width=200)
      self.box.add(Play_button)

      Rules_button = gui.UIFlatButton(text="Règles", width=200)
      self.box.add(Rules_button)

      Quit_button = gui.UIFlatButton(text="Quitter", width=200)
      self.box.add(Quit_button)

      Play_button.on_click = self.on_click_Play_button
      Rules_button.on_click = self.on_click_Rules_button
      Quit_button.on_click = self.on_click_Quit_button

      self.manager.add(
          arcade.gui.UIAnchorWidget(
              anchor_x="center_x",
              anchor_y="center_y",
              child=self.box)
      )
    
    # Buttons method.
    def on_click_Play_button(self, event):
        self.window.show_view(PlayMenu())
        self.manager.disable()
    
    def on_click_Rules_button(self, event):
        rm.RulesMenu().run()

    def on_click_Quit_button(self, event):
        self.window.close()

    def on_draw(self):
        self.clear()
        self.manager.draw()

def main():
    window = arcade.Window(800, 600, "Othello")
    start_view = StartMenu()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
