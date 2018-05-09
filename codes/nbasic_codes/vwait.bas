// Vertical Retrace wait code, by Bob Rost
// Allows you to spinlock until start or end of vertical retrace,
// or wait for and entire interval to pass

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
