from tkinter import *
import pandas as pd
import random

current_card = {}
to_learn = {}

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/hu_50k.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card['Hungarian'])
    canvas.itemconfig(card_title, text='Hungarian', fill= 'Black')
    canvas.itemconfig(card_word, text= current_card['Hungarian'], fill= 'Black')
    canvas.itemconfig(card_background, image= card_front_img)
    flip_timer = window.after(7500, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='English', fill= 'White')
    canvas.itemconfig(card_word, text=current_card['English'], fill= 'White')
    canvas.itemconfig(card_background, image= card_back_image)

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index= False)

BACKGROUND_COLOR = "#B1DDC6"



#Window setup
window = Tk()
window.title('Flash Card App')
window.config(padx= 50, pady= 50, background= BACKGROUND_COLOR)

flip_timer = window.after(7500, func=flip_card)


#Canvas setup
canvas = Canvas(width= 800, height= 526)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image= card_front_img)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text=f'word', font=('Ariel', 60, 'bold'))

canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row= 0 , column= 0, columnspan= 2)

#Buttons setup
cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image= cross_image, highlightthickness= 0, command= next_card)
unknown_button.grid(row= 1, column= 0)

check_image = PhotoImage(file='images/right.png')
known_button = Button(image=check_image, highlightthickness= 0, command= is_known)
known_button.grid(row=1, column= 1)


next_card()

window.mainloop()

