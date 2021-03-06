from datetime import datetime
import os
import sys
import time
from os import system
import ctypes

try:
    from pymem.process import module_from_name
    from pymem.ptypes import RemotePointer
    import pymem
except ImportError:
    print('Attempting to install PyMem')
    os.system('python -m pip install pymem')

from pymem.process import module_from_name
from pymem.ptypes import RemotePointer
import pymem

try:
    p = pymem.Pymem("RainbowSix.exe")
except:
    ctypes.windll.user32.MessageBoxA(0, b"Cannot find rocket league, please run rocket league before attempting to use", b"Cannot find rocket league", 0)
    time.sleep(2)
    exit()

system("title " + 'blue nebula unlock - made by e')
os.system('cls')

def resolve_pointer(base, offsets):
    last = base
    for offset in offsets:
        last = RemotePointer(
            p.process_handle,
            last.value + offset
        )
    return last.v.value

unlock = True
while unlock == True:
    print('Unlocking')
    time.sleep(2)
    playerBase = RemotePointer(p.process_handle, module_from_name(p.process_handle, "RainbowSix.exe").lpBaseOfDll + 0x059F18D0)
    playerAddr = resolve_pointer(playerBase, [0xE8, 0x0, 0x0, 0x20, 0x690, 0x10, 0x0])
    uplayID = p.read_string(playerAddr)
    p.write_string(playerAddr, "33c3134a-e9f2-40e2-aac3-4a66e7c4ff38")
    time.sleep(2)
    print('Unlocked equip and close game')
    time.sleep(5)
    break

