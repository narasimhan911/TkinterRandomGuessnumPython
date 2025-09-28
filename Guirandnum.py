from tkinter import *
import random

attempts =20
answer =random.randint(1,100)

def check_answer():
    global attempts
    global text

    attempts -= 1
    guess = int(entry_window.get())
    if answer == guess:
        text.set("Congratulations! You guessed my number!")
        btn_check.pack_forget()
    elif attempts == 0:
        text.set("You are Out of Attempts!")
        btn_check.pack_forget()
    elif guess < answer:
        text.set("Incorrect! You have"+str(attempts)+"attempts remaining - Go Higher!!")
    elif guess > answer:
        text.set("Incorrect! You have"+str(attempts)+"attempts remaining - Go Lower!!")
    return

root = Tk()

root.title("Random Guess Game In The Number")
root.config(bg="dark blue")

root.geometry("500x190")
label = Label(root, text="Enter a number between 1 and 100", font=("Times New Roman", 14,"bold"), bg="#f0f8ff", fg="#333333")
label.pack(pady=10)

entry_window = Entry(root, width=40,borderwidth=4)
entry_window.pack()

btn_check = Button(root, text="Check", command=check_answer,bg="#4CAF50",fg="#FF7F00",borderwidth=2, font=("Times New Roman", 12))
btn_check.pack(pady=5)

btn_quit = Button(root, text="Quit", command=root.destroy,bg="#4CAF50",fg="#FF7F00",borderwidth=2, font=("Times New Roman", 12))
btn_quit.pack()

text = StringVar()
text.set("You have the 20 attempts remaining! GoodLuck!")

guess_attempts=Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()