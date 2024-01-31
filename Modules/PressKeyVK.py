import ctypes
from ctypes import wintypes
from Modules.KeyCode import KeyCode
import time
import mouse

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_KEYBOARD = 1
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
MAPVK_VK_TO_VSC = 0
# msdn.microsoft.com/en-us/library/dd375731

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))
    
class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))
    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)
class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))
    
class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))
    
LPINPUT = ctypes.POINTER(INPUT)

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

keyCode = KeyCode()

def pressKey(common_key):
    key = common_key[0]
    try:
        if key == "w":
            print(f"Pressing {key}")
            hex = keyCode.toKeyCode(key)
            PressKey(hex)
            time.sleep(0.1)
            ReleaseKey(hex)

        elif key == "a":
            print(f"Pressing {key}")
            hex = keyCode.toKeyCode(key)
            PressKey(hex)
            time.sleep(0.1)
            ReleaseKey(hex)

        elif key == "s":
            print(f"Pressing {key}")
            hex = keyCode.toKeyCode(key)
            PressKey(hex)
            time.sleep(0.1)
            ReleaseKey(hex)

        elif key == "d":
            print(f"Pressing {key}")
            hex = keyCode.toKeyCode(key)
            PressKey(hex)
            time.sleep(0.1)
            ReleaseKey(hex)

        elif key == "e":
            print(f"Pressing {key}")
            hex = keyCode.toKeyCode(key)
            PressKey(hex)
            time.sleep(0.1)
            ReleaseKey(hex)
        
        elif key == "q":
            print(f"Pressing {key}")
            hex = keyCode.toKeyCode(key)
            PressKey(hex)
            time.sleep(0.1)
            ReleaseKey(hex)

        elif key == "r":
            print(f"Pressing {key}")
            hex = keyCode.toKeyCode(key)
            PressKey(hex)
            time.sleep(0.1)
            ReleaseKey(hex)

        elif key == "m1":
            print(f"Pressing left mouse button")
            time.sleep(0.2)
            mouse.click("left")

        elif key == "m2":
            print(f"Pressing right mouse button")
            time.sleep(0.2)
            mouse.click("right")

        elif key == "space":
            print(f"Pressing {key}")
            hex_int = int("0x20", 16)
            PressKey(hex_int)
            time.sleep(0.1)
            ReleaseKey(hex_int)
        
        elif key == "shift":
            print(f"Pressing {key}")
            hex_int = int("0xA0", 16)
            PressKey(hex_int)
            time.sleep(0.1)
            ReleaseKey(hex_int)
        
        elif key == "ctrl":
            print(f"Pressing {key}")
            hex_int = int("0xA2", 16)
            PressKey(hex_int)
            time.sleep(0.1)
            ReleaseKey(hex_int)

        elif key == "f1":
            print(f"Pressing {key}")
            hex_int = int("0x70", 16)
            PressKey(hex_int)
            time.sleep(0.1)
            ReleaseKey(hex_int)
        
        elif key == "alt":
            print(f"Pressing {key}")
            hex_int = int("0xA4", 16)
            PressKey(hex_int)
            time.sleep(0.1)
            ReleaseKey(hex_int)

        elif key == "1":
            print(f"\nPressing {key}")
            hex = keyCode.toKeyCode(key)
            PressKey(hex)
            time.sleep(0.1)
            ReleaseKey(hex)

        elif key == "2":
            print(f"\nPressing {key}")
            hex = keyCode.toKeyCode(key)
            PressKey(hex)
            time.sleep(0.1)
            ReleaseKey(hex)
        
        elif key == "3":
            print(f"Pressing {key}")
            hex = keyCode.toKeyCode(key)
            PressKey(hex)
            time.sleep(0.1)
            ReleaseKey(hex)

        elif key == "4":
            print(f"Pressing {key}")
            hex = keyCode.toKeyCode(key)
            PressKey(hex)
            time.sleep(0.1)
            ReleaseKey(hex)

        elif key == "5":
            print(f"Pressing {key}")
            hex = keyCode.toKeyCode(key)
            PressKey(hex)
            time.sleep(0.1)
            ReleaseKey(hex)

    except:
        print("\nInvalid Keypress\n")
