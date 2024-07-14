import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    convert_mile = mile_input * 1.61
    output_string.set(convert_mile)
    
#window
window = ttk.Window(themename='pulse')
window.title('Mile Converter')
window.geometry('300x150')

#title
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
title_label.pack()


#input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=15)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, font='Calibri 20', textvariable=output_string)
output_label.pack(pady=5)

#run 
window.mainloop()