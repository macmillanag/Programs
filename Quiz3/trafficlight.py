import time
import guizero
import gpiozero

Button.was_pressed = False

red1 = LED(22)
red2 = LED(4)
green1 = LED(17)
green2 = LED(3)
yellow1 = LED(27)
button = Button(2)

button.when_pressed = walk

def walk(button):
       red1.off()
       red2.off()
       green1.off()
       green2.off()
       yellow1.on()
       sleep(3)
       red1.on()
       red2.on()
       green1.off()
       green2.off()
       yellow1.off()
       
     
if __name__ == '__main__':
    while True:
    red1.on()
    red2.off()
    green1.off()
    green2.on()
    yellow1.off()
    sleep(5)
    red1.off()
    red2.off()
    green1.off()
    green2.off()
    yellow1.on()
    sleep(3)
    red1.off()
    red2.on()
    green1.on()
    green2.off()
    yellow1.off()
    sleep(5)
    

    