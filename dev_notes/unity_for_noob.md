

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

## Module 2: Shooting Game

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
        // gun's rotation * bullet's rotation
        transform.rotation * m_BulletPrefab.transform.rotation )
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

