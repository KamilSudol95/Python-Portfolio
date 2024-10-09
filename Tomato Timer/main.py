from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_count = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_count)
    timer.config(text='Timer', fg='green')
    canvas.itemconfig(timer_text, text='00:00')
    check.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        count_down(work_sec)
        timer.config(text='Work', fg='green', font=(FONT_NAME, 35,))
    if reps % 2 == 0:
        if reps == 8:
            count_down(long_break_sec)
            timer.config(text='Long Break', fg='red', font=(FONT_NAME, 35,))
        else:
            count_down(short_break_sec)
            timer.config(text='Break', fg='pink', font=(FONT_NAME, 35,))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer_count
        timer_count = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        session = math.floor(reps / 2)
        for i in range(session):
            mark += "✔"
        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title('Tomato')
window.config(padx=100, pady=50)

#Canvas
canvas = Canvas(width=200, height=224, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column= 1, row= 1)

#Buttons
start = Button(text= 'Start', command=start_timer)
start.grid(column= 0, row= 2)

reset = Button(text= 'Reset', command=reset_timer)
reset.grid(column= 2, row= 2)

#Labels
timer = Label(text='Timer', fg='green', font=(FONT_NAME, 35,))
timer.grid(column= 1, row=0)

check = Label(text="", fg='green')
check.grid(column= 1, row= 3)


window.mainloop()