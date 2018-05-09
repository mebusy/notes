// Example NMI code, by Bob Rost
// nmi_wait allows you to spinlock until the Non-Maskable Interrupt is signaled
// at the start of a vblank. Note that you must set bit 7 of $2000 to enable NMI.


nmi_wait:
	set nmi_hit 0
	nmi_wait_1:
		if nmi_hit = 0 branchto nmi_wait_1
	return

nmi:
	//save registers so we don't destroy them during interrupt
	push a
	push x
	push y

	set nmi_hit 1

	//restore registers
	pop y
	pop x
	pop a
	resume
