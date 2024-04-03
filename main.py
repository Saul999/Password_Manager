from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ------------------------- GENERATE PASS ------------------------- #
def generate_pass():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '@', '%', '*', '&']

    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)
    password_list = []

    password_letters = [random.choice(letters) for i in range(num_letters)]
    password_symbols = [random.choice(symbols) for i in range(num_symbols)]
    password_numbers = [random.choice(numbers) for i in range(num_numbers)]

    random.shuffle(password_list)
    password_list += password_numbers
    password_list += password_letters
    password_list += password_symbols
    random.shuffle(password_list)
    print(password_list)
    password = "".join(password_list)
    # for i in range(len(password_list)):
    #     password += password_list[i]
    print(password)
    password_entry.insert(1, password)
    pyperclip.copy(password)

# ------------------------- SAVE PASS ------------------------- #

def save_pass():
    email = email_entry.get()
    email_entry.delete(0,END)
    website = website_entry.get()
    website_entry.delete(0, END)
    password = password_entry.get()
    password_entry.delete(0, END)
    website_entry.focus()
    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Whoops!", message="Please dont leave any empty fields!")
    else:
        is_okay= messagebox.askokcancel(title="Confirm Password", message=f"Are these credentials correct?\nWebsite:{website}\n"
                                                             f"Email:{email}\n"
                                                             f"Password:{password}\n")
        if is_okay:
            with open("passwords.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password} \n")


# ------------------------- UI ------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username Label + Entry
email_label = Label(text="Email:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

# Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate_pass)
password_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(column=1,row=4, columnspan=2)


window.mainloop()
