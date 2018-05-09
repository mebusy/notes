// 6502 8-bit random number originally by Lee Davison
// From http://members.lycos.co.uk/leeedavison/6502/code/prng.html


// You must set random_seed to a non-zero value to initialize
array random_seed 1

// The function returns the random number in the A register
random_number:
	asm
	lda random_seed
	and #$b8
	ldx #$05
	ldx #$00
	random_number_floop:
		asl a
		bcc random_number_bitclr
		iny
	random_number_bitclr:
		dex
		bne random_number_floop
	random_number_noclr:
		tya
		lsr a
		lda random_seed
		rol a
		sta random_seed
		rts
	endasm
