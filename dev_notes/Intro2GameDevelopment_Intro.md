...menustart

	 * [Intro to U3D](#60073da63a8fe62f03ad41e9dd3257d8)
		 * [U3D Editor Walkthrough](#d1baf48cbf113af8eb5fe82dd6835bd7)
			 * [View Control](#98149d4649b603a544c9c52e4a842c31)
			 * [Object Manipulation](#3a6bba43d17d16a59c5b287ae52383a9)
			 * [Camera Manipulation](#6341038ef23e05b20e67a11b1df8cfad)
		 * [小技巧](#97944c42c1af0393a037161a6f969a8a)
			 * [1  区分scene  / game](#a13e518689723e0780936b80012211ae)
			 * [2 如何在Play模式下快速调整数值！？](#ccd349d281be8d5c207785a3037dd3a4)
			 * [3 使用右上角的Layers显示和隐藏物体（适用于Scene视角里编辑多个物体）](#2d60eef6e7cb6b1489d153f83010c7c2)
			 * [4 使用Profiler查看游戏运行性能！](#d07d9f90950e46921b452a73c8be0108)
			 * [5 Unity有个bug！](#40903d7d8ae23cd3a6de269c23c061db)
	 * [Creating and Integrating Assets](#7cd83a4c3d9124376629e883503fe5c5)
		 * [Game Graphics Concept](#3a666fc0fa871ff40964391fc84261aa)
			 * [Resolution](#b5a4b64b2aa505bd7c11f79b8a9f458d)
			 * [Frame Rate](#9cb334507c95e83a9c863f5014ab317e)
			 * [Model](#a559b87068921eec05086ce5485e9784)
			 * [Bitmap File Formats](#d954d326bf4f38870ad7610986913a5a)
			 * [3D File Formats](#42982212f6c8f711f99351449fddec7e)
		 * [Creating Game Graphics](#97cf7ccbe9cc98650c55677345d94ca3)
			 * [Finding Graphics](#b916431abdc2a84097274818cb0bae18)
		 * [Game Audio Concept](#9653e3c0b73e9abc3cfdd77c294872a1)
			 * [Model](#a559b87068921eec05086ce5485e9784)
			 * [Audio File Formats](#89036a6d4d6e0e480158ac61180cceeb)
		 * [Creating Game Audio](#8a19ec7ba24710f9381af1ee60f19f6a)
			 * [Sound Editing Tools](#be1b94570f67133ffca33a9aaec8b3ae)
			 * [Music](#47dcbd834e669233d7eb8a51456ed217)
			 * [Finding Sound Effects](#a1c71b065d3eb978fd93e5f02f25e91a)
			 * [Finding Music](#6859823ead2a91ee4b87255df0ca6463)
		 * [The Asset Pipeline](#cc0375b28e24087901bf75b252540534)
			 * [Import Settings](#352a228c155779f9e34542d5c4e945ce)

...menuend


<h2 id="60073da63a8fe62f03ad41e9dd3257d8"></h2>
## Intro to U3D

<h2 id="d1baf48cbf113af8eb5fe82dd6835bd7"></h2>
### U3D Editor Walkthrough

You can copy **new** assets directly into assets folder in the OS, and they'll be imported into Unity. But you should **only rename or move** files within the projects tab itself of Unity Editor. This will ensure that any connections to the game assets will be maintained within the editor.

<h2 id="98149d4649b603a544c9c52e4a842c31"></h2>
#### View Control

Short Cut Key | desc 
--- | --- 
Shift + Space | Toggle view (mouse at) to full screen
Alt + Left M | Rotate
Alt + Meddle M | Panning
Alt + Right M | Zomming 

> PS: Alt relate to observer mode

<h2 id="3a6bba43d17d16a59c5b287ae52383a9"></h2>
#### Object Manipulation

click to select an object in Scene or Hieratchy

Q,W,E,R,T  respond to 5 modes lies on the top-left corner of Editor.

short cut | switch to mode  | desc 
--- | --- | ---
Q | pan mode | with mouse
W | translate tool | Cmd+Drag:snapping; Shift+cmd:snapping 2 surface; Hold V: Vertex snapping
E | rotate tool | Cmd+Rotate:15度旋转; Shift+Cmd: 什么鬼？
R | scale tool |
T | 
F | frame select |  zoom to selected object,鼠标必须在Scene View中
Cmd + Delete |  | delete object


<h2 id="6341038ef23e05b20e67a11b1df8cfad"></h2>
#### Camera Manipulation

 - Move scene to desired view
 - Select Camera
 - Choose GameObject -> Align with View
 - Also can move camera like an object

<h2 id="97944c42c1af0393a037161a6f969a8a"></h2>
### 小技巧

<h2 id="a13e518689723e0780936b80012211ae"></h2>
#### 1  区分scene  / game 

如果你有时会在播放模式下改文件，改完以后发现在Play模式下白改了...

那么这个功能还是蛮有用的，点击Edit/Preferences,点击Color, 修改 Playmode tint ,这就是播放模式下的面板颜色。（改成一个醒目的颜色）

<h2 id="ccd349d281be8d5c207785a3037dd3a4"></h2>
#### 2 如何在Play模式下快速调整数值！？

首先点击播放进入Play模式，在这个模式下你可以一次性调整好你要的数值，（这里我们用位置Position举例）

然后右键CopyComponent，回到Scene模式下。

在你复制的Component这里右键PastComponentValue就可以复制刚才你调整的数值~！

记住 一次只能Copy一个Component

<h2 id="2d60eef6e7cb6b1489d153f83010c7c2"></h2>
#### 3 使用右上角的Layers显示和隐藏物体（适用于Scene视角里编辑多个物体）

<h2 id="d07d9f90950e46921b452a73c8be0108"></h2>
#### 4 使用Profiler查看游戏运行性能！

Profiler 可以通过 scene view 右下角的menu 调出

<h2 id="40903d7d8ae23cd3a6de269c23c061db"></h2>
#### 5 Unity有个bug！

有时候 当你用鼠标中键放大物体的时候，物体会消失！这个时候点击Edit/LockView to Selected 或者直接按快捷键Shift+F,物体就可见了！~


---

<h2 id="7cd83a4c3d9124376629e883503fe5c5"></h2>
## Creating and Integrating Assets

<h2 id="3a666fc0fa871ff40964391fc84261aa"></h2>
### Game Graphics Concept

<h2 id="b5a4b64b2aa505bd7c11f79b8a9f458d"></h2>
#### Resolution

 - resolution or pixel dimensions
 - pixel density
 - aspect ratio

are all important concepts to grasp when designing.

<h2 id="9cb334507c95e83a9c863f5014ab317e"></h2>
#### Frame Rate

The goal of **frame rate** is 30+ fps.

<h2 id="a559b87068921eec05086ce5485e9784"></h2>
#### Model

 - Bitmap
 - Vector

Non-power of 2 images are possible, they may slow down performance of your game , and should *only* be used for user interface elements.

3D graphics (mesh) are essentially vector graphics in 3 dimension.

<h2 id="d954d326bf4f38870ad7610986913a5a"></h2>
#### Bitmap File Formats

file format | extension | Feature 
---  | --- | --- 
Photoshop | .psd | Photoshop feature , uncompressed
TIFF | .tif or .tiff | Layers , uncompressed
PNG | .png | Good for overall compression , alpha transparency
JPEG | .jpg or .jpeg | Great for compressing photos
GIF | .gif | Great for compressing images with text or cartoons, basic transparency

Unity actually will compress bitmap images for you based on your **import setting** and your **build settings** for the target platform.

Therefore, I prefer to import uncompressed images such as photoshop files. 

Unity does **NOT** directly support 2D vector Graphics.

<h2 id="42982212f6c8f711f99351449fddec7e"></h2>
#### 3D File Formats

File Format | Extension | Features
--- | --- | ---
Maya | .mb or .ma | Maya feature
3dsmax | .max | 3dsmas feature
Blender | .blend | Blender feature
FBX | .fbx | 3D objects + animation , Unity default format
OBJ | .obj | Static 3D objects

Unity actually converts the proprietary formats into an FBX file upon. Therefore, you can have an proprietary format in your project.

<h2 id="97cf7ccbe9cc98650c55677345d94ca3"></h2>
### Creating Game Graphics

<h2 id="b916431abdc2a84097274818cb0bae18"></h2>
#### Finding Graphics

 - Unity Asset Store
 - OpenGameArt.org
 - TurboSquid
 - BitGem
 - cgTrader.com
 
<h2 id="9653e3c0b73e9abc3cfdd77c294872a1"></h2>
### Game Audio Concept

<h2 id="a559b87068921eec05086ce5485e9784"></h2>
#### Model

 - Digitized Audio (focus in this lecture)
 - Synthesized

<h2 id="89036a6d4d6e0e480158ac61180cceeb"></h2>
#### Audio File Formats

File Format | Extension | Features
--- | --- | ---
Audition | .sesx | Audition multitrack features
Audacity | .aup | Audacity project feature
WAV | .wav | uncompressed or compressed audio
AIFF | .aif or .aiff | uncompressed or compressed audio
MPEG-1 Layer 3 | .mp3 | compressed audio
OGG Vorbis | .ogg | compressed audio, open source

<h2 id="8a19ec7ba24710f9381af1ee60f19f6a"></h2>
### Creating Game Audio

<h2 id="be1b94570f67133ffca33a9aaec8b3ae"></h2>
#### Sound Editing Tools

 - Adobe Audition
 - Avid Pro Tools
 - Audacity (free)

<h2 id="47dcbd834e669233d7eb8a51456ed217"></h2>
#### Music

 - Think about it early in the design process
 - Pick a style
 - Take inventory of what you need


<h2 id="a1c71b065d3eb978fd93e5f02f25e91a"></h2>
#### Finding Sound Effects

 - Unity Asset Store
 - www.freesound.org
 - www.newgrounds.com
 - www.sounddogs.com

<h2 id="6859823ead2a91ee4b87255df0ca6463"></h2>
#### Finding Music

 - Unity Asset store
 - incompetech.com
 - SFX resources

<h2 id="cc0375b28e24087901bf75b252540534"></h2>
### The Asset Pipeline

you must have Maya installed on your computer to import Maya files.

<h2 id="352a228c155779f9e34542d5c4e945ce"></h2>
#### Import Settings

on the game asset within the Unity Editor

