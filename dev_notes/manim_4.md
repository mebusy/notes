
# Manim 4 : Transformations

## 4.1 Transformations

```python
class TransformationText1V1(Scene):
    def construct(self):
        texto1 = TextMobject("First text")
        texto2 = TextMobject("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1,texto2))
        self.wait()
```

- `Transform(M1,M2)`
    - M1 transfrom from M1 to M2, M2 is unchanged
        - the ojbect that we see on the screen is M1 all the times
    - 
    ```python
    self.play(Transform(M1,M2))
    self.wait()
    self.play(Transform(M1,M3))
    self.wait()
    self.play( FadeOut(M1) )
    ```
- `ReplacementTransform(M1,M2)`
    - M1 transforms from M1 to M2, after transformation, M1 is hidden it has been replace by M2. 
        - you normally need `.copy()` when u are using ReplaceTransform
    - 
    ```python
    self.play(ReplacementTransform(M1,M2))
    self.wait()
    self.play(ReplacementTransform(M2,M3))
    self.wait()
    self.play( FadeOut(M3) )
    ```


### Change Property Animation

```python
class ChangeTextColorAnimation(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.scale(3)
        self.play(Write(text))
        self.wait()
        self.play(
                text.set_color, YELLOW,
                run_time=2
            )
        self.wait()

class ChangeSizeAnimation(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.scale(2)
        self.play(Write(text))
        self.wait()
        self.play(
                text.scale, 3,
                run_time=2
            )
        self.wait()

class ChangeColorAndSizeAnimation(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.scale(2)
        text.shift(LEFT*2)
        self.play(Write(text))
        self.wait()
        self.play(
                text.shift, RIGHT*2,
                text.scale, 2,
                text.set_color, RED,
                run_time=2,
            )
        self.wait()

class ChangeColorAndSizeAnimation2(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.scale(2)
        text.shift(LEFT*2)
        self.play(Write(text))
        self.wait()

        text.generate_target()
        text.target.shift( RIGHT*2 )
        text.target.scale(2)
        text.target.set_color(RED)
        self.play(
                MoveToTarget(text),
                run_time=2,
            )
        self.wait()
```









