...menustart

- [PPU registers](#ce3374e3bdbab692e3e6d81eefca5fa6)
    - [Summary](#290612199861c31d1036b185b4e69b75)
        - [PPUSTATUS $2002 < read](#12db96d2c957aa2e0f62efba7438d684)
        - [PPUADDR ($2006) >> write x2](#e610d6d0ebcec60e47429845a26b4cdc)
    - [PPU power up state](#2ea9139a25965e25aa6292e0d86f9ebf)
        - [Best practice](#50802d3e5a25b93d471686a10da03dd8)
    - [Init code](#08c865722ec499f5a7baef6aecb8afa0)

...menuend


<h2 id="ce3374e3bdbab692e3e6d81eefca5fa6"></h2>


# PPU registers

https://wiki.nesdev.com/w/index.php/PPU_registers

- PPU 暴露了8个 内存映射过的 寄存器给CPU, 位于 CPU的地址空间 $2000 - $2007 , 并且 在 $2008-$3FFF 做镜像, 这8k内存都是 PPU I/O区


<h2 id="290612199861c31d1036b185b4e69b75"></h2>


## Summary

Common Name | Address | access | Bits | Notes
--- | --- | --- | --- | --- 
PPUCTRL | $2000 | write | VPHB SINN | NMI enable (V), PPU master/slave (P), sprite height 8 or 16 (H), background tile select (B), sprite tile select (S), increment mode (I), bg nametable select (NN)
PPUMASK | $2001 | write | BGRs bMmG | color emphasis (BGR), show sprite enable (s), show background enable (b), sprite left column enable (M), background left column enable (m), greyscale (G)
PPUSTATUS | $2002 | read | VSO- ---- | vblank (V) 1: in vblank , sprite 0 hit (S), sprite overflow (O) (>8 in a line), read resets write pair for $2005/2006
OAMADDR | $2003 | write | aaaa aaaa | OAM address you want to access 
OAMDATA | $2004 | read/write | dddd dddd | OAM data read/write,write will increase OAM address
PPUSCROLL | $2005 | writex2 | xxxx xxxx | fine scroll position (two writes: X, Y)
PPUADDR | $2006 | writex2 | aaaa aaaa | PPU read/write address (two writes: MSB, Less Significant Bits)
PPUDATA | $2007 | read/write | dddd dddd | PPU data read/write
OAMDMA | $4014 | write | aaaa aaaa | OAM DMA high address


<h2 id="12db96d2c957aa2e0f62efba7438d684"></h2>


### PPUSTATUS $2002 < read

- 该寄存器反映了PPU内各种功能的状态
- 它通常用于确定时间
    - 为了确定PPU何时到达屏幕的给定像素，将精灵0的不透明像素放在那里。

```
7  bit  0
---- ----
VSO. ....
|||| ||||
|||+-++++- Least significant bits previously written into a PPU register
|||        (due to register not being updated for this address)
||+------- Sprite overflow. The intent was for this flag to be set
||         whenever more than eight sprites appear on a scanline, but a
||         hardware bug causes the actual behavior to be more complicated
||         and generate false positives as well as false negatives; see
||         PPU sprite evaluation. This flag is set during sprite
||         evaluation and cleared at dot 1 (the second dot) of the
||         pre-render line.
|+-------- Sprite 0 Hit.  Set when a nonzero pixel of sprite 0 overlaps
|          a nonzero background pixel; cleared at dot 1 of the pre-render
|          line.  Used for raster timing.
+--------- Vertical blank has started (0: not in vblank; 1: in vblank).
           Set at dot 1 of line 241 (the line *after* the post-render
           line); cleared after reading $2002 and at dot 1 of the
           pre-render line.
```

- Note
    - 读取状态寄存器将清除上面提到的D7，
        - 还有PPUSCROLL和PPUADDR使用的address latch。
    - 一旦精灵0命中标志被设置，它将不会被清除，直到下一个VBlank结束。
        - 如果试图将该标志用于光栅定时，要确保精灵0命中检查发生在垂直空白之外，否则CPU将will "leak" through , 并且检查将失败。

<h2 id="e610d6d0ebcec60e47429845a26b4cdc"></h2>


### PPUADDR ($2006) >> write x2

- The CPU writes to VRAM through a pair of registers on the PPU
    - First it loads an address into PPUADDR
    - and then it writes repeatedly to PPUDATA to fill VRAM.
- For example, to set the VRAM address to $2108:
    - 选择地址后，通过 PPUDATA 连续写入数据

```
  lda #$21
  sta PPUADDR
  lda #$08
  sta PPUADDR
```
 



----


- 开机后，PPU 不一定处于可用状态，CPU需要做一些事情使它工作 ...

<h2 id="2ea9139a25965e25aa6292e0d86f9ebf"></h2>


## PPU power up state

- Initial Register Values
    - ? = unknown, x = irrelevant, + = often set, U = unchanged

Register | At Power | After Reset
---| ---| ---
PPUCTRL ($2000) | 0000 0000 | 0000 0000
PPUMASK ($2001) | 0000 0000 | 0000 0000
PPUSTATUS ($2002) | +0+x xxxx | U??x xxxx
OAMADDR ($2003) | $00 | unchanged1
$2005 / $2006 latch | cleared | cleared
PPUSCROLL ($2005) | $0000 | $0000
PPUADDR ($2006) | $0000 | unchanged
PPUDATA ($2007) read buffer | $00 | $00
odd frame | no | no
OAM | pattern | pattern
NT RAM (external, in Control Deck) | mostly $FF | unchanged
CHR RAM (external, in Game Pak) | unspecified pattern | unchanged


<h2 id="50802d3e5a25b93d471686a10da03dd8"></h2>


### Best practice

- Writes to the following registers are ignored if earlier than ~29658 CPU clocks after reset:
    - PPUCTRL, PPUMASK, PPUSCROLL, PPUADDR. 
    - This also means that the PPUSCROLL/PPUADDR latch will not toggle.
- The other registers work immediately
    - PPUSTATUS, OAMADDR, OAMDATA ($2004), PPUDATA, and OAMDMA ($4014).
- 确保29658个周期过去的最简单方法，这也是 商业NES游戏使用的方式，在您的初始化代码中包含一对如下所示的循环：

```
  bit PPUSTATUS  ; clear the VBL flag if it was set at reset time
vwait1:          ; wait PPUSTATUS d7 to set 
  bit PPUSTATUS  
  bpl vwait1     ; at this point, about 27384 cycles have passed
vwait2:
  bit PPUSTATUS
  bpl vwait2     ; at this point, about 57165 cycles have passed
```

<h2 id="08c865722ec499f5a7baef6aecb8afa0"></h2>


## Init code

- 当NES上电或复位时，程序应在fixed bank中执行以下操作：
    - Set IRQ ignore bit    
        - 不是必须的, 因为 6502在包括RESET在内的所有中断上设置了该标志, 但是它允许程序代码使用 `JMP ($FFFC)` 来模拟RESET
    - 禁用PPU NMI和渲染
    - 初始化堆栈指针
    - 初始化mapper（如果有的话）
- 此后的init code可以放在fixed bank, 或 另一个单独的bank , using a bankswitch followed by a JMP:
    - 禁用十进制模式
        - 由于2A03没有十进制模式，所以不是必须的，但禁用它 可以保持与通用6502调试器的兼容性
    - 如果使用了一个 会产生 IRQ的 mapper( 如 MMC3 , MMC5),  请禁用 [APU timer IRQs](https://wiki.nesdev.com/w/index.php/APU_Frame_Counter)
    - 禁用DMC IRQ
    - 将程序使用的所有RAM设置为 known state 。  这通常涉及
        - 清除内部 2K RAM$0000- $07FF
        - 清除 PRG RAM，如果需要的话 $6000- $7FFF (用作存档的话 不清)
    - 至少等待 30000个周期，再访问 OAMADDR , PPUDATA 寄存器
        - 见上面的 PPU power up state, 等待 PPU通过 PPUSTATUS  发出两次VBlank开始的信号

---

- 一些mapper 没有 fixed bank. 
    - 因为它们一次切换整个 32k的PRG. 
    - 这些包括AxROM，BxROM，GxROM和MMC1的一些配置。
    - 你必须在每个bank都加入同样的代码，包括 中断向量，bank swith的代码。通常情况下, 位于 $FF00-$FFFF 的页面 包括 中断向量，init code的开始，以及 一个跳板(trampoline) 用来从一个bank的代码 跳到 另一个bank的代码.

- Sample implementation:

```
reset:
    sei        ; ignore IRQs
    cld        ; disable decimal mode
    ldx #$40
    stx $4017  ; disable APU frame IRQ
    ldx #$ff
    txs        ; Set up stack
    inx        ; now X = 0
    stx $2000  ; disable NMI
    stx $2001  ; disable rendering
    stx $4010  ; disable DMC IRQs

    ; Optional (omitted):
    ; Set up mapper and jmp to further init code here.

    ; If the user presses Reset during vblank, the PPU may reset
    ; with the vblank flag still true.  This has about a 1 in 13
    ; chance of happening on NTSC or 2 in 9 on PAL.  Clear the
    ; flag now so the @vblankwait1 loop sees an actual vblank.
    bit $2002

    ; First of two waits for vertical blank to make sure that the
    ; PPU has stabilized
@vblankwait1:
    bit $2002
    bpl @vblankwait1

    ; We now have about 30,000 cycles to burn before the PPU stabilizes.
    ; One thing we can do with this time is put RAM in a known state.
    ; Here we fill it with $00, which matches what (say) a C compiler
    ; expects for BSS.  Conveniently, X is still 0.
    txa
@clrmem:
    sta $000,x
    sta $100,x
    ; $0200 skip , it used for sprite
    sta $300,x
    sta $400,x
    sta $500,x
    sta $600,x
    sta $700,x  ; Remove this if you're storing reset-persistent data

    ; We skipped $200,x on purpose.  Usually, RAM page 2 is used for the
    ; display list to be copied to OAM.  OAM needs to be initialized to
    ; $EF-$FF, not 0, or you'll get a bunch of garbage sprites at (0, 0).

    inx
    bne @clrmem

    ; Other things you can do between vblank waits are set up audio
    ; or set up other mapper registers.

@vblankwait2:
    bit $2002
    bpl @vblankwait2
```






