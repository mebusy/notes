...menustart

- [Inferring DQN structure for high-dimensional continuous control](#30b6658c5954486ffbd28f91e0eefeaf)

...menuend


<h2 id="30b6658c5954486ffbd28f91e0eefeaf"></h2>


# Inferring DQN structure for high-dimensional continuous control

- Problem: continuous action spaces
- Solution: discretize the continuous action space into n different bins

- Problem: sub-actions spaces 
    - i.e, for a racing game, player can input acc, brake, steer simultaneously. 
    - With m sub-actions and n discrete bins for each, the number of possible discrete action tuples is nᵐ
- Solution: decompose the Q network into m sub-modules. 

```bash
   S
   |
--------
|  |   |
A0 A1  A2

(Figure 1)
```

- A0,A1, A2 are sub-action space, in this architecture, A0,A1,A2 are independent.

```bash
   S
   |
--------
|  |   |
A0 |   |
|__|   |
   |   |
   A1  |
   |___|
       |
       A2
 
(Figure 2)
```

- the sub-actions already chosen by the sub-modules ‘higher’ in the structure

- Problem: how to order those sub-action space ?
- Solution: 
    1. Preliminary learning-phase with the fully parallel structure ( Figure 1 )
    2. Uncertainty estimation:
        - Estimate the uncertainty associated to each sub module
        - Group sub modules with similar uncertainty together
        - Rank sub module groups based on their uncertainty values
    3. Resume learning with the updated sequential architecture. 
        - postulate that sub-modules that exhibit high uncertainty during the learning phase, when trained with the fully parallel architecture,would benefit from having more information coming from other more certain modules. 
        - they should be placed 'lower' in the sequential structure
 

```bash
   S
   |
-----------
|  |   |  |
A0 |   |  |
|__|   |  |
   |   |  |
   A1  |  A3
   |___|__|
       |
       A2
```


- Problem: How to estimate uncertainty ?
- Solution: The way to estimate uncertainty for each sub-module is to directly use the output values of each sub-module. For a given state s, if the sub-module is certain which action it should select, then its resultant Q-value should be higher than the others. This would point to a high standard deviation among the output values. On the contrary, if the sub-module is uncertain about which action to choose, it will output similar values for all sub-actions, so the standard deviation will be low. 







