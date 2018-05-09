// NES Joystick usage code, by Bob Rost
// Simply "gosub joystick1" to update info about player 1's controller
// nbasic automatically allocates variables joy1a, joy1b, etc.
// Similar usage for player 2.

joystick1:
	set $4016 1 //first strobe byte
	set $4016 0 //second strobe byte
	set joy1a		& [$4016] 1
	set joy1b		& [$4016] 1
	set joy1select	& [$4016] 1
	set joy1start	& [$4016] 1
	set joy1up		& [$4016] 1
	set joy1down	& [$4016] 1
	set joy1left	& [$4016] 1
	set joy1right	& [$4016] 1
	return

joystick2:
	set $4017 1 //first strobe byte
	set $4017 0 //second strobe byte
	set joy2a		& [$4017] 1
	set joy2b		& [$4017] 1
	set joy2select	& [$4017] 1
	set joy2start	& [$4017] 1
	set joy2up		& [$4017] 1
	set joy2down	& [$4017] 1
	set joy2left	& [$4017] 1
	set joy2right	& [$4017] 1
	return
