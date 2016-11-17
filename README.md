# BDC-6500: ROMs and other information gathered from a customized KIM-1

I purchased this customized KIM-1 computer from an estate sale, and have since been documenting it and trying to get it working again.

In the handmade enclosure, I found a Rev D KIM-1, a 16K memory board, an 8K "Visable memory" board, and finally a hand-wired ROM board. The 4 1k ROMs were labelled KVOS.

The only documentation I've found of KVOS is a single ad announcing its availability as a 6502 OS available from CGRS Microtech, in the December 1978 issue of Popular Electronics:
http://www.classiccmp.org/cini/pdf/pe/1978/PE1978-Dec-pg90.pdf#page=2

I was able to dump the ROMs with a handmade board (see https://github.com/option8/ROMbie) though the dumps seem to be corrupted in places. I'm not sure yet if it's the ROMs themselves or the reader.

This repo is to document the disassembly of the ROMs and other findings as I get deeper into rehabbing the original BDC-6500.

## Disassembly
I'm using da65 with the info.txt file in the main directory. Since the ROMs seem to be corrupted, I've made some modifications to the complete dump, in the file F000-FFFF-combined-modified.rom. The original dump can be found, unmodified, as well. As I update my reader, I will replace the dumps, if they end up being cleaner.

## Hardware
Photos of the enclosure, boards and wiring here:
http://retroconnector.com/bdc-6500-computer-kim-1/

## Character ROM
I've recreated the KVOS font from the character section of the ROM. Bitmaps of the full ASCII set are in the "Character ROM" directory. 

