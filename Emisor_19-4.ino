#include <SPI.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN

const byte identificacion[6] = "00001";

void setup() 
{
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(identificacion);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();

  Serial.println("Conexion con el emisor exitosa");
}

void loop() 
{
 if (Serial.available() > 0) {
    char command = Serial.read();  // Leer el comando enviado desde la PC
    Serial.println(command);  // Imprimir el comando en el monitor serial
    radio.write(&command, sizeof(command));
  }
}
