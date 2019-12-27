...menustart

 - [Trim Image Whitespace](#044b8396fbd6ae9de3416b0b6ac5322a)
     - [RGB 2 HLS](#e347469f9fd55367a3a83c5761256a2c)

...menuend


<h2 id="044b8396fbd6ae9de3416b0b6ac5322a"></h2>


# Trim Image Whitespace

```python
from PIL import Image, ImageColor, ImageEnhance, ImageChops

def trim(im):
    R,G,B,A = im.split()
    bg = Image.new( A.mode, A.size, A.getpixel((0, 0)))
    diff = ImageChops.difference(A, bg)
    bbox = diff.getbbox()
    if not bbox:
        return im
    return im.crop(bbox)
```

<h2 id="e347469f9fd55367a3a83c5761256a2c"></h2>


## RGB 2 HLS

```python
def rgb2hls(t):
    """ convert PIL-like RGB tuple (0 .. 255) to colorsys-like
    HSL tuple (0.0 .. 1.0) """
    r,g,b,a = t
    r /= 255.0
    g /= 255.0
    b /= 255.0
    return rgb_to_hls(r,g,b)

def hls2rgb(t):
    """ convert a colorsys-like HSL tuple (0.0 .. 1.0) to a
    PIL-like RGB tuple (0 .. 255) """
    r,g,b = hls_to_rgb(*t)
    r *= 255
    g *= 255
    b *= 255
    return (int(r),int(g),int(b))
```
