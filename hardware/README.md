### Schematic and layout
The schematic and layout was/is created with KiCad version 4.

I'm using some custom symbols, mods and 3D models, they are all
in this folder.

### LED placement
First I placed the LEDs manually. I have drawn a few
circles on the layout and lines from the middle in ~6° steps...

All in all that was really messy and not the way I used to work.  
So I wrote a small Python program to calculate position and angle
of every LED and wite it to the layout file.

Check out the scrit in the *scripts* folder.

### BOM
BOM generation is done using the *bom2csv.xsl* plugin.
Most schemativ parts have a *R* attribute with the reichelt.de
part number.