import tkinter as tk
import ttkbootstrap as tb
from PIL import Image, ImageTk, ImageDraw

root = tb.Window(themename="superhero")
root.title("Calculator")
root.geometry("402x520")
root.resizable(False, False)
root.configure(bg='#282828')  

def update_display(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

def clear_display():
    display.delete(0, tk.END)

def evaluate_expression():
    try:
        expression = display.get().replace('^', '**')
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

display = tk.Entry(root, font=("Arial", 24), borderwidth=0, relief="sunken", justify="right", bg='#404040', fg='#ffffff', insertbackground='#ffffff')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=8, ipady=8)

buttons = [
    '(', ')', '^', 'C',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

def create_glowy_button_image(width, height, radius, color, glow_color):
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    glow_radius = 10
    for i in range(glow_radius, 0, -1):
        alpha = int(255 * (i / glow_radius))
        draw.rounded_rectangle(
            [(glow_radius - i, glow_radius - i), (width - (glow_radius - i), height - (glow_radius - i))],
            radius + i, fill=(*glow_color, alpha)
        )
    
    draw.rounded_rectangle([(glow_radius, glow_radius), (width - glow_radius, height - glow_radius)], radius, fill=color)
    
    return ImageTk.PhotoImage(image)

# Create and place buttons
row_val = 1
col_val = 0
button_images = {}
for button in buttons:
    action = lambda x=button: update_display(x) if x not in ["=", "C"] else evaluate_expression() if x == "=" else clear_display()

    img = create_glowy_button_image(70, 70, 20, '#4da6ff', (77, 166, 255))
    button_images[button] = img
    
    btn = tk.Button(root, text=button, font=("Arial", 18), command=action, height=70, width=70, image=img, compound='center', bg='#282828', fg='#ffffff', borderwidth=0, relief='flat')
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
