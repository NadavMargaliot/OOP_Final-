import pygame
from pygame import *

background = "/Users/adielbenmeir/Desktop/pics_Ex4/battle_field.jpeg"
pokeball = "/Users/adielbenmeir/Desktop/pics_Ex4/pokeball2.png"
bulbasaur = "/Users/adielbenmeir/Desktop/pics_Ex4/bulbasaur.png"


background_img = image.load(background)
# init pygame
WIDTH, HEIGHT = 1080, 720
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)