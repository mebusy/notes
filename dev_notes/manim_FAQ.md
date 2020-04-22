...menustart

 - [Manim](#cbcd3fecff4c0ef0c063f8c41726d34a)
     - [Installation](#7cd8fb6e31cc946c078d2740c76a9899)
     - [FAQ](#1fe917b01f9a3f87fa2d7d3b7643fac1)

...menuend


<h2 id="cbcd3fecff4c0ef0c063f8c41726d34a"></h2>


# Manim

Manim is composed of 5 parts 

1. Python
2. Latex, the program used to write texts and formulas 
3. Cairo, the program that makes the figures
4. FFmpge
5. Sox, audio program

But we only need to write codes in python to create the animations.


<h2 id="7cd8fb6e31cc946c078d2740c76a9899"></h2>


## Installation 

---

1. git clone repository
1. build image 
    - 
    ```bash
    docker build -t manim:v1 .  --network=host
    ```
2. run
    - 
    ```bash
    input="input"
    output="media"

    docker run --entrypoint="" --rm -it --name manim  \
        -v `pwd`/$output:/media \
        -v `pwd`:/$input manim:v1 \
        /bin/sh -c "manim $input/$cmd" \
            | tee o.txt 
    ```

<h2 id="1fe917b01f9a3f87fa2d7d3b7643fac1"></h2>


## FAQ

https://github.com/Elteoremadebeethoven/AnimationsWithManim

1. What is CONFIG 
    - CONFIG is a python dict. In it we can create objects or numerical variables to be used in the scene
    - to call these objects you must type "self."
    - 
    ```python
    class WhatIsCONFIG(Scene):
        CONFIG={
            "object_1":TextMobject("Object 1"),
            "object_2":Square(),
            "number":3,
            "vector":[1,1,0]
        }
        def construct(self):
            self.play(
                Write(self.object_1)
            )
            ...
    ```
2. Scene from another Scene
    - A great advantage of using this dict is that you can **ganerate new scenes** from others already made.  With this dict we can omit the **constuct** method 
    - 
    ```python
    class SceneFromAnotherScene(WhatIsCONFIG):
        CONFIG={
            "object_1":TextMobject("Another object"),
            "object_2":Circle(),
            "number":4,
            "vector":[-1,-1,0]
        }    
    ```
3. Change background color
    - To change backgroud color you can do it with the CONFIG dict
    - 
    ```python
    class ChangeBackgroundColor(Scene):
        CONFIG={
            "camera_config":{"background_color":RED},
            "text":TexMobject(r"\frac{d}{dx}\Bigr|_{y=2}").scale(5)
        }
        def construct(self):
            self.add(self.text)
    ```
4. Remove background stroke width of texts
    - using `background_stroke_width=0` 
    - 
    ```python
    class RemoveBackgroundStrokeWidth(ChangeBackgroundColor):
        CONFIG={
            "text":TexMobject(
                r"\frac{d}{dx}\Bigr|_{y=2}",
                background_stroke_width=0, #<- Add this line
                ).scale(5)
        }
    ```
    - To set this parameter by default
        - `manimlib/mobject/svg/tex_mobject.py`
5. Arrange Objects
    - To arrange a set of objects 
    - using a `VGroup()` and `.arrange_submobjects(...)`
        - note: in the most recent version , the function is `.arrange(...)`
    - 
    ```python
        text1 = TextMobject("You have")
        text2 = TextMobject("to use")
        text3 = TextMobject("\\tt VGroup")

        text_group = VGroup(
            text1,
            text2,
            text3
        )

        #         .arrange # <- For recent versions
        text_group.arrange_submobjects(
            DOWN, # <- Direction
            aligned_edge = LEFT,
            buff=0.4
        )
        self.add(text_group)
        self.wait()

        self.play(
            text_group.arrange_submobjects,UP,{"aligned_edge":RIGHT,"buff":2}
        )
        self.wait()

        self.play(
            text_group.arrange_submobjects,RIGHT,{"buff":0.4}
        )
    ```
6. Change position and size of the camera
    - `MovingCameraScene`
    - You can manipluate the camera with `self.camera_frame`
    - 
    ```python
    class ChangePositionAndSizeCamera(MovingCameraScene):
        def construct(self):
            ...

            # Save the state of camera
            self.camera_frame.save_state()

            # Animation of the camera
            self.play(
                # Set the size with the width of a object
                self.camera_frame.set_width,text.get_width()*1.2,
                # Move the camera to the object
                self.camera_frame.move_to,text
            )
            self.wait()
    ```
    - If you want to use this camera movement in other scenes you must first configure the **setup** methods.
    - 
    ```python
    class ChangePositionAndSizeCameraInAnotherScene(GraphScene,MovingCameraScene):
        ...
        # Setup the scenes
        def setup(self):            
            GraphScene.setup(self)
            MovingCameraScene.setup(self)
        ...
    ```
7. Linear transformation
    - use `LinearTransformationScene`. That are all CONFIG parameters that you can change.
    - 
    ```python
    class LinearTransformation(LinearTransformationScene):
        CONFIG = {
            "include_background_plane": True,
            "include_foreground_plane": True,
            "foreground_plane_kwargs": {
                "x_radius": FRAME_WIDTH,
                "y_radius": FRAME_HEIGHT,
                "secondary_line_ratio": 0
            },
            "background_plane_kwargs": {
                "color": GREY,
                "secondary_color": DARK_GREY,
                "axes_color": GREY,
                "stroke_width": 2,
            },
            "show_coordinates": False,
            "show_basis_vectors": True,
            "basis_vector_stroke_width": 6,
            "i_hat_color": X_COLOR,
            "j_hat_color": Y_COLOR,
            "leave_ghost_vectors": False,
        }
    ```
    - `.apply_matrix`  Apply the transformation with a matrix.
    - `.add_transformable_mobject`  Add the object to the transformation.
    - 
    ```python
        def construct(self):
            mob = Circle()
            mob.move_to(RIGHT+UP*2)
            vector_array = np.array([[1], [2]])
            matrix = [[0, 1], [-1, 1]]

            self.add_transformable_mobject(mob)

            self.add_vector(vector_array)

            self.apply_matrix(matrix)

            self.wait()
    ```
8. Remove all objects in screen
    - 
    ```python
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
    ```

