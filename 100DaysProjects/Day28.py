#Day 28 Project: Pomodoro App
import tkinter
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
check_marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    global check_marks
    check_marks = ""
    Timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    global check_marks
    Check_label.config(text=check_marks)

    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        Timer_label.config(text= "Break", fg=RED)
        reps = 0
        check_marks = ""
    elif reps % 2 == 1:
        count_down(WORK_MIN * 60)
        Timer_label.config(text= "Work", fg=GREEN)
        check_marks += "✔"
    else:
        count_down(SHORT_BREAK_MIN * 60)
        Timer_label.config(text= "Break", fg=PINK)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Timer Title
Timer_label = tkinter.Label(text= "Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
Timer_label.grid(column=1, row=0)


# Tomato Image
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness= 0)
TOMATO_IMG = tkinter.PhotoImage(file="Extra_Data/Data28/tomato.png")
canvas.create_image(100, 112, image=TOMATO_IMG)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Buttons

Start_button = tkinter.Button(text="Start", command=start_timer) 
Start_button.grid(column=0, row=2)

Reset_button = tkinter.Button(text="Reset", command=reset_timer)
Reset_button.grid(column=2, row=2)


# Check Marks
Check_label = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 13, "bold"))
Check_label.grid(column=1, row=4)


window.mainloop()