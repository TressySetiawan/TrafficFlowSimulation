import tkinter as tk
import os
import platform
import pygame
import time

class window(object):
    def __init__(self):
        self.root = tk.Tk()  # Main window
        self.root.title("SquareScape")
        # self.root.iconbitmap(r'C:\Users\17_es\PycharmProjects\square_puzzle\images\icon.ico')
        self.root.configure(background='#9b9b9b')

        # Large Frame
        self.win_frame = tk.Frame(self.root, width=670, height=520, highlightbackground='#595959', highlightthickness=2)

        # menu (left side)
        self.menu = tk.Frame(self.win_frame, width=150, height=516, highlightbackground='#595959', highlightthickness=2)
        self.menu_label = tk.Label(self.menu, text="Settings", bg='#8a8a8a', font=("Courier", "16", "bold roman"))
        self.mute = tk.Button(self.menu, text="XXXX", font="Courier", bg='#bcbcbc', activebackground='#cdcdcd')

        tk.Button(self.menu, text="<->", command=lambda: setattr(self, "direction", (-self.direction[0], self.direction[1]))).pack()
        tk.Button(self.menu, text="^", command=lambda: setattr(self, "direction", (self.direction[0], -self.direction[1]))).pack()

        # pygame
        self.pygame_frame = tk.Frame(self.win_frame, width=514, height=514, highlightbackground='#595959', highlightthickness=2)
        self.embed = tk.Frame(self.pygame_frame, width=512, height=512,)

        # Packing
        self.win_frame.pack(expand=True)
        self.win_frame.pack_propagate(0)

        self.menu.pack(side="left")
        self.menu.pack_propagate(0)
        self.menu_label.pack(ipadx=60, ipady=2)
        self.mute.pack(ipadx=40, ipady=2, pady=5)

        self.pygame_frame.pack(side="left")
        self.embed.pack()
        #This embeds the pygame window
        os.environ['SDL_WINDOWID'] = str(self.embed.winfo_id())
        system = platform.system()
        if system == "Windows":
            os.environ['SDL_VIDEODRIVER'] = 'windib'
        elif system == "Linux":
            os.environ['SDL_VIDEODRIVER'] = 'x11'

        self.root.update_idletasks()
        #Start pygame
        pygame.init()
        self.win = pygame.display.set_mode((512, 512))

        self.bg_color = (255, 255, 255)
        self.win.fill(self.bg_color)
        self.pos = 0, 0
        self.direction = 10, 10
        self.size = 40
        self.color = (0, 255, 0)
        self.root.after(30, self.update)

        self.root.mainloop()


    def update(self):

        first_move = True
        pygame.draw.rect(self.win, self.bg_color, self.pos + (self.size, self.size))


        self.pos = self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]


        if self.pos[0] < 0 or self.pos[0] > 512 - self.size:
            self.direction = -self.direction[0], self.direction[1]
            self.pos = self.pos[0] + 2 * self.direction[0], self.pos[1] + self.direction[1]
        if self.pos[1] < 0 or self.pos[1] > 512 - self.size:
            self.direction = self.direction[0], -self.direction[1]
            self.pos = self.pos[0] + self.direction[0], self.pos[1] + 2 * self.direction[1]

        pygame.draw.rect(self.win, self.color, self.pos + (self.size, self.size))
        pygame.display.flip()
        self.root.after(30, self.update)


screen = window()
tk.mainloop()