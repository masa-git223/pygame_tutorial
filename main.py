# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import math
import sys
import pygame.mixer
import datetime

#画面サイズ
pygame.init()
SCREEN = Rect(0,0,400,400)
SURFACE=pygame.display.set_mode((500,500))
pygame.display.set_caption("デジタル時計")

def main():
    while True:
        SURFACE.fill("Black")

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__=="__main__":
    main()