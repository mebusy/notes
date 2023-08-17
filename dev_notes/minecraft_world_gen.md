
# Reinventing Minecraft world generation

- chunk
    - 16x16x256
- what is the "procedure" ?
    ```java
    BlockState = getBlock(int x, int y, int z) {
        // Figure out which block should be at this coordinate
    }
    ```
- a chunk is generated in steps
    1. terrain shaping
        - just deciding stone and air(empty)
    2. water filling
        - all blocks below 64 (height) is going to be filled with water
    3. surface replacement
        - what biome is it ?  jungle, or desert ? and base on that we replace the top layer with somethings( dirt, grass...)
    4. features and structures 
        - trees, villages...


# Terrain Shaping

## Perlin Noise

- Example: 2d noise to generate height map
    ```java
    BlockState = getBlock(int x, int y, int z) {
        PerlinNoise noise = new PerlinNoise();
        var surfaceY = 100 + noise.sample2d(x,y) * 20;
        return y < surfaceY ? STONE: AIR;
    }
    ```
    - <img src="../imgs/2d-perlin-noise-example.png" width=400 />

## Octaves

- What is octaves ?
    - normally doule the frequency and half the amplitude
- Multioctaves on sine(x)
    - <img src="../imgs/ocatave_example.png" width=400 />
- MultiOcatves on Perlin Noise
    - <img src="../imgs/octave-perlin-noise.png" width=400 />
- MultiOcatves for terrain generation
    ```java
    BlockState = getBlock(int x, int y, int z) {
        final int octaves = 4;
        PerlinNoise noise = new PerlinNoise(octaves); // new constructor
        var surfaceY = 100 + noise.sample2d(x,y) * 20;
        return y < surfaceY ? STONE: AIR;
    }
    ```
    - <img src="../imgs/2d-perlin-noise-example2.png" width=400 />
    - more interesting


## Noise Transformation

- noise value gives us value from -1 to 1
    ```java
        var surfaceY = 100 + noise.sample2d(x,y) * 20;
    ```
- and we doing somthing on it
    ```java
        return y < surfaceY ? STONE: AIR;
    ```
- and gave us such terrain
    - <img src="../imgs/2d-perlin-noise-example.png" width=400 />


## Do more deliberate Noise Transformation: Continentalness

- we're going to take our Perlin noise, and I'm going to call it `Continentalness`.
- everywhere in the world has a value for continentalness.
- shaping
    - shaping really means creating an indirect connection between continentalness and terrain height.
- this shaping give us a boring flat world
    - <img src="../imgs/spline_points_flat.png" width=300 /> , <img src="../imgs/boring_flat_world.png" width=300 />
    - I don't care what continentalness it is, the surface height is always going to be 100.
- straight line shaping
    - <img src="../imgs/spline_points_straight_line.png" width=300 /> , <img src="../imgs/2d-perlin-noise-example.png" width=300 />
- segment lines shaping
    - <img src="../imgs/spline_points_segment.png" width=300 /> , <img src="../imgs/terrain-with-segments-shaping.png" width=300 />



## Multinoise

- We have 3 noises here
    - Continentalness, Erosion, Peaks & valleys
    - ![](../imgs/multinoise-3.png)
    - Erosion changes quite slowly, Peaks & valleys tends to generate ridges.
