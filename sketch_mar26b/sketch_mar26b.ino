int state;

//Moteur de droite
int m1_in1 = 2;
int m1_in2 = 3;
int m1_in3 = 4;
int m1_in4 = 5;

//Moteur de gauche
int m2_in1 = 6;
int m2_in2 = 7;
int m2_in3 = 10;
int m2_in4 = 9;

void setup() {
  Serial.begin(9600);
  pinMode(m1_in1, OUTPUT);
  pinMode(m1_in2, OUTPUT);
  pinMode(m1_in3, OUTPUT);
  pinMode(m1_in4, OUTPUT);
  pinMode(m2_in1, OUTPUT);
  pinMode(m2_in2, OUTPUT);
  pinMode(m2_in3, OUTPUT);
  pinMode(m2_in4, OUTPUT);


}
//-----------------------------------------------------------------------// 
void loop() {
  if(Serial.available())
  {  
    state = Serial.read();
  }

  //===============================================================================
  //                          Key Control Command
  //===============================================================================   
         if(state == 5){Stop(); }    
  else if(state == 1){forword(); delay(3000); state=5;}  
  else if(state == 2){backword(); delay(3000); state=5;}  
  else if(state == 3){turnLeft(); delay(3000); state=5;}  
  else if(state == 4){turnRight(); delay(3000); state=5;} 
  else if(state == 6){forword(); delay(3000); backword(); delay(3000); turnLeft(); delay(3000); turnRight(); delay(3000); state=5;}
  /////////////////////////////////////END\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

  delay(80); 
  
} 

void backword(){
digitalWrite(m1_in1, LOW);
digitalWrite(m1_in3 ,HIGH);
digitalWrite(m2_in1, HIGH);
digitalWrite(m2_in3,HIGH);
digitalWrite(m1_in2,HIGH);
digitalWrite(m1_in4,LOW);
digitalWrite(m2_in2,LOW);
digitalWrite(m2_in4,LOW);
}

void forword(){
digitalWrite(m1_in1, HIGH);
digitalWrite(m1_in3, LOW);
digitalWrite(m2_in1, LOW);
digitalWrite(m2_in3, LOW);
digitalWrite(m1_in2, LOW);
digitalWrite(m1_in4, HIGH);
digitalWrite(m2_in2, HIGH);
digitalWrite(m2_in4,HIGH);
}

void turnRight(){
digitalWrite(m1_in1,LOW);
digitalWrite(m1_in3,LOW);
digitalWrite(m2_in1,HIGH);
digitalWrite(m2_in3,HIGH);
digitalWrite(m1_in2,HIGH);
digitalWrite(m1_in4,HIGH);
digitalWrite(m2_in2,LOW);
digitalWrite(m2_in4,LOW);
}

void turnLeft(){
digitalWrite(m1_in1,HIGH);
digitalWrite(m1_in3,HIGH);
digitalWrite(m2_in1,LOW);
digitalWrite(m2_in3,LOW);
digitalWrite(m1_in2,LOW);
digitalWrite(m1_in4,LOW);
digitalWrite(m2_in2,HIGH);
digitalWrite(m2_in4,HIGH);
}
  
void Stop(){
digitalWrite(m1_in1,LOW);
digitalWrite(m1_in3 ,LOW);
digitalWrite(m2_in1,LOW);
digitalWrite(m2_in3,LOW);
digitalWrite(m1_in2,LOW);
digitalWrite(m1_in4,LOW);
digitalWrite(m2_in2,LOW);
digitalWrite(m2_in4,LOW);
}
