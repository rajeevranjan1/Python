from PIL import Image, ImageGrab
from numpy import asarray
def takeScreenshot():
    sshot = ImageGrab.grab()
    return sshot

if __name__=='__main__':
    image=takeScreenshot()
    data=image.load()
print(asarray(data)
    for i in range(1920):
        for j in range(1080):
            data[i,j]=(i)%255

    image.show()