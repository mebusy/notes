## Intro to U3D

### U3D Editor Walkthrough

You can copy **new** assets directly into assets folder in the OS, and they'll be imported into Unity. But you should **only rename or move** files within the projects tab itself of Unity Editor. This will ensure that any connections to the game assets will be maintained within the editor.

#### View Control

Short Cut Key | desc 
--- | --- 
Shift + Space | Toggle view (mouse at) to full screen
Alt + Left M | Rotate
Alt + Meddle M | Panning
Alt + Right M | Zomming 

> PS: Alt relate to observer mode

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


#### Camera Manipulation

 - Move scene to desired view
 - Select Camera
 - Choose GameObject -> Align with View
 - Also can move camera like an object

### 小技巧

#### 1  区分scene  / game 

如果你有时会在播放模式下改文件，改完以后发现在Play模式下白改了...

那么这个功能还是蛮有用的，点击Edit/Preferences,点击Color, 修改 Playmode tint ,这就是播放模式下的面板颜色。（改成一个醒目的颜色）

#### 2 如何在Play模式下快速调整数值！？

首先点击播放进入Play模式，在这个模式下你可以一次性调整好你要的数值，（这里我们用位置Position举例）

然后右键CopyComponent，回到Scene模式下。

在你复制的Component这里右键PastComponentValue就可以复制刚才你调整的数值~！

记住 一次只能Copy一个Component

#### 3 使用右上角的Layers显示和隐藏物体（适用于Scene视角里编辑多个物体）

#### 4 使用Profiler查看游戏运行性能！

Profiler 可以通过 scene view 右下角的menu 调出

#### 5 Unity有个bug！

有时候 当你用鼠标中键放大物体的时候，物体会消失！这个时候点击Edit/LockView to Selected 或者直接按快捷键Shift+F,物体就可见了！~


---

## Creating and Integrating Assets

### Game Graphics Concept

#### Resolution

 - resolution or pixel dimensions
 - pixel density
 - aspect ratio

are all important concepts to grasp when designing.

#### Frame Rate

The goal of **frame rate** is 30+ fps.

#### Model

 - Bitmap
 - Vector

Non-power of 2 images are possible, they may slow down performance of your game , and should *only* be used for user interface elements.

3D graphics (mesh) are essentially vector graphics in 3 dimension.

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

#### 3D File Formats

File Format | Extension | Features
--- | --- | ---
Maya | .mb or .ma | Maya feature
3dsmax | .max | 3dsmas feature
Blender | .blend | Blender feature
FBX | .fbx | 3D objects + animation , Unity default format
OBJ | .obj | Static 3D objects

Unity actually converts the proprietary formats into an FBX file upon. Therefore, you can have an proprietary format in your project.

### Creating Game Graphics

#### Finding Graphics

 - Unity Asset Store
 - OpenGameArt.org
 - TurboSquid
 - BitGem
 - cgTrader.com
 
### Game Audio Concept

#### Model

 - Digitized Audio (focus in this lecture)
 - Synthesized

#### Audio File Formats

File Format | Extension | Features
--- | --- | ---
Audition | .sesx | Audition multitrack features
Audacity | .aup | Audacity project feature
WAV | .wav | uncompressed or compressed audio
AIFF | .aif or .aiff | uncompressed or compressed audio
MPEG-1 Layer 3 | .mp3 | compressed audio
OGG Vorbis | .ogg | compressed audio, open source

### Creating Game Audio

#### Sound Editing Tools

 - Adobe Audition
 - Avid Pro Tools
 - Audacity (free)

#### Music

 - Think about it early in the design process
 - Pick a style
 - Take inventory of what you need


#### Finding Sound Effects

 - Unity Asset Store
 - www.freesound.org
 - www.newgrounds.com
 - www.sounddogs.com

#### Finding Music

 - Unity Asset store
 - incompetech.com
 - SFX resources

### The Asset Pipeline

you must have Maya installed on your computer to import Maya files.

#### Import Settings

on the game asset within the Unity Editor

