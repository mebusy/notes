...menustart


...menuend


```
WAITFORVBLANK:
    BIT $2002
    BPL WAITFORVBLANK
    RTS
```


```
RESET:
    SEI     ; turn off interrupt
    CLD     ; turn off decimal math,not work on 6502
    LDX #$40    ; turn off audio interrupt
    STX $4017
    LDX #$FF    ; set Stack pointer to 0xFF
    TXS 
    INX         ; X -> 0
    STX $2000   ; turn off graphic rendering
    STX $2001
    STX $4010   ; turn off audio playback

    JSR WAITFORVBLANK   

    TXA         ; init A register
```

```
CLEARMEM:    
    ; clear 2K PRAM
    STA $0000, x
    STA $0100, x
    ; $0200 skip , it used for sprite
    STA $0300, x
    STA $0400, x
    STA $0500, x
    STA $0600, x
    STA $0700, x
    LDA #$FF        ; make all sprite non-visible
    STA $0200, x
    LDA #$00
    STA controller
    INX 
    BNE CLEARMEM
    
    LDA #$21
    STA hswaph 

```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/6502_asm_6.png)


```
; clear register and set 
; palette address
    LDA $2002
    LDA #$3F
    STA $2006
    LDA #$10
    STA $2006

; initialize background hi and low
    LDA #$10
    STA seed
    STA seed+1

    LDA #$02
    STA scrolly

    LDX #$00
PALETTELOAD:
    LDA PALETTE, x    ; PALETTE defined in end
    STA $2007
    INX 
    CPX #$20
    BNE PALETTELOAD

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/6502_asm_8.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/6502_asm_9.png)

 - 64中固定颜色中挑32种颜色供游戏使用，每个tile 同时只能显示4色？


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/6502_asm_end.png)


 - END
