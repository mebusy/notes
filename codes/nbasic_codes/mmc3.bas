// MMC3 memory mapper support
// by Bob Rost

//Commands for $8000 (bits 0-2):
//	0  Select 2k VROM page at PPU $0000  (table 0, tiles 0-127)
//	1  Select 2k VROM page at PPU $0800  (table 0, tiles 128-255)
//	2  Select 1k VROM page at PPU $1000  (table 1, tiles 0-63)
//	3  Select 1k VROM page at PPU $1400  (table 1, tiles 64-127)
//	4  Select 1k VROM page at PPU $1800  (table 1, tiles 128-191)
//	5  Select 1k VROM page at PPU $1c00  (table 1, tiles 192-255)
//	6  Copy to first switchable ROM page
//	7  Copy to second switchable ROM page


// your code should set the variables mmc3_command and mmc3_pagenum
// then call mmc3_execute_command

array mmc3_command 1
array mmc3_pagenum 1


// You should call this once before you use the MMC3
mmc3_init:
	set mmc3_prg_mode 0
	set mmc3_chr_mode 0
	return

//this function is called by
mmc3_execute_command:
	set $8000 + + mmc3_chr_mode mmc3_prg_mode mmc3_command
	set $8001 mmc3_pagenum
	return

// Set to swap banks at $8000 and $a000 (32k and 40k)
mmc3_use_lower_banks:
	set mmc3_prg_mode 0
	return

// Set to swap banks at $a000 and $c000 (40k and 48k)
mmc3_use_upper_banks:
	set mmc3_prg_mode %01000000
	return

// Use normal CHR pattern table address for commands 0-5
mmc3_normal_pattern_table:
	set mmc3_chr_mode 0
	return

// XOR address for commands 0-5 by $1000 (affect the other pattern table)
mmc3_swap_pattern_table:
	set mmc3_chr_mode %10000000
	return

// Set the PPU to horizontal screen mirroring
mmc3_horizontal_mirroring:
	set $a000 0
	return

// Set the PPU to vertical screen mirroring
mmc3_vertical_mirroring:
	set $a000 1
	return

// Enable battery-backed ram at $6000-$7fff
mmc3_enable_save_ram:
	set $a001 1
	return

// Disable battery-backed ram
mmc3_disable_save_ram:
	set $a001 0
	return
