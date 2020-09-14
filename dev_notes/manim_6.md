...menustart

- [6 2D and 3D graphs](#312bf578721d08a7b38fd5618e429125)
    - [CONFIG](#73e99d350a4aa6f1a5af04ec29173f73)
        - [Camera Config](#a66b5d8b4f3b40557caa6f1c314a4d03)
    - [GraphSceen](#06be78bec5d0013e03f081750f9f368d)
    - [Path](#ac70412e939d72a9234cdebb1af5867b)
- [7 Add sounds, svgs and Images](#496fb824b065320ced81010be958c7d7)

...menuend


<h2 id="312bf578721d08a7b38fd5618e429125"></h2>


# 6 2D and 3D graphs

<h2 id="73e99d350a4aa6f1a5af04ec29173f73"></h2>


## CONFIG

<h2 id="a66b5d8b4f3b40557caa6f1c314a4d03"></h2>


### Camera Config

See `manimlib/camera/camera.py`

```python
CONFIG = {
    "camera_config":{"background_color":RED},
}
```


<h2 id="06be78bec5d0013e03f081750f9f368d"></h2>


## GraphSceen

TODO



<h2 id="ac70412e939d72a9234cdebb1af5867b"></h2>


## Path



[source code](https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/extra/faqs/paths.py)

[doc](https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/extra/faqs/paths.md)


<h2 id="496fb824b065320ced81010be958c7d7"></h2>


# 7 Add sounds, svgs and Images

create folder `assets` , create 3 sub-folders

- raster_images
    - 
    ```python
    img = SVGMobject("finger")
    self.play(write(img))
    ```
- svg_images
    - 
    ```python
    svg = SVGMobject("finger")
    # self.play(write(svg))
    self.play( DrawBorderThenFill(svg, rate_func=linear) )
    ```
- sounds
    - 
    ```python
    self.add_sound( "click" )
    ```
    - the sound file could be `click.wav` or `click.mp3`




