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

