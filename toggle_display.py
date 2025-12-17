#!/usr/bin/env python3
import subprocess
import re
from ctypes import CDLL, util, c_void_p, c_uint32, c_int, c_bool, POINTER, byref


def disable_display(display_id):
    cg = CDLL(util.find_library("CoreGraphics"))

    cg.CGBeginDisplayConfiguration.argtypes = [POINTER(c_void_p)]
    cg.CGBeginDisplayConfiguration.restype = c_int
    cg.CGCompleteDisplayConfiguration.argtypes = [c_void_p, c_int]
    cg.CGCompleteDisplayConfiguration.restype = c_int
    cg.CGCancelDisplayConfiguration.argtypes = [c_void_p]
    cg.CGCancelDisplayConfiguration.restype = c_int
    cg.CGSConfigureDisplayEnabled.argtypes = [c_void_p, c_uint32, c_bool]
    cg.CGSConfigureDisplayEnabled.restype = c_int

    config_ref = c_void_p()
    if cg.CGBeginDisplayConfiguration(byref(config_ref)) != 0:
        return
    if cg.CGSConfigureDisplayEnabled:
        if cg.CGSConfigureDisplayEnabled(config_ref, display_id, False) != 0:
            cg.CGCancelDisplayConfiguration(config_ref)
            return
    cg.CGCompleteDisplayConfiguration(config_ref, 0)


def enable_display(display_id):
    cg = CDLL(util.find_library("CoreGraphics"))

    cg.CGBeginDisplayConfiguration.argtypes = [POINTER(c_void_p)]
    cg.CGBeginDisplayConfiguration.restype = c_int
    cg.CGCompleteDisplayConfiguration.argtypes = [c_void_p, c_int]
    cg.CGCompleteDisplayConfiguration.restype = c_int
    cg.CGCancelDisplayConfiguration.argtypes = [c_void_p]
    cg.CGCancelDisplayConfiguration.restype = c_int
    cg.CGSConfigureDisplayEnabled.argtypes = [c_void_p, c_uint32, c_bool]
    cg.CGSConfigureDisplayEnabled.restype = c_int

    config_ref = c_void_p()
    if cg.CGBeginDisplayConfiguration(byref(config_ref)) != 0:
        return
    if cg.CGSConfigureDisplayEnabled:
        if cg.CGSConfigureDisplayEnabled(config_ref, display_id, True) != 0:
            cg.CGCancelDisplayConfiguration(config_ref)
            return
    cg.CGCompleteDisplayConfiguration(config_ref, 0)


def reset_displays():
    for display_id in range(1, 32):
        enable_display(display_id)


def find_builtin_display():
    max_displays = 32
    cg = CDLL(util.find_library("CoreGraphics"))
    display_ids = (c_uint32 * max_displays)()
    display_count = c_uint32()
    cg.CGGetOnlineDisplayList(max_displays, display_ids, byref(display_count))

    screen_id = 0
    enabled = False

    for i in range(display_count.value):
        cur_screen = display_ids[i]
        if cg.CGDisplayIsBuiltin(cur_screen):
            screen_id = cur_screen
            if cg.CGDisplayIsActive(cur_screen) or cg.CGDisplayIsInMirrorSet(cur_screen):
                enabled = True
            else:
                enabled = False

    return (screen_id, enabled)


if __name__ == "__main__":
    screen_id, enabled = find_builtin_display()
    if screen_id == 0:
        print("No built-in display found. Forcingly enable all of displays")
        reset_displays()
    else:
        if enabled == True:
            print(f"Screen #{screen_id} is built-in display. Disabling")
            disable_display(screen_id)
        else:
            print(f"Screen #{screen_id} is built-in display. Enabling")
            enable_display(screen_id)
