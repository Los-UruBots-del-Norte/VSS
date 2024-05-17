#include <SPI.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN

const byte identificacion[6] = "00001";

// Pins para controlar el puente H
const int IN1 = 2;
const int IN2 = 3;
const int IN3 = 4;
const int IN4 = 5;

void setup() {
  Serial.begin(9600);
  
  radio.begin();
  radio.openReadingPipe(0, identificacion);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  detenerMotores();

  Serial.println("Receptor listo");
}

void loop() {
  if (radio.available()) {
    char command;
    radio.read(&command, sizeof(command));
    
    if (command == 'X') {
      avanzar();
    } else if (command == 'S') {
      detenerMotores();
    }
  }
}

void avanzar() {
  Serial.println("Encendiendo motores hacia adelante");
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void detenerMotores() {
  Serial.println("Deteniendo motores");
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}
