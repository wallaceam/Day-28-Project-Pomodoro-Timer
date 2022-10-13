from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#f8a89d"
RED = "#c14632"
GREEN = "#608474"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    tracker.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN *60)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmarks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            checkmarks += "✓"
            tracker.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Auto-Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

label = Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 50), pady=20)
label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, bg=YELLOW, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

tracker = Label(fg=GREEN, bg=YELLOW, text="", font=(FONT_NAME, 50, "normal"), pady=10)
tracker.grid(row=3, column=1)

window.mainloop()
