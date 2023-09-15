#	requires ImageMagick: http://www.imagemagick.org/
#	 and python PNG module: https://pypi.python.org/pypi/pypng 

import os,sys				# filesystem functions
import png				# PNG image library

try:
	INPUTFILE = sys.argv[1]				# what RAM file to parse
	RAM = open(INPUTFILE, "rb")		# open the RAM file for reading
except:
	sys.exit(0)				# exit on exception - no file chosen
finally:
	PNG = open("VisableMemory.png", "wb")	# open a PNG for writing

BYTES = []
PIXELS = []

try:
	byte = RAM.read(1)			# read a byte
	while byte !="":			# while the file still has bytes in it
		byte = RAM.read(1)	
	if len(byte) > 0:		# the last byte, for whatever reason, is length 0. Bah.
		BYTES.append(ord(byte)) # append the number representing the byte (0-255) to the BYTES array	
except:
	print("\n\nOops.")
	sys.exit(0)				# exit on exception - file is empty, etc
finally:
	for LINE in range(0,35,1):		# for each of the 35 tracks
		LINE=[]				# start a new line of pixels
	for SECTOR in range(0,4096,1):	# write the bytes for the sectors in that track to the line array
		offset = (SECTOR * TRACK) + SECTOR
		LINE.append(BYTES[(SECTOR * TRACK) + SECTOR])

	sys.stdout.write("\r Track: " + str(TRACK))
	sys.stdout.flush()
	PIXELS.append(LINE)		# add the array of pixels to the array of arrays

	sys.stdout.write("\n\n\r Done.\n\n")
	sys.stdout.flush()
 
					# write to the PNG file 
w = png.Writer(4096,35, greyscale=True, bitdepth=8) 
w.write(PNG, PIXELS)			# each number in the array becomes a pixel in the image. each array becomes a line.


RAM.close()				# done with these files. close them.
PNG.close()

OUTPUTFILE = os.path.join(INPUTFILE + ".png")
os.system('open ' + OUTPUTFILE)		# opens the resulting image in the default image viewer (Preview.app)

