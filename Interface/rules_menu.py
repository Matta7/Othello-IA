import arcade
import random
import os
import webbrowser
import Interface.start_menu as sm

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

WIDTH = 800
HEIGHT = 600

#La classe RulesMenu devra afficher la page web contenant les règles du jeu
class RulesMenu():
    def __init__(self):
        super().__init__()
    
    def run(self):
        #La page web contenant les règles du jeu est dans le dossier ressources
        #La page web est nommée rules.html
        print(os.path.realpath("ressources/rules.html"))
        webbrowser.get().open('file://' + os.path.realpath("ressources/rules.html"))