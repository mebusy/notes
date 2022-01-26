# Unity For Adv

## 1 - Advanced Animations


## 2 - Unity Editor Extensions

- Customize Editor
    - We want a cube generate random color.
    ```cs
        MeshRenderer meshRenderer = GetComponent<MeshRenderer>();
        if(meshRenderer) {
            meshRenderer.sharedMaterial.color = Random.ColorHSV();
        }
    ```

    - CustomEditor adds custom Editor UI
        - now we want to change cube color by a button in editor
        - put editor codes under `Editor` folder, any assets under `Editor` won't be included when building a executable.
        - don't even attack the script to any object
    - OnInspectorGUI to add functionality
        ```cs
        Using UnityEditor;
        ...
        [CustomEditor(typeof(CubeLogic))]  // We want to custom the inspector panel of `CubeLogic` script
        public class CubeLogicEditor: Editor {  // not Monobehavior
            Color m_color;

            public override void OnInspectorGUI() {
                base.OnInspectorGUI();
        
                CubeLogic cubeLogic = (CubeLogic)target; // access CubeLogic
                // add GUI lable
                GUILayout.Label( "Press the button below to generate a color" );
                // add GUI button
                if(GUILayout.Button("Generate Color")) {
                    if (cubeLogic) {
                        cubeLogic.GenerateColor();
                    }
                }
            }
        }
        ```
    - GUILayout.Lable
    - GUILayout.Button
    - EditorGUILayout.Colorfield
        ```cs
        [CustomEditor(typeof(CubeLogic))]  // We want to custom the inspector panel of `CubeLogic` script
        public class CubeLogicEditor: Editor {  // not Monobehavior
            ...
            EditorGUILayout.ColorField( "Select your color", m_color );
            // add another GUI button
            if(GUILayout.Button("Set Colorfield Color")) {
                if (cubeLogic) {
                    cubeLogic.SetColor(m_color);
                }
            }
        }
        ```
    - Make 2 GUI items lie in same line
        ```cs
        GUILayout.BeginHorizontal(); 
        ...
        item1 
        ...
        item2
        ...
        GUILayout.EndHorizontal(); 
        ```
    - EditorGUILayout.Slider
        ```cs
        m_cubeSize = EditorGUILayout.Slider(m_cubeSize, 0, 5);
        ...
        transform.localscale = Vector3.one * scale ;
        ```
    - Execute actions in EditorMode

- MENUITEM & PLAYERPREFS
    - MenuItem allows adding new entries in Toolbars
    - Execute action by clicking on it or by assigning a shortcut
    ```cs
    public class CustomMenuItems: Editor {
        [MenuItem("Tools/PlayerPrefs/Delete All")]
        private static void DeleteAllPlayerPrefs() {
            PlayerPrefs.DeleteAll();
        }

        [MenuItem("Tools/Spawn/Ground Platform")]
        private static void SpawnGroundPlatform() {
            GameObject basePlatform = GameObject.CreatePrimitive(PrimitiveType.Cube);
            basePlatform.transform.localscale = new Vector3(30,1,30);
        }
    }
    ```
- EDITORWINDOW & RENAMING OBJECTS EXAMPLE
    - EditorWindow allows creation of new Windows
        - Each Window can have unique functionality
        ```cs
        public void RenameObjectsWindow: EditorWindow {
            [MenuItem("Tools/Rename Objects/Rename Object From Selection")]
            static void RenameObject() {
                EditorWindow window = GetWindow(typeof(RenameObjectsWindow));
                window.show();
            }

            // add GUI items on window
            private void OnGUI() {
                GUILayout.Label("Select an object in the scene hierarchy to rename");
                if (Selection.activeGameObject)  {
                    Selection.activeGameObject.name = EditorGUILayout.TextField("Object name: ", Selection.activeGameObject.name);
                }
                Repaint();
            }
        }
        ```
        ```cs
        public void RenameMultipleObjectsWindow: EditorWindow {
            [MenuItem("Tools/Rename Objects/Rename Object From Selection")]
            static void RenameObject() {
                EditorWindow window = GetWindow(typeof(RenameMultipleObjectsWindow));
                window.show();
            }

            // add GUI items on window
            private void OnGUI() {
                GUILayout.Label("Select all object in the scene hierarchy to rename");
                m_inputName = EditorGUILayout.TextField("Object name: ", Selection.activeGameObject.name);
                int numObjectsSelected = Selection.gameObjects.Length;
                if (numObjectsSelected > 0)  {
                    for(int index=0; index< numObjectsSelected; ++index) {
                        Selection.gameObjects[index].name = m_inputName ;
                    }
                }
                Repaint();
            }
        }

        ```
    - SELECTIONS
        - Selection.activeObject -> Main active object as shown in inspector
        - Selection.gameOjbect -> Multiple objects selected using CTRL
    - Spawn Select Object
        ```cs
        Quaternion rotation = Quaternion.Euler( new Vector3(rotX, rotY, rotZ) );
        Instantiate(Selection.activeGameObject, new Vector3(posX, posY, posX) , rotation, null);
        ```
    - Spawn Trees Onto Platform
        ```cs
        Vector3 pos = new Vector3(posX, posY, posZ) ;
        Ray ray = new Ray(pos, Vector3.down) ;
        RaycastHit rayHit; 
        if (Physics.Raycast(ray, out rayHit, 10.0f)) {
            ...
        }
        ```
- GUI selector
    ```cs
    private void OnGUI() {
        ...
        string[] selectionOptions = { "Enter Position Coordinates", "Select Spawn Box" } ;
        m_selectionIndex = GUILayout.SelectionGrid( m_selectionIndex, selectionOptions, selectionOptions.Length-1 ) ;
        if (m_selectionIndex==0) {
            ...
        } else {
            ...
        }
        ...
    }
    ```


## 3 - Advanced Visuals

## 4 - Source Control & Creating a FPS game

- in order to set unity for source control,  Project Settings/Editor
    - Version Control ->  `Visible Meta Files`
    - Asset Serializtion -> `Force Text`
- unity folders shouble be ignored by SCM
    - Library/ , obj/ , Temp/

## 5 - Multiplayer Networking

- UNet [Command] & [ClientRpc]
    - let's say a player wants to shoot, you would use a [Command] function.
    - let's say you shoot at other player, and other player dies, and the server want to broadcast the dying to all other players, in that case you uses [ClientRpc]
- [SyncVar] + [ClientRpc] to sync varialbes
    - `[SyncVar]` declare that this variable will be sync whenever a new client joins

## 6 - Advanced Multiplayer Networking

## 7 - Unity2D, Performance Optimization & ECS Intro

- Sprite Sheet
    1. import your sprite sheet into unity, in inspector, et `Sprite Mode` to `Multiple`, apply
    2. launch Sprite Editor, `Slice` it, add Apply.
    3. you can click each sprite, see its name, position, border , etc...
    4. in assets windows, drag the sprite you want to use into the scene
- If you enlarge the sprite ( by scaling ), it will blur.
    - solve it by setting the sprite sheet `Filter Mode` to `Point (no filter)`
- 2D Movement using Rigidbody2D
    - CharacterController is NOT available in Unity2D, use Rigidbody2D instead
    - Calculating movement using input is similar, now useing Vector2
    ```cs
    m_rigidBody.MovePosition( m_rigidBody.position + m_movementVelocity * Time.deltaTime );
    ```
- Animating Sprites
    - name sprites using Spritesheet Editor
    - Open Animation window adn setup sprites in order
        - select the charactor ,  Window > Animation > Animation > Create
        - it will also automatically create an Animator Controller
    - setup Animator Controller for Player Sprite
- 2D Triggers & attack collisions
    - Setup BoxCollider2D around character
    - Make as Trigger
    - Activate during Attack using View Direction
        ```cs
        m_hitColliders[index].enabled = true;
        ```
    - Deactivate after Attack
        ```cs
        m_hitColliders[index].enabled = false ;
        ```
- Add a sprite as bg
    1. create 2D Object > Sprite
    2. draw image to the sprite renderer
    3. rescale it
- UI
    - create UI > ...
    - Canvas , UI Scale Mode -> Scale with Screen Size
- Profiler
    - Window > Analysis
    - When you open profile windows, be sure to turn on `Deep Profile`
- performance optimization
    - use Static Batching when possible
    - Reduce & Reuse Textures
    - Use Culling to reduce Rendered Objects
        - default by camera
    - Optimize objects using LOD
    - Optimize Physics calculations using LayerMasks
        - when using raycast, you won't want to check every collider
    - Use simple colliders and don't overuse Rigidbodies


