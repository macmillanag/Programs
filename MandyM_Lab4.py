from gpiozero import LED # from gpiozeroimport module LED
from time import sleep #import sleep module
led =LED(21)

# loop 10 times
for i in range(20):
  led.on() # set the GPIO 21 to high
  sleep(1)  #delay 1 second
  led.off() #set the GPIO 21 to low
  sleep(1) #delay 1 second
print("All done")