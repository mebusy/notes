# An overview of tkinter layouts

## 3 major methods

![](../imgs/tkinter_layout_s.png)

1. pack
    - takes a window and lets you stack widgets in a certain direction.
    - by default, you are going place widgets from the top to the bottom
        - while you're doing that, you can also customize things quite a bit.
        - for example, you can tell widgets to take up the entire horizontal space, or the entire vertical space, or both as well.
    - besides that, you can also stack widgets in different directions.
        - e.g. from left to right, from right to left, from bottom to top.
2. grid
    - works by creating a grid over the window, and this grid you are then using to place widgets in a certain position with a certain size.
    - this system gives you a ton of flexibility.
        - you can change the height of each row, or the width of each column.
    - grid is generally the system you want to use if you want to create really complex layouts.
3. place
    - take a window and you place widgets with a certain position.
    - you can also change the size.
    - fairly straightforward you always have an X and a Y postion.
