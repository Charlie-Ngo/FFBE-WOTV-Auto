import functions as func

print(func.pgui.position())
x = func.pgui.locateOnScreen('images/x.png')
print(x)
if x==None:
    print('There is no X on the screen')

    