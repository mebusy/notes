
# Perlin Noise

## 1. Introduction

- 1D perlin noise
    - smooth coherent random number
- how to generate ?
    - let's say I'm going to pick random values over time to start with.
        - let's say I'm going to pick them very 10 units of time
        - And I'm to pick those random values with some amplitude, between something like  0~100
        - ![](../imgs/perlin_noise_start_0.png)
    - Now, the next thing I want to do is to an interpolation function.
        - so here is the start of my Perlin noise function.
        - ![](../imgs/perlin_noise_start_1.png)
    - Now, the next thing I want to do is to an interpolation function.
    - ANd let's just pretend I also had to pick a value a 0, which let's say I picked this 1
        - ![](../imgs/perlin_noise_start_2.png)
        - ![](../imgs/perlin_noise_graph_1_octave.png)
            - use extra cosine function to interpolate it ???
    - Now I'm going to do that again. This time, however, I'm going to pick those random values every 5 units of time. 
        - and instead of picking between 0 and 100, I'm just going to pick between 0 and 50. 
        - **double freq, halve amplitude**.
        - ![](../imgs/perlin_noise_start_3.png)
    - repeat the process,  every 2.5 units of time, and values between 0 and 25
        - ![](../imgs/perlin_noise_start_4.png)
    - ...
    - Now, what if I were to do this prossibly 8 times, 16 times, 25 times, however many times I want, and each time I'm halving essentially the sampling time interval, and also halving the amplitude ? What then if I take all of these and add them together ?
        - THis is essentially how Perlin noise is calculated. And these, what the above pictures show, by the way, are known as octaves.
    - So Perlin noise is calculated over a number of octaves. And essentially it's a bunch of random waveforms. 
        - **the more ocatves that you have, the more fine detail you're getting.**
        - **the smaller the shrinking factor is (currently 0.5), the smoother the graph has.**.


## 2. noise() vs random()

- perlin noise function needs a parameter: the offset in x-axis, in float.
- calling `noise(100)` always return same value until reinitialize


## 4. 2D noise

```javascript
// 2D Noise
// The Coding Train / Daniel Shiffman
// https://thecodingtrain.com/learning/noise/0.5-2d-noise.html
// https://youtu.be/ikwNrFvnL3g
// https://editor.p5js.org/codingtrain/sketches/2_hBcOBrF

// This example has been updated to use es6 syntax. To learn more about es6 visit: https://thecodingtrain.com/Tutorials/16-javascript-es6

let inc = 0.01;

function setup() {
  createCanvas(200, 200);
  pixelDensity(1);
}

function draw() {
  let yoff = 0;
  loadPixels();
  for (let y = 0; y < height; y++) {
    let xoff = 0;
    for (let x = 0; x < width; x++) {
      let index = (x + y * width) * 4;
      // let r = random(255);
      let r = noise(xoff, yoff) * 255;
      pixels[index + 0] = r;
      pixels[index + 1] = r;
      pixels[index + 2] = r;
      pixels[index + 3] = 255;

      xoff += inc;
    }
    yoff += inc;
  }
  updatePixels();
  //noLoop();
}
```


## 6. Coding Challenge #24: Perlin Noise Flow Field

- instead of having a grayscale value for each pixel,  what I want to have is a vector, an arrow pointing in some direction according to Perlin noise.
- flow field animation
    ```javascript
    noise( xoff,yoff,zoff )
    ```



