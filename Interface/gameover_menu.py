import arcade
import os
import Interface.start_menu as sm
import arcade.gui as gui

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

WIDTH = 800
HEIGHT = 600

class GameoverMenu(arcade.View):

    def __init__(self, black_score: int, white_score: int):
        super().__init__()
        self.black_score = black_score
        self.white_score = white_score

        if self.black_score > self.white_score:
            self.winner = "Black"
        elif self.black_score < self.white_score:
            self.winner = "White"
        else:
            self.winner = "Nobody"

        self.window = arcade.get_window()
        self.manager = gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.WHITE)

        self.box = gui.UIBoxLayout(vertical=False, space_between=20)

        menu_button = gui.UIFlatButton(text="Menu", width=200)
        self.box.add(menu_button)

        quit_button = gui.UIFlatButton(text="Quitter", width=200)
        self.box.add(quit_button)

        menu_button.on_click = self.on_click_menu_button
        quit_button.on_click = self.on_click_quit_button

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=-150,
                child=self.box)
        )

    # Buttons method.
    def on_click_menu_button(self, event):
        self.window.show_view(sm.StartMenu())
        self.manager.disable()

    def on_click_quit_button(self, event):
        self.window.close()

    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        arcade.draw_text("Game Over", WIDTH / 2, HEIGHT / 2 + 200, arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text(f"Black : {self.black_score}", WIDTH / 2, HEIGHT / 2 + 100, arcade.color.BLACK, font_size=25, anchor_x="center")
        arcade.draw_text(f"White : {self.white_score}", WIDTH / 2, HEIGHT / 2, arcade.color.BLACK, font_size=25, anchor_x="center")
        arcade.draw_text(f"{self.winner} wins !", WIDTH / 2, HEIGHT / 2 - 100, arcade.color.BLACK, font_size=25, anchor_x="center")
        self.manager.draw()