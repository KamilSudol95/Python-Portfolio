from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def fetch_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website or password == '':
        messagebox.showinfo(title='Oops', message='Please dont leave any fields empty!')
        return

    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \n Website:{website} \n Username:{username} \n'
                                                  f'Password:{password} \n Is it ok to save?')
    if is_ok:
        with open('data.txt', 'a') as file:
            file.write(f'{website} | {username} | {password}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

#Canvas
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

#Buttons
generate_button = Button(text='Generate Password', width=32, command=fetch_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', command=save)
add_button.grid(column=1, row=4, columnspan=2)

#Entries
website_entry = Entry(width=60)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=60)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, 'kamil.sudol5@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

window.mainloop()


