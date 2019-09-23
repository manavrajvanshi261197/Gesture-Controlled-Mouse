
void setup() {
  int baud_rate = 9600;
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  Serial.begin(baud_rate);

}

int x , y;
int delay_time=118;

void loop() {
  x=analogRead(A3);
  y=analogRead(A2);
  
  
  Serial.print(y);
  Serial.print("-");
  Serial.print(x);
 
  Serial.println();
  

 
  delay(delay_time);
}
