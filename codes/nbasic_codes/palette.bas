// Palette example code, by Bob Rost
// Allows you to clear palette, or load an example palette

clear_palette:
	set x 0
	set $2006 $3f
	set $2006 0
	clear_palette_1:
		set $2007 0
		inc x
		if x <> 32 branchto clear_palette_1
	return

load_palette:
	set x 0
	set $2006 $3f
	set $2006 $00
	load_palette_1:
		set $2007 [palette_data x]
		inc x
		if x <> 32 branchto load_palette_1
	return

palette_data:
	data $22,$07,$2d,$3d,$22,$0d,$08,$18,$22,$16,$28,$20,$22,$18,$1a,$29
	data $22,$04,$16,$28,$22,$0d,$20,$29,$22,$0d,$20,$03,$22,$22,$22,$22
