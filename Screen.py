import pygame, os
import Images as im

windowSize = width, height = 1024, 768
os.environ['SDL_VIDEO_CENTERED'] = '1'
path = os.path.realpath(os.path.expanduser('res'))
screen = pygame.display.set_mode(windowSize, pygame.NOFRAME)
posDict = {"frame" : (420, 310),
               "power" : (width-75, 75),
               "upload" : (250, height-140),
               "score" : (585, height-140),
               "tensDig" : (width-190, 275),
               "onesDig" : (width-90, 275)}

background = pygame.image.load(path + "/Background.png")

emptyFrame = im.Button(path + "/Empty_Picture_Frame.png", posDict["frame"], False)
filledFrame = im.Sprite(path + "/Filled_Picture_Frame.png", (emptyFrame.pos))
imageFile = im.Sprite(path + "/Test_Image.jpg", (emptyFrame.pos))

powerButton = im.Button(path + "/buttons/Power.png", posDict["power"])
uploadButton = im.Button(path + "/buttons/Upload.png", posDict["upload"])
getScoreButton = im.Button(path + "/buttons/Get_Score.png", posDict["score"])

pressedGetScoreButton = im.Sprite(path + "/buttons/Pressed_Get_Score.png", (getScoreButton.pos))
pressedPowerButton = im.Sprite(path + "/buttons/Pressed_Power.png", (powerButton.pos))
pressedUploadButton = im.Sprite(path + "/buttons/Pressed_Upload.png", (uploadButton.pos))

numZero = im.Sprite(path + "/nums/Zero.png")
numOne = im.Sprite(path + "/nums/One.png")
numTwo = im.Sprite(path + "/nums/Two.png")
numThree = im.Sprite(path + "/nums/Three.png")
numFour = im.Sprite(path + "/nums/Four.png")
numFive = im.Sprite(path + "/nums/Five.png")
numSix = im.Sprite(path + "/nums/Six.png")
numSeven = im.Sprite(path + "/nums/Seven.png")
numEight = im.Sprite(path + "/nums/Eight.png")
numNine = im.Sprite(path + "/nums/Nine.png")

def render():
    screen.blit(background, background.get_rect())
    for i in initialRenders:
        screen.blit(i.image, i.rect)
    pygame.display.flip()

def update_image(imageSprite):
    screen.blit(imageSprite.image, imageSprite.rect)
    pygame.display.update(imageSprite.rect)

def update_frame():
    if emptyFrame.enabled:
        update_image(emptyFrame)
        emptyFrame.enabled = False
    else:
        update_image(filledFrame)
        emptyFrame.enabled = True

def get_nums(numPath, pos):
    return im.Sprite(path + numPath, pos)

def display_score(score):
    tens = get_nums(numDict[score[:1]], posDict["tensDig"])
    ones = get_nums(numDict[score[1:2]], posDict["onesDig"])
    update_image(tens)
    update_image(ones)

def clear_screen():
    pygame.display.quit()

initialRenders = [emptyFrame, powerButton, uploadButton,
                  getScoreButton]
buttonDict = {powerButton : pressedPowerButton,
              uploadButton : pressedUploadButton,
              getScoreButton : pressedGetScoreButton,
              emptyFrame : filledFrame}
numDict = {'0' : "/nums/Zero.png", '1' : "/nums/One.png",
           '2' : "/nums/Two.png", '3' : "/nums/Three.png",
           '4' : "/nums/Four.png", '5' : "/nums/Five.png",
           '6' : "/nums/Six.png", '7' : "/nums/Seven.png",
           '8' : "/nums/Eight.png", '9' : "/nums/Nine.png"}
