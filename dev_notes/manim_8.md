[](...menustart)

- [8](#c9f0f895fb98ab9159f51fd0297e236d)
    - [8.1 Update Function](#df1cf19aca45f655925be995ae3491d0)
    - [8.2 Advanced Animation - Using Methods and alpha parameter](#d7aa3049ba8eeb1a11825c6907405f9b)
    - [8.3 Rate Frunction](#3473e7a6278c2b485bb52a2dcad706b5)

[](...menuend)


<h2 id="c9f0f895fb98ab9159f51fd0297e236d"></h2>

# 8

<h2 id="df1cf19aca45f655925be995ae3491d0"></h2>

## 8.1 Update Function

- `obj.add_update(func)`
    - 
    ```python
    dot = Dot()
    text = TextMobject("Label")
    text.next_to(dot, RIGHT, buff=SMALL_BUFF)
    
    self.add(dot,text)

    # can have 2 parameters, the 2nd is alpha
    def update_text(obj):
        obj.next_to(dot, RIGHT, buff=SMALL_BUFF)
    text.add_update( update_text )
    # important: add the object again once you 
    # call add_updater()
    self.add(text)

    self.play(dot.shift, UP*2)
    text.remove_updater( update_text )
    # or use .clear_updaters() to remove all
    self.wait()
    ```

- `UpdateFromFunc`
    - 
    ```python
    def update_text(obj):
        obj.next_to(dot, RIGHT, buff=SMALL_BUFF)

    self.play(dot.shift, UP*2,
        UpdateFromFunc( text, update_text ) 
        )
    self.wait()
    ```
    - similarly , `UpdateFromAlphaFunc`


<h2 id="d7aa3049ba8eeb1a11825c6907405f9b"></h2>

## 8.2 Advanced Animation - Using Methods and alpha parameter

- `manimlib/mobject/mobject.py`
    - We can use **almost every** method of Mobject as an animation
- If we use VGroups , we can not modify specific elements using methods
    - to solve this problem, we have to create a function that performs this task and use it with `ApplyFunction`
    - 
    ```python
    # suppose a vgroup contains 2 element
    # 1 circle and 1 rect
    def modify(vg):
        r,c = vg
        r.set_height(1)
        vg.arrange(DOWN)
        return vg
    self.add(vgroup)
    self.play( ApplyFunction(modify, vgroup) )
    self.wait()
    ```


<h2 id="3473e7a6278c2b485bb52a2dcad706b5"></h2>

## 8.3 Rate Frunction

- Rate functions are the functions that change the behavior of the animations, they depend entirely on *run_time*
- 
```python
class ExampleRateFunc(Scene):
    def construct(self):
        path = Line(LEFT*5, RIGHT*5)
        dot = Dot(path.get_start())
        self.add(path,dot)
        self.play(
            MoveAlongPath(
                dot,path,
                rate_func=linear,  # smooth by default
                run_time=4  # 4 sec
            )
        )
```

- the rate functions are already defined in `manimlib/utils/rate_functions.py`

- 
```python
class ExampleRateFunc(Scene):
    def construct(self):
        text = TextMobject("hello world!").scale(3)
        self.play( Write(
                text,
                rate_func=lambda t:smooth(1-t)
            )
        )
        self.wait()
```

- You might need your rate function to be obtained from discrete data, for that you have to normalize the data from 0 to 1 in both domain and range.




