from cgitb import text
from textwrap import fill
from tkinter import *
from turtle import color
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
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    reps+=1
    work_in_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_in_sec=LONG_BREAK_MIN*60
    if(reps%8==0):
        title_label.config(text="Long Break",fg="red")
        count_down(long_break_in_sec)
    elif reps%2==0:
        title_label.config(text="Break",fg="pink")
        count_down(short_break_sec)
    else:
        title_label.config(text="Working",fg="green")
        count_down(work_in_sec)


#reseting every thing.
def reset():
    global reps;
    reps=0
    windows.after_cancel(timer)
    title_label.config(text="Timer",fg="green")
    canvas.itemconfig(timer_text,text="00:00")
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_minute=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_minute}:{count_sec}")
    if count>0:
       timer= windows.after(1000,count_down,count-1)
    else:
        start_count()
# ---------------------------- UI SETUP ------------------------------- #

windows=Tk()
windows.title("Promodoro")
windows.config(padx=100,pady=100,bg=YELLOW)
title_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,25,"bold"))
title_label.grid(row=0,column=1)
#creating canvas
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
timer_text=canvas.create_text(100,120,text="00:00",fill="white",font=(FONT_NAME,24,"bold"))
canvas.grid(column=1,row=1)
#creating buttons.
start_button=Button(text="Start",command=start_count)
start_button.grid(row=2,column=0)
reset_button=Button(text="reset",command=reset)
reset_button.grid(row=2,column=2)
check_mark=Label(text="✔️",fg=GREEN,bg=YELLOW,font=(FONT_NAME,18,"bold"))
check_mark.grid(row=3,column=1)
windows.mainloop()