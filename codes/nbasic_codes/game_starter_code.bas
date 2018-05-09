//header for nesasm
asm
	.inesprg 1 ;//one PRG bank
	.ineschr 1 ;//one CHR bank
	.inesmir 0 ;//mirroring type 0
	.inesmap 0 ;//memory mapper 0 (none)
	.org $8000
	.bank 0
endasm



start:
	set a 0
	set $2000 a
	set $2001 a //turn off the PPU
	asm
		sei ;//disable interrupts
	endasm
	gosub vwait
	gosub vwait //it's good to wait 2 vblanks at the start
	asm
		ldx #$ff
		txs ;//reset the stack
	endasm
	set $2000 %10101000 //NMI, 8x16 sprites, bg 0, fg 1
	set $2001 %00011000 //show sprites, bg, clipping
mainloop:
	gosub nmi_wait
	gosub draw
	gosub vwait_end
	//gosub game_step
	goto mainloop

nmi_wait:
	set nmi_hit 0
	nmi_wait_1:
		if nmi_hit = 0 branchto nmi_wait_1
	return

//When enabled (bit 7 of $2000) NMI executes at 60fps
nmi:
	push a
	push x
	push y
	set nmi_hit 1
	pop y
	pop x
	pop a
	resume

irq:
	resume

//wait full vertical retrace
vwait:
	gosub vwait_start
	gosub vwait_end
	return

//wait until start of vertical retrace
vwait_start:
	asm
		lda $2002
		bpl vwait_start
	endasm
	return

//wait until end of vertical retrace
vwait_end:
	asm
		lda $2002
		bmi vwait_end
	endasm
	//set scroll and PPU base address
	set a 0
	set $2005 a
	set $2005 a
	set $2006 a
	set $2006 a
	return

draw:
	return


//file footer
asm
;//jump table points to NMI, Reset, and IRQ start points
	.bank 1
	.org $fffa
	.dw nmi, start, irq
;//include CHR ROM
	.bank 2
	.org $0000
	.incbin "background.chr"
	.incbin "foreground.chr"
endasm
