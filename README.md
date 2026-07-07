# Sealflux

An 8-key macropad with OLED, rotary encoder, and RGB LEDs. Powered by a Seeed XIAO RP2040 running KMK firmware.

## Features
- 7 Cherry MX switches + 1 rotary encoder (with pushbutton)
- 5 layers: Main, Media, Home Assistant, Game, Other
- Rotary encoder for volume and scrolling
- 128x64 OLED display showing current layer
- WS2812 RGB LEDs with animations
- KMK firmware (CircuitPython)

## Hardware
- Seeed XIAO RP2040
- 7x Cherry MX switches
- 1x EC11 rotary encoder
- 1x SSD1306 128x64 OLED
- 7x WS2812 RGB LEDs
- 3D-printed case (top + bottom)

## BOM
| Part | Quantity | Notes |
|------|----------|-------|
| Seeed XIAO RP2040 | 1 | |
| Cherry MX switches | 7 | |
| EC11 rotary encoder | 1 | |
| SSD1306 OLED 128x64 | 1 | I2C |
| WS2812 LEDs | 7 | |
| 1N4148 diodes | 7 | |
| M2 screws | 4 | |
| 3D-printed case | 1 set | top + bottom |

## Pinout
| Function | XIAO Pin | GPIO |
|----------|----------|------|
| Col 0 | D0 | GP0 |
| Col 1 | D1 | GP1 |
| Col 2 | D2 | GP2 |
| Col 3 | D3 | GP3 |
| SDA | D4 | GP4 |
| SCL | D5 | GP5 |
| Row 0 | D6 | GP6 |
| Enc A | D7 | GP7 |
| Enc B | D8 | GP8 |
| Row 1 | D9 | GP9 |
| LED | D10 | GP10 |

## Firmware
KMK (CircuitPython). To install, copy `main.py` and the KMK library folder to the XIAO RP2040 after flashing CircuitPython.

## Photos
[Add photos after assembly]

## Demo
[Add video link after assembly]