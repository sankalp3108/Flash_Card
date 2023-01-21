from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_list = original_data.to_dict(orient= "records")
else:
    data_list = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_list)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(word_text, text= current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=front_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill= "white")
    canvas.itemconfig(canvas_img, image= back_img)
    canvas.itemconfig(word_text, text = current_card["English"], fill="white")

def is_known():
    data_list.remove(current_card)
    new_data = pandas.DataFrame(data_list)
    new_data.to_csv("data/words_to_learn.csv", index =False)
    next_card()
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="./images/right.png")
known_button= Button(image=right_img, highlightthickness=0, command= is_known)
known_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
unknown_button= Button(image=wrong_img, highlightthickness=0, command= next_card)
unknown_button.grid(column=0, row=1)

next_card()
window.mainloop()