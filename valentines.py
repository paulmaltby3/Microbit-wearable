from microbit import *
import random

relationship = ["marry?", "kiss?", "avoid?", "love?"]
names = ["Harry", "Daddy", "Mae", "Eva", "Jack", "Lillie", "Leah", "Ted", "Frankie" ]


while True:
    if button_a.is_pressed():
        display.scroll("Who r u going to")
        display.scroll(random.choice(relationship))
        display.scroll(random.choice(names))
        display.show(Image.HEART)

    if button_b.is_pressed():
        display.show(Image.SAD)
        
    else:
        display.show(Image.HAPPY)

display.clear()
