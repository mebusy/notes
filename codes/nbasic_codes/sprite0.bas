// Sprite 0 Hit test, by Bob Rost

// Usage: Detect start of vblank, update sprite DMA, name table,
// and initial scroll values. Gosub wait_for_sprite_0_hit, which
// will return once sprite 0 has hit. Then you may set a new
// scroll value, or use it for frame timing.

wait_for_sprite_0_hit:
	set a 0
	asm
	wait_for_sprite_0_hit_1:
		bit $2002
		bmi wait_for_sprite_0_hit_1
	wait_for_sprite_0_hit_2:
		bit $2002
		bvs wait_for_sprite_0_hit_2
	wait_for_sprite_0_hit_3:
		bit $2002
		bvc wait_for_sprite_0_hit_3
	endasm
	return
