import os
import random
import pygame
import time


class Settings():
    window_width = 1280
    window_height = 540
    fps = 60
    title = "PyFighter"
    path = {}
    path['file'] = os.path.dirname(os.path.abspath(__file__))
    path['image'] = os.path.join(path['file'], "images")
    Speed = 3

    @staticmethod
    def dim():
        return (Settings.window_width, Settings.window_height)

    @staticmethod
    def filepath(name):
        return os.path.join(Settings.path['file'], name)

    @staticmethod
    def imagepath(name):
        return os.path.join(Settings.path['image'], name)

    #health bar
    Health_Bar1 = 100
    Health_Bar2 = 100

    #1st players health bar
    Health_Bar1 = 10
    Health_Bar1.ht()
    Health_Bar1.speed(0)
    Health_Bar1.color("yellow")
    Health_Bar1.penup()
    Health_Bar1.goto(50,220)
    Health_Bar1.pendown()
    #2nd players health bar
    Health_Bar2 = 10
    Health_Bar2.ht()
    Health_Bar2.speed(0)
    Health_Bar2.color("yellow")
    Health_Bar2.penup()
    Health_Bar2.goto(-50,220)
    Health_Bar2.left(180)
    Health_Bar2.pendown()

class Timer(object):
    def __init__(self, duration, with_start = True):
        self.duration = duration
        if with_start:
            self.next = pygame.time.get_ticks()
        else:
            self.next = pygame.time.get_ticks() + self.duration

    def is_next_stop_reached(self):
        if pygame.time.get_ticks() > self.next:
            self.next = pygame.time.get_ticks() + self.duration
            return True
        return False

    def change_duration(self, delta=10):
        self.duration += delta
        if self.duration < 0:
            self.duration = 0

class player_1(pygame.sprite.Sprite):
    def __init__(self, Picturefile):
        super().__init__()
