# A simple script to do MAthematical calaculation
import time

from pywebio.input import *
from pywebio.output import *


def mathemticaloperation():
    put_text('Future is here')
    img = open('C://automation//Python_project//logo.JPG', 'rb').read()
    put_image(img, width='1080px')
    time.sleep(30)


if __name__ == '__main__':
    mathemticaloperation()