import pygame
import time
import serial
import UI.config as config
from UI.TableUI import TableUI

pygame.init()

nano = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1) # open serial port for smac
plist = ["Jakob","Shantanu","Troy","Matt","Jason"]

tableui = []

for i in range(config.NO_TABLES):
    tableui.append(TableUI(i*config.WINDOW_WIDTH/config.NO_TABLES, 0, 
                    config.WINDOW_WIDTH/config.NO_TABLES, config.WINDOW_HEIGHT, 
                    i+1,
                    plist, False))
                    
# Game Setup
FPS = 60
clock = pygame.time.Clock()

pygame.display.set_caption('FIL PingPong League')
window = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), pygame.FULLSCREEN)

is_running = True

while is_running:
    time_delta = clock.tick(FPS)/1000.0
    
    # Processing
    # This section will be built out later
    event_list = pygame.event.get()
    
    for event in event_list:
        if event.type == pygame.QUIT:
            is_running = False
    
    for i in range(config.NO_TABLES):
        if tableui[i].saveGameShow:
            state = tableui[i].updateWinScreen(window, event_list)
        else:
            state = tableui[i].updateGameScreen(window, event_list)

        if state == 'p1add':
            pass
        elif state == 'p1sub':
            pass
        elif state == 'p2add':
            pass
        elif state == 'p2sub':
            pass
        elif state == 'reset':
            tableui[i].saveToFile()
            tableui[i].saveGameShow = False
            tableui[i].player1List.selected == 0
            tableui[i].player2List.selected == 0
    
    while nano.in_waiting:
         recieved = nano.readline().decode("utf-8")
        
         i = int(recieved[0])-1
         p1Score = int(recieved[1:3])
         p2Score = int(recieved[3:5])
        
         if tableui[i].activegame == True and bool(int(recieved[6])) == False:
             if (p1Score >= 11 or p2Score >= 11) and abs(p1Score - p2Score) >= 2:
                 tableui[i].saveGameShow = True
             else:
                 tableui[i].saveGameShow = False
            
         tableui[i].activegame = bool(int(recieved[6]))
         tableui[i].updateScores(p1Score, p2Score)

    
    # Render elements of the game    
    window.fill(config.BACKGROUND)
    for i in range(config.NO_TABLES):
        if tableui[i].saveGameShow:
            tableui[i].drawWinScreen(window)
        else:
            tableui[i].drawGameScreen(window)
            
    for i in range(1, config.NO_TABLES):
        pygame.draw.line(window, config.LINE_COLOR, (i*config.WINDOW_WIDTH/config.NO_TABLES, 0), (i*config.WINDOW_WIDTH/config.NO_TABLES, config.WINDOW_HEIGHT), 3)
    
    pygame.display.update()
    
    
pygame.quit()
