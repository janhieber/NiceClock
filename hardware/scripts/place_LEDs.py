#!/bin/env python3

import math as m

# set in / out file
filein = 'NiceClock.kicad_pcb'
fileout = 'NiceClock_.kicad_pcb'

# search for this to get the LED sections in the file
fidx1 = '(module custom_janh:PLCC2 (layer F.Cu) '

# this are the radii where the LEDs are placed
rad1 = (250/2) -6 -5
rad2 = rad1 -5 -5 -5

# this is the general offset, it depends on the grid origin and your layout position
offsetx = 160.528 -4.32
offsety = 147.32 

# open the layout file and read it to list
f = open(filein, 'r')
l = f.read().split('\n')
f.close()

# process every entry and find LED sections
for i in range(0, len(l)-1):
    if l[i].strip().startswith(fidx1):
        # get the LEDs reference, it's used to calculate its position and angle
        ref = l[i+3].strip().split(' ')[2]
        # calc angle
        angle = int((int(ref[1:]) -1) /2 ) *6
        # calc placement for inner or outer circle
        if (int(ref[1:]) % 2) == 0:
            posy = round(offsety - rad2 * m.cos(m.radians(angle)), 2)
            posx = round(rad2 * m.sin(m.radians(angle)) + offsetx, 2)
        else:
            posy = round(offsety - rad1 * m.cos(m.radians(angle)), 2)
            posx = round(rad1 * m.sin(m.radians(angle)) + offsetx, 2)
        # correct the angle the way KiCad wants it (CCW)
        angle = 360 -angle
        # write the new positions and angles
        l[i+1] = '    (at %s %s %s)' % (posx, posy, angle)
        l[i+3] = '    (fp_text reference %s (at -0.508 -3.302 %s) (layer F.SilkS)' % (ref, angle)
        l[i+6] = '    (fp_text value LED (at 0.254 3.302 %s) (layer F.Fab)' % (angle)
        l[i+11] = '    (pad 2 smd rect (at 1.524 0 %s) (size 1.5 2.6) (layers F.Cu F.Paste F.Mask)' % (angle)
        l[i+13] = '    (pad 2 smd rect (at 2.286 0 %s) (size 4 5) (layers F.Cu)' % (angle)
        l[i+15] = '    (pad 1 smd rect (at -2.286 0 %s) (size 4 5) (layers F.Cu)' % (angle)
        l[i+17] = '    (pad 1 smd rect (at -1.524 0 %s) (size 1.5 2.6) (layers F.Cu F.Paste F.Mask)' % (angle)

# open new file and write back the changed layout
f = open(fileout, 'w')
for line in l:
    l = f.write("%s\n" % line)
f.close()
