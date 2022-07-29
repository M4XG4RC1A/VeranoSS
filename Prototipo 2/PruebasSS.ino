#include <FastLED.h>

#define NUM_LEDS 64
#define DATA_PIN 9

#define BRIGHTNESS  30

CRGB leds[NUM_LEDS];

int ypos = 0;
int xpos = 0;

int yleds[8] = {0,1,2,3,4,5,6,7};
int xleds[8] = {0,8,16,24,32,40,48,56};

//Define Colors
#define A 0xFFFF00
#define O 0x7FFF00
#define W 0xFFFFFF
#define P 0x00FF80
#define N 0x000000
#define B 0x0000FF
#define G 0xFF0000

String Mode = "Write";
int Game = 0;

/*
unsigned long Design[64] = {A,A,O,O,O,O,A,A,\
          A,W,O,O,O,O,W,A,\
          O,A,A,A,A,A,A,O,\
          O,A,N,A,A,N,A,O,\
          O,A,N,A,A,N,A,O,\
          O,A,W,P,P,W,A,O,\
          N,A,W,W,W,W,A,N,\
          N,N,O,O,O,O,N,N};
*/
unsigned long DesignBase[64] = {N,N,N,N,N,N,N,N,\
          N,N,N,N,N,N,N,N,\
          N,N,B,B,B,B,N,N,\
          N,N,B,N,N,B,N,N,\
          N,N,B,N,N,B,N,N,\
          N,N,B,B,B,B,N,N,\
          N,N,N,N,N,N,N,N,\
          N,N,N,N,N,N,N,N};
          
unsigned long DesignMap[64] = {N,N,N,N,N,N,N,N,\
          N,N,N,N,N,N,N,N,\
          N,N,B,B,B,B,N,N,\
          N,N,B,B,B,B,N,N,\
          N,N,B,B,B,B,N,N,\
          N,N,B,B,B,B,N,N,\
          N,N,N,N,N,N,N,N,\
          N,N,N,N,N,N,N,N};

unsigned long Design[64] = {N,N,N,N,N,N,N,N,\
          N,N,N,N,N,N,N,N,\
          N,N,B,B,B,B,N,N,\
          N,N,B,N,N,B,N,N,\
          N,N,B,N,N,B,N,N,\
          N,N,B,B,B,B,N,N,\
          N,N,N,N,N,N,N,N,\
          N,N,N,N,N,N,N,N};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Bienvenido");
  Serial.println("Presiona el boton blanco para iniciar el juego");
  Serial.println("");
  Serial.println("");

  FastLED.addLeds<WS2812B, DATA_PIN>(leds, NUM_LEDS);
  FastLED.setBrightness(BRIGHTNESS);

  pinMode(2,INPUT_PULLUP);
  pinMode(3,INPUT_PULLUP);
  pinMode(4,INPUT_PULLUP);
  pinMode(5,INPUT_PULLUP);
  
  line(xpos,ypos,0x00FF00);
}

void loop() {
  //Code
  int xVal = analogRead(2);
  int yVal = analogRead(3);

  //Start Game
  if(!digitalRead(2)){
    if(Game == 0){
      Serial.println("Starting Game");
      Game = 1;
      delay(1000);
      array2leds(DesignBase);
      line(xpos,ypos,0x00FF00);
    }else{
      array2leds(Design);
      delay(500);
      line(xpos,ypos,0x00FF00);
      Serial.println("Game Started");
    }
  }

  //Change Mode
  if(!digitalRead(3)){
    if(Game == 0){
      Serial.println("No Game");
    }else{
      Mode = Mode=="Write" ? "Erase" : "Write";
      Serial.println("Mode: "+Mode);
      delay(500);
    }
  }

  //End Game
  if(!digitalRead(4)){
    if(Game == 0){
      Serial.println("No Game");
    }else{
      Serial.println("");
      Serial.println("");
      Serial.println("");
      Serial.println("Game End");
      unsigned long color = 0xFFFFFF;
  
      float correct = 0;
      float incorrect = 0;
      float total = 0;
      float original = 0;
      
      for (int i=0; i<64; i++){
        if(DesignMap[i]==B){
          correct = Design[i]==G ? correct+1 : correct;
          original++;
        }else{
          incorrect = Design[i]==G ? incorrect+1 : incorrect;
        }
      }
  
      total = correct-incorrect;
  
      blackout();

      Serial.println(original);
      float per1 = correct/original;
      Serial.println(per1);
      
      Serial.print("Correct: ");
      Serial.print(int(correct));
      Serial.print(" (");
      Serial.print(per1*100);
      Serial.println("%)");
      Serial.print("Incorrect: ");
      Serial.println(int(incorrect));
      Serial.print("Total: ");
      Serial.print(int(total));
      Serial.print(" (");
      Serial.print(total/original*100);
      Serial.println("%)");
  
      if(total/original*100 > 50){
        color = 0xFF0000;
      }else{
        color = 0x00FF00;
      }
      
      for (int i=0; i<64; i++){
        leds[i] = color;
      }
      FastLED.show();
      delay(10000);

      blackout();
      ypos = 0;
      xpos = 0;
      Game = 0;
      
      for (int i=0; i<64; i++){
        Design[i] = DesignBase[i];
      }
      
      line(xpos,ypos,0x00FF00);
    }
  }

  if(!digitalRead(5)){
    if(Game == 0){
      Serial.println("No Game");
    }else{
      if(Mode=="Write"){
        Design[xpos+ypos*8] = G;
        leds[xpos+ypos*8] = G;
        FastLED.show();
      }else{
        Design[xpos+ypos*8] = DesignBase[xpos+ypos*8];
        leds[xpos+ypos*8] = DesignBase[xpos+ypos*8];
        FastLED.show();
      }
    }
  }
  
  delay(100);
  if (xVal<200){
    if(Game == 1){
      lineMove(xpos,ypos);
    }else{
      line(xpos,ypos,0x000000);
    }
    xpos = xpos<7 ? xpos+1 : xpos;
    line(xpos,ypos,0x00FF00);
    delay(100);
  }else if(xVal>900){
    if(Game == 1){
      lineMove(xpos,ypos);
    }else{
      line(xpos,ypos,0x000000);
    }
    xpos = xpos>0 ? xpos-1 : xpos;
    line(xpos,ypos,0x00FF00);
    delay(100);
  }
  
  if (yVal<200){
    if(Game == 1){
      lineMove(xpos,ypos);
    }else{
      line(xpos,ypos,0x000000);
    }
    ypos = ypos<7 ? ypos+1 : ypos;
    line(xpos,ypos,0x00FF00);
    delay(100);
  }else if(yVal>900){
    if(Game == 1){
      lineMove(xpos,ypos);
    }else{
      line(xpos,ypos,0x000000);
    }
    ypos = ypos>0 ? ypos-1 : ypos;
    line(xpos,ypos,0x00FF00);
    delay(100);
  }
}

void lineMove(int x, int y){
  
  for (int i=0; i<8; i++){
    leds[xleds[i] + 1*x] = Design[xleds[i] + 1*x];
    leds[yleds[i] + 8*y] = Design[yleds[i] + 8*y];
  }
  FastLED.show();
  delay(10);
}

void line(int x, int y, unsigned long color){
  
  for (int i=0; i<8; i++){
    leds[xleds[i] + 1*x] = color;
    leds[yleds[i] + 8*y] = color;
  }
  FastLED.show();
  delay(10);
}

//Convierte un arreglo a matriz led
void array2leds(unsigned long arrayLeds[64]){
  for (int i=0; i<64; i++){
    leds[i] = arrayLeds[i];
  }
  FastLED.show();
  delay(10);
}

void blackout(){
  for(int dot = 0; dot <= NUM_LEDS; dot++){
    leds[dot] = 0x000000;
    FastLED.show();
    delay(30);
  }
}
