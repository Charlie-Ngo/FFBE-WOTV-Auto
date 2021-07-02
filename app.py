import functions as func

def main():
    windowName = 'ONEPLUS A5010'
    func.windowLocationReset(windowName)
    func.time.sleep(1)
    img_rgb = func.cv.imread("images/x.jpg")
    img_gray = func.cv.ctvColor(img_rgb, func.cv.COLOR_BGR2GRAY)
    im1 = func.pgui.screenshot()
    im1.save(r"C:\Users\cshng\OneDrive\Documents\GitHub\FFBE-WOTV-Auto\images\screen.jpg")
    template = func.cv.imread('')



if __name__ == '__main__':
    main()
