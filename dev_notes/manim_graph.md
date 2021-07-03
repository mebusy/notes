
# Manim Graph

## Basic

```python
from manim import *
import numpy as np

class graphx(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            # range of coordinates system
            x_min= -4,
            x_max= 4,
            y_min= -2,
            y_max= 2,
            # axis label
            x_axis_label= "$x$",
            y_axis_label= "$y$",

            # graph_origin=ORIGI ,
            
            **kwargs
        )

    # Defining graph functions
    def show_function_graph(self):
        # axis with animaton
        self.setup_axes(animate=True)
        # sin function
        func_sin = lambda x: np.sin(x)
        # function graph
        graph_sin = self.get_graph( func_sin, x_min=-np.pi, x_max=np.pi)
        # set graph color
        # graph_sin.set_color(RED)

        self.play( Create(graph_sin) )
        # self.wait(3)  # wait 3 seconds

    def construct(self):
 
```

![](../imgs/manim_graph1.gif)

## Modification

As you see there is a lot of problems, we need do a little bit modification the axis and range.

- To center whole graph scene, use config `graph_origin=ORIGIN`. 
    - ORIGIN is `0*DOwn + 0*LEFT`
- We can set graph color `graph_sin.set_color(RED)`.
- We can set runtime for `play` function
    - `self.play( Create(graph_sin), run_time=4 )`
- And we can use `wait()` function wait some time.
    - `self.wait(3)  # wait 3 seconds`

![](../imgs/manim_graph2.gif)

<details>
<summary>
<b>Modified Code</b>
</summary>

```python
from manim import *
import numpy as np

class graphx(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            # range of coordinates system
            x_min= -4,
            x_max= 4,
            y_min= -2,
            y_max= 2,
            # axis label
            x_axis_label= "$x$",
            y_axis_label= "$y=sin(x)$",
            graph_origin=ORIGIN,
            **kwargs
        )

    # Defining graph functions
    def show_function_graph(self):
        # axis with animaton
        self.setup_axes(animate=True)
        # sin function
        func_sin = lambda x: np.sin(x)
        # function graph
        graph_sin = self.get_graph( func_sin, x_min=-np.pi, x_max=np.pi)
        # set color
        graph_sin.set_color(RED)
        # set runtime
        self.play( Create(graph_sin), run_time=4)
        # wait 3 seconds when play animation is done
        self.wait(3)

    def construct(self):
        self.show_function_graph()
```

</details>


## Two graphs , and Text

Add another graph , and some text.


![](../imgs/manim_2graphs.gif)


<details>
<summary>
<b>Code for 2 graphs</b>
</summary>

```python
from manim import *
import numpy as np

class graphx(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            # range of coordinates system
            x_min= -4,
            x_max= 4,
            y_min= -2,
            y_max= 2,
            # axis label
            x_axis_label= "$x$",
            y_axis_label= "$y$",
            graph_origin=ORIGIN,
            **kwargs
        )

    # Defining graph functions
    def show_function_graph(self):
        # axis with animaton
        self.setup_axes(animate=True)
        # sin function
        func_sin = lambda x: np.sin(x)
        # function graph
        graph_sin = self.get_graph( func_sin, x_min=-np.pi, x_max=np.pi)
        graph_sin.set_color(RED)

        graph_cos = self.get_graph( lambda x:np.cos(x), x_min=-np.pi, x_max=np.pi)
        graph_cos.set_color(YELLOW)

        # graph sin plays first
        self.play( Create(graph_sin), run_time=3)
        self.wait(1)
        self.play( Create(graph_cos), run_time=3)
        self.wait(1)

        # Adding text
        text1 = Text('y=Sine(x) .. y=Cos(x)')
        # where place ?
        text1.next_to( graph_cos, UP )
        text1.set_color(BLUE)
        self.play(Write(text1))

    def construct(self):
        self.show_function_graph()
```

</details>

## Make a thumnail picture

![](../imgs/manim_makethumb.gif)

```python
    ...

    def thumbnail(self):
        picture = Group(*self.mobjects) 
        # move 2 left screen, the BUFF value is the margin to left edge
        picture.scale(0.6).to_edge( LEFT, buff=SMALL_BUFF )

        text = Text( 'Manim' ).next_to(picture, RIGHT)
        text.shift(DOWN*0.7)
        self.play( Create(text) )
        self.wait(1)

    def construct(self):
        self.show_function_graph()
        self.thumbnail()
```





