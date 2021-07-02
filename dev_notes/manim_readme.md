<h2 id="cbcd3fecff4c0ef0c063f8c41726d34a"></h2>


# Manim

There are 2 versions of manim.  One is created by [Grant](https://github.com/3b1b/manim) , and one is forked and maintained by the [Manim Community](https://github.com/ManimCommunity/manim).

Manim Community's version is updated more frequently and better tested than Grant’s version.


<h2 id="05bff63b61f38b96b6f040dfdfc00fa4"></h2>


## Quick Start

create a python file `test_scene.py`

```python
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
```

run manim ( docker ), render video in low quality.

```bash
$ docker run --rm -it  --user="$(id -u):$(id -g)" -v "$(pwd)":/manim manimcommunity/manim:stable manim test_scene.py SquareToCircle -ql
```

Pretty long command ...

To save life, on linux or OSX, you can create a bash function in your bash profile file to later use

```bash
function manim() {
    docker run --rm -it  --user="$(id -u):$(id -g)" -v "$(pwd)":/manim manimcommunity/manim:stable manim $@
}
```

Life becomes easy ...

```bash
$ manim test_scene.py SquareToCircle -ql
...
    File ready at /manim/media/videos/test_scene/480p15/SquareToCircle.mp4   
```

But can use `-p` parameter to play video right after things done when we use docker manin.

Solution on OSX:

Create a python3 script mplay.py

```python
#!python3
import sys
import re

RE_DST_FILE = re.compile( r'File ready at /manim\/(.+?\.(?:mp4|gif))' )
RE_COLOR_TAG = re.compile( r'\[\d+(;\d+)?m' )

if __name__=="__main__":
    output=""
    for line in sys.stdin:
        # output stderr, so wont pass to next pipe
        print(line, end="", file=sys.stderr )
        output += line.strip()

    output = RE_COLOR_TAG.sub("",output)


    all_mp4 = RE_DST_FILE.findall( output )
    # output 1st video
    if len(all_mp4) > 0 :
        print( all_mp4[0])
```

```bash
$ chmod +x mplay.py
$ cp mplay.py /usr/local/bin/
$ manim test_scene.py SquareToCircle -ql | mplay.py | xargs open 
```

## Get Start

### Create a Blue Square that Grows from the Center

![](../imgs/manim_point2square.gif)

```python
# start.py
from manim import *

class PointMovingOnShapes(Scene):
    def construct(self):
        square = Square(color=BLUE) # Create a square
        square.flip(RIGHT) # Flip the square to the right
        square.rotate(-3 * TAU / 8) # Rotate the square -3/8 * 2*PI

         # Play the animation of a square growing from the center
        self.play(GrowFromCenter(square))
```

- A class that derives from `Scene`
    - `construct` method

```bash
$ manim -ql start.py PointMovingOnShapes | mplay.py | xargs open
```

- `-ql` means quality low

### create a gif

- `-i` create a Gif instead of video

```bash
$ manim -i -ql start.py PointMovingOnShapes | mplay.py 
media/videos/start/480p15/PointMovingOnShapes_ManimCE_v0.7.0.gif
```

### Turn a Square into a Circle, with rotate and flip

![](../imgs/manim_square2circle.gif)

```python
from manim import *

class PointMovingOnShapes(Scene):
    def construct(self):

        # Create a square
        square = Square(color=BLUE)
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)

        # Create a circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5) # set the color and transparency

        # Create animations
        self.play(GrowFromCenter(square))
        self.play(Transform(square, circle))  # turn the square into a circle

        self.wait() # wait for some seconds
```


### List of Manim Shapes

[list of manim shapes](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.html#module-manim.mobject.geometry)

### Customize Manim

- change backgroud color
    ```python
    from manim import *

    config.background_color = YELLOW
    ```
    - ![](../imgs/manim_square2circle2.gif)

### Manim Configurations

- [manim configuration](https://docs.manim.community/en/stable/tutorials/configuration.html)



<h2 id="52ef9633d88a7480b3a938ff9eaa2a25"></h2>


## Others

Tutorial using Grant version manim. Not recommended.

1. [Installation & FAQ](manim_FAQ.md)
2. [Tutorial](manim_1.md)
3. [leTax,Array,CrossText](manim_2.md)
4. [Transformations](manim_4.md)
5. [graph scene,Path,Sound,SVG,Image](manim_6.md)
6. [Animation, Rate Func](manim_8.md)



