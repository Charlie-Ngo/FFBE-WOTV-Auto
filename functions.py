import pyautogui as pgui
import pygetwindow as gw
import time
import cv2 as cv

def imageLocation(imageFile):
    print('Image File: ',imageFile)
    image = pgui.locateOnScreen(imageFile)
    if image==None:
        print('Image is missing')
    else:
        pgui.moveTo(image[0],image[1])
        pgui.click()

def goBack():
    imageLocation('images/back.png')

def clickX():
    #imageLocation('images/x.png')
    img = cv.imread('images/x.png')
    cv.imshow('x',img)
    
def closeWindow():
    imageLocation('images/close.png')

def mouseLocation():
    position = pgui.position()
    print('Position:', position)

def skipIntro():
    x = 0
    while x < 15:
        pgui.click(1117,77)
        time.sleep(1)
        clickX()
        time.sleep(1)
        closeWindow()
        x = x+1
    
def windowLocationReset(name):
    win = gw.getWindowsWithTitle(name)[0]
    win.activate()
    win.moveTo(0,0)
    win.resizeTo(1280,720)
    return(win)

def windowMid():
    pgui.moveTo(1,1)
    pgui.click(x=(1280/2),y=(720/2))

def exitStartMessages():
    pgui.click(1117,77)

def main():
    name = 'ONEPLUS A5010'
    win = windowLocationReset(name)
#    windowMid()
    exitStartMessages()
    time.sleep(3)
    exitStartMessages()

if __name__ == '__main__':
    main()
