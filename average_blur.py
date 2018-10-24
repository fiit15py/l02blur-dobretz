from PIL import Image
import numpy as np

def average_blur(img, r):
    w, h = img.size
    a = np.array(img.getdata(), dtype=np.uint8).reshape(h, w)
    b = np.zeros((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            s = 0.
            up, bt = max(i-r,0), min(i+r+1,h)
            lf, rt = max(j-r,0), min(j+r+1,w)
            n = (bt-up)*(rt-lf)
            for y in range(up,bt):
                for x in range(lf,rt):
                    s += a[y,x]
            b[i,j] = s / n
    return Image.fromarray(b)

img = Image.open('darwin.png')
img.load()

print("Image size:", img.size)
print("Image mode:", img.mode)

average_blur(img,4).save('darwin2.png')