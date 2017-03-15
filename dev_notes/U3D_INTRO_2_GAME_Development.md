...menustart

 - [Projects](#54e1d44609e3abed11f6e1eb6ae54988)
	 - [Project 1 :](#6d791572a76856bb23442d3a04bdaf53)
		 - [Setting Up the Solar System Simulation](#e146688675a13c76dde2fd52e790038b)
		 - [Materials, Lighting, and Audio](#8578a0f2b5f7f9fab6ab15a3ca42c469)
			 - [Materials](#23ce0eb7d180f3dc8391d4af48572d21)
			 - [Lighting](#2e4b97fde8cf63085ec969fcc7e490c0)
				 - [Real-time Lighting](#d2da94913f9bfb60bf8744e04701732c)
				 - [Change ambient light](#0b7dbebb68099152ba453cb992a19ee4)
				 - [Point Light](#c578e22deb4b879b0a68b887b4a6e5ce)
			 - [Audio](#b22f0418e8ac915eb66f829d262d14a2)
		 - [Cameras, Building for Web, and Deploying](#5548d227c389d436b5533a8e72058981)
			 - [Camera](#967d35e40f3f95b1f538bd248640bf3b)
				 - [create a minimap Camera](#5241862f585708e8be3777b44d9d6441)
		 - [Building , Deploying](#bc9eb11a4b1b7761c1941d0ca36e9d72)
	 - [Project 2 : Roller Madness Game](#aa52d2f45f695a401e95e6a21bd24f1f)
		 - [Physics](#50ae99e9c35446c2580e4b540b0fd104)
			 - [Collider  (碰撞相关)](#af17bfc214bfe362db7ee5deaada8711)
			 - [Rigidbody  (物理相关)](#48640050253b1ce0c375421d95b77d74)
			 - [Review](#457dd55184faedb7885afd4009d70163)
		 - [Trail Render](#997e837eabd8235dd27a016e5906d54e)
		 - [Controller](#9bbf373797bf7cf7ba62c80023682e25)
		 - [Coins](#a2aa6b4bebf569d55787e53bb224c072)
		 - [UI Basic](#aec53bb2266ce5b41cc0539da9f7de20)
		 - [Animation](#d6b6b668dbca9d4fe774bb654226ebe3)

...menuend


<h2 id="54e1d44609e3abed11f6e1eb6ae54988"></h2>

# Projects

http://docs.unity3d.com/

http://wiki.unity3d.com/

http://wiki.unity3d.com/index.php/CSharp_Unity_Tutorial

---

<h2 id="6d791572a76856bb23442d3a04bdaf53"></h2>

## Project 1 : 

<h2 id="e146688675a13c76dde2fd52e790038b"></h2>

### Setting Up the Solar System Simulation

1 unit means 1 **meter** in Unity.

RGB=XYZ , Unity 三个坐标轴的颜色

 - Position = Vector3(x,y,z)
 - Rotation = Vector3(x,y,z)   (degree in Unity)
 - Scale    = Vector3(x,y,z)

Transform packages Position/Rotation/Scale.  All gameObject has a transform component.

<h2 id="8578a0f2b5f7f9fab6ab15a3ca42c469"></h2>

### Materials, Lighting, and Audio

<h2 id="23ce0eb7d180f3dc8391d4af48572d21"></h2>

#### Materials

A gameobject is often made up of 3D geometry, sometimes called a 3D model. 

You could think the **materials** are the wrapping paper around the gameobject.

A **shader** is basically a formula that defined how the material is rendered , that is how the material looks. There are different types of shaders, each with its own properties. One of the common properties of shader is a texture.

Material -> shader -> texture

A **skybox** is a special type of material that is a wrap around your entire scene, that displays the vast beyond of the world.

You can easily drag a texture to a gameobject. It'll set the texture as main Albedo map (反照率图) in shaer.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/u3d_shader_albedo_map.png)

You can click the albedo icon to show which texture is used by highlighting it in the project view. You can also ctrl+click the albedo icon to show the texture.

The other thing it (drag a texture to a gameobject) did is , it acutally created a material (but how it can find the Material fold and create in the folder ?) . 

You can share same material between game objectes.

Tips: 让某个物体自己表现出像 太阳，灯泡一样发光的效果

删除平行光源，在表示太阳的game object 的shader上，修改 Main Maps的 Emission setting.

Tips: create Skybox

create a material -> change shader type to "Skybox/6 sided" -> set skybox texture -> apply it to the world by UnityMenu Window/Lighting/Scene/skybox


<h2 id="2e4b97fde8cf63085ec969fcc7e490c0"></h2>

#### Lighting

Goal of lighting:

 1. Illumination
    - with illumination , we can see game objects within our scene, but illumination alone often is not enough
 2. Modeling
    - structural and dimensional qualities(reveal or conceal) 
    - spatial（空间的） relationships
    - establish time of day
 3. Focus
    - define contrast in the scene
    - focus the player's attention
 4. Visual Style


Light Type | Description| Primary purpose
--- | --- | ---
ambient | Reflected Light | illumination
directional | Sunlight (parallel rays) | illumination and modeling
point | Light bulb(灯泡) | illumination and modeling
spot | Flashlight | modeling and focus

<h2 id="d2da94913f9bfb60bf8744e04701732c"></h2>

##### Real-time Lighting

 - lights has no geometry
    - we see the result of a light , but we don't see the light itself. 
 - the more lights, the more processor intensive
 - shadows and other lighting effectes also processor intensive


<h2 id="0b7dbebb68099152ba453cb992a19ee4"></h2>

##### Change ambient light

Window/Lighting/Scene

change "AmbientSource" from "Skybox" to "Color" , you can change the color and intensity.

<h2 id="c578e22deb4b879b0a68b887b4a6e5ce"></h2>

##### Point Light

you can change the Range, Color, and so on.

<h2 id="b22f0418e8ac915eb66f829d262d14a2"></h2>

#### Audio

Basic audio of Unity:

 - Audio Listener
    - often attached to the camera
    - you only have 1 audio listener component turned on at any one time in your unity scene.
    
 - Audio Source
    - attached to game objects
    - drag a sound file to game object to easily add a audio source component , choose "Loop" to loop the sound.
    - you can modify the 3D sound setting

<h2 id="5548d227c389d436b5533a8e72058981"></h2>

### Cameras, Building for Web, and Deploying

<h2 id="967d35e40f3f95b1f538bd248640bf3b"></h2>

#### Camera

In a game engine, the camera really is just a projection of the 3D geometry onto a 2D plane of the display. 

Two types of 3D projection:

 - perspective 
 - orthographics
 
The view frustum determines what is rendered in the display. 
     
<h2 id="5241862f585708e8be3777b44d9d6441"></h2>

##### create a minimap Camera

close the audio listener of new camera to turn off warning messager.

change projection to "Orthographic".

多个camera的渲染顺序由它们的depth决定。 

Modify the w/h of Viewport Rect to make a minimap camera. Change the "Clear flags" to "Solid color" to remove the skybox from minimap camera.

<h2 id="bc9eb11a4b1b7761c1941d0ca36e9d72"></h2>

### Building , Deploying


---

<h2 id="aa52d2f45f695a401e95e6a21bd24f1f"></h2>

## Project 2 : Roller Madness Game

When you change a audio setting , eg. click "Force To Mono" , it didn't actually replace the asset or update the asset, it just stored a new copy in the cache of the project. So you can undo that.  

So it's not modifying those files in project asset folder. When it imports , it makes a separate copy into the ***library*** with the various import settings.

 1. Use **Standard Assets**/Prototyping
    - FloorPrototype64\*1\*64 , reset the component
    - The floor is a little bigger, so set the scale to (0.5,1,0.5)
    - ok
    - FloorPrototype4\*1\*4
    - Find the material 414 userd , duplicated a new material *"bumper Material"*
    - change Albedo map texture to *"swatch teal"*
    - apply the new material to bumper
    - creat a prefab
 2. **Standard Assets**/Characters/Characters/ RollerBall/Prefabs/RollerBall
    - Roller ball is tagged as "Player" , this is many script used to detect the roller ball on collision detect.
 3. Camera Setup
    - choose the roller ball, F key
    - Apply **Standard Assets**/Utility/SmoothFollow script to camera
    - add a audio source to camera 
        - **A good place to add game music is typically a gameObject that has the active audio listener component.** 

<h2 id="50ae99e9c35446c2580e4b540b0fd104"></h2>

### Physics

 - 3D Physics = PhysX Engine
 - 2D Physics = Box2D Engine


<h2 id="af17bfc214bfe362db7ee5deaada8711"></h2>

#### Collider  (碰撞相关)

The collider component is what is acctually used to detect collisions on the game object.

This green circle is basically representative of the collider on this object.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/green_line_collider.png)

You can change the size of collider.

By default colliders prevent things from overlapping, but if you turn on this ***"Is Trigger"*** it makes this into a trigger.

So **triggers** are useful to detect a collision between game objects without actually preventing the object from passing through each other.

你可以有两个collider，一个负责碰撞，一个作为trigger。


A collider has a physic "material".

<h2 id="48640050253b1ce0c375421d95b77d74"></h2>

#### Rigidbody  (物理相关)

RigidBodies allow colliders to be affected by physics.

It's generally a good idea to have rigid bodies on any game objects that have colliders and that are moving in some fashion(以某种方式), like the Roller Ball.

 - Use Gravity  使用重力
 - Is Kinematic(运动)
    - if checked , the object will not be driven by physics. 
    - This is useful when you want to move an object directly through the transform. 当我们给一个物体添加rigidbody，这个物体就受无力引擎控制了，like the Roller ball, the ball script actully moves the ball by applying forces rather than than just moving it directly through the transform. But if you wanted to modify the transform directly through scripts, or if wanted to have an animation on the ball through the animation system , you would turn "Is Kinematic" on.
     

<h2 id="457dd55184faedb7885afd4009d70163"></h2>

#### Review

Physics are created throuth 2 components on game objects, the rigidBody and the collider.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/rigidbody_and_collider.png)

 - RigidBody : enables physics on the game object
 - collider : detect collisions between game objects

<h2 id="997e837eabd8235dd27a016e5906d54e"></h2>

### Trail Render

 - select a game object -> add Component -> Effect -> Trail Renderer
    - change Time/Start Width/End Width to maybe 2/0.8/0
 - create a material "Trail Material" 
    - change shader to "Particles-> Alpha Blender" 
    - change color tint to white "FFFFFF"
 - Apply the material to Trail Renderer component
 - Change Trail render "Colors (5 totals)"


<h2 id="9bbf373797bf7cf7ba62c80023682e25"></h2>

### Controller

[360 Controller Mac Driver](https://github.com/360Controller/360Controller/releases)

[InControl](http://www.gallantgames.com/pages/incontrol-introduction)
 
InControl is a great 3D party enhanced Input Manager to Unity for making games that support multiple controllers on multiple platforms. We do not use it here because it costs money on the Unity Asset Store. However, if you are serious about building games that support multiple controllers across multiple platforms, I highly recommend taking a look at it.


<h2 id="a2aa6b4bebf569d55787e53bb224c072"></h2>

### Coins

We commonly create coins by "PickupPrototype", but in unity5 , it seems have some bug, there is no mesh attached.

We tag the coin with "Pickup".

<h2 id="aec53bb2266ce5b41cc0539da9f7de20"></h2>

### UI Basic

create UI/Text -> rename 2 Score Text

Canvas Scaler (Script) -> Ui Scale Mode: **Scale with screen size**

Text -> anchor setting (shift + alt 同时)

Text -> set Font Size -> horizontal/vertical overlap

add a GameOverCanvas -> Ui Scale Mode: **Scale with screen size** 

 - add a "EndGameScore Text" , copy the setting from "Score Text" (Paste Component Values).
 - add a "Play Again Button" ,  button "On Click" 属性中添加 相应 脚本事件。


<h2 id="d6b6b668dbca9d4fe774bb654226ebe3"></h2>

### Animation

select a game object -> #6 

click record button,  start editing clip
