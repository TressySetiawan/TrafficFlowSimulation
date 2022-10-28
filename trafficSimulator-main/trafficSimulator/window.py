import pygame
from pygame import gfxdraw
from pygame.locals import *
import os
import numpy as np
import asyncio
import tkinter as tk
from tkinter import *

class Window:
    def __init__(self, sim, config={}):
        # Simulation to draw
        self.sim = sim

        # Set default configurations
        self.set_default_config()

        # Update configurations
        for attr, val in config.items():
            setattr(self, attr, val)
        
    def set_default_config(self):
        """Set default configuration"""
        self.width = 960
        self.height = 720
        self.bg_color = (250, 250, 250)

        self.fps = 60
        self.zoom = 0
        self.offset = (0, 0)

        self.mouse_last = (0, 0)
        self.mouse_down = False
        # self.car_image = "car.png"
        self.img_car = pygame.image.load("car_.png")
        self.car_rect = self.img_car.get_rect()


    def loop(self, root, loop=None):
        """Shows a window visualizing the simulation and runs the loop function."""
        
        # Create a pygame window
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (575,189)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.flip()

        # Fixed fps
        clock = pygame.time.Clock()

        # To draw text
        pygame.font.init()
        self.text_font = pygame.font.SysFont('Lucida Console', 16)
        
        # pygame.image.save(self.screen, "window.bmp")
        # os.environ['SDL_VIDEO_CENTERED'] = '0'
        # Draw loop
        running = True
        while running:
            # Update simulation
            if loop: loop(self.sim)

            # Draw simulation
            self.draw()

            # Update window
            root.update()
            pygame.display.update()
            clock.tick(self.fps)
            # await asyncio.sleep(0)
            _, text_avg = self.get_stats()
            avg_speed = ttk.Label(
                root,
                text=text_avg
            )
            avg_speed.grid(
                row=10,
                column=1,
                columnspan=2,
                sticky='n'
            ) 
            # Handle all events
            for event in pygame.event.get():
                # Quit program if window is closed
                if event.type == pygame.QUIT:
                    running = False
                # Handle mouse events
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # If mouse button down
                    if event.button == 1:
                        # Left click
                        x, y = pygame.mouse.get_pos()
                        x0, y0 = self.offset
                        self.mouse_last = (x-x0*self.zoom, y-y0*self.zoom)
                        self.mouse_down = True
                    if event.button == 4:
                        # Mouse wheel up
                        self.zoom *=  (self.zoom**2+self.zoom/4+1) / (self.zoom**2+1)
                    if event.button == 5:
                        # Mouse wheel down 
                        self.zoom *= (self.zoom**2+1) / (self.zoom**2+self.zoom/4+1)
                elif event.type == pygame.MOUSEMOTION:
                    # Drag content
                    if self.mouse_down:
                        x1, y1 = self.mouse_last
                        x2, y2 = pygame.mouse.get_pos()
                        self.offset = ((x2-x1)/self.zoom, (y2-y1)/self.zoom)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_down = False           

    def run(self, root, steps_per_update=1):
        """Runs the simulation by updating in every loop."""
        def loop(sim):
            sim.run(steps_per_update)
        self.loop(root, loop)

    def convert(self, x, y=None):
        """Converts simulation coordinates to screen coordinates"""
        if isinstance(x, list):
            return [self.convert(e[0], e[1]) for e in x]
        if isinstance(x, tuple):
            return self.convert(*x)
        return (
            int(self.width/2 + (x + self.offset[0])*self.zoom),
            int(self.height/2 + (y + self.offset[1])*self.zoom)
        )

    def inverse_convert(self, x, y=None):
        """Converts screen coordinates to simulation coordinates"""
        if isinstance(x, list):
            return [self.convert(e[0], e[1]) for e in x]
        if isinstance(x, tuple):
            return self.convert(*x)
        return (
            int(-self.offset[0] + (x - self.width/2)/self.zoom),
            int(-self.offset[1] + (y - self.height/2)/self.zoom)
        )


    def background(self, r, g, b):
        """Fills screen with one color."""
        self.screen.fill((r, g, b))

    def line(self, start_pos, end_pos, color):
        """Draws a line."""
        gfxdraw.line(
            self.screen,
            *start_pos,
            *end_pos,
            color
        )

    def rect(self, pos, size, color):
        """Draws a rectangle."""
        gfxdraw.rectangle(self.screen, (*pos, *size), color)

    def box(self, pos, size, color):
        """Draws a rectangle."""
        gfxdraw.box(self.screen, (*pos, *size), color)
    
    # def car(self, pos, size, img) :


    def circle(self, pos, radius, color, filled=True):
        gfxdraw.aacircle(self.screen, *pos, radius, color)
        if filled:
            gfxdraw.filled_circle(self.screen, *pos, radius, color)



    def polygon(self, vertices, color, filled=True):
        gfxdraw.aapolygon(self.screen, vertices, color)
        if filled:
            gfxdraw.filled_polygon(self.screen, vertices, color)

    

    def rotated_box(self, pos, size, angle=None, cos=None, sin=None, centered=True, color=(0, 0, 255), filled=True):
        """Draws a rectangle center at *pos* with size *size* rotated anti-clockwise by *angle*."""
        x, y = pos
        l, h = size

        if angle:
            cos, sin = np.cos(angle), np.sin(angle)
        
        vertex = lambda e1, e2: (
            x + (e1*l*cos + e2*h*sin)/2,
            y + (e1*l*sin - e2*h*cos)/2
        )

        if centered:
            vertices = self.convert(
                [vertex(*e) for e in [(-1,-1), (-1, 1), (1,1), (1,-1)]]
            )
        else:
            vertices = self.convert(
                [vertex(*e) for e in [(0,-1), (0, 1), (2,1), (2,-1)]]
            )

        self.polygon(vertices, color, filled=filled)

    def rotated_car(self, pos, size, angle=None, cos=None, sin=None, centered=True, color=(0, 0, 255), filled=True):
        """Draws a rectangle center at *pos* with size *size* rotated anti-clockwise by *angle*."""
        x, y = pos
        l, h = size

        if angle:
            cos, sin = np.cos(angle), np.sin(angle)
        
        vertex = lambda e1, e2: (
            x + (e1*l*cos + e2*h*sin)/2,
            y + (e1*l*sin - e2*h*cos)/2
        )

        if centered:
            vertices = self.convert(
                [vertex(*e) for e in [(-1,-1), (-1, 1), (1,1), (1,-1)]]
            )
        else:
            vertices = self.convert(
                [vertex(*e) for e in [(0,-1), (0, 1), (2,1), (2,-1)]]
            )

        self.car(vertices, l, h, x, y, color, filled=filled)
    
    def car(self, vertices, l , h, x, y, color, filled=True):
        # w, h = vertices[2][0] - vertices[0][0], vertices[0][1] - vertices[1][1]
        rect = self.img_car.get_rect()
        rect.center = vertices[0][0] + h, vertices[0][1] + l
        # print(rect.center)
        # print(x,y)
        # rect.center = x, y
        # gfxdraw.textured_polygon(self.screen, vertices, self.img_car.convert_alpha().copy(), 50,50)
        self.screen.blit(pygame.transform.scale(self.img_car, (20, 10)), rect)
        # self.screen.blit(self.img_car, rect)
        # print(vertices)
        # if filled:
        #     gfxdraw.filled_polygon(self.screen, vertices, color)

        # pygame.draw.polygon(self.img_car, color, vertices)

    def rotated_rect(self, pos, size, angle=None, cos=None, sin=None, centered=True, color=(0, 0, 255)):
        self.rotated_box(pos, size, angle=angle, cos=cos, sin=sin, centered=centered, color=color, filled=False)

    def arrow(self, pos, size, angle=None, cos=None, sin=None, color=(150, 150, 190)):
        if angle:
            cos, sin = np.cos(angle), np.sin(angle)
        
        self.rotated_box(
            pos,
            size,
            cos=(cos - sin) / np.sqrt(2),
            sin=(cos + sin) / np.sqrt(2),
            color=color,
            centered=False
        )

        self.rotated_box(
            pos,
            size,
            cos=(cos + sin) / np.sqrt(2),
            sin=(sin - cos) / np.sqrt(2),
            color=color,
            centered=False
        )


    def draw_axes(self, color=(100, 100, 100)):
        x_start, y_start = self.inverse_convert(0, 0)
        x_end, y_end = self.inverse_convert(self.width, self.height)
        self.line(
            self.convert((0, y_start)),
            self.convert((0, y_end)),
            color
        )
        self.line(
            self.convert((x_start, 0)),
            self.convert((x_end, 0)),
            color
        )

    def draw_grid(self, unit=50, color=(150,150,150)):
        x_start, y_start = self.inverse_convert(0, 0)
        x_end, y_end = self.inverse_convert(self.width, self.height)

        n_x = int(x_start / unit)
        n_y = int(y_start / unit)
        m_x = int(x_end / unit)+1
        m_y = int(y_end / unit)+1

        for i in range(n_x, m_x):
            self.line(
                self.convert((unit*i, y_start)),
                self.convert((unit*i, y_end)),
                color
            )
        for i in range(n_y, m_y):
            self.line(
                self.convert((x_start, unit*i)),
                self.convert((x_end, unit*i)),
                color
            )

    def draw_roads(self):
        for road in self.sim.roads:
            # Draw road background
            self.rotated_box(
                road.start,
                (road.length, 3.7),
                cos=road.angle_cos,
                sin=road.angle_sin,
                color=(180, 180, 220),
                centered=False
            )
            # Draw road lines
            # self.rotated_box(
            #     road.start,
            #     (road.length, 0.25),
            #     cos=road.angle_cos,
            #     sin=road.angle_sin,
            #     color=(0, 0, 0),
            #     centered=False
            # )

            # Draw road arrow
            if road.length > 5: 
                for i in np.arange(-0.5*road.length, 0.5*road.length, 10):
                    pos = (
                        road.start[0] + (road.length/2 + i + 3) * road.angle_cos,
                        road.start[1] + (road.length/2 + i + 3) * road.angle_sin
                    )

                    self.arrow(
                        pos,
                        (-1.25, 0.2),
                        cos=road.angle_cos,
                        sin=road.angle_sin
                    )   
            


            # TODO: Draw road arrow

    def draw_vehicle(self, vehicle, road):
        l, h = vehicle.l,  2
        sin, cos = road.angle_sin, road.angle_cos

        x = road.start[0] + cos * vehicle.x 
        y = road.start[1] + sin * vehicle.x

        #change to rotated_car
        self.rotated_box((x, y), (l, h), cos=cos, sin=sin, centered=True)

    def draw_vehicles(self):
        for road in self.sim.roads:
            # Draw vehicles
            for vehicle in road.vehicles:
                self.draw_vehicle(vehicle, road)

    def draw_signals(self):
        for signal in self.sim.traffic_signals:
            for i in range(len(signal.roads)):
                color = (0, 255, 0) if signal.current_cycle[i] else (255, 0, 0)
                for road in signal.roads[i]:
                    a = 0
                    position = (
                        (1-a)*road.end[0] + a*road.start[0],        
                        (1-a)*road.end[1] + a*road.start[1]
                    )
                    self.rotated_box(
                        position,
                        (1, 3),
                        cos=road.angle_cos, sin=road.angle_sin,
                        color=color)

    def draw_status(self):
        text_fps = self.text_font.render(f't={self.sim.t:.5}', False, (0, 0, 0))
        text_frc = self.text_font.render(f'n={self.sim.frame_count}', False, (0, 0, 0))
        
        # self.screen.blit(text_fps, (0, 0))
        # self.screen.blit(text_frc, (100, 0))

        n_vehicles = 0
        total_velocity = 0
        for road in self.sim.roads:
            # Draw vehicles
            n_vehicles += len(road.vehicles)
            for vehicle in road.vehicles :
                total_velocity += vehicle.v
        if n_vehicles == 0 :
            avg_velocity = 0
        else :
            avg_velocity = total_velocity/n_vehicles
        
        text_n_vehicle = self.text_font.render(f'Total Vehicles={n_vehicles}', False, (0, 0, 0))
        text_n_velocity = self.text_font.render(f'Avg Speed={avg_velocity}', False, (0, 0, 0))
        self.screen.blit(text_n_vehicle, (0, 0))
        self.screen.blit(text_n_velocity, (0, 30))

    def get_stats(self) :
        n_vehicles = 0
        total_velocity = 0
        for road in self.sim.roads:
            # Draw vehicles
            n_vehicles += len(road.vehicles)
            for vehicle in road.vehicles :
                total_velocity += vehicle.v
        if n_vehicles == 0 :
            avg_velocity = 0
        else :
            avg_velocity = total_velocity/n_vehicles
        
        return n_vehicles, avg_velocity

    def draw(self):
        # Fill background
        self.background(*self.bg_color)

        # Major and minor grid and axes
        # self.draw_grid(10, (220,220,220))
        # self.draw_grid(100, (200,200,200))
        # self.draw_axes()

        self.draw_roads()
        self.draw_vehicles()
        self.draw_signals()

        # Draw status info
        self.draw_status()
        