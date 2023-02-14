import tkinter as tk
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
timer = 0


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    canvas.after_cancel(timer)
    global reps
    reps = 0
    pomodoro.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    tick.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #
# start and stop button display
def start_timer():
    global reps
    reps += 1
    ticks = ''
    for x in range(int(reps/2)):
        ticks += '✔'

    if reps % 2 == 1:
        pomodoro.config(text='Work', fg=GREEN)
        count_down(WORK_MIN)
    elif reps % 8 == 0:
        pomodoro.config(text='Break', fg=RED)
        count_down(LONG_BREAK_MIN)
        tick.config(text=ticks)
    elif reps % 2 == 0:
        pomodoro.config(text='Break', fg=PINK)
        count_down(SHORT_BREAK_MIN)
        tick.config(text=ticks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count_min, count_sec=0):
    canvas.itemconfig(timer_text, text=f'{count_min:02d}:{count_sec:02d}')
    # so timer does not run below 00:00
    if count_min == 0 and count_sec == 0:
        return
    # counting down the minute
    elif count_sec == 0:
        canvas.after(1000, count_down, count_min-1, 59)
    # counting down the seconds
    elif count_sec > 0:
        global timer
        timer = canvas.after(1000, count_down, count_min, count_sec - 1)


# ---------------------------- UI SETUP ------------------------------- #
# main screen
screen = tk.Tk()
screen.title('Pomodoro')
screen.config(bg=YELLOW, padx=100, pady=50)

# canvas
pomodoro_img = tk.PhotoImage(file='tomato.png')
canvas = tk.Canvas(width=200, height=300)
canvas.config(bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 150, image=pomodoro_img)
timer_text = canvas.create_text(100, 170, fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Pomodoro label
pomodoro = tk.Label(text='Timer')
pomodoro.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, 'bold'))
pomodoro.grid(column=1, row=0)

# start button
start_stop = tk.Button(text='Start')
start_stop.config(highlightbackground=YELLOW, width=2, command=start_timer)
start_stop.grid(column=0, row=2)

# reset button
reset = tk.Button(text='Reset')
reset.config(highlightbackground=YELLOW, width=2, command=reset_timer)
reset.grid(column=3, row=2)

# ticks
tick = tk.Label()
tick.config(bg=YELLOW, fg=GREEN)
tick.grid(column=1, row=3)

screen.mainloop()