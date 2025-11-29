#include <Wire.h>
#define ACL_ADDRESS 0x1D

void setup() {
  Serial.begin(9600);
  Wire.begin();
  
  Wire.beginTransmission(ACL_ADDRESS);
  Wire.write(0x2D);
  Wire.write(0x08);
  Wire.endTransmission();
  
  Serial.println("READY");
}

void loop() {
  float x, y, z;
  if (readSensorData(x, y, z)) {
    Serial.print(x, 4);
    Serial.print(",");
    Serial.print(y, 4);
    Serial.print(",");
    Serial.println(z, 4);
  }
  delay(100);
}

bool readSensorData(float &x, float &y, float &z) {
  Wire.beginTransmission(ACL_ADDRESS);
  Wire.write(0x32);
  if (Wire.endTransmission() != 0) return false;
  
  Wire.requestFrom(ACL_ADDRESS, 6);
  if (Wire.available() == 6) {
    byte x0 = Wire.read(), x1 = Wire.read();
    byte y0 = Wire.read(), y1 = Wire.read();
    byte z0 = Wire.read(), z1 = Wire.read();
    
    int16_t x_raw = (x1 << 8) | x0;
    int16_t y_raw = (y1 << 8) | y0;
    int16_t z_raw = (z1 << 8) | z0;
    
    x = x_raw / 256.0;
    y = y_raw / 256.0;
    z = z_raw / 256.0;
    
    return true;
  }
  return false;
}
