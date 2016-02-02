...menustart

 * [U3D 官方视频笔记](#7bc3cbf4be4261fd45c4c7b5d33dc6d7)

	 * [Project Management](#9c1330f0dda3f188a3813b9840d1143f)

		 * [Mid-size project must have](#3f285537c0fcae175e311accfb41198a)

		 * [LevelManager](#3d9687e9851018a33e09bce2e1d5f2ec)

			 * [Why level manager ?](#a2ceed21aa61d341a5508d5f14214d7e)

			 * [LevelManager Design](#e40882d99c80772070faa494568ff842)

		 * [PoolManager](#850bbb4af7a4e88699989bdeb4a7527f)

			 * [Design Rules for PoolManager](#a93b8f8cd4cc57be6fba670068bc24a5)


...menuend


<h2 id="7bc3cbf4be4261fd45c4c7b5d33dc6d7"></h2>
# U3D 官方视频笔记

<h2 id="9c1330f0dda3f188a3813b9840d1143f"></h2>
## Project Management

Manager of managers

 - MainManager costomizes and manages all the submanagers
 - Submanagers operate as singletons and can easily address each other or colaborate.

**Submanagers**:

EventManager | Streamline messaging between classes
--- | ---
AudioManager | COntrol audio playback from one place
GUIManager  | centralize the controls to handle clicks , etc.
PoolManager | Persist perfab instances in RAM and display them as needed
LevelManager | Queue up levels and perfrom transitions between them.
GameManager | Manage the core game mechanics , usually project specific.
SaveManager | Save and load user preference and achievements
MenuManager | Controls all menus' animations,contents, and behaviors.

<h2 id="3f285537c0fcae175e311accfb41198a"></h2>
### Mid-size project must have

 - LevelManager
 - PoolManager
 - SaveManager

<h2 id="3d9687e9851018a33e09bce2e1d5f2ec"></h2>
### LevelManager

<h2 id="a2ceed21aa61d341a5508d5f14214d7e"></h2>
#### Why level manager ?

**Issus 1**: You need to know the scene name or the index of the scene which you want to load, but most probably the name or order will be changed later.

```
Application.LoadLevel("FirstLevel");
Application.LoadLevel(1);
```

**Issus 2**: There's no simple method of passing arguments to a scene, eg, assuming you're resuing one scene for many different levels.

> Application.LoadLevel("FirstLevel" , ~~LevelArgs~~ );

<h2 id="e40882d99c80772070faa494568ff842"></h2>
#### LevelManager Design

 - Compose a configuration table
 - Create a new API:  `LevelManager.LoadNext();`
 - manager the transitions between two levels easily

---

<h2 id="850bbb4af7a4e88699989bdeb4a7527f"></h2>
### PoolManager

*A simple pool design*:

 - Maintain a list of dormant(暂时不用的) objects 
```
private List<GameObject> dormantObjects = new List<GameObject>();
```

 - The list contains all different types of game objects/perfabs
 - Spawn(), Despawn(), Trim() 

```
pubic GameObject Spawn( GameObject go ) {
    GameObject temp = nil;
    if (dormantObjects.Count > 0) {
        foreach ( GameObject dob in dormantObjects ) {
            if (dob.name == go.name) {
                // find an available GameObject
                temp = dob ;
                dormantObjects.Remove(temp);
                return temp ;
            } // end if dob.name
        } //end for
    } // end if
    
    //Now instantiate a new GameObject
    temp = GameObject.Instantiate(go) as GameObject ;
    temp.name = go.name ;
    return temp ;
} // end func
```

```
public void Despawn( GameObject go ) {
    go.transform.parent = PoolManager.transform ; // why shoud have this ?
    go.SetActive( false );
    dormantObjects.Add(go) ;
    Trim();
}
```

```
public void Trim() {
    while ( dormantObjects.Count > Capacity ) {
        GameObject dob = dormantObjects[0];
        dormantObjects.RemoveAt(0);
        Destroy( dob ) ;
    } // end while
} // end func
```


**A better design:

 - PoolManger   // top pool manager
    - SpawnPool  // for a type of prefabs
        - PrefaPool // for a prefab
            - Active instances
            - Inactive instances


<h2 id="a93b8f8cd4cc57be6fba670068bc24a5"></h2>
#### Design Rules for PoolManager

 - As a singleston.
 - Manage multiple SpawnPools.

For prefab pool:

 - Create a PrefabPool for each prefab.
 - Maintain a list of activated objects and another list of deactive objects.
 - Centrally manager the Load/Unload process here.
 - Avoid setting an instance limitation number
 - if really necessary, follow the following rules:
    - Waits for 'cullDelay' in seconds and culls the 'despawned' list if above amount
    - cull less 5 instances each time
    - start a separate coroutine to do the culling work.

