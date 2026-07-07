import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.oled import Oled

keyboard = KMKKeyboard()

# Matrix
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D6, board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Layers
layers = Layers()
keyboard.modules.append(layers)

# Encoder
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D7, board.D8, None),)
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),
    ((KC.BRIGHTNESS_UP, KC.BRIGHTNESS_DOWN),),
    ((KC.TRNS, KC.TRNS),),
    ((KC.TRNS, KC.TRNS),),
    ((KC.TRNS, KC.TRNS),),
]
keyboard.modules.append(encoder_handler)

# Keymap — 2 rows × 4 cols
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H],
    [KC.MPLY, KC.MUTE, KC.VOLU, KC.VOLD, KC.MNXT, KC.MPRV, KC.MSTP, KC.TRNS],
    [KC.F13, KC.F14, KC.F15, KC.F16, KC.F17, KC.F18, KC.F19, KC.F20],
    [KC.W, KC.A, KC.S, KC.D, KC.LSFT, KC.SPC, KC.E, KC.R],
    [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS],
]

if __name__ == '__main__':
    keyboard.go()