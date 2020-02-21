
# 6 2D and 3D graphs

## CONFIG

### Camera Config

See `manimlib/camera/camera.py`

```python
CONFIG = {
    "camera_config":{"background_color":RED},
}
```


## GraphSceen

TODO



## Path



[source code](https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/extra/faqs/paths.py)

[doc](https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/extra/faqs/paths.md)


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




