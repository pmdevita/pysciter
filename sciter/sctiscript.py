"""TIScript Virtual Machine Runtime.

Incomplete.
"""
import ctypes

HVM = ctypes.c_void_p


class tiscript_native_interface(ctypes.Structure):
    """."""
    _fields_ = [
        ("create_vm", ctypes.c_void_p),
        ]
