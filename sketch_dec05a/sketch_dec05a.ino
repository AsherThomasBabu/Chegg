
int RedLed = 12;
int YellowLed = 11;
int GreenLed = 10;
int buzzer = 9;
int smokeA0 = A9;

//threshold value
int warning = 300;
int Risk = 400; 

void setup() {

  pinMode(RedLed, OUTPUT);
pinMode(YellowLed, OUTPUT);
pinMode(GreenLed, OUTPUT);
pinMode(buzzer, OUTPUT);
pinMode(smokeA0, INPUT);
  Serial.begin(9600);
}

void loop() {
  int analogSensor = analogRead(smokeA0);

  Serial.print("Pin A0: ");
  Serial.println(analogSensor);
  // Checks if it has reached the threshold value
  if (analogSensor > Risk)
  {
    digitalWrite(RedLed, HIGH);
    digitalWrite(YellowLed, LOW);
    digitalWrite(GreenLed, LOW);
    tone(buzzer, 5000, 1000);
  }
  else if (analogSensor > warning == analogSensor < Risk)
  { 
    digitalWrite(RedLed, LOW);
    digitalWrite(YellowLed, HIGH);
    digitalWrite(GreenLed, LOW);
    noTone(buzzer);
  }
else
{
digitalWrite(RedLed, LOW);
    digitalWrite(YellowLed, LOW);
    digitalWrite(GreenLed, HIGH);
    noTone(buzzer);
}
  delay(100);
}
