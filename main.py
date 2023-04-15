from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_SETTINGS = ("Arial", 16, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)

    #print(f"Your password is: {password}")

    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_name = password_entry.get()
    new_data = {website_name:
                    {
                        "email": email_name,
                        "password": password_name
                    }

                }

    if len(website_name) == 0 or len(password_name) == 0:
        messagebox.showinfo(title="Error", message="Please fill out all of the forms.")
    else:
        try:
            with open(file="data.json", mode="r") as file:
            #read old data
                data = json.load(file)

        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)

        else:
            #update data
            data.update(new_data)

            with open("data.json", "w") as file:
                #save
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

#find pw

def find_password():
    website = website_entry.get()
    with open("data.json") as data_file:
        data = json.load(data_file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=FONT_SETTINGS)
website_label.grid(row=1, column=0)

website_entry = Entry(width=18)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:", font=FONT_SETTINGS)
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.insert(0, "anthonychen50@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password", font=FONT_SETTINGS)
password_label.grid(row=3, column=0)

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=0, columnspan=3)





window.mainloop()
