[](...menustart)

- [Manim Draw Logo](#b857c3961e456ecc256a9092dd83255b)

[](...menuend)


<h2 id="b857c3961e456ecc256a9092dd83255b"></h2>

# Manim Draw Logo


![](../imgs/manim_mylogo.gif)

```python
from manim import *

class MyLogo(Scene):
    def construct(self):
        # create logo
        circle_logo = Circle( fill_opacity = 0.5 ).scale(2)
        circle_logo.set_fill()
        circle_logo.set_color(BLUE)

        text1 = Text( "Ap i X" )
        text1[:2].set_color(YELLOW)
        text1.next_to( circle_logo, ORIGIN , buff=0 ).scale(2)

        # play logo
        self.play(
            DrawBorderThenFill( circle_logo, run_time=6 ) ,
            Write(text1, run_time =6 )
        )
        self.wait(1)

```


