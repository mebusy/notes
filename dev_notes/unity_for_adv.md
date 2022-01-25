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

## 5 - Multiplayer Networking

## 6 - Advanced Multiplayer Networking

## 7 - Unity2D, Performance Optimization & ECS Intro



