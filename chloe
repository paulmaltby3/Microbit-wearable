from microbit import *
import random

ChloeQ = ["Do you like coding?", "What is your favourite type of food?", "What is your name?", "What is your favourite colour?", "Who do you love the most?", "What is the name of the band that sang Mama Mia", "Where were you born?", "Who sang Lush Life?", "Where are the toilets?", "What is 3 + 4 = ?", " Who lives in a pineapple under the sea?", "Quelle age a tu?"]


while True:
    if button_a.is_pressed():
        display.scroll('Hello my name is Chloe and I come from France')
        display.show(Image.HEART)
        sleep(2000)
       
    elif button_b.is_pressed():
        #display.scroll('I have a vaiety of diferent questions i would like to ask you. Would you like to see them?')
        display.scroll(random.choice(ChloeQ))
    else:
        display.show(Image.HAPPY)
        if accelerometer.was_gesture("shake"):
             display.show(Image.SURPRISED)
             sleep(3000)
