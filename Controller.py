import tkinter as tk
from datetime import datetime
import json
import time
import hashlib

windows=tk.Tk()
windows.geometry('600x300')
windows.title('Trafficware - Controllers')
windows.iconbitmap('Trafficlight.ico')

def Done_button_click(event):
    print('Done button clicked')
    controller=Entry_controller.get()
    stamptime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    record={'controller':controller, 'stamptime':stamptime}
    with open('Controller.json', 'r+') as file:
        file_data=json.load(file)
        file_data['Controllers'].append(record)
        file.seek(0)
        json.dump(file_data, file, indent=4)
    Entry_controller.delete(0, 'end')
    Message_label.config(text='Controlador registrado.')
    Message_label_2.config(text=controller)


# Create a frame
Frame_controller=tk.Frame(windows, width=1000, height=700)
Label_controller=tk.Label(Frame_controller, text='Controller:', font=('Arial', 20), width=10, height=2)
Label_controller.grid(row=0, column=0, columnspan=1, sticky='w')
Entry_controller=tk.Entry(Frame_controller, font=('Arial', 20), width=20)
Entry_controller.focus()
Entry_controller.grid(row=0, column=1, columnspan=1, sticky='w')
Done_button=tk.Button(Frame_controller, text='Done', font=('Arial', 10), width=10, height=2)
Done_button.grid(row=1, column=0, columnspan=1, sticky='w')
Done_button.bind('<Button-1>', Done_button_click)
Message_label=tk.Label(Frame_controller, text='Escanear numero de serie del controlador.', font=('Arial', 20), width=34, height=2)
Message_label.grid(row=2, column=0, columnspan=2, sticky='w')
Message_label_2=tk.Label(Frame_controller, text='', font=('Arial', 20), width=34, height=2)
Message_label_2.grid(row=3, column=0, columnspan=2, sticky='w')




Frame_controller.pack()
windows.mainloop()
