#!/usr/bin/env python3 -u

import py65.monitor
import select
import os,sys				# filesystem functions
#import png				# PNG image library

# Write to a specific video address
def video_output(address,value):
	# write to binary "visable memory" file
	# tell imagemagick to convert to a png

	file = open('VisableMemory.bin', "r+b")
	file.seek(address - 0x6000) 
	file.write(value.to_bytes(1,'big'))
	file.close()

# Raw file underlying stdin
raw_stdin = sys.stdin.buffer.raw

def map_hardware(m):
	# Video RAM at 0xd000-xd400
	m.subscribe_to_write(range(0x6000,0x7FFF),video_output)

	# Bad memory address to force end to memory check
	m.subscribe_to_read([0x8000], lambda x: 0)

def main(args=None):
	c = py65.monitor.Monitor()
	map_hardware(c._mpu.memory)
	try:
		import readline
	except ImportError:
		pass

	# Load the ROMs and boot
	c.onecmd("load boot-tracing.rom 0000")
	try:
		c.onecmd('version')
		c.cmdloop()
	except KeyboardInterrupt:
		c._output('')

if __name__ == "__main__":
	main()