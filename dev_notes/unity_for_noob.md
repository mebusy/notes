

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
- character controller
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

