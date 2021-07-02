<h2 id="cbcd3fecff4c0ef0c063f8c41726d34a"></h2>


# Manim

There are 2 versions of manim.  One is created by [Grant](https://github.com/3b1b/manim) , and one is forked and maintained by the [Manim Community](https://github.com/ManimCommunity/manim).

Manim Community's version is updated more frequently and better tested than Grant’s version.


<h2 id="05bff63b61f38b96b6f040dfdfc00fa4"></h2>


## Quick Starting

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

Too long command ...

To save life, on linux of OSX, you can create a bash function to later use 

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





<h2 id="52ef9633d88a7480b3a938ff9eaa2a25"></h2>


## Others

Tutorial using Grant version manim. Not recommended.

1. [Installation & FAQ](manim_FAQ.md)
2. [Tutorial](manim_1.md)
3. [leTax,Array,CrossText](manim_2.md)
4. [Transformations](manim_4.md)
5. [graph scene,Path,Sound,SVG,Image](manim_6.md)
6. [Animation, Rate Func](manim_8.md)



