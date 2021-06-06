# A simple script to do display message and logo
import time
from pywebio.input import *
from pywebio.output import *


def mathemticaloperation():
    put_text('DEVCLOUD')
    img = open("intel.JPG", 'rb').read()
    put_image(img, width='1080px')
    time.sleep(30)


if __name__ == '__main__':
    mathemticaloperation()
