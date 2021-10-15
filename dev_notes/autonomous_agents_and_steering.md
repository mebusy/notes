
# Autonomous Agents and Steering

## 1: Autonomous Agents and Steering

- Autonomous Agent
    - has **limited** ability to perceive its environment
        - e.g. can perceive anything with 25 pixel of itself , or only to see things that are in its field of view.
    - process the environment, **calculate an action**, it's going to result a **force**.
    - no global plan , or leader
- Vehicles
    - action/selection
        - desire velocity
    - steering
        - calculate a steering force based on desire velocity
    - locmotion
        - physics simulation

## 2: Steering Behaviors: Seek

- `steering = desired - velocity`


```javascript
class Vehicle {
    float maxspeed;
    // how good is it at turning
    float maxforce;
}
```


