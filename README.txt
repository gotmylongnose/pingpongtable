This project was created for the unofficial Fives (Feev) Ping Pong League

Before running the Python Host program:

py -m pip install pyserial
py -m pip install pygame

UI/config.py

Setup the right screen resolution and the other colors for the UI
Change the address of the Data reciever to ensure that the arduino can communicate with the python UI.

Run new.py to launch the code.

The code for the arduinos is also linked in the repo. OG_Table_Current is the code for the table. The pins
for the LEDs and buttons can be changed in the code.

The reviever is an arduino with an nrf24l01 module. The code for that is also available.
