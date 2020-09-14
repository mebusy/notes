...menustart

- [Manim tutorial 1](#fa8eae884562efa031678a4f969634c7)
    - [1.1 Basic elements](#b1ca84327953e47e438a77e1dfbdceb1)
    - [1.2 Animations and pauses](#028178975b2d3dfe503d769da4acc4a5)
    - [1.3 Positions, rotations and fonts](#be289a13773875e5f0f91d2b57183105)
    - [1.4 Render Setting](#c407b4893110cfbf424118ba9d7c140e)

...menuend


<h2 id="fa8eae884562efa031678a4f969634c7"></h2>


# Manim tutorial 1

<h2 id="b1ca84327953e47e438a77e1dfbdceb1"></h2>


## 1.1 Basic elements


```python
from manimlib.imports import *
class NameOfScene(Scene):
    def construct(self):
        # Animation progress
```

<h2 id="028178975b2d3dfe503d769da4acc4a5"></h2>


## 1.2 Animations and pauses

```python
    def construct(self):
        text = TextMobject("another text")
        self.play( Write(text), run_time=3)  # play anim
        self.wait(3) # pause
```

- other animations
    - GrowFromCenter 
    - FadeIn
    - ...
    - more: `manimlib/animation/creation.py`
- `self.remove` to remove an object

<h2 id="be289a13773875e5f0f91d2b57183105"></h2>


## 1.3 Positions, rotations and fonts

- positions 
    1. Abs postions
        1. `.to_edge()` to place an object on the sides of screen
            - i.e. `obj.to_edge(UP)`,  UP = np.array( [0,1.0] )
        2. `.to_corner()`  to place an object on the corner
            - i.e. `obj.to_corner(DR)` , DR = np.array( [1,-1.0]) = UP + RIGHT
    2. Relative postions
        1. `.move_to([ vector|obj ])`  # from center of obj
        2. `next_to(obj, vector, buff=x)`  # from the edge of obj
        3. `shift(vector)`  # move 1 unit
- rotation
    - `.rotate( radians, about_point = coord )`  
        - or you can use `.rotate( n * DEGREES )`
    - `.flip(vector)`  , i.e. `.flip(UP)`
- font
    - 
    ```python
    class TextFonts(Scene):
        def construct(self):
            textNormal = TextMobject("{Roman serif text 012.\\#!?} Text")
            textItalic = TextMobject("\\textit{Italic text 012.\\#!?} Text")
            textTypewriter = TextMobject("\\texttt{Typewritter text 012.\\#!?} Text")
            textBold = TextMobject("\\textbf{Bold text 012.\\#!?} Text")
            textSL = TextMobject("\\textsl{Slanted text 012.\\#!?} Text")
            textSC = TextMobject("\\textsc{Small caps text 012.\\#!?} Text")
            textNormal.to_edge(UP)
            textItalic.next_to(textNormal,DOWN,buff=.5)
            textTypewriter.next_to(textItalic,DOWN,buff=.5)
            textBold.next_to(textTypewriter,DOWN,buff=.5)
            textSL.next_to(textBold,DOWN,buff=.5)
            textSC.next_to(textSL,DOWN,buff=.5)
            self.add(textNormal,textItalic,textTypewriter,textBold,textSL,textSC)
            self.wait(3)
    ```


- to bring the objects closer to the edges of screen you have to modify the `buff` parameter.
    - `.to_edge( DIRECTION, buff=NUMBER )` 
- screen grid 
    - 
    ```python
    grid=ScreenGrid() # ScreenGrid(rows=ROWS, columns=COLUMNS)
    self.add(grid,obj)
    ```

<h2 id="c407b4893110cfbf424118ba9d7c140e"></h2>


## 1.4 Render Setting

option | fps | width | height
--- | --- | --- | ---
l | 15 | 854 | 480
m | 30 | 1280 | 720
· | 60 |  2560 | 1440

- To specify the video height use:  `-r HEIGHT`
- To sepcify both width,height , use:  `-r HEIGHT,WIDTH` (caution: height first)
- To render a video with alpha channel (with transparency) use: `-t`
- Suppose your scenen is very long, then, to render only a section of the animation, you can use:
    - `-n START` , or, `-n START,END+1`
    - START to specify the command index of `play`,`wait` instruction, start from 0.


-----

- object type
    - Dot
    - TextMobject



