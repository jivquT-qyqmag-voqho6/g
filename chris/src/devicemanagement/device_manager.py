"""
Chris Device Manager
Handles USB device connection, detection, and iOS version info.
"""

from __future__ import annotations
import platform
from dataclasses import dataclass
from typing import Optional


@dataclass
class DeviceInfo:
    name: str
    udid: str
    ios_version: str
    model: str
    hardware: str
    color: str
    capacity: str
    paired: bool = True


class DeviceManager:
    """
    Wraps pymobiledevice3 to find and connect to iOS devices.
    Falls back gracefully if no device is connected.
    """

    def __init__(self):
        self._device: Optional[DeviceInfo] = None
        self._lockdown = None

    def find_device(self) -> Optional[DeviceInfo]:
        """Attempt to connect to a plugged-in iOS device."""
        try:
            from pymobiledevice3.lockdown import create_using_usbmux
            self._lockdown = create_using_usbmux()
            info = self._lockdown.all_values

            self._device = DeviceInfo(
                name        = info.get("DeviceName", "Unknown Device"),
                udid        = self._lockdown.udid,
                ios_version = info.get("ProductVersion", "?"),
                model       = info.get("ProductType", "Unknown"),
                hardware    = info.get("HardwareModel", "Unknown"),
                color       = info.get("DeviceColor", "Unknown"),
                capacity    = info.get("TotalDiskCapacity", "?"),
                paired      = True,
            )
            return self._device

        except ImportError:
            print("[Chris] pymobiledevice3 not installed — running in demo mode.")
            return self._demo_device()
        except Exception as e:
            print(f"[Chris] Device not found: {e}")
            return None

    def _demo_device(self) -> DeviceInfo:
        """Return a fake device for UI testing without a real iPhone."""
        return DeviceInfo(
            name        = "Demo iPhone",
            udid        = "00000000-DEMO-DEMO-DEMO-000000000000",
            ios_version = "18.1.1",
            model       = "iPhone16,2",
            hardware    = "D84AP",
            color       = "#1C1C1E",
            capacity    = "128GB",
            paired      = False,
        )

    @property
    def device(self) -> Optional[DeviceInfo]:
        return self._device

    @property
    def lockdown(self):
        return self._lockdown

    def ios_version_tuple(self) -> tuple[int, ...]:
        """Parse iOS version string to comparable tuple, e.g. '18.1.1' → (18,1,1)."""
        if not self._device:
            return (0,)
        try:
            return tuple(int(x) for x in self._device.ios_version.split("."))
        except Exception:
            return (0,)

    def supports_sparserestore(self) -> bool:
        v = self.ios_version_tuple()
        return (17, 0) <= v <= (18, 1, 1)

    def supports_bookrestore(self) -> bool:
        v = self.ios_version_tuple()
        return v >= (18, 2)

    def restore_method(self) -> str:
        if self.supports_bookrestore():
            return "BookRestore"
        if self.supports_sparserestore():
            return "SparseRestore"
        return "Unsupported"
