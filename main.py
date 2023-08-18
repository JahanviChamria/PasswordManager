from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gener():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pw = []
    pwl=[random.choice(letters) for le in range(nr_letters)]
    pwn=[random.choice(numbers) for le in range(nr_numbers)]
    pws=[random.choice(symbols) for le in range(nr_symbols)]
    pw=pwl+pwn+pws
    random.shuffle(pw)
    passs="".join(pw)
    pyperclip.copy(passs)
    passe.insert(0, passs)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    w=webe.get()
    e=eme.get()
    p=passe.get()
    datad={w:
               {"email":e,
              "password":p}
           }
    if len(w)==0 or len(p)==0 or len(e)==0:
        messagebox.showinfo(title="Error!", message="Please don't leave any fields empty!")
    else:
        b=messagebox.askokcancel(title=w, message=f"These are the details entered: \nEmail: {e}\nPassword: {p}\nIs it ok to save?")
        if b:
            try:
                with open("./data.json", mode="r") as file:
                    d=json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(datad, file, indent=4)
            except:
                with open("data.json", "w") as file:
                    json.dump(datad, file, indent=4)
            else:
                d.update(datad)
                with open("./data.json", mode="w") as file:
                    json.dump(d, file, indent=4)
            finally:
                webe.delete(0, 'end')
                passe.delete(0, 'end')

def sea():
    web=webe.get()
    try:
        with open("data.json", "r") as file:
            d=json.load(file)
            em = d[web]["email"]
            pw = d[web]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="Search Results", message="No data file found!")
    except:
        messagebox.showinfo(title="Search Results", message="No saved passwords!")
    else:
        messagebox.showinfo(title="Search Results", message=f"Email: {em}\nPassword: {pw}")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas=Canvas(height=200, width=200)
logoimg=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoimg)
canvas.grid(row=0, column=1)

web=Label(text="Website:")
web.grid(row=1, column=0)

webe=Entry(width=21)
webe.grid(row=1, column=1)
webe.focus()

email=Label(text="Email/Username:")
email.grid(row=2, column=0)

eme=Entry(width=35)
eme.grid(row=2, column=1, columnspan=2)
eme.insert(0, "angela@gmail.com")

passw=Label(text="Password:")
passw.grid(row=3, column=0)

passe=Entry(width=21)
passe.grid(row=3, column=1)

gen=Button(text="Generate Password", command=gener)
gen.grid(row=3, column=2)

add=Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)

search=Button(text="Search", command=sea)
search.grid(row=1, column=2)







window.mainloop()