...menustart

 - [PPU registers](#ce3374e3bdbab692e3e6d81eefca5fa6)

...menuend


<h2 id="ce3374e3bdbab692e3e6d81eefca5fa6"></h2>

# PPU registers

https://wiki.nesdev.com/w/index.php/PPU_registers

 - PPU 暴露了8个 内存映射过的 寄存器给CPU, 位于 CPU的地址空间 $2000 - $2007 , 并且 在 $2008-$3FFF 做镜像, 这8k内存都是 PPU I/O区


## Summary

Common Name | Address | access | Bits | Notes
--- | --- | ---
PPUCTRL | $2000 | write | VPHB SINN | NMI enable (V), PPU master/slave (P), sprite height 8 or 16 (H), background tile select (B), sprite tile select (S), increment mode (I), bg nametable select (NN)
PPUMASK | $2001 | write | BGRs bMmG | color emphasis (BGR), show sprite enable (s), show background enable (b), sprite left column enable (M), background left column enable (m), greyscale (G)
PPUSTATUS | $2002 | read | VSO- ---- | vblank (V) 1: in vblank , sprite 0 hit (S), sprite overflow (O) (>8 in a line), read resets write pair for $2005/2006
OAMADDR | $2003 | | aaaa aaaa | OAM read/write address
OAMDATA | $2004 | | dddd dddd | OAM data read/write
PPUSCROLL | $2005 | | xxxx xxxx | fine scroll position (two writes: X, Y)
PPUADDR | $2006 | | aaaa aaaa | PPU read/write address (two writes: MSB, LSB)
PPUDATA | $2007 | | dddd dddd | PPU data read/write
OAMDMA | $4014 | | aaaa aaaa | OAM DMA high address





 - 开机后，PPU 不一定处于可用状态，CPU需要做一些事情使它工作






