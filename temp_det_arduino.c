//temperature sensor with Arduino UNO 

float temp; 
int tempPin = 0; 

void setup() { 
    Serial.begin(9600); 
} 

void loop() { 
    temp analogRead(tempPin); 
    temp = temp * 0.48828125; 
    Serial.print("TEMPERATURE = "); 
    Serial.print(temp); // display temperature value 
    Serial.print("C"): 
    Serial.println(); 
    delay(1000); 
} 
