[](...menustart)

- [Manim Integral](#6ea9733a7e6af5cd29933b5f3b8c99d5)

[](...menuend)


<h2 id="6ea9733a7e6af5cd29933b5f3b8c99d5"></h2>

# Manim Integral

A simple curve

![](../imgs/manim_integral.gif)


<details>
<summary>
<b>Code</b>
</summary>

```python
from manim import *
import numpy as np

class Integral(GraphScene):
    # instead of call GraphScene.__init__ to change setting
    # we can also use CONFIG
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5
    }

    def construct(self):
        self.show_function_graph()

    def show_function_graph(self):
        self.setup_axes(animate=True)

        # curve
        def func(x):
            return 0.1 * (x+3-5) * (x-3-5) * (x-5) + 5
        graph = self.get_graph(func, x_min=0.2, x_max=9, color=YELLOW)
        self.play( Create(graph), run_time=3  )
        self.wait(1)
```

</details>


Riemann 

![](../imgs/manim_integral2.gif)


<details>
<summary>
<b>Code</b>
</summary>

```python
from manim import *
import numpy as np

class Integral(GraphScene):
    # instead of call GraphScene.__init__ to change setting
    # we can also use CONFIG
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5
    }

    def construct(self):
        self.show_function_graph()

    def show_function_graph(self):
        self.setup_axes(animate=True)
        def func(x):
            return 0.1 * (x+3-5) * (x-3-5) * (x-5) + 5
        # curve
        graph = self.get_graph(func, x_min=0.2, x_max=9, color=YELLOW)
        self.play( Create(graph), run_time=3  )

        # adding reimann rectangle
        kwargs = {
            "x_min": 2,
            "x_max": 8,
            "fill_opacity": 0.75,
            "stroke_width": 0.25,
        }

        iteractions = 6

        self.rect_list = self.get_riemann_rectangles_list(
            graph, iteractions, start_color= PURPLE, end_color= ORANGE, **kwargs
        )

        flat_rects = self.get_riemann_rectangles(
            self.get_graph(lambda x: 0), dx=0.5,
                start_color=invert_color(PURPLE), end_color=invert_color(ORANGE),
                **kwargs
        )

        rects = self.rect_list[0] # define the size of rectangles
        self.transform_between_riemann_rects(
            flat_rects, rects, replace_mobject_with_target_in_scene = True,
            run_time = 0.9
        )

        self.wait(1)
```

</details>

We can change the size of rectangles , e.g.

```python
rects = self.rect_list[2] # define the size of rectangles
```

![](../imgs/manim_integral3.gif)

We can play with that by using a for loop.

![](../imgs/manim_integral_4.gif)


<details>
<summary>
<b>Code</b>
</summary>

```python
from manim import *
import numpy as np

class Integral(GraphScene):
    # instead of call GraphScene.__init__ to change setting
    # we can also use CONFIG
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5
    }

    def construct(self):
        self.show_function_graph()

    def show_function_graph(self):
        self.setup_axes(animate=True)
        def func(x):
            return 0.1 * (x+3-5) * (x-3-5) * (x-5) + 5
        # curve
        graph = self.get_graph(func, x_min=0.2, x_max=9, color=YELLOW)
        self.play( Create(graph), run_time=3  )

        # adding reimann rectangle
        kwargs = {
            "x_min": 2,
            "x_max": 8,
            "fill_opacity": 0.75,
            "stroke_width": 0.25,
        }

        iteractions = 6

        self.rect_list = self.get_riemann_rectangles_list(
            graph, iteractions, start_color= PURPLE, end_color= ORANGE, **kwargs
        )

        flat_rects = self.get_riemann_rectangles(
            self.get_graph(lambda x: 0), dx=0.5,
                start_color=invert_color(PURPLE), end_color=invert_color(ORANGE),
                **kwargs
        )

        rects = self.rect_list[0] # define the size of rectangles
        self.transform_between_riemann_rects(
            flat_rects, rects, replace_mobject_with_target_in_scene = True,
            run_time = 0.9
        )

        for i in range(1,iteractions):
            self.transform_between_riemann_rects(
                self.rect_list[i-1], self.rect_list[i], dx= 0.5,
                replace_mobject_with_target_in_scene = True,
                run_time = 0.9
            )

        self.wait(1)
```

</details>



