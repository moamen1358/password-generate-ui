from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    letter_chosen = [choice(letters) for i in range(randint(8, 12))]
    number_chosen = [choice(numbers) for i in range(randint(8, 12))]
    symbol_chosen = [choice(symbols) for i in range(randint(8, 12))]
    final = letter_chosen + number_chosen + symbol_chosen
    shuffle(final)
    my_password = "".join(final)
    password_entry.insert(0, my_password)
    pyperclip.copy(my_password)


def save():
    my_website = website_entry.get()
    my_password = password_entry.get()
    my_email = email_entry.get()
    if len(my_website) == 0 or len(my_password) == 0:
        messagebox.showwarning(title="error ", message=" plz enter")
    with open("my_passwords", "a") as my_file:
        my_file.write(f"{my_website}     ::   {my_email}        ::   {my_password}\n")
        password_entry.delete(0, END)
        website_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=40)
password_entry.grid(row=4, column=1, columnspan=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=1)
add_button = Button(text="Add", command=save)
add_button.grid(row=5, column=1)

window.mainloop()
