
# Manim 2 : Tex Forumulas

[useful latex tools](https://www.codecogs.com/latex/eqneditor.php)

```python
class Formula(Scene):
    def construct(self):
        # caution: it is TexMobject
        formula_tex=TexMobject(r"\lim_{x\rightarrow 0} \frac{ f(x+h) - f(x)  }{h}" )
        formula_tex.scale(2)
        self.add(formula_tex)

        # if u want to create with a TextMobject
        # then u must encapsulate the latex with `$`
        formula_tex2=TextMobject(r"$\lim_{x\rightarrow 0} \frac{ f(x+h) - f(x)  }{h}$" )
        formula_tex2.to_edge(DOWN)
        self.add(formula_tex2)

        self.wait(3)
```

# Manim 3: Array


```python
class TextColor( Scene ):
    def construct(self):
        text = TextMobject( "A","B","C","D","E","F" )
        text[0].set_color(RED)
        text[1].set_color("#00FF00")
        text[3].set_color(ORANGE)

        self.play(Write(text))
        self.wait(3)
```

- color constant :  `manimlib/constants.py`

```python
class TextColor( Scene ):
    def construct(self):
        text = TexMobject( "x", "=", "{a" , "\\over", "b}"  )
        text[0].set_color(RED)
        text[2].set_color("#00FF00")
        text[4].set_color(ORANGE)
        text.set_color_by_tex( "=" , YELLOW )
        self.play(Write(text))
        self.wait(3)
```


### Cross Text

```python
class CrossText1(Scene):
    def construct(self):
        text = TexMobject("\\sum_{i=1}^{\\infty}i","=","-\\frac{1}{2}")
        cross = Cross(text[2])
        cross.set_stroke(RED, 6)
        self.play(Write(text))
        self.wait(.5)
        self.play(ShowCreation(cross))
        self.wait(2)
```





