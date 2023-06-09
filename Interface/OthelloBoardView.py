import arcade
import os
import time
import sys
import threading

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import Interface.gameover_menu as gm
from IA.AbstractIA import AbstractIA
from Model.OthelloBoardModel import OthelloBoardModel
from Model.Color import Color
from Model.Memory import Memory

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
CELL_LENGTH = SCREEN_HEIGHT / BOARD_HEIGHT - 5 # 75 = SCREEN_HEIGHT / BOARD_HEIGHT - 5

MENU_POS_X = CELL_LENGTH * BOARD_HEIGHT + CELL_LENGTH
MENU_POS_Y = SCREEN_HEIGHT + CELL_LENGTH // 2
MENU_CENTER_X = MENU_POS_X + ((SCREEN_WIDTH - CELL_LENGTH // 2) - MENU_POS_X) // 2
MENU_CENTER_Y = MENU_POS_Y // 2
MENU_WIDTH = 180 #SCREEN_WIDTH - MENU_POS_X - 20
MENU_HEIGHT = SCREEN_HEIGHT - CELL_LENGTH


class OthelloBoardView(arcade.View):

    def __init__(self, ia1: AbstractIA = None, ia2: AbstractIA = None, firstPlayer: AbstractIA = None):
        super().__init__()
        self.othelloBoardModel = OthelloBoardModel()
        self.memory = Memory(self.othelloBoardModel)
        #self.ia = AbstractIA()
        self.ia1 = ia1
        self.ia2 = ia2
        self.firstPlayer = firstPlayer
        self.fisrtTurn = True

    def setIa1(self, ia: AbstractIA):
        self.ia1 = ia

    def setIa2(self, ia: AbstractIA):
        self.ia2 = ia

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        # On dessine la grille
        for row in range(BOARD_HEIGHT):
            for column in range(BOARD_WIDTH):
                x = CELL_LENGTH + column * CELL_LENGTH
                y = CELL_LENGTH + row * CELL_LENGTH
                self.drawCell(x, y)
                self.drawPawn(row, column, x, y)
                self.drawGrid(x, y)

        self.drawValidMoves()
        self.drawMenu()

        #Si l'IA commence la partie, on fait jouer l'IA
        if self.ia1 is not None and self.ia2 is None and self.fisrtTurn:
            if self.firstPlayer is not None:
                t = threading.Thread(target=self.ai_thread, args=(self.ia1,))
                t.start()
                self.fisrtTurn = False

        # On dessine le message de fin de partie
        if self.othelloBoardModel.getGameOver():
            self.drawGameOverMessage()
            

    # Draw empty cells
    def drawCell(self, x: int, y: int):
        arcade.draw_rectangle_filled(x, y, CELL_LENGTH, CELL_LENGTH, (25,123,48))

    # Draw the player's pawns on the board
    def drawPawn(self, row: int, column: int, x: int, y: int):
        if self.othelloBoardModel.getCell(row, column) == Color.BLACK:
            arcade.draw_circle_filled(x, y, 20, arcade.color.BLACK)
        elif self.othelloBoardModel.getCell(row, column) == Color.WHITE:
            arcade.draw_circle_filled(x, y, 20, arcade.color.WHITE)

    # Draw the board's grid
    def drawGrid(self, x: int, y: int):
        arcade.draw_rectangle_outline(x, y, CELL_LENGTH, CELL_LENGTH, arcade.color.BLACK)

    # Draw the current player moves that are playable
    def drawValidMoves(self):
        for row, column in self.othelloBoardModel.getValidMoves():
            # On ne dessine pas les cases valides si on est dans le tour de l'IA
            x = CELL_LENGTH + column * CELL_LENGTH
            y = CELL_LENGTH + row * CELL_LENGTH
            arcade.draw_circle_filled(x, y, 10, arcade.color.RED)

    # Draw the menu at the right of the interface.
    def drawMenu(self):
        arcade.draw_rectangle_filled(MENU_CENTER_X, MENU_CENTER_Y, MENU_WIDTH, MENU_HEIGHT, (127, 127, 127))
        arcade.draw_rectangle_outline(MENU_CENTER_X, MENU_CENTER_Y, MENU_WIDTH, MENU_HEIGHT, arcade.color.BLACK, 2)
        self.drawScore()
        self.drawUndoAndNextButton()

    # Draw the scores of both players
    def drawScore(self):
        xPosBlack = (MENU_POS_X + MENU_WIDTH // 2) - CELL_LENGTH
        xPosWhite = xPosBlack + MENU_WIDTH // 2
        yPos = MENU_POS_Y - (CELL_LENGTH // 2) - CELL_LENGTH // 1.5
        arcade.draw_circle_filled(
            xPosBlack,
            yPos,
            20,
            arcade.color.BLACK
        )
        arcade.draw_text(f"{self.othelloBoardModel.getBlackScore()}", xPosBlack - 10, yPos - CELL_LENGTH // 1.5, arcade.color.BLACK, 16)

        arcade.draw_circle_filled(
            xPosWhite,
            yPos,
            20,
            arcade.color.WHITE
        )
        arcade.draw_text(f"{self.othelloBoardModel.getWhiteScore()}", xPosWhite - 10, yPos - CELL_LENGTH // 1.5, arcade.color.BLACK, 16)

    # Draw Undo and Next button when an IA play VS another IA
    def drawUndoAndNextButton(self):
        # Si la partie désigne 2 IA, on met un bouton pour lancer le mouvement de l'IA et un bouton pour revenir au coup précédent
        # On placera ces deux bouton côte à côte, juste en dessous du score
        if self.ia1 is not None and self.ia2 is not None:
            xPosUndo = (MENU_POS_X + MENU_WIDTH // 2) - CELL_LENGTH
            xPosNext = xPosUndo + MENU_WIDTH // 2
            yPos = MENU_POS_Y - CELL_LENGTH*2.75
            arcade.draw_rectangle_filled(xPosUndo, yPos+5, CELL_LENGTH, CELL_LENGTH//2, arcade.color.WHITE)
            arcade.draw_rectangle_outline(xPosUndo, yPos+5, CELL_LENGTH, CELL_LENGTH//2, arcade.color.BLACK, 2)
            arcade.draw_rectangle_filled(xPosNext, yPos+5, CELL_LENGTH, CELL_LENGTH//2, arcade.color.WHITE)
            arcade.draw_rectangle_outline(xPosNext, yPos+5, CELL_LENGTH, CELL_LENGTH//2, arcade.color.BLACK, 2)
            arcade.draw_text("Undo", xPosUndo, yPos, arcade.color.BLACK, 15, anchor_x="center")
            arcade.draw_text("Next", xPosNext, yPos, arcade.color.BLACK, 15, anchor_x="center")

    # Draw a message when the game is over
    def drawGameOverMessage(self):
        if self.othelloBoardModel.getBlackScore() > self.othelloBoardModel.getWhiteScore():
            arcade.draw_text("Black wins", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, 20, anchor_x="center")
        elif self.othelloBoardModel.getBlackScore() < self.othelloBoardModel.getWhiteScore():
            arcade.draw_text("White wins", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, 20, anchor_x="center")
        else:
            arcade.draw_text("Draw", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, 20, anchor_x="center")
        # On affiche la vue game over
        window = arcade.get_window()
        window.show_view(gm.GameoverMenu(self.othelloBoardModel.getBlackScore(), self.othelloBoardModel.getWhiteScore()))



    # Detect a left click and place a pawn if possible.
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            # On convertit les coordonnées de la souris en coordonnées de la grille
            row = int((y - CELL_LENGTH/2) // CELL_LENGTH)
            column = int((x - CELL_LENGTH/2) // CELL_LENGTH)

            # Si la partie concerne 2 IA, on fait jouer les 2 IA
            if self.ia1 is not None and self.ia2 is not None:
                # Si on clique sur le bouton "Next", on fait jouer l'IA dont c'est le tour
                xPosUndo = (MENU_POS_X + MENU_WIDTH // 2) - CELL_LENGTH
                xPosNext = xPosUndo + MENU_WIDTH // 2
                yPos = MENU_POS_Y - CELL_LENGTH*2.75

                if x > xPosNext-CELL_LENGTH//2 and x < xPosNext+CELL_LENGTH//2 and y > yPos-CELL_LENGTH//3 and y < yPos+CELL_LENGTH//3:
                    if self.othelloBoardModel.getTurn() == Color.BLACK:
                    # On fait jouer l'IA 1 sur son thread
                        print("Next")
                        move = self.ia1.getMove(self.othelloBoardModel)
                        print(move)
                        self.memory.next(move)
                        
                    else:
                    # On fait jouer l'IA 2 sur son thread
                        print("Next")
                        move = self.ia2.getMove(self.othelloBoardModel)
                        print(move)
                        self.memory.next(move)

                # Si on clique sur le bouton "Undo", on annule le dernier coup
                if x > xPosUndo-CELL_LENGTH//2 and x < xPosUndo+CELL_LENGTH//2 and y > yPos-CELL_LENGTH//3 and y < yPos+CELL_LENGTH//3:
                    print("Undo")
                    self.memory.undo()
                    # On redessine complètement la vue

            # On est assuré d'avoir au moins un joueur humain
            elif (row, column) in self.othelloBoardModel.getValidMoves():
                self.othelloBoardModel.setCell(row, column, self.othelloBoardModel.getTurn())
                self.othelloBoardModel.updateBoard(row, column)
                self.othelloBoardModel.updateScores()
                self.othelloBoardModel.switchTurn()
                self.othelloBoardModel.updateValidMoves()
                self.othelloBoardModel.updateGameOver()
                # Si l'IA est activée (n'est pas égale a "None"), elle effectue son coup
                if self.ia1 is not None:
                    if self.firstPlayer is not None:
                        if self.othelloBoardModel.getTurn() == Color.BLACK:
                            t = threading.Thread(target=self.ai_thread, args=(self.ia1,))
                            t.start()
                    if self.firstPlayer is None:
                        if self.othelloBoardModel.getTurn() == Color.WHITE:
                            t = threading.Thread(target=self.ai_thread, args=(self.ia1,))
                            t.start()
            else:
                print("Invalid move")

    def ai_thread(self, ia: AbstractIA):
        time.sleep(0.5)
        # On ajoute un délai pour que l'IA ne joue pas trop vite
        row, column = ia.getMove(boardModel=self.othelloBoardModel)
        self.othelloBoardModel.setCell(row, column, self.othelloBoardModel.getTurn())
        self.othelloBoardModel.updateBoard(row, column)
        self.othelloBoardModel.updateScores()
        # On ajoute un délai pour que l'utilisateur puisse voir le coup de l'IA
        time.sleep(0.5)
        self.othelloBoardModel.switchTurn()
        self.othelloBoardModel.updateValidMoves()
        self.othelloBoardModel.updateGameOver()