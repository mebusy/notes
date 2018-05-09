// Example sprite code, by Bob Rost
// Allows you to easily write and manage sprite memory,
// and use sprite DMA for fast drawing

array absolute $200 spritemem 256

DMA_sprites:
	set $4014 2
	return

// draw_sprite requires these variables:
// sprite_y, sprite_tile, sprite_attrib, and sprite_x
draw_sprite:
	set x numsprites
	set [spritemem x] sprite_y
	inc x
	set [spritemem x] sprite_tile
	inc x
	set [spritemem x] sprite_attrib
	inc x
	set [spritemem x] sprite_x
	inc x
	set numsprites x
	return

// "clear" unused sprites by making sure they are
// below the visible portion of the screen
clear_end_sprites:
	set x numsprites
	clear_sprites_1:
		set [spritemem x] 245
		inc x
		if x <> 0 branchto clear_sprites_1
	set numsprites 0
	return
