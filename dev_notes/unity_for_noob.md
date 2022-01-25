

# Unity For Noob

## Module 1

- basic platform
    - cube -> reset postion -> scale X & Z to 30
- light shadow
    - **property**: ShadowType
    - lights by default do not cast shadow, set `ShadowType`
- script
    ```csharp
    void Start() ... 
    void Update() ... 
    ```
- rigidbody
    - physics using Rigidbody & AddForce
        ```csharp
        m_rigidBody = GetComponent<Rigidbody>();
        ...
        // press space to jump
        if (Input.GetKeyDown( KeyCode.Space )) {
            m_rigidBody.AddForce( new Vector3( 0,200,0 ) );
        }
        ```
    - collisions & trigger
        - rigidbody will interact with collider
        - collider **property**: `Is Trigger` 
            - if this check-box is actived , you need manually implement the collision detecting.
    - OnTriggerEnter & OnTriggerExit
        ```csharp
        private void OnTriggerEnter(Collider other) ...
        private void OnTriggerExit(Collider other) ...
        ```
- character controller:  handle movement...
    - `Time.deltaTime` = time between updates
    - `Update()` has a variable Time.deltaTime
        - capturing input
        ```csharp
        Vector3 m_movement ;
        float m_horizontalInput ;
        ...
        m_characterController = GetComponent<CharacterController>();
        ...
        // By default they are mapped to the arrow keys.
        // The value is in the range -1 to 1
        m_horizontalInput = Input.GetAxis("Horizontal"); // input in axis
        ```
    - `FixedUpdate()` has a fixed Time.deltaTime
        - physics update
        ```csharp
        m_movement.x = m_horizontalInput * m_movementSpeed * Time.deltaTime ;
        m_characterController.Move(m_movement);
        ```
- constant gravity VS. variable intensity gravity(Mario use it)
    - Character controller **property**: `isGrounded`
    ```csharp
    float m_jumpHeight = 0.5f;
    float m_gravity = 0.045f ;
    bool m_jump  = false;
    ```
    ```csharp
    // Update()
    if (!jump && Input.GetButtonDown("Jump")) {
        m_jump = true;
    }
    ```
    ```csharp
    // FixedUpdate()
    // Apply Gravity
    if (!m_charactercontroller.isGrounded ) {
        /*
        // constant gravity
        m_movement.y -= m_gravity;
        /*/
        // variable gravity
        if (m_movement.y > 0) {
            m_movement.y -= m_gravity;
        } else {
            // falling much faster
            m_movement.y -= m_gravity*1.5f;
        }
        //*/
    } else {
        m_movement.y = 0 ;
    }
    // Set Jump Height to movement y
    if (m_jump) {
        m_movement.y = m_jumpHeight;
        m_jump = false;
    }
    ```
- playing a sound when collecting a coin
    ```csharp
    void OnTriggerEnter(Collider other) {
        if (other.tag == "Player") {
            if (m_audioSource && m_coinSound) {
                m_audioSource.PlayOneShot( m_coinSound ) ;
            }
            // if you play a sound, and destroy gameobject immediately
            // the sound won't be played.
            // GameObject.Destroy( gameObject );

            // instead, you can disable the meshrender and collider
            m_meshRenderer.enable = false; // GetComponent<MeshRenderer>();
            m_collider.enable = false; // GetComponent<Collider>();
        }
    }
    ```
    - another possible approcach is to make other object to play the sound.
    - how to play a sound
        1. add AudioSource component
        2. an AudioClip 
            ```csharp
            // We want to assign the sound from editor
            // Making it public is not the best way because other class 
            //    can access this variable which may not want to
            // Use `[SerializeField]` instead
            [SerializeField]
            AudioClip m_coinSound;
            ```
        3. sound listener
            - To hear the sound, you need at least 1 sound listener, by default, it is attached to your main camera.

## Module 2: A Shooting Game

- x,z movement
    ```csharp
    // void Update()
    m_horizontalInput = Input.GetAxis( "Horizontal" ) ; // x-axis
    m_verticalInput = Input.GetAxis( "Vertical" ) ; // y-axis

    m_movementInput = new Vector3( m_horizontalInput, 0, m_verticalInput);
    ```
    ```csharp
    // void FixedUpdate()
    m_movement = m_movementInput * m_movementSpeed * Time.deltaTime;
    // we want to make this character facing the way he's moving
    if (m_movementInput != Vector3.zero) {
        transform.forward = m_movementInput.normalized;
        // or sometimes you also need an extra rotation
        transform.forward = Quaternion.Euler(0,-90,0) * m_movementInput.normalized;
    }
    ```
- character rotation to mouse positon
    1. Detect mouse position in *Screen Space*
    2. Convert player's **World Postion** to Screen Space
    3. Subtract player *Screen Space* position from Mouse *Screen Space* Position
    4. Use Mathematics to get Angle from Vector (Atan)
    5. Apply Angle Rotation to Player
    - code
        ```csharp
        void RotateCharacterTowardsMouseCursor() {
            Vector3 mousePosInScreenSpace = Input.mousePosition;
            Vector3 playerPosInScreenSpace = Camera.main.WorldToScreenPoint( transform.position );
            Vector3 directionInScreenSpace = mousePosInScreenSpace - playerPosInScreenSpace ;

            float angle = Mathf.Atan2( directionInScreenSpace.y, directionInScreenSpace.x ) * Mathf.Rad2Deg;
            // assuming the direction the player is facing right
            transform.rotation = Quaternion.AngleAxis( -angle, Vector3.up );
        }
        ```
- spawning bullets
    ```csharp
    // Gun Logic
    [SerializeField]
    GameObject m_bulletPrefab;
    
    [SerializeField]
    Transform m_bulletSpawnPoint;
    ...
    Instantiate( m_bulletPrefab, m_BulletSpawnPoint.position, 
        // spawn point's rotation * bullet's rotation
        m_BulletSpawnPoint.rotation * m_BulletPrefab.transform.rotation )
    ```
- bullet speed
    - prefab of bullet
        ```
        ^
        |
        ```
    - set velocity, we want the bullets move along its y-axis (up)
        ```csharp
        m_rigidBody.velocity = transform.up * m_bulletSpeed
        ```
- UI text
    - creating a text will automatically create a Canvas , and an EventSystem.
    - Canvas has **Canvas Scaler** component, we can set its **UI Scale Mode** to *Scale With Screen Size*, so that the text size will change with the screen size.
    ```csharp
    m_ammoText.text = "Ammo: " + m_ammoCount;
    ```
- apply texture to materials
    1. Create Material
    2. Click on *Albedo*
        - select texture
    3. Setup Tiling X and Tiling Y if needed
    4. drag the material to object
- check with specific tag
    ```csharp
    private void OnTriggerEnter(Collier other) {
        if (other.tag == "<YourTarget>") {
            Destroy( other.gameobject );
            Destroy( gameobject );
        }
    }
    ```
- access the script attached to the children of a object
    ```csharp
    GunLogic gunlogic = other.GetComponentInChildren<GunLogic>();
    if (gunLogic) {  // if player have a weapon
        ...
    }
    ```
- Equip and UnEquip the gun
    - add Rigidbody to gun
        - when equipping the gun, uncheck its **Use Gravity**, when unequipping, activate **Use Gravity**.
    - add Box Collider to gun
        - you may use 2 box collider, one for normal collide, one for trigger( bigger ).
        - use `GetComponents<T>` instead `GetComponent<T>` to retrieve the type T components all.  `GetComponent<T>` only return the 1st component T in inspector order.
    - add a equipment point to the player


## Module 3:   AI Behaviour & Navigation

- Navmesh Baking
    - in order for a AI to traverse a navigate map, we have to bake a nevmesh.
    - in order to bake a nevmesh, simply select object, and mark them as **static** at top-right corner
        - then we goto Window/AI/Navigation, select *bake*, then you will see a blue surface appear on top of your mesh, and this will be the walkable surface.
- If you want to use navmesh, then we have to setup a navmesh agent in the components of a character.
- Navmesh Max Slope
    - you can also add navmesh to slopes, and in the settings , you can define the max angle of slope for navmesh agent to walk on
- NavMesh Agent Component
    - Setup Steering Settings
        - speed, angular speed, etc...
    - Set Destination in code
        ```csharp
        m_navMeshAgent.SetDestination( m_destination.position) ;
        ```
    - Stop/Resume NavMeshAgent
        - e.g. policy according to distance
        ```csharp
        float distance = Vector3.Distance( m_destination.position, transform.position ) ;
        if (distance < 1.5f) {
            m_navMeshAgent.isStopped = true;
            m_navMeshAgent.velocity = Vector3.zero;
        } else {
            m_navMeshAgent.isStopped = false ;
        }
        ```
- Use Gizmos to debug
    ```csharp
    // draw radius sphere
    private void OnDrawGizmos() {
        Gizmos.color = new Color(1,0,0,0.25f) ;
        Gizmos.DrawSphere(transform.position, m_aggroRadius);
    }
    ```


## Module 4: Raycasting, Animation timeline & Animator

- Raycast 
    - Raycast = Shoot Laster from point A to point B, check for any object hit.
        - if it hits an object, that will be stored in a RayCastHit
    - We're going to use a Raycast from Camera to Mouse Postion in **World Space**.
        ```csharp
        RaycastHit hit;
        ...
        Ray ray = Camera.main.ScreenPointToRay( Input.mousePosition );
        if (Physics.Raycast(ray, out hit, 100.f) ) {  // last param is distance
            ...
        }
        ```
    - We can use mouse and Raycast to set player's destination

- Camera Movement
    - Move Camerea based on Mouse Position in Screen Space
        ```csharp
        float m_cameraMovementOffset = 0.15f;
        ...
        // Assuming this script is attached to the main camera
        void UpdateCameraPosition() {
            if (Input.mousePosition.x >= Screen.width) {
                // Move camera to the RIGHT
                transform.position = new Vector3(transform.position.x + m_cameraMovementOffset,
                       transform.position.y,  transform.position.z );
            } else if (Input.mousePosition.x <= 0.0f) {
                // Move camera to the LEFT
                transform.position = new Vector3(transform.position.x - m_cameraMovementOffset,
                       transform.position.y,  transform.position.z );
            }
            
            // PS. it's z-axis, not the vertical y-axis
            if (Input.mousePosition.y >= Screen.height) {
                // Move camera  UP
                transform.position = new Vector3(transform.position.x ,
                       transform.position.y,  transform.position.z + m_cameraMovementOffset);
            } else if (Input.mousePosition.y <= 0.0f) {
                // Move camera  DOWN
                transform.position = new Vector3(transform.position.x ,
                       transform.position.y,  transform.position.z - m_cameraMovementOffset);
            }
        }
        ```
    - CenterCamera on Player when you press Spacebar
        ```csharp
        if (Input.GetKeyDown(keyCode.Space)) {
            transform.position = new Vector3( m_player.transform.position.x, 
                transform.position.y,   // keep camera y
                m_player.transform.position.z );
        }
        ```
- Import 3D Model
    - how to import a 3D model
        1. Download .FBX file
        2. Import in Unity editor
        3. Example websites:
            - https://www.turbosquid.com/Search/3D-Models/free
            - https://free3d.com
            - Unity Asset Store
    - how to rotate the model around its some specify postion
        1. create an empty object as an anchor
        2. attach the model to that anchor, adjust its position
        3. rotate that anchor

- Animation Timeline
    1. select the object you want to animate
    2. **Window / Animation / Animation**
        - create
    3. **Add Keyframes and change properties such as position, rotation, ...**
        - click the red record button
        - repeat
            - set the timeline
            - adjust object's positon/rotaton/...
    4. stop record, and play it
- After adding a animation, an Animator component will be added to the object.
    - Controller: link to the animation controller
    - Avatar
    - Apply Root Motion
- Animation Events
    - Create A Code function to handle the event
    - On animation timeline editor,  Right-Click -> Add Animation Event
    - In inspector, Link this AnimationEvent to Code Function we created
- New Animator state, and Animator parameters
    - add animator  Parameter `IsAttacking`  in Animator Editor
    - add new state Idle 
        - you can set the state as default state 
        - you can make a transition to other state
            - at the transition arrow, you can set Condition, and use the animator parameter in the condition.
            - if you want instantly go to the target state, disable **has exit time**
    - set animator parameter
        ```csharp
        m_animator = GetComponent<Animator>();
        ...
        m_animator.SetBool( "IsAttacking", true );
        ```
- Shoot Ray forward from Player position to another object
    ```csharp
    float MELEE_RANGE = 1.5f;
    ...
    void CheckAttackRange() {
        Debug.DrawRay( transform.position, transform.forward * MELEE_RANGE, Color.Red );

        RaycastHit hit;
        Ray ray = new Ray( transform.position, transform.forward ) ;
        if (Physics.Raycast(ray, out hit, MELEE_RANGE)) {
            if( hit.collider.gameobject.tag == "Enemy") {
                if (m_swordLogic) {
                    m_swordLogic.SetAttacking(true);
                }
                m_navMeshAgent.isStopped = true;
            }
        }
    }
    ```

## Module 5:  Creating a Third Person Game

- Third person camera
    - Camera is behind player in the Z axis,  a little bit high
    - Camera can rotate around player on Y axis and X axis
    - Camera looks at Player
    - procedurally pricely control, or adjusting camera and attach it onto player
- Camera Movement (procedurally)
    - Camera Position = Camera Target(Player) + Camera Offset( y-axis )
    ```csharp
    // CameraLogic
    float m_cameraTargetOffset = 1.0f;  // high in y-axis
    float m_distanceZ = 5.0f;  // behind the player, in z axis
    ...
    void Update() {
        m_cameraTarget = m_player.transform.positon;
        m_cameraTarget.y += m_cameraTargetOffset ;
    }
    // the reason why we assign new position to the cameras in the LateUpdate
    //   is it gives better effect for camera's , this happens after the rendering is done.
    // you will see my we split it up when we add rotations
    private void LateUpdate() {
        Vector3 cameraOffset = new Vector3(0,0, -m_distanceZ);
        transform.position = m_cameraTarget + cameraOffset ;
    }
    ```
- Camera Rotation
    - Use Mouse Axis to increase Rotation
    - Clamp Rotation X
        ```csharp
        float m_rotateX;
        float m_rotateY;
        float m_rotateZ;
        const float MIN_X = -20.f;
        const float MAX_X = 20.f;
        ...
        if (Input.GetButton("Fire2")) {
            m_rotationY += Input.GetAxis("Mouse X"); // mouse move left/right
            m_rotationX -= Input.GetAxis("Mouse Y"); // mouse move up/down
            // ensure that camera does not go below the ground
            m_rotationX  = Mathf.Clamp( m_rotationX, MIN_X, MIN_Y );
        }
        ```
    - Multiply Rotation with Camera Offset
    - Add up with CameraTarget and assign to Camera Position
        ```csharp
        // all rotations in unity are done in `Quaternion`
        // angles -> rotation
        Quaternion cameraRotation = Quaternion.Euler(m_rotationX, m_rotationY, 0);
        Vector3 cameraOffset = new Vector3(0,0, -m_distanceZ);
        transform.position = m_cameraTarget + cameraRotation * cameraOffset;
        ```
    - next, we will want to make the camera face the player because currently the camera only looks forwards, we want the camera to look at the player.
- Camera LookAt
    - lucky for us, LookAt functin will face an object towards it's target.
        - `transform.LookAt( m_cameraTarget );`
    - add this code
        ```csharp
        // all rotations in unity are done in `Quaternion`
        // angles -> rotation
        Quaternion cameraRotation = Quaternion.Euler(m_rotationX, m_rotationY, 0);
        Vector3 cameraOffset = new Vector3(0,0, -m_distanceZ);
        transform.position = m_cameraTarget + cameraRotation * cameraOffset;
        // new
        transform.LookAt( m_cameraTarget );
        ```
- Camera Zooming
    - Mouse ScrollWheel Axis can be used to Zoom in / Zoom out
    - Value should be clamped to prevent Camera going too far forward / back
        ```csharp
        // in Update()
        m_distanceZ -= Input.GetAxis("Mouse ScrollWheel");
        m_distanceZ = Mathf.Clamp( m_distanceZ, MIN_Z, MAX_Z ) ;  //  2.0f/8.0f
        ```
- DOWNLOADING MODEL & ANIMATION ASSETS USING MIXAMO
    - [mixamo.com](https://www.mixamo.com/#/)
    - register Adobe account
    - Preview & Select Characters(model)
        - download -> Format FBX for unity
    - Preview & Select Animations
        - download -> same format, 60fps, without skin( we've download the model in T-pose separately, not include skin in animation can reduce the file size )
            - for "walking" animation, click "in place"
        - ADVANCE: you can edit the clip, set frames , or create multiple clips, each clip could be state, and use them as different purpose.
    - Download & Import .FBX to Unity
- IMPORTING & SETTING UP THE CHARACTER
    - in practice: 
        - put the model fbx for unity ( e.g. xx.fbx )    in `Models` folder
        - put the animation fbxs ( e.g. xx@Idel.fbx ) in `Animation` folder
    - you may not need to adjust the model , for animations, if you want it loop,  in its Animation tab, check the `Loop Time` & `Loop Pose`, and apply
        - it's also a good practice  for animations to use the same Rig. In its Rig tab, change the Avatar definition from `Create From This Model` to `Copy From Other Avart` and select the model fbx.
        - in case the texture doesn't show up, goto `Material` tab,  change `Location` field to `Use External Materials(Legacy)` and hit *apply* & fix.
    - use the model and animations
        - drag the model to the scene, this object is not playing any animtion yet because it does not has any animator controller yet .
        - create a empty animator controller, and we can drag animation to animator layer
        - select this animator controller in object's inspector
- 0509 ANIMATION BLENDTREE
    - in order to implement our character's movement animation smoothly, and have the animations transition blend into each other nicely base on the state, we have to use an animation blendtree.
    - first we only setup an animation blendtree with movement parameters, we will only setup 2 parameters , HorizontalMovementInput, and VerticalMovementInput. Based on these parameters, we have to setup a **2D Freeform Cartesian** blendtree. Based on the X & Y value, we need to play different animation.
        - in animation base layer, right click-> Create State-> From New Blend Tree,   set the blendtree as default state.
        - add 2 new parameters: HorizontalMovementInput &  VerticalMovementInput
        - select blendtree, go inside, set blendType to `2D Freeform Cartesian`,  change the preset parameter to HorizontalMovementInput & VerticalMovementInput. then we can start add motion -> Add motion field
    - how to set animator parameter
        ```csharp
        if (m_animator) {
            m_animator.SetFloat("HorizontalMovementInput", m_horizontalInput);
            m_animator.SetFloat("VerticalMovementInput", m_verticalInput);
        }
        ```
- SETTING UP ANIMATION EVENTS IN EDITOR
    - setup animation events for footsteps ( 0=left, 1=right) , and play sound effect per step
    - select a running animation, select its Animation tab, drag the model into inspector panel
    - play the animation, each time when the foot hit the ground, 
    - click the button left to the timeline within `Events` field
        - add callback function `PlayFootstepSound`  and give it a parameter value
        ```csharp
        [SerializeField]
        List<AudioClip> m_footstepSounds = new List<AudioClip>();
        ...
        public void PlayFootstepSound( int footIndex ) {
            if (m_footstepSounds.Count > 0 && m_audioSource ) {
                int rand = Random.Range( 0, m_footstepSounds.Count -1 );
                m_audioSource.PlayOneShot( m_footstepSounds[rand] );
            }
        }
        ```
- ADVANCED - CONTEXTUAL SOUND THEORY & SCENE SETUP.mp4
    - we will raycast from the positon of foots towards the groud, and we check what's the tag of the groud , and we will play sound based on this tag.
    ```csharp
    // you need first serialize left/right foot
    public void PlayFootstepSound( int footIndex ) {
        if (footIndex == 0) {
            RayCastTerrain( m_leftFoot.position) ;
        } else if (footIndex == 1) {
            RayCastTerrain( m_rightFoot.position) ;
        }
    }
    ```
    - first we need to change the platform's(ground) `Layer` tag, add a new layer `Terrain`, 
        - and then add tags `Grass`, `Stone`, `Earth`, ... 
        - create multiple terrains, and assign different tag to them
    ```csharp
    void RayCastTerrain( Vector3 position) {
        LayerMask layerMask = LayerMask.GetMask("Terrain") ;
        Ray ray = new Ray(position, Vector3.down);
        RaycastHit hit;

        if (Physics.Raycast(ray, out hit, layerMask  )) {
            string hitTag = hit.collider.gameObject.tag ;
            if (hitTag = "Grass" ) {
                PlayRandomSound( m_runGrassSounds) ;
            }
            else if (hitTag = "Stone" ) {
                ...
            }
            ...
        }
    }
    ```
- PLAYER TURNING TOWARDS CAMERA DIRECTION & OUTRO
    ```c#
    // Camera_logic.cs
    public vector3 GetForwardVector() {
        Quaternion rotation = Quaternion.Euler(0, m_rotationY, 0) ;
        return rotation * Vector3.forward; 
    }

    // player_logic.cs
    private void FixedUpdate() {
        ...
        // if player move...
        if (Mathf.Abs(m_horizontalInput)>0.1f || Mathf.Abs( m_verticalInput )>0.1f ) {
            transform.forward = m_cameraLogic.GetForwardVector();
        }
    }
    ```

## Module 6: Saving & Loading using PlayerPrefs

- animator parameter : trigger
    ```csharp
    m_enemyState = EnemyState.StandingUp;
    m_animator.SetTrigger("PlayerNearby");
    ```
- Behavior State Machine
    - we want the zombie move after he standing up
    - within the animator editor,  select the `Zombie Stand up` state, click `Add Behavior`  to add a new script
        ```csharp
        public class EnemyBehavior: StateMachineBehavior {
            ...
            override public void OnStateExit( Animator animator, AnimatorStateInfo stateinfo, int layerIndex ) {
                EnemyLogic enemyLogic = animator.GetComponent<EnemyLogic>();
                if (enemyLogic) {
                    enemyLogic.SetState( EnemyState.Attack ) ;
                }
            }
        }
        ```
- enemy weak point: use a collider trigger as a collision box
- Saving
    ```csharp
    PlayerPrefs.SetFloat( "PlayerPosX", transform.position.x );
    ...
    PlayerPrefs.Save();
    ```
- Loading
    ```csharp
    float playerPosX = PlayerPrefs.GetFloat( "PlayerPosX" ) ;
    ```
- a modern thead-safe singleton in Unity
    ```csharp
    public abstract class Singleton<T> : MonoBehaviour where T : MonoBehaviour
    {
        private static readonly Lazy<T> LazyInstance = new Lazy<T>(CreateSingleton);

        public static T Instance => LazyInstance.Value;

        private static T CreateSingleton()
        {
            var ownerObject = new GameObject($"{typeof(T).Name} (singleton)");
            var instance = ownerObject.AddComponent<T>();
            DontDestroyOnLoad(ownerObject);
            return instance;
        }
    }

    //usage:
    public class GameManager : Singleton<GameManager> {
        …
    }
    ```
    - requires enabling the .NET 4 scripting runtime to access the `Lazy<T>` type.
        1. Open player settings in the Unity Inspector by selecting Edit > Project Settings > Player.
        2. Under the Configuration heading, click the Scripting Runtime Version drop-down and select .NET 4.x Equivalent. You will have to restart Unity for the change to take effect.
    - The advantage of this is that `Lazy<T>` handles the thread-safety out of the box and we don’t have to do any locking ourselves.
    - Create an empty GameObject, attach our component to it and finally mark it so that it won’t be destroyed when new scene is loaded.


## Module 7: Controller Input, Local Multiplayer & VFX

- Project Setting - Input
    - Edit > Project Settings ... > Input
    - You can duplicated the existing setting, and name your own, e.g. "Horizontal_P1", "Horizontal_P2"
- INPUT
    - GetButton(), GetButtonDown()
    - GetAxis()  smoothing on the values
    - GetAxisRaw()  no smoothing

- SHOOTING A FIREBALL
    - Instantiate Object based on hand transform
        - run game, pause game, adjust animation to the frame you want to cast a fireball,  add fireball spawn postion object to the right-hand, copy its transform data
        - stop the game
        - re-add fireball spawn postion, paste the transform data we copied
    - Initialize Fireball movement at correct time using animation event
        ```csharp
        Instantiate( m_fireball, m_fireballSpawn.transform.position, transform.rotation );
        ```
    - Attach Rigidbody and Trigger to detect collision
- particle Emitter
    - right-click > Effects > Particle System
    - get fireball effects...
        1. assetstore.unity.com
        2. search `explosion`,  in Publisher search bar , input `unity` , and then you will find free asset pack
- procedurally play a particle effect which doesn't PlayOnAwake
    ```csharp
    // fileball_logic.cs
    m_collider.enable = false; // disable the collider
    m_fireball.Stop(true);  // stop the current particle effect
    m_explosion.Play(true);  // play a new one, explosion effect should be not play on awake, and disable looping
    m_rigidBody.velocity = Vector3.zero;  // stop fireball moving
    ```
- EVENTS & DELEGATES
    - so far, when we want to call a function in a class, we need to access to that object. Now we're going to learn event & delegates.
    - we can ``send events`` with parameters from class X;  **Subscrib/Listen** to events from class Y; Multiple classes can react to events without having access to each other.
    ```csharp
    // PlayerLogic.cs
    // Events
    public delegate void PlayerDeath(int playerNum) ;
    public static event  PlayerDeath OnPlayerDeath ; 

    // Increase the score for the opposing player
    public void Die() {
        ...
        if (OnPlayerDeath != null) {
            // wheneven the player dies, we will call this event 
            OnPlayerDeath( GetPlayerNum() );
        }
    }
    ```
    ```csharp
    // UIManager.cs
    void OnEnable() {
        // subscribe to the event
        PlayerLogic.OnPlayerDeath += OnUpdateScore;
    }

    void OnDisable() {
        PlayerLogic.OnPlayerDeath -= OnUpdateScore;
    }
    void OnUpdateScore(int playerNum) {
        ...
    }
    ```


## Module 8: UI, XML, Localization, Scene Load & Build .exe

- MainMenu
    - Create Scene
    - Add BG
        - create a plane
        - add a material, or just drag a picture onto it as a texture
    - Add Canvas
        - automatially added when adding text
    - Add Text, Button (component)
    - Setup Anchor Alignment
        - interact:  set callback function in Button(Script)'s `On Click()` field
    - Setup Hover & Select Color
- Localization file
    - English.xml
        ```xml
        <Localization>
            <Entry>
                <Key>Title</Key>
                <Value>UI MainMenu</Value>
            </Entry>
            <Entry>
                <Key>Start</Key>
                <Value>Start</Value>
            </Entry>
        </Localization>
        ```
    - Chinese.xml
        ```xml
        <Localization>
            <Entry>
                <Key>Title</Key>
                <Value>界面主菜单</Value>
            </Entry>
            <Entry>
                <Key>Start</Key>
                <Value>开始</Value>
            </Entry>
        </Localization>
        ```
- Load Localization files from Resources Folder
        ```csharp
        public enum Languages {
            English,
            Chinese
        }
        ...

        Dictionary<Languages, TextAsset> m_localizationFiles = new Dictionary<Languages, TextAsset>();
        Dictionary<string, string> m_localizationData = new Dictionary<string, string>() ;

        void SetupLocalizationFiles() {
            foreach( Languages language in Languages.GetValues( typeof(Languages) ))  {
                string textAsetPath = "Localization/" + language;
                TextAsset textAsset = (TextAsset) Resources.Load(textAssetPath);
                if (textAsset) {
                    m_localizationFiles[textAsset.name] = textAsset;
                } else {
                    Debug.LogError( "TextAsset not found:" + textAssetPath );
                }
            }
        }
        ```
    - Create Dictionary of Key and Value from XML
    - Create Dictionary of Key and Value from XML
    - Retrieve Localized string from Data
- Make an object to exist in multiple scenes
    ```csharp
    void Start() {
        // this object won't be destroyed when loading a new scene
        DontDestoyOnLoad(gameobject);
    }
    ```
- READING LOCALIZATION DATA
    ```csharp
    void SetupLocalizationData() {
        TextAsset textAsset;
        if(m_localizationFiles.ContainKey(m_currentLanguage)) {
            textAsset = m_localizationFiles[m_currentLanguage];
        } else {
            Debug.LogError("Couldn't find localization file for: " + m_currentLanguage );
            // default
            textAsset = m_localizationFiles[Languages.English];
        }
        // +Using System.Xml
        XmlDocument xmlDocument = new XmlDocument();
        xmlDocument.LoadXml( textAsset.text ) ;

        XmlNodeList entryList = xmlDocument.GetElementsByTagName("Entry");

        foreach(XmlNode entry in entryList) {
            if (!m_localizationData.ContainKey( entry.FirstChild.InnerText )) {
                // add key-value
                m_localizationData.Add(  entry.FirstChild.InnerText ,  entry.LastChild.InnerText );
            }
        } 
    }
    ```
    ```cs
    public string GetLocalizedString(string key) {
        string localizedString = "";
        if(!m_localizationData.TryGetValue(key, out localizedString)) {
            localizedString = "MISS LOC KEY: "  + key;
        }
        return localizedString;
    }
    ```
- Load Scene
    ```cs
    using UnityEngine.SceneManagement;

    public void OnStartClicked() {
        SceneManager.LoadScene( "GameScene" ) ;
    }
    public void OnQuitClicked() {
        Application.Quit();
    }
    ```

---

# Unity Scripting

- script architecture
    - backeds: mono / IL2CPP
    - you should use the **.NET Standard 2.0 API** Compatibility Level for all new projects 
        - for code size, cross-platform support, moves more errors to compile time, etc...
        - Edit > Project Settings > Player > Other Settings, Api Compatibility Level
- C# reflection overhead
    - all C# reflection (System.Reflection) objects are cached, and do NOT be GC, this behavior will causes unnecessary and potentially GC overhead.
    - avoid methods such as Assembly.GetTypes and Type.GetMethods() in your application, which create a lot of C# reflection objects at runtime.
        - Instead, you should scan assemblies in the Editor for the required data and serialize and/or codegen it for use at runtime.
- UnityEngine.Object special behavior
    - UnityEngine.Object is a special type of C# object in Unity, because it is linked to a **native C++ counterpart object**, e.g. `Camera`
        - For this reason Unity does not currently support the use of the **C# WeakReference** class with UnityEngine.Objects
    - Object.Destroy or Object.DestroyImmediate will destroy the native counter object, the GC will handle its C# **managed object**.
    - If a destroyed UnityEngine.Object is accessed again, Unity **recreates** the native counterpart object for most types. 
        - Two exceptions to this recreation behavior are **MonoBehaviour** and **ScriptableObject**: Unity never reloads them once they have been destroyed.
        - So you can compare a destroyed MonoBehaviour or ScriptableObject against `null`, and will get `true`.
- Avoid using async and await
    - Async tasks often allocate objects when invoked, which might cause performance issues if you overuse them. 
    - Additionally, Unity does not automatically stop async tasks that run on managed threads when you exit Play Mode.
    - Unity overwrites the default SynchronizationContext with a custom UnitySynchronizationContext and runs all the tasks on the main thread in both Edit and Play modes. 
-  Unity Editor uses a C# compiler
    scripting runtim version | C# compiler | C# language version
    --- | --- | --- 
    .NET 4.6 equivalent | Roslyn | C# 8.0

- Script Serialization
    - Serialization is the automatic process of transforming data structures or object states into a format that Unity can store and reconstruct later.
        - saving/loading/Inspector windows/Prefabs ...
    - To use field serialization: 
        - Is `public`, or has a `SerializeField` attribute
        - Is not static, const, readonly
        - Has a fieldtype that can be serialized. 
            - Custom non-abstract, non-generic classes non-static with the *Serializable* attribute
            - Custom structs with the *Serializable* attribute
            - Primitive data types (int, float, double, bool, string, etc.)
            - Enum types
            - Certain Unity built-in types: Vector2, Vector3, Vector4, Rect, Quaternion, Matrix4x4, Color, Color32, LayerMask, AnimationCurve, Gradient, RectOffset, GUIStyle
    - Container field types that can be serialized
        - An array of a simple field type that can be serialized
        - A List<T> of a simple field type that can be serialized

