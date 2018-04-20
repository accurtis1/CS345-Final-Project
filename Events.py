import sys, pygame, ApiRadio
import Screen as s

api = ApiRadio.Api()

def mouse_click(pos):
    for button in s.buttonDict:
        if button.rect.collidepoint(pos):
            press_button(button)

def mouse_release():
    for button in s.buttonDict:
        if button.pressed:
            release_button(button)

def press_button(button):
    if button.enabled:
        s.update_image(s.buttonDict[button])
        button.pressed = True

def release_button(button):
    s.update_image(button)
    button.pressed = False
    eventDict[button]()

def shut_down():
    s.clear_screen()
    sys.exit()

#
def upload_image():
    s.update_image(s.imageFile)
    s.update_frame()

def get_score():
    if s.emptyFrame.enabled:
        # To prevent sending too many calls to the API
        #score = api.get_score_from_file(s.imageFile.imageName)
        score = 33.145
        s.display_score(str(score))
        s.update_frame()
    else:
        pass

eventDict = {s.powerButton : shut_down,
             s.uploadButton : upload_image,
             s.getScoreButton : get_score}
