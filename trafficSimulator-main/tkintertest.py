import tkinter as tk
from tkinter import ttk
# from tkinter import *
import pygame
import os
import numpy as np
from trafficSimulator import *
import main
from simulations import *
from PIL import ImageTk, Image

# root window
root = tk.Tk()

root.geometry('1280x720') #720p
# root.resizable(False, False)
root.title('Simulasi Lalu Lintas dengan Intelligent Driving Model di Kota Bandung')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

process = None
win = None

# Inisiasi variable slider
current_value = tk.IntVar()
current_value_speed = tk.DoubleVar()
current_traffic_light = tk.IntVar()

#retrieve tipe jalan (e.g roundabout, simpang lima, etc)
def get_road_type():
    return variable_.get()

def option_changed(event):
    road_opt = get_road_type()
    if road_opt == 'SIMPANG EMPAT BUAH BATU' :
        img_ = ImageTk.PhotoImage(Image.open("SimpangEmpatEdited.jpg"))
        label_img.configure(image = img_)
        label_img.image = img_
        # label_img.pack()
    else :
        img_ = ImageTk.PhotoImage(Image.open("SimpangLimaEdited.jpg"))
        label_img.configure(image = img_)
        label_img.image = img_

#retrieve nilai vehicle rate
def get_current_value():
    return current_value.get()

#retrieve nilai speed
def get_current_speed():
    return '{: .2f}'.format(current_value_speed.get())

#retrieve nilai durasi lampu lalu lintas
def get_current_light():
    return current_traffic_light.get()

#fungsi update nilai variables
def slider_changed(event): #vehicle rate
    value_label.configure(text=get_current_value())

def slider_changed_speed(event):
    value_speed_label.configure(text=get_current_speed())

def slider_changed_light(event):
    value_light_label.configure(text=get_current_light())

# def get_stats(sim) :
#     if sim != None :
#         n, avg = sim.get_stats()
#         txt_avg = "%.2f" % avg
#         return [str(n), txt_avg]
#     return ['0','0']

#running simulation
def run_simulation():
    global win
    if get_road_type() == 'SIMPANG EMPAT BUAH BATU' :
        sim = perempatanbuahbatu(int(get_current_value()), float(get_current_speed()), int(get_current_light()))
        win = Window(sim)
        win.zoom = 5
        win.offset = (-150, -100)

    elif get_road_type() == 'ROUNDABOUT' :
        sim = main.runsim(int(get_current_value()), float(get_current_speed()), int(get_current_light()))
        win = Window(sim)
        win.zoom = 5
    
    elif get_road_type() == 'SIMPANG LIMA GATOT SUBROTO' :
        sim = simpanglima(int(get_current_value()), float(get_current_speed()), int(get_current_light()))
        win = Window(sim)
        win.zoom = 3
        win.offset = (-150, -110)
    
    win.run(root, steps_per_update=5)
         



# label for the slider for vehicle rate
slider_label = ttk.Label(
    root,
    text='Vehicle Rate:'
)

#posisi label vehicle rate
slider_label.grid(
    column=0,
    row=2,
    sticky='w'
)

#slider vehicle rate
slider = ttk.Scale(
    root,
    from_=1,
    to=60,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value
)

slider.grid(
    column=1,
    row=2
    # ,sticky='we'
)

#label value vehicle rate
value_label = ttk.Label(
    root,
    text=get_current_value()
)
value_label.grid(
    row=3,
    column=1,
    columnspan=2,
    sticky='n'
)

# Slider for speed of vehicles

vehiclespeed_label = ttk.Label(
    root,
    text='Vehicle Speed:'
)

vehiclespeed_label.grid(
    column=0,
    row=4,
    sticky='w'
)

#  slider speed
slider = ttk.Scale(
    root,
    from_=1,
    to=60,
    orient='horizontal',  # vertical
    command=slider_changed_speed,
    variable=current_value_speed
)

slider.grid(
    column=1,
    row=4
    # ,sticky='we'
)

#value label speed
value_speed_label = ttk.Label(
    root,
    text=get_current_speed()
)
value_speed_label.grid(
    row=5,
    column=1,
    columnspan=2,
    sticky='n'
)

# Slider for Traffic Light Duration

trafficlight_label = ttk.Label(
    root,
    text='Traffic Light Duration:'
)

trafficlight_label.grid(
    column=0,
    row=6
    ,sticky='w'
)

#  slider traffic light
slider = ttk.Scale(
    root,
    from_=10,
    to=80,
    orient='horizontal',  # vertical
    command=slider_changed_light,
    variable=current_traffic_light
)

slider.grid(
    column=1,
    row=6
    # ,sticky='we'
)

#value slider traffic light
value_light_label = ttk.Label(
    root,
    text=get_current_light()
)
value_light_label.grid(
    row=7,
    column=1,
    columnspan=2,
    sticky='n'
)

OPTIONS = [
            'SIMPANG EMPAT BUAH BATU',
            'SIMPANG LIMA GATOT SUBROTO'
        ]

variable_ = StringVar(root)
variable_.set(OPTIONS[0]) # default value

#option menu for road type
w = OptionMenu(root, variable_, *OPTIONS, command=option_changed)

w.grid(
    row=1,
    columnspan=2
)

#submit button to run simulation
submit_button = tk.Button(text="Start", command=run_simulation)

submit_button.grid(
    row=8,
    columnspan=2
)

#label for average speed
avgspeed_label = ttk.Label(
    root,
    text='Average Speed:'
)

avgspeed_label.grid(
    column=0,
    row=10
    ,sticky='w'
)

#label for total vehicle
totalvehicle_label = ttk.Label(
    root,
    text='Total Vehicle:'
)

totalvehicle_label.grid(
    column=0,
    row=12
    ,sticky='w'
)

img_road = tk.Frame(win, width=320, height=210)
img_road.grid(row=14, column=0,rowspan=20, columnspan=3)

img_ = ImageTk.PhotoImage(Image.open("SimpangEmpatEdited.jpg"))

label_img = Label(img_road, image = img_, width=320, height=210)
label_img.pack()


credit_label = ttk.Label(root,
                        text="oleh :\nTressy Melani Setiawan \nDr. Putu Harry Gunawan, S.Si., M.Si., M.Sc. \nS1 Informatika \nTelkom University, 2022")
credit_label.grid(row=36, column=0, columnspan=3)
# if win != None :
#     text_total, text_avg = win.get_stats()
#     txt_avg = "%.3f" % text_avg

#     avg_speed = ttk.Label(
#         root,
#         text=txt_avg
#     )
#     avg_speed.grid(
#         row=10,
#         column=1,
#         columnspan=2,
#         sticky='w'
#     )

#     tot_veh = ttk.Label(
#         root,
#         text=text_total
#     )
#     tot_veh.grid(
#         row=12,
#         column=1,
#         columnspan=2,
#         sticky='w'
#     )
embed = tk.Frame(root, width = 960, height = 720) #creates embed frame for pygame window
embed.grid(row=0, column=4,rowspan=40, columnspan=10) # Adds grid
# embed.pack() #packs window to the left

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

root.update_idletasks()

root.mainloop()