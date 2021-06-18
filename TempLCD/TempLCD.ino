#include <LiquidCrystal.h>

int sensorPin = 0; // Initialising Sensor Pin

const int rs = 10, en = 9, d4 = 8, d5 = 7, d6 = 6, d7 = 5; //Initialising Pins needed for LCD
LiquidCrystal lcd(rs, en, d4, d5, d6, d7); // Calling the lcd from the Library
int reading;      // initalising global variables
float voltage;
float temperatureC;
float reftemp ;


void setup() {
  lcd.begin(16, 2); //starting the lcd
  lcd.setCursor(0, 0);
  lcd.print("NAME: RAHAF ALAMI"); //displaying name and ID
  lcd.setCursor(0, 1);
  lcd.print("ID: 89105");
  delay(2000);  //waiting for 2 seconds before clearing the screen
  lcd.clear();
}

void loop() {
  int reading = analogRead(sensorPin);  //Reading the Value of the Temperature Sensor Used
  float voltage = reading * 5.0;
  voltage /= 1024.0;
  float ftemperatureC = (voltage - 0.5) * 100 ; //Converting the raw voltage into Temperature in Celcius

  if (temperatureC != ftemperatureC) { //Only if there is a change in the value of the temperatre the control is passed to the next step
    if (ftemperatureC < 18.00) {  //According to the given conditions, the conditions are checked and the required text displayed on the LCD
      lcd.clear();
      lcd.setCursor(0, 1);
      lcd.print("It is Cold");
    } else if (ftemperatureC > 30.00) {
      lcd.clear();
      lcd.setCursor(0, 1);
      lcd.print("It is Hot");
    }
    else {
      lcd.clear();
      lcd.setCursor(0, 1);
      lcd.print("It is Normal");
    }

    lcd.setCursor(0, 0);
    lcd.print(ftemperatureC);
    lcd.print(" C");

    temperatureC = ftemperatureC; // Initial Variable being changed to monitior any further change after full iteration of this loop
  }
}
