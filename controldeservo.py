#include <Servo.h>
Servo servo;

void setup() {
  servo.attach(9);  // Conecta el servo al pin 9
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char dato = Serial.read();
    if (dato == '1') {
      servo.write(90);   // Mueve la mano a posición "cerrada"
      delay(1000);
      servo.write(0);    // Vuelve a posición "abierta"
    }
  }
}
