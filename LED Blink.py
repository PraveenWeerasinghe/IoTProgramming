import machine
from machine import Pin
from machine import ADC
import time

LED = Pin(2, Pin.OUT)
adc = Pin(36, Pin.IN)
sensor=ADC(adc)

while True:
   print("Welcome")
   val=sensor.read()
   print(val)
   time.sleep(1)
   LED.value(1)
   print(LED.value())
   time.sleep(2)
   LED.value(0)
   print(LED.value())
   time.sleep(1)
   time.sleep(2)
   
   
   
   
 
    
    

