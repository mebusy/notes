
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
- Pseudo code
    ```java
    PVector desired = PVector.sub( target, location );
    // normalized first, and multiply `maxSpeed`
    desired.SetMag( maxSpeed );

    PVector steering = PVector.sub( desired - velocity );
    steering.limit( maxForce ); // not SetMag !!

    applyForce( steering );
    ```
    - class
    ```java
    class Vehicle {
        float maxspeed;
        // how good is it at turning
        float maxforce;
    }
    ```
- simple seek, but this implementation has weird behavior, it's always sort of flying past the target and then it has to turn aroud and turn back.




