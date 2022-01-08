const int led = 13;
const int sensorPin = 2;
int i=0;
void setup() 
{
 // put your setup code here, to run once:
 Serial.begin(115200);
 pinMode(sensorPin, INPUT);
 pinMode(led, OUTPUT);
for(i=0;i<=60;i++)
{
digitalWrite(led, HIGH);
delay(500);
digitalWrite(led,LOW);
delay(500); 
}
}
void loop() 
{
 // put your main code here, to run repeatedly:
 if(digitalRead(sensorPin) == HIGH)
 {
 digitalWrite(led, HIGH);
 Serial.print(1);
 delay(1000);
 }else 
 {
 digitalWrite(led, LOW);
 //Serial.print(0);
 }
}
