

# Pong From Pixel 

[pong from pixel](http://karpathy.github.io/2016/05/31/rl/)

 - the game works as follows:
    - we receive an image frame (a 210x160x3 byte array (integers from 0 to 255 giving pixel values)) 
    - and we get to decide if we want to move the paddle UP or DOWN (i.e. a binary choice). 
    - After every single choice the game simulator executes the action and gives us a reward: 
        - Either a +1 reward if the ball went past the opponent
        - a -1 reward if we missed the ball
        - or 0 otherwise
    - our goal is to move the paddle so that we get lots of reward.

Keep in mind that we’ll try to make very few assumptions about Pong because we  don’t really care about Pong; We care about complex, high-dimensional problems like robot manipulation, assembly and navigation.

Pong is just a fun toy test case, something we play with while we figure out how to write very general AI systems that can one day do arbitrary useful tasks.

---

## Policy network

 - This network will take the state of the game and decide what we should do (move UP or DOWN). 
 - we’ll use a 2-layer neural network that takes the raw image pixels (100,800 numbers total (210\*160\*3)) , and produces a single number indicating the probability of going UP. 
    - As our favorite simple block of compute
 - Note that it is standard to use a *stochastic* policy, meaning that we only produce a *probability* of moving UP.
 - Every iteration we will sample from this distribution (i.e. toss a biased coin) to get the actual move. 


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/pong_policy_2layer_network.png)

> Our policy network is a 2-layer fully-connected net.


