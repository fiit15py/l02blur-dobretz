# -*- coding: utf-8 -*-

from PIL import Image
from math import pi
import numpy as np
import sys

def gauss(filename, r):
    # должна обрабатывать файл filename гауссовым размытием в квадрате [-r, +r] x [-r, +r]
    # и записывать результат в <filename>.gaussblurred.png
    img = Image.open(filename)
    img.load()

    dx, dy = np.meshgrid(np.arange(-r, +r+1, 1.), np.arange(-r, +r+1, 1.0))
    sigma = 0.38*r
    gauss_dist = np.exp( -(dx*dx+dy*dy)/(2*sigma**2) ) / (2*pi*sigma**2)
    coeff = gauss_dist / np.sum(gauss_dist)

    for i in range(2*r+1):
        for j in range(2*r+1):
            print('{:.03f}'.format(gauss_dist[i,j]),end='')
        print()

    w, h = img.size
    a = np.array(img.getdata(), dtype=np.uint8).reshape(h, w)
    b = np.zeros((h, w), dtype=np.uint8)
    for i in range(r+1,h-r-1-2700):
        for j in range(r+1,w-r-1-2700):
            for k in range(-r,r+1):
                for m in range(-r,r+1):
                    b[i,j] += coeff[k+r,m+r] * a[i+k,j+m]
    # код сюда ....
    newimg = Image.fromarray(b)
    newimg.show()
    newimg.save(filename+'.gaussblurred.png')


if __name__=='__main__':
    # Запускать с командной строки с аргументом <имя файла>, например: python gauss.py darwin.png
    if len(sys.argv) > 1:
        gauss(sys.argv[1], 3)
    else:
        print("Must give filename.\n")