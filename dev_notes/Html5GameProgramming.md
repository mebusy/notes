
# HTML5 Game Programming

# Canvas 

```
<body>
	<canvas> id="my_canvas"</canvas>
</body>
<script>
var canvas = null ;
var context = null ;

setup = function() {
	canvas = document.getElementById( "my_canvas" ) ;
	context = canvas.getContext(  '2d') ;
	canvas.width = 1200 ; // windows.innerWidth ;
	canvas.height = 720 ; // windows.innerHeight ;
} ;

setup();

</script>
```

## Loading an Image

 1. Declare a new Image() object
 2. Declare it's 'onload' method
 3. set Image.src = "url"
 	- as soon as the Image.src is set through a value , JS will kick off `onload` function.
 	- because of this, we need to specify the callback function first before setting the source attribute

```javascript
setup = function() {
	canvas = document.getElementById( "my_canvas" ) ;
	context = canvas.getContext(  '2d') ;
	canvas.width = 1200 ; // windows.innerWidth ;
	canvas.height = 720 ; // windows.innerHeight ;

	img new Image();
	img.onload = onImageLoad;
	img.src = 'ralphyrobot.png'
} ;

onImageLoad = function() {
	console.log( "Image" ) ;
}
``` 

## drawImage
 
 - `var object = object.drawImage( ... )`
 - you can find API details in `webplatform.org`

```
onImageLoad = function() {
	console.log( "Image" ) ;
	context.drawImage( img, 192, 192 ) ;
}
```

## 播放动画

 - load all animation image assets and place then in the frame array
 - after you images are loaded , you should go through and fill out the rest of the animation function
 - before this you need to have some logic that checks for whether or not the images are loaded 
 - and once all of the frames have been loaded , actually does a call to `setInterval`.



```javascript
var frameRate = 1000/30 ;
var frame = 0 ;
var assets = [ 'xxx00.png' , 'xxx01.png' , ... ] ;

setup = function() {
	...

	for (var i =0; i < assets.length ; i++ ) {
		frame.push( new Image() ) ;
		frame[i].src = assets[i] ;
		frame[i].src = assets[i] ;
	}

	setInterval ( animate , frameRate ) ;

} ;

var animate = function() {
	context.clearRect( 0,0,  canvas.width , canvas.height ) ;
	context.drawImage( frames[frame] , 192,192 ) ;
	frame = (frame +1) % frame.length
}

``` 

The canvas doesn't actually clear itself each frame.  You need call clearRect to clear it.


---

# Atlas

 - it's up to about 6 connection for a modern browse.
 - when the upper limit is reached , the browse will actullay block subsequent requests until an open connection becomes available.


usign output from texture packer

```javascript
defSprite: function ( name, x, y, w, h , cx ,cy ) {
	var spt = {
		"id" :	name,
		"x" :	x,
		"y" :	y,
		"w" :	w,
		"h" :	h,
		"cx" :	cx==null ? 0 : cx ,
		"cy" :	cy==null ? 0 : cy ,
	} ;
	this.sprites.push(spt) ;
}

parseAtlasDefinition: function( atlasJson ) {
	var parsed = JSON.parse( atlasJson ) ;

	for( var key in parsed.frames ) {
		var sprite = parsed.frames[key];
		// define the center of the sprite as an offset
		var cx = -sprite.frame.w * 0.5 ;
		var cy = -sprite.frame.h * 0.5 ;

		// define the sprite for this sheet
		this.defSprite( key , sprite.frame.x , sprite.frame.y , sprite.frame.w, sprite.frame.h ,  cx, cy) ;
	}
} 
```

--- 

# Input

## Event listeners

```
document.getElementById( 'canvas' ).addEventListener( 'mousemove' , onMouseMove ) ;
document.getElementById( 'canvas' ).addEventListener( 'keydown' , onKeyDown ) ;

function onMoseMove() {
	var posx = event.clientX ;
	var posy = event.clientY ;

}

function onKeyDown( event ) {
	var keyId = event.keyID ;  // ASCII value

}
```

## an approache

 - Input manager handle the event ,  and keep the input temporarily , for "update procedure" to comsume it later.


## Physics Engine

```
player: init()
{
	var physDat = {
		pos: {x,y} ,
		maxx : 0 ,
		size: {x:20, y:20} ,
		velocity: {x:5 , y:5}
	};
	mpPhysBody = PhysicsEngine.newBody() ;
}
```

 - Directly, the physics body itself exposes a function that allows us to set a linear velocity on it. 

```
function update() {
	var move_dir = new Vec2(0,0) ;
	if(move_dir.LengthSquared()) {
		move_dir.Normalize() ;
		move_dir.Multiply( this.gPlayer0.walkSpeed ) ;  // important  
	}
	this.mpPhysBody.setLinearVelocity( move_dir.x , move_dir.y ) ;
}
``` 

---

# Entity

```
gGameEngine.factory['WeaponInstance'] = WeaponInstanceClass ;

...

var ent = new( entityClass ) (x, y, es) ;
```

Tiled  工具 可以用来编辑相应的 entity object



## Implementing Z-ordering


---

# Physics

## Missing 

可以把 运动物理前后两帧的 collision box 组成一个 大的 collision box ， 做 碰撞检测 ， 以防止 missing.

## Box2D , JS version

```
<script src="./box2d.min.js"> </script>
```

### The World

```
	create: function() {
		this.world = new World() {
			new Vec2( 0 ,0 ) ,	// Gravity vector
			false 				// Boolean for allowing sleep
		} ;
	}
```

upadte:

```
	update: function() {
		var start = Data.now();

		// the more iterations, the more accurate the calculations
		this.world.Step (
			PHYSICS_LOOP_HZ ,   // frame-rate
			10,					// velocity iterations
			10					// position iteration
		) ;

		// call the clearforces method of the world object to 
		// remove any forces at every physics update
		this.world.ClearForces() ;

		return (Date.now() - start);
	}
```


### Physics Bodies

```
registerBody: function( bodyDef ) {
	var body = this.world.CreateBody( bodyDef ) ;
	return body ;
}

addBody : function( entityDef ) {
	var bodyDef = new BodyDef();

	// type:
	// Body.b2_staticBody
	// Body.b2_dynamicBody
	if (entityDef.type== "static") {
		bodyDef.type = Body.b2_staticBody ;
	} else {
		bodyDef.type = Body.b2_dynamicBody ;		
	}

	// Set the position{x,y} member object 
	// of your BodyDef object 
	bodyDef.position.x = entityDef.x ; 
	bodyDef.position.y = entityDef.y ;

	var body = this.registBody(bodyDef) ;
	var fixtureDefinition = new FixtureDef() ;

	if (entityDef.useBouncyFixture ) {
		fixtureDefinition.density = 1.0 ;
		fixtureDefinition.friction = 0 ; 
		fixtureDefinition.restitution = 1.0 ;
	}

	// we now define the shape of this object as a box
	fixtureDefinition.shape = new PolygonShape() ;
	fixtureDefinition.shape.SetAsBox( entityDef.halfWidth, entityDef.halfHeight ) ;
	body.CreateFixture( fixtureDefinition ) ;

	return body ;
}
```

### Destorying Physics Bodies

```
removeBody: function(obj) {
	this.world.DestoryBody(obj) ;
}
```

### Entities and Physics  : TODO 

--- 

# Sound

 - Checking for Compatibility

```
try {
	this._context = new webkitAudioContext();
} 
catch( e ) {
	alert( "web audio API not supported in this browse" ) ;
}
this._mainNode = this._context.createGainNode(0);
this._mainNode.connect( this._context.destination ) ;
```

 - Asynchronous Loading

```
Loaded --> yes -----------------------> callback
	   |-> no  --> Xml Http Request --> callback
```

```
loadAsync: function( path , callbackFcn ) {
	if(this.clips[path]) {
		callbackFcn( this.clips[path].s ) ;
		return this.clip[path].s ;
	}

	var clip = { s: new Sound() , b: null , l: false  } ;
	this.clips[path] = clip ;
	clip.s.path = path ;

	var request = new XMLHttpRequest();
	request.open( "GET" , path, true ) ;
	request.responseType = "arraybuffer" ;
	request.onload = function() {
		gSM._context.decodeAudioData( request.response ,  
		function(buffer) {
			clip.b = buffer ;
			clip.l = true ; 
			callbackFcn( clip.s ) ;
		}
		function(data) {
			Logger.log( "fail" )
		} ) ;
	}
	request.send();

	return clip.s ;
}
``` 


 - Play Sound

```
playSound: function(path , settings) {
	...
	var sd = this.clips[path] ;

	// creates a sound source
	var currentClip = gSM._context.createBufferSource() ;

	// tell the source which sound to play
	currentClip.buffer = sd.b ;
	currentClip.gain.value = volumen ;
	currentClip.connect( gSM._mainNode ) ;
	currentClip.loop = looping ;

	// play the source now
	currentClip.noteOn(0) ;
	return true ;
}
```

 - Stopping Sounds 
 	- The way we do that , is by simply disconnection our main node from the node graph ; creating a new one in its place, and connecting it to our output.

```
stopAll: function() {
	
}
```





