


# NES

# Architecture

NES Console

 - 6502 CPU 
 	- 16 bit address bug
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

