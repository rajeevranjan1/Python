from PIL import Image, ImageGrab
from numpy import asarray
def takeScreenshot():
    sshot = ImageGrab.grab()
    return sshot

def draw(image,redness=0):
    data=image.load()
    for i in range(1920):
        for j in range(1080):
            data[i,j]=(redness,j%255,i%255)
    image.show()

def box(image,x=800,y=600,color='black'):
    color=color.lower()
    if color=='red':
        mode=(255,0,0)
    elif color == 'green':
        mode=(0,255,0)
    elif color == 'blue':
        mode=(0,0,255)
    else:
        mode = 0
    
    data=image.load()
    for i in range(x):
        for j in range(y):
            data[i,j]=mode
    image.show()

def pixelise(image):
    data=image.load()
    for i in asarray(image):
        print(i)

if __name__=='__main__':
    image=takeScreenshot()
    #draw(image,200)
    #box(image,x=1200,y=300)
    pixelise(image)

    
