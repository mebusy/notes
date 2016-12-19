

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
