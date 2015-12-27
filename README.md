# About
This project was started for testing the new KiCad v4
as a replacement for EAGLE.

I want a free ECAD software without the limiations, so
I started this to explore the capabilities of KiCad.

Conclusion: KiCad can be a good replacement for EAGLE and co.  
It has some rough edges, but makes a point with some
great features.

# Nice 3D pics :)
![PCB 3D](https://cdn.rawgit.com/janhieber/NiceClock/master/doc/PCB_3D.jpg)

# Current progress
### Hardware

TODO:  
- [ ] schematic
  - [x] LEDs and WS2803 ICs
    - [x] wire up
    - [x] connect to CPU
  - [x] CPU (STM32F1)
  - [ ] real time clock
    - [x] wire up
    - [x] connect to CPU
  - [x] SWD program and serial terminal
- [ ] layout
  - [ ] LEDs
  - [ ] WS2803
  - [ ] STM32 CPU
  - [x] RTC
  - [x] power supply
  

For the current progress, look at the
[schematic](https://raw.githubusercontent.com/janhieber/NiceClock/master/hardware/doc/schematic.pdf)
and
[layout](https://raw.githubusercontent.com/janhieber/NiceClock/master/hardware/doc/board.pdf) PDFs.

### Software
Software development not started yes.

The software will be written in pure C.  
STM32CubeMX will be used as initialisation code generator.

TODO:  
- [ ] STM32 software
  - [ ] hardware initialisation
  - [ ] cooperative scheduler
  - [ ] real time clock code
  - [ ] LED control code for WS2803 ICs via SPI
  - [ ] DCF77 code
  - [ ] Bootloader for serial program download over UART
- [ ] Software to flash firmware via serial connection


# Community
If you are interessted in this, feel free to contact me.  
I'll also have some spare PCBs when I ordner them, so I'll sell them.
