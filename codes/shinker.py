#!python3

from PIL import Image
import sys
import os
import shutil

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python shinker.py <image path> <newWidth> <numberColor>")
        print(
            "if newWidth <= 0, newWidth = width, if numberColor <= 0, numberColor = 256"
        )
        sys.exit(1)

    numberColor = 256
    imagePath = sys.argv[1]
    newWidth = int(sys.argv[2])

    if len(sys.argv) == 4:
        numberColor = int(sys.argv[3])
        if numberColor <= 0:
            numberColor = 256

    if not os.path.exists(imagePath):
        print("Image file not found")
        sys.exit(1)

    image = Image.open(imagePath)
    width, height = image.size

    if newWidth <= 0:
        newWidth = width

    newHeight = int(newWidth * height / width)
    # print("Resizing image to %sx%s pixels" % (newWidth, newHeight))
    image = image.resize((newWidth, newHeight))

    # convert ot pallete image, and limit the number of colors to numberColor
    image = image.convert("P", palette=Image.Palette.ADAPTIVE, colors=numberColor)

    ppath, ext = os.path.splitext(imagePath)
    newPath = ppath + "_s" + ext
    image.save(newPath)

    # if platform is darwin
    if sys.platform == "darwin":
        cmd = 'mdfind -onlyin /Volumes/WORK/  "kind:folder" -name "imgs"   2>/dev/null | grep "_notes/imgs" '
        # excute  cmd , and capture the output
        distPath = os.popen(cmd).read().strip()
        if distPath and os.path.exists(distPath):
            # move image to distPath
            fullDistPath = os.path.join(distPath, os.path.basename(newPath))
            shutil.move(newPath, fullDistPath)
            print("Image moved to %s" % fullDistPath)
            sys.exit(0)

    print("Image saved at %s" % newPath)
