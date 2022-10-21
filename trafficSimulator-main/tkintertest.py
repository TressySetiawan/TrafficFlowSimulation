import tkinter as tk
from tkinter import ttk
import pygame
import os
import numpy as np
from trafficSimulator import *
import sys
import asyncio
import main
import subprocess

# root window

root = tk.Tk()

root.geometry('400x300+100+179')
root.resizable(False, False)
root.title('TrafficFlowSimulator')

process = None

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# slider current value
current_value = tk.IntVar()
current_value_speed = tk.DoubleVar()
current_traffic_light = tk.IntVar()


def get_current_value():
    return current_value.get()

def get_current_speed():
    return '{: .2f}'.format(current_value_speed.get())

def get_current_light():
    return current_traffic_light.get()


def slider_changed(event):
    value_label.configure(text=get_current_value())

def slider_changed_speed(event):
    value_speed_label.configure(text=get_current_speed())

def slider_changed_light(event):
    value_light_label.configure(text=get_current_light())

def run_simulation():
    global process
    if process == None :
        print("heyyo")
    else :
        process.terminate()
    # pid=os.fork()
    command_ = "python simulation_1.py Intersection " + str(get_current_value()) + " " + str(get_current_speed()) + " " + str(get_current_light())
    # if pid==0 :
    process = subprocess.Popen(command_)
    #     os.system(command_)
    #     exit()
    # sim = main.runsim()
    # win = Window(sim)
    # win.zoom = 10
    # win.run(steps_per_update=5)


# label for the slider
slider_label = ttk.Label(
    root,
    text='Vehicle Rate:'
)

slider_label.grid(
    column=0,
    row=0,
    sticky='w'
)

#  slider
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
    row=0,
    sticky='we'
)

# current value label
# current_value_label = ttk.Label(
#     root,
#     text='Current Value:'
# )

# current_value_label.grid(
#     row=1,
#     columnspan=2,
#     sticky='n',
#     ipadx=10,
#     ipady=10
# )

# value label
value_label = ttk.Label(
    root,
    text=get_current_value()
)
value_label.grid(
    row=2,
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
    row=5,
    sticky='w'
)

#  slider
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
    row=5,
    sticky='we'
)

value_speed_label = ttk.Label(
    root,
    text=get_current_speed()
)
value_speed_label.grid(
    row=6,
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
    row=7,
    sticky='w'
)

#  slider
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
    row=7,
    sticky='we'
)

value_light_label = ttk.Label(
    root,
    text=get_current_light()
)
value_light_label.grid(
    row=8,
    columnspan=2,
    sticky='n'
)

submit_button = tk.Button(text="Start", command=run_simulation)

submit_button.grid(
    row=10,
    columnspan=2
)

# os.environ['SDL_WINDOWID'] = str(root.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

root.update_idletasks()

root.mainloop()

# """Shows a window visualizing the simulation and runs the loop function."""

# window = Window()        
# # Create a pygame window
# self.screen = pygame.display.set_mode((self.width, self.height))
# pygame.display.flip()

# # Fixed fps
# clock = pygame.time.Clock()

# # To draw text
# pygame.font.init()
# self.text_font = pygame.font.SysFont('Lucida Console', 16)

# # pygame.image.save(self.screen, "window.bmp")
# os.environ['SDL_VIDEODRIVER'] = 'windib'
# # Draw loop
# running = True
# while running:

#     # Draw simulation
#     self.draw()

#     # Update window
#     pygame.display.update()
#     clock.tick(self.fps)
    
#     # await asyncio.sleep(0)

#     # Handle all events
#     for event in pygame.event.get():
#         # Quit program if window is closed
#         if event.type == pygame.QUIT:
#             running = False
#         # Handle mouse events
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # If mouse button down
#             if event.button == 1:
#                 # Left click
#                 x, y = pygame.mouse.get_pos()
#                 x0, y0 = self.offset
#                 self.mouse_last = (x-x0*self.zoom, y-y0*self.zoom)
#                 self.mouse_down = True
#             if event.button == 4:
#                 # Mouse wheel up
#                 self.zoom *=  (self.zoom**2+self.zoom/4+1) / (self.zoom**2+1)
#             if event.button == 5:
#                 # Mouse wheel down 
#                 self.zoom *= (self.zoom**2+1) / (self.zoom**2+self.zoom/4+1)
#         elif event.type == pygame.MOUSEMOTION:
#             # Drag content
#             if self.mouse_down:
#                 x1, y1 = self.mouse_last
#                 x2, y2 = pygame.mouse.get_pos()
#                 self.offset = ((x2-x1)/self.zoom, (y2-y1)/self.zoom)
#         elif event.type == pygame.MOUSEBUTTONUP:
#             self.mouse_down = False