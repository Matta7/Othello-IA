import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

WIDTH = 800
HEIGHT = 600

class TestGame(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_GRAY)
    
    def on_draw(self):
        arcade.start_render()