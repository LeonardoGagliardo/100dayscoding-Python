#Day 29 Project: Password Manager
import tkinter
from tkinter import messagebox

# Save Password

def save():
    should_continue = True
    
    Website = Website_entry.get()
    Email = Email_entry.get()
    Passsword = Passsword_entry.get()


    if Website == "" or Email == "" or Passsword == "":
        messagebox.showinfo(title="Warning!", message="Please don't leave any fields empty!")
        should_continue = False
    else:
        should_continue == True

    if should_continue == True:
        should_continue = messagebox.askokcancel(title= "Info Confirmation", message=f"These are the datails entered: \nWebsite: {Website}\nEmail: {Email}\nPassword: {Passsword}")


        if should_continue == True:
            Website_entry.delete(0, 'end')
            Email_entry.delete(0, 'end')
            Passsword_entry.delete(0, 'end')

            with open ("Extra_Data/Data29/passwords", mode='a') as saved_passwords:
                saved_passwords.write(f"\n\nWebsite: {Website}\nEmail: {Email}\nPassword: {Passsword}")

            messagebox.showinfo(title="Add confirmation", message="Your password has been save on the file 'passwords'.")

 
# Window config
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width= 200, height= 200)

# Image config
LOCKER_IMAGE = tkinter.PhotoImage(file="Extra_Data/Data29/logo.png")
canvas = tkinter.Canvas(width=200, height=200, highlightthickness= 0)
canvas.create_image(100, 100, image=LOCKER_IMAGE)
canvas.grid(column=1, row=0)

# Labels config
FONT = ("Arial", 12)

Website_label = tkinter.Label(text="Website:", font=FONT)
Email_label = tkinter.Label(text="Email/Username:", font=FONT)
Passsword_label = tkinter.Label(text="Password:", font=FONT)

Website_label.grid(column=0 , row= 1)
Email_label.grid(column=0 , row= 2)
Passsword_label.grid(column=0 , row= 3)

# Entrys config

Website_entry = tkinter.Entry(width=35)
Website_entry.focus()
Email_entry = tkinter.Entry(width=35)
Email_entry.insert(0, "@hotmail.com")
Passsword_entry = tkinter.Entry(width=35)

Website_entry.grid(column=1 , row= 1, columnspan= 2)
Email_entry.grid(column=1 , row= 2, columnspan= 2)
Passsword_entry.grid(column=1 , row= 3, columnspan=35)


# Buttons config

Add_button = tkinter.Button(text="Add", width= 30, command=save)

Add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()