import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

rgb = RGB(pixel_pin=board.D6, num_pixels=4)
keyboard.modules.append(rgb)

# 8 key pins
PINS = [board.D1, board.D2, board.D4, board.D3,
        board.D7, board.D0, board.D29, board.D28]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Keymap for 8 keys

keyboard.keymap = [
    [
        KC.Macro(Press(KC.ALT), Tap(KC.TAB), Release(KC.ALT)),
        KC.Macro(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)),  # Copy
        KC.Macro(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)),  # Paste
        KC.MACRO("hi, i need a macro to type this sentence"),  # types text
        KC.MUTE,
        KC.VOLU,
        KC.LAYER_NEXT,
        KC.LAYER_PREV,   # I'm going to add more presets later as needed
    ],
    [
        KC.RGB_TOG,
        KC.RGB_MODE_PLAIN,
        KC.RGB_MODE_BREATHE_RAINBOW,
        KC.RGB_MODE_KNIGHT,
        KC.RGB_HUI,   # color shift
        KC.RGB_SAI,
        KC.LAYER_NEXT,
        KC.LAYER_PREV, 
    ],
]


# Rotary encoder setup
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D26, board.D27),)
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),)  # CW = Volume Up, CCW = Volume Down
]

if __name__ == '__main__':
    keyboard.go()
