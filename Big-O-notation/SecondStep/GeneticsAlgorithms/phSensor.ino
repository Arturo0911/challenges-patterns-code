
//=========================================================================
const int AnalogInpin = A1; //0 -- 1023 sensor de PH
//=========================================================================
int buf[10], temp; // pH 


void setup() {

  Serial.begin(9600);
}
//=========================================================================

void loop() 
{
  int Arturin = 0;

  while (Arturin < 6)
  {
    // Serial.println(AnalogInpin);
    //Serial.println("VICTORIA");
    
    if (AnalogInpin >= 15)
      {
        Serial.println("Sensor pH desconectado ");
      }
    else
      {
        for(int i = 0; i<10; i++)
        {
          buf[i] = analogRead(AnalogInpin);
          delay(10);
        }
        for(int i = 0; i<9; i++)
        {
          for(int j =i+1;j<10;j++)
          {
            if (buf[i] > buf[j])
            {
              temp = buf[i];
              buf[i] = buf[j];
              buf[j] = temp;
            }
          }
        }
        avgValue = 0;
        for (int i=2;i<8;i++)
        avgValue +=buf[i];
        
        float pHVol = (float)avgValue*5.0/1024/6;
        float pHValue = -5.70* pHVol + 21.34;

      
        //Serial.println("- NIVEL DE pH: ");
        Serial.println (pHValue);
    
        Arturin = Arturin + 1;
    
        delay(5000);  // AQUIESPERA 5 SEGUNDOS PARA QUE DE NUEVO EL LOOP SIGA
    }
    
    delay(10000);  

  }
}

