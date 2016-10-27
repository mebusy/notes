


# NES

# Architecture

NES Console

 - 6502 CPU 
 	- 16 bit address bus
 	- 64 kB address space
 		- 0x0000 - 0xFFFF
 	- Four register
 		- Accumulator
 			- perform maathematical operations 
 			- compare the value stored in it
 		- X , Y increment register
 			- basically those are used for storing values such as counters 
 		- Status
 			- can not write
 			- but can read from it to get certain value like if the accumulator overflows and it will put a status there saying that your value has overflowed
 - APU ( Audio Processing Unit )
 - PPU ( Picture Processing Unit  )
 	- 16 KB address space
 - Lockout chip


Game Cartridge

 - CHR ( Charater Memory ) ROM or RAM
 	- where all your sprite data is stored 
 - PRG ( Program Memory ) ROM
 	- where your game code is stored
 - WRAM ( optional ) and battery
 - Lockout chip

When NES is on ,

 - PRG ROM copied to CPU
 - CHR copied to PPU
 - CPU write to the PPU 
 	- to modify the background and the sprites



# CPU / PPU address space

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/6502_CPU_PPU_address_space.png)

from CPU

 - buttom 2KB internal RAM 
 	- which can be used for things like variables 
 - next 2KB ?
 	- PPU ports , use for writing to the PPU
 - on the top of it,    APU  and control ports
 - WRAM
 - Cartridge ROM 
 - at the very end of it  , NMI / RESET / IRQ vectors
 	- NMI , for every frame that gets displayed to the screen , that's going to called and then from there it's going to run all of the code that modified your sprites and backgrounds and upateds the game engine.
 	- RESET , gets called whenever the nes starts up , beasts up, and reset button is pressed 
 	- IRQ , i haven't used that , it uesd for special circumstances


from PPU 

 - 1st 2KB , 
 	- the pattern tables , and that's basically all the sprite data
 - name tabels 
 	- basically the arrangement of all the sprites on the screen that creats the background
 - attribute tabels
 	- determines the colors that are used to paint the background 
 	- you have multiple name tables and attribute tables  , so you can switch between these to give you different backgourds in your game 
 - sprite palette , backgroud palette
 	- you have limited number of colors you can choose from , and that is stored in these palette variables


# 6502 Assembly

 - Directives 
 	- Assembler commands
 	- Start with a period
 - Labels
 	- Used to organize code
 	- Like a BASIC line number (for GOTO)
 	- Not intented and followed by a colon
 - Opcodes
   	- Program instructions
   	- Indented 


# 6502 Opcodes

you should take special considerations if your values are going to add to more than 256

 - Load / Store
 	- Load: LDA , LDX, LDY
 	- Store:  STA , STX, STY
 - Math
 	- Add: ADD , CLC
 	- Subtract : SBC, SEC
 	- Increment:  INC, DEC , INX , INY , DEX , DEY 
 	- Shift :  ASL  , LSR 
 - Comparision
 	- CMP , CPX , CPY
 - Control
 	- JMP
 	- BEQ , BNE 


# Assembly Starter

 \ | C   |  6502  | Desc
 --- |:--- |:---  | --- 
declare  |  int num;   |   .rsset  $0000  |  where your variable in the memory address
vars     |			   |   num .rs 1	  |  reserved 1 byte space 
ASSIGN	 |  num = 42   |   LDA #$2A
		 |			   |   STA num
IF       |  if (num==5) |  LDA num 
		 | | 				CMP #$05
		 | |				BNE Done
		 | | 				; do something
		 | | 			    Done: 
PROCEDURE |  void MyMethod() {  | MyMethod:
		 |	 // do somthing  	|   : do something
		 |	}					|  RTS
		 |	...					| ...
		 |  MyMethod();			| JSR MyMethod
INCREMENT | x = 10; 		| LDA #$0A
		  | x ++ ;			| STX
		  | y = 32 ;		| INX 
		  | y-- ;			| LDA #$20
		  |					| STY
		  |					| DEY
WHILE LOOP  | x = 0 ;			| LDA #$0
			| while (x<255) {	| STX
			|	// do something | Loop:
			|	x ++ 			|	; do something
			|	} 				| INX 
			|					| CPX #$FF
			|					| BNE Loop
INTERRUPT 	|	void Draw() {		| NMI:
METHODS		|		// draw code 	| ; modify sprites
			|	} 					| ; modify background
			|	void Update() { 	| ; update code
			|		// update code  | RTI
			|   } 					| 


# Sprite

 - Can be created with programs like YY-CHR
 - Each sprite tile is 8x8 pixels
 - Each sprite tile can only have 4 unique colors
 	- actually 3  colors and 1 transparency layer
 - Objects , such as mario , are usually composed of multiple sprite tiles
 - All sprites must fit on a single spritesheet


# Palettes

 - Less than 60 total colors
 - PPU IO ports : $2006 , $2007
 	- you write to the palette table by using PPU $2006, $2007 ports
 - Sprite palette: $3F10
 - Background palette :  $3F00





















