import pygame, Events, Screen

pygame.init()
pygame.event.pump()
Screen.render()

def event_loop():
    while True:
        for event in pygame.event.get():
            if event.type == 5:
                Events.mouse_click(pygame.mouse.get_pos())
            if event.type == 6:
                Events.mouse_release()

event_loop()
