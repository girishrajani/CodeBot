import tkinter as tk
from tkinter import *

# file = open('mypyfile.txt', 'w') 
# file.truncate()
# file.close()

# file = open('user_globals.txt', 'w') 
# file.truncate()
# file.close()

root = tk.Tk()
root.geometry("500x720")
root.title("c0deb0t")
root.iconbitmap("icon.ico")
canvas1 = tk.Canvas(root, width=1000, bg="#191919", height=1000)
canvas1.pack()

label1 = tk.Label(
    root, text="welcome to c0deb0t", fg="#A6A6A6", bg="#191919", font=("Calibri", 18, "bold")
)
label1.place(x=140, y=50)

my_list = tk.Text(root)
my_list.pack(pady=20)
canvas1.create_window(250, 355, width=398, height=500, window=my_list)

my_text = tk.Text(root)
my_text.pack(pady=20)
canvas1.create_window(200, 640, width=300, height=50, window=my_text)

# def out():
#     code = my_text.get(1.0, tk.END)
#     text_file = open('mypython_input.txt', 'w+')
#     text_file.write(code)
#     text_file.close()

#     import myoutput
#     myoutput.WriteMyOutput()

#     file = open('mypython_output.txt', 'r') 
#     message = file.read()
#     file.close()
    
#     l3.config(text = message)
    
#     file = open('mypyfile.txt', 'a') 
#     file.write("mypython In: " + code)
#     file.write("mypython Out: " + message)
#     file.close() 

# def check():
#     file = open('mypyfile.txt', 'r') 
#     content = file.read()
#     my_text1.insert(tk.END, content)
#     file.close()

# def clear():
#     my_text1.delete(1.0, tk.END)
#     file = open('mypyfile.txt', 'w') 
#     file.truncate()
#     file.close()

# def save():
#     file = filedialog.asksaveasfile(defaultextension=".*", mode='w', initialdir="C:\\Users\\drpre\\OneDrive\\Desktop\\teams", title="Save Text File", filetypes=(("Text Files", "*.txt"), ))
#     stuff = my_text1.get(1.0, tk.END)
#     file.write(stuff)
#     file.close()
#     my_text1.delete('1.0', tk.END)
#     my_text1.update()

# def get_user():
#     file = open('user_globals.txt', 'r') 
#     variables = file.read()
#     my_text2.insert(tk.END, variables)
#     file.close()

    
button1 = tk.Button(
    text="Enter", bg="#929292", font=("SansSerif", 12)
    )
canvas1.create_window(400, 641, width=100, height=52, window=button1)

root.mainloop()
