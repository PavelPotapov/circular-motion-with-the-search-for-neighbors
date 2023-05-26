import play
import pygame
import math
from random import randint, random


clock = pygame.time.Clock()

pygame.display.set_caption(str(clock.get_fps()))

class Planet:
    def __init__(self, x0=100, y0=0, radius_obj=10, radius_move=10, color='black', name='planet', angle=0, speed=0.01):
        self.planet = play.new_circle(radius=radius_obj, color=color, x=x0, y=y0, angle=angle)
        self.name = name
        self.speed = speed
        self.x0 = x0
        self.y0 = y0
        self.radius_obj = radius_obj
        self.radius_move = radius_move
        self.angle = angle
        self.delta_x = 0
        self.delta_y = 0
        self.dot = play.new_circle(radius=1, color='red', x=x0, y=y0) #центр окружности
        self.dot.hide()
        self.id = id(self.planet)
    # x1 = x0 + r * cos a
    # y1 = y0 + r * sin 
    
    def go(self):
        self.dot.hide()
        self.planet.x = self.x0 + (self.radius_move + self.delta_x) * math.cos(self.angle)
        self.planet.y = self.y0 + (self.radius_move + self.delta_y)* math.sin(self.angle)
        self.angle += self.speed 
        self.angle %= 6.28 #радианы
        self.planet.angle = self.angle
        self.dot = play.new_circle(radius=1, color='red', x=self.x0, y=self.y0)
        self.dot.show()
        #print(p.angle, p.angle * 180 / math.pi)

    def create_new_moving(self):
        self.radius_move += 5
        self.speed *= -1
        self.x0 = self.planet.x +  self.radius_move * math.cos(self.angle)
        self.y0 = self.planet.y +  self.radius_move * math.sin(self.angle)
        self.angle = self.angle + 180 * math.pi / 180
        #print(self.angle)
        #print(self.radius_move, self.id)


planets = [Planet(color=play.random_color(), radius_move=randint(50,150), speed=0.05, x0=randint(-100, 100), y0=randint(-100,100))for i in range(5)]
ways = {}

def find_shortest_way(planets):
    
    for i in planets:
        for j in planets:
            if i.id != j.id:
                minimum = i.planet.distance_to(j.planet)
                if i.planet.distance_to(j.planet) < minimum:
                    minimum = i.planet.distance_to(j.planet)
                    ways[i.id] = j.id
                else:
                    ways[i.id] = j.id
                    
    print(ways)


lines = []

def draw_ways(planets):
    for key in ways:
        for i in planets:
            if key == i.id:
                for j in planets:
                    if ways[key] == j.id:
                        line = play.new_line(color=i.planet.color, x=i.planet.x, y=i.planet.y,thickness=1, x1=j.planet.x, y1=j.planet.y)
                        lines.append(line)
    
@play.repeat_forever
def do():
    find_shortest_way(planets)
    draw_ways(planets)
    for p in planets:
        p.go()

@play.repeat_forever
async def do1():
    play.set_backdrop( (255, 255, 255) )
    lines.clear()

@play.repeat_forever
async def do2():
    await play.timer(seconds=random())
    for p in planets:
        if randint(1,2) == 1:
            p.create_new_moving()




play.start_program()