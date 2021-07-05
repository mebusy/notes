# Manim Text

There are two different ways by which you can render Text in videos:

1. Using Pango ( [text_mobject](https://docs.manim.community/en/stable/reference/manim.mobject.svg.text_mobject.html#module-manim.mobject.svg.text_mobject) )
    - use either Text or MarkupText
2. Using LaTex ( [tex_mobject](https://docs.manim.community/en/stable/reference/manim.mobject.svg.tex_mobject.html#module-manim.mobject.svg.tex_mobject) )
    - be used when you need mathematical typesetting


## Text Without LaTeX


### MarkupText

![](../imgs/manim_markuptext1.png)

```python
from manim import *

class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED)
        self.add(text)
```


### Font Weight

![](../imgs/manim_font_weights.png)

```python
from manim import *

class DifferentWeight(Scene):
    def construct(self):
        import manimpango

        g = VGroup()
        weight_list = dict(sorted({weight: manimpango.Weight(weight).value for weight in manimpango.Weight}.items(), key=lambda x: x[1]))
        for weight in weight_list:
            g += Text(weight.name, weight=weight.name, font="Open Sans")
        self.add(g.arrange(DOWN).scale(0.5))
```

### Text To Color t2c

![](../imgs/manim_text_t2c.png)


```python
from manim import *

class Textt2cExample(Scene):
    def construct(self):
        t2cindices = Text('Hello', t2c={'[1:-1]': BLUE}).move_to(LEFT)
        t2cwords = Text('World',t2c={'rl':RED}).next_to(t2cindices, RIGHT)
        self.add(t2cindices, t2cwords)
```


### Gradients

![](../imgs/manim_text_gradient.png)

```python
from manim import *

class GradientExample(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, BLUE, GREEN)).scale(2)
        self.add(t)
```


### Text To Gradient t2g

![](../imgs/manim_text_t2g.png)

```python
from manim import *

class t2gExample(Scene):
    def construct(self):
        t2gindices = Text(
            'Hello',
            t2g={
                '[1:-1]': (RED,GREEN),
            },
        ).move_to(LEFT)
        t2gwords = Text(
            'World',
            t2g={
                'World':(RED,BLUE),
            },
        ).next_to(t2gindices, RIGHT)
        self.add(t2gindices, t2gwords)
```

### Interating 

Text objects behave like VGroups. Therefore, you can slice and index the text.

![](../imgs/manim_text_iter_color.png)

```python
from manim import *

class IterateColor(Scene):
    def construct(self):
        text = Text("Colors").scale(2)
        for letter in text:
            letter.set_color(random_bright_color())
        self.add(text)
```


## Text With LaTeX

### MathTex

Everything passed to [MathTex](https://docs.manim.community/en/stable/reference/manim.mobject.svg.tex_mobject.MathTex.html#manim.mobject.svg.tex_mobject.MathTex) is in math mode by default.

To be more precise, MathTex is processed within an `align*` environment.  You can achieve a similar effect with [Tex](https://docs.manim.community/en/stable/reference/manim.mobject.svg.tex_mobject.Tex.html#manim.mobject.svg.tex_mobject.Tex) by enclosing your formula with `$` symbols:  e.g. `$\xrightarrow{x^6y^8}$`

![](../imgs/manim_mathtex.png)

```python
from manim import *

class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}").scale(2)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$").scale(2)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))
```


### LaTeX commands and keyword arguments

We can use any standard LaTeX commands in the AMS maths packages. Such as the *mathtt* math-text type or the *looparrowright* arrow.

Some commands require special packages to be loaded into the TeX template. For example, to use the *mathscr* script, we need to add the *mathrsfs* package.  Since this package isn’t loaded into Manim’s tex template by default, we have to add it manually.

![](../imgs/manim_addtexpackage.png)

```python
from manim import *

class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', color=BLUE).scale(1.5)
        self.add(tex)

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(r'$\mathscr{H} \rightarrow \mathbb{H}$}', tex_template=myTemplate).scale(2)
        tex.shift( DOWN * 3 )
        self.add(tex)
```

### Substrings and parts

The TeX mobject can accept multiple strings as arguments. 

![](../imgs/manim_tex_sub_str.png)

```python
from manim import *

class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX').scale(3)
        tex.set_color_by_tex('e', RED)
        self.add(tex)
```

Note that set_color_by_tex() colors the entire substring containing the Tex.

---

![](../imgs/manim_tex_sub_str2.png)

```python
from manim import *

class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex("x", RED)
        self.add(equation)
```

By setting substring_to_isolate to x, we split up the MathTex into substrings automatically and isolate the x components into individual substrings.

Note that Manim also supports a custom syntax that allows splitting a TeX string into substrings easily: simply enclose parts of your formula that you want to isolate with double braces. In the string MathTex(r"{{ a^2 }} + {{ b^2 }} = {{ c^2 }}"), the rendered mobject will consist of the substrings a^2, +, b^2, =, and c^2. This makes transformations between similar text fragments easy to write using TransformMatchingTex.


### Aligning formulae

MathTex mobject is typeset in the LaTeX align* environment. This means you can use the `&` alignment character when typesetting multiline formulae:

![](../imgs/manim_align_formula.png)

```python
from manim import *

class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6').scale(2)
        self.add(tex)
```



