from tkinter import *
import random

#Define constants
BLACK = "#000000"
WHITE = "#FFFFFF"
FONT_NAME = "Courier" 
BLUE = "#050A30"
GREY = "#808080"

def generate_password():

    password_field.delete(1, 99999999)

    #Collection of letters, numbers and symbols is used to generate password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #Getting number of letters , symbols and numbers from spinboxes
    nr_letters = int(letter_input.get())
    nr_symbols = int(symbols_input.get())
    nr_numbers = int(number_input.get())

    #Initialising an empty password array
    password = []

    #Adding letters , symbols and numbers to the password array
    for letter in range(nr_letters):
        password += random.choice(letters)

    for symbol in range(nr_symbols):
        password += random.choice(symbols)

    for letter in range(nr_numbers):
        password += random.choice(numbers)

    #Randomly shuffling the password array to make the password scrambled
    random.shuffle(password)

    # Initialise an empty password string
    new_pass = ""

    # Add all characters from password array to the password string
    for char in password:
        new_pass += char

    #Set the value of Password Field to the Generated Password
    password_field.insert(index=0, string=new_pass)


#GUI using tkinter
window = Tk()

#Label for the title
letter_label = Label(text="       Password Generator      ", bg=WHITE,fg=BLUE ,font=(FONT_NAME, 25))
letter_label.pack()

#Label for Number of Letters
letter_label = Label(text="1. Select the letters you want in your password? ",bg=WHITE,fg=BLACK, font=(FONT_NAME,15))
letter_label.place(x=0, y=100)

#Spinbox for Number of Letters
letter_input = Spinbox(from_=0, to=20, width=4, font=(FONT_NAME, 0))
letter_input.place(x=640, y=100)

#Label for Number of Symbols
symbols_label = Label(text="2. Select the symbols you want in your password? ",bg=WHITE, fg=BLACK, font=(FONT_NAME, 15))
symbols_label.place(x=0, y=150)

#Spinbox for Number of Symbols
symbols_input = Spinbox(from_=0, to=20, width=4, font=(FONT_NAME, 0))
symbols_input.place(x=640, y=150)

#Label for Number of Numbers
number_label = Label(text="3. Select the numbers you want in yor password? ",bg=WHITE, fg=BLACK, font=(FONT_NAME, 15))
number_label.place(x=0, y=200)

#Spinbox for Number of Numbers
number_input = Spinbox(from_=0, to=20, width=4, font=(FONT_NAME, 0))
number_input.place(x=640, y=200)

#Button for Generating Password
generate_button = Button(text="GENERATE PASSWORD",bg=BLUE,fg=WHITE, font=(FONT_NAME, 18), command=generate_password)
generate_button.pack(pady=225)

#Field for the Generated Password
password_field = Entry(width=30, font=(FONT_NAME, 15), fg=BLUE)
password_field.place(x=130, y=350)

#Screen configurations
window.title("Password Generator App")
window.config(padx=100, pady=50, bg=GREY)
window.geometry("+250+100")
window.minsize(width=270, height=300)
window.resizable(False, False)

window.mainloop()
