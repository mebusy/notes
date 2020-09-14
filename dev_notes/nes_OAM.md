...menustart

- [OAM](#1d43a61d31daf8523c598d4679150bd5)
- [DMA](#33fd5f6391f2f0cb4c91179d7f521949)
- [Sprite zero hits](#a543bc0784c262c9da625159ca924ff3)
- [Sprite overlapping](#93433b909a9b00016c6047bd84e2c65d)
- [Internal operation](#5ccdf8c4b0352ef1435663d5f5a7a22a)
- [Dynamic RAM decay](#72c46d82eb28c395ef46aca1c91d10aa)

...menuend


<h2 id="1d43a61d31daf8523c598d4679150bd5"></h2>


# OAM

http://wiki.nesdev.com/w/index.php/PPU_OAM

 - object attributes memory , PPU 内部的一页内存， 最多可以显示 256/4=64个精灵
 - 一般在PRAM中选择1页($200)更新 精灵数据，然后在 V-Blank期间 把数据拷贝到PPU中
 - PPU中的 sprite数据不会保持(dynamic RAM)，所以需要 reflesh it every time 
 - so every time we go through the V-Blank loop , we have to update that memory in the PPU.

---

每个精灵定义，需要4个字节

 - Byte 0 : Y position of top of sprite
    - 精灵数据 会被延迟一个扫描线， 在写入之前，你必须把 Y坐标 减去1
    - 因为电视机上最多显示240行扫描线，所以，只需要在这里 写入 $EF~$FF ， 就可以隐藏精灵
        - $EF = 239 = 240-1
    - Sprites are never displayed on the first line of the picture, and it is impossible to place a sprite partially off the top of the screen.
 - Byte 1 : The index number
    - 可以指定从哪个 4k pattern table 中获取 tile ( PPU  $0000 , $1000 )
        - 8x8 sprite , 由 PPUCTRL ($2000) 的 bit 3 指定
        - 8x16 sprite, 由 Byte1 的 bit 0 指定 (注：每个8x16 精灵pattern 是连续的32个字节, i.e. #0: $0000-$001F)

```
76543210
||||||||
|||||||+- Bank ($0000 or $1000) of tiles
+++++++-- Tile number of top of sprite (0 to 254)
```

 - Byte 2 : Attributes
    - 翻转 不会改变精灵的 bounding box
    - 8x16 mode下，垂直翻转 除了翻转 每个8x8tile之外，还会互换两个tile的位置

```
76543210
||||||||
||||||++- Palette (4 to 7) of sprite
|||+++--- Unimplemented
||+------ Priority (0: in front of background; 1: behind background)
|+------- Flip sprite horizontally
+-------- Flip sprite vertically
```

 - Byte 3 : X position of left side of sprite.
    - 水平滚动值 位于 $F9-FF 区间的时候，(最左的)移除屏幕的精灵部分会 从屏幕右侧出现，为了避免这种情况，屏幕最左侧不会 部分显示精灵
        - left-clipping through PPUMASK ($2001) can be used to simulate this effect.


<h2 id="33fd5f6391f2f0cb4c91179d7f521949"></h2>


# DMA

 - 大部分程序在 CPU RAM的 2页 ( $0200-$02FF ) 处理精灵数据，然后通过 OAMDMA ($4014) register  拷贝到 PPU. 
 - 把 n 写入 $4014, CPU内部的DMA电路 会使用 地址 `$100 *n`  开始的连接字节 写入 OAMDATA ($2004) register 256次 来初始化OAM.
 - 传输过程中，CPU处于暂停状态。
 - 要复制的地址范围 可以位于 PRAM 之外， 仅适用于没有动画的静态画面。
 - 不计算 OAMDMA 的写入时间， 上述过程需要 513个CPU周期;  展开的LDA/STA循环通畅需要4倍时间


<h2 id="a543bc0784c262c9da625159ca924ff3"></h2>


# Sprite zero hits

 - PPU绘制图片时，当精灵0的不透明像素与背景的不透明像素重叠时，这就是一个 **sprite zero hit**
 - PPU检测到这种情况，从该像素开始 将PPUSTATUS（$ 2002）的第6位设置为1，letting the CPU know how far along the PPU is in drawing the picture.


<h2 id="93433b909a9b00016c6047bd84e2c65d"></h2>


# Sprite overlapping

 - 精灵之间的优先权取决于他们在OAM中的地址
    - the sprite data that occurs first will overlap any other sprites after it. 

<h2 id="5ccdf8c4b0352ef1435663d5f5a7a22a"></h2>


# Internal operation

 - 除了主OAM内存之外，PPU还包含32个字节（enough for 8个精灵）的辅助OAM内存, 程序不能直接访问这部分内存。
 - 在每个可见行扫描期间， 首先清除该辅助OAM，然后执行整个主OAM的线性搜索，以找出在下一个扫描线上的精灵 (the sprite evaluation phase) , 并拷贝数据到 辅助OAM,然后用它初始化八个内部精灵输出单元。

<h2 id="72c46d82eb28c395ef46aca1c91d10aa"></h2>


# Dynamic RAM decay

 - 因为OAM是用动态RAM而不是静态RAM来实现的，所以存储在OAM存储器中的数据如果没有被刷新，会很快开始衰减为随机位。
 - 一般来说 OAM内存 每次行扫描的时候都会刷新
 - 但当渲染关闭时，或在帧之间的垂直消隐期间，OAM存储器会在短时间内保持稳定的，然后开始衰减
    - 它将持续至少与NTSC垂直空白区间（〜1.3ms）一样长，但不会比这更长。
 - 因此，在V-Blank之外写入OAM通常不是很有用。 写入$4014 或 $2004 通常应在NMI 中断中完成，否则 应在 V-Blank内完成(NMI可关闭)。
 - If using an advanced technique like forced blanking to manually extend the vertical blank time, it may be necessary to do the OAM DMA last, before enabling rendering mid-frame, to avoid decay.




  

