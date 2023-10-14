from UI.OptionBox import OptionBox
from UI.Button import Button
from UI.TextBox import TextBox

from UI.config import *

import pygame

class TableUI():

    def __init__(self, x, y, w, h, tableNo, pList, activeGame):
        
        self.updatePlayerList(pList, first = True)
        self.activegame = True
        self.p1Score = 0
        self.p2Score = 0
        self.saveGameShow = False
        
        # Universal elements

        self.TitleText = TextBox(
            x+0.3*w, y+0.07*h, 0.4*w, 0.1*h, TEXT_COLOR,BUTTON_COLOR, pygame.font.SysFont(None, 100),
            "Table " + f"{tableNo:01}"
            )
        
        # Game Elements

        self.p1ScoreText = TextBox(
            x+0.1*w, y+0.4*h, 0.3*w, 0.1*h, TEXT_COLOR,BUTTON_COLOR, pygame.font.SysFont(None, 200),
            "00" 
            )

        self.p2ScoreText = TextBox(
            x+0.6*w, y+0.4*h, 0.3*w, 0.1*h, TEXT_COLOR,BUTTON_COLOR, pygame.font.SysFont(None, 200),
            "00" 
            )
        
        # Player Selectors

        self.player1List = OptionBox(
            x+0.05*w, y+0.2*h, 0.4*w, 0.1*h, BUTTON_COLOR, HIGHLIGHT_COLOR, pygame.font.SysFont(None, 60), 
            self.p1list, 9
            )

        self.player2List = OptionBox(
            x+0.55*w, y+0.2*h, 0.4*w, 0.1*h, BUTTON_COLOR, HIGHLIGHT_COLOR, pygame.font.SysFont(None, 60), 
            self.p2list, 9
            )
        
        # Buttons

        self.subP1Button = Button(
            x+0.1*w, y+0.6*h, 0.14*w, 0.1*h, BUTTON_COLOR, HIGHLIGHT_COLOR, pygame.font.SysFont(None, 30),
            "-"
            )

        self.addP1Button = Button(
            x+0.26*w, y+0.6*h, 0.14*w, 0.1*h, BUTTON_COLOR, HIGHLIGHT_COLOR, pygame.font.SysFont(None, 30),
            "+"
            )

        self.subP2Button = Button(
            x+0.6*w, y+0.6*h, 0.14*w, 0.1*h, BUTTON_COLOR, HIGHLIGHT_COLOR, pygame.font.SysFont(None, 30),
            "-"
            )

        self.addP2Button = Button(
            x+0.76*w, y+0.6*h, 0.14*w, 0.1*h, BUTTON_COLOR, HIGHLIGHT_COLOR, pygame.font.SysFont(None, 30),
            "+"
            )

        
        # Win Elements

        self.winText = TextBox(
            x+0.1*w, y+0.4*h, 0.8*w, 0.1*h, TEXT_COLOR,BUTTON_COLOR, pygame.font.SysFont(None, 128),
            ""
            )

        self.resetTableButton = Button(
            x+0.1*w, y+0.6*h, 0.8*w, 0.1*h, BUTTON_COLOR, HIGHLIGHT_COLOR, pygame.font.SysFont(None, 30),
            "New Game"
            )

        

    def drawGameScreen(self, window):
        self.TitleText.draw(window)

        if self.activegame:
            self.p1ScoreText.draw(window)
            self.p2ScoreText.draw(window)

            self.addP1Button.draw(window)
            self.addP2Button.draw(window)

            self.subP1Button.draw(window)
            self.subP2Button.draw(window)

        self.player2List.draw(window)
        self.player1List.draw(window)


    def updateGameScreen(self, window, event_list):
        self.p1ScoreText.update(event_list)
        self.p2ScoreText.update(event_list)

        self.player1List.update(event_list)
        self.player2List.update(event_list)
        
        returnable = 0
        if self.addP1Button.update(event_list):
            returnable = "p1add"
        if self.addP2Button.update(event_list):
            returnable = "p2add"
        if self.subP1Button.update(event_list):
            returnable = "p1sub"
        if self.subP2Button.update(event_list):
            returnable = "p2sub"

        return returnable

    def drawWinScreen(self, window):
        self.winText.draw(window)
        self.resetTableButton.draw(window)

        self.player2List.draw(window)
        self.player1List.draw(window)

    def updateWinScreen(self, window, event_list):
        self.winText.update(event_list)
    
        if self.p1Score > self.p2Score:
            self.winText.dispText = self.player1List.curSelection() + " Wins " + str(self.p1Score) + " to " + str(self.p2Score)
        else:
            self.winText.dispText = self.player2List.curSelection() + " Wins " + str(self.p2Score) + " to " + str(self.p1Score)
        
        self.player1List.update(event_list)
        self.player2List.update(event_list)

        
        
        if self.resetTableButton.update(event_list):
            return 'reset'
        else:
            return ''


    def updateScores(self, p1score, p2score):
        self.p1Score = p1score
        self.p2Score = p2score
        self.p1ScoreText.dispText = f"{p1score:02}"
        self.p2ScoreText.dispText = f"{p2score:02}"

    def resetoptions(self):
        pass
        
        
    def updatePlayerList(self, pList, first = False):
        self.p1list = pList.copy()
        self.p2list = self.p1list.copy()
        self.p1list.insert(0,"Player 1")
        self.p2list.insert(0, "Player 2")
        
        if not first:
            self.player1List.option_list = self.p1list
            self.player2List.option_list = self.p2list
            
    def saveToFile(self):
        with open('gamesFile.txt','a') as file:
            if self.p1Score > self.p2Score:
                file.write(self.player1List.curSelection() + "," + self.player2List.curSelection() + "," + str(self.p1Score) + "," + str(self.p2Score) + '\n')
            else:
                file.write(self.player2List.curSelection() + "," + self.player1List.curSelection() + "," + str(self.p2Score) + "," + str(self.p1Score) + '\n')
