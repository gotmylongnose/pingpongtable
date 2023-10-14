#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define CE_PIN   9
#define CSN_PIN 10

RF24 radio(CE_PIN, CSN_PIN); // CE, CSN

const byte address1[5] = "000011";
const byte address2[5] = "000012";

char msg[9];

char tableNo;
int p1Score;
int p2Score;
int server;
bool activeGame;
int timeSinceAction;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  radio.begin();
  radio.setDataRate( RF24_250KBPS );
  radio.openReadingPipe(1, address1);   //Setting the address at which we will receive the data
  radio.openReadingPipe(2, address2);   //Setting the address at which we will receive the data

  radio.startListening();              //This sets the module as receiver
}

void loop() {
  // put your main code here, to run repeatedly:
  if(radio.available()){
    radio.read(&msg, 8);
    // Serial.println(msg[0]);
    // tableNo = atoi(msg[0]);
    // p1Score = atoi(msg[1])*10 + atoi(msg[2]);
    // p2Score = atoi(msg[3])*10 + atoi(msg[4]);
    // server = atoi(msg[5]);
    // activeGame = bool(atoi(msg[6]));
    // timeSinceAction = atoi(msg[7]);

    // Serial.print("Table "); Serial.println(tableNo);
    // Serial.print("P1 Score: "); Serial.println(p1Score);
    // Serial.print("P2 Score: "); Serial.println(p2Score);
    // Serial.print("Current Server: "); Serial.println(server);
    // Serial.print("Active Game: "); Serial.println(activeGame);
    // Serial.print("Time Since Last Action: "); Serial.println(timeSinceAction);

    Serial.println(msg);

    // switch (tableNo) {
    //   case 1:
        
    //     break;
    //   case 2:
    //     // Node 2 sent data, handle it here.
    //     break;
    // }
  }
}
