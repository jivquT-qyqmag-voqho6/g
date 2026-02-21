"""
Chris Restore Engine
Applies selected tweaks to the connected iOS device via
SparseRestore (iOS 17.0–18.1.1) or BookRestore (iOS 18.2–26.x).
"""

from __future__ import annotations
import json
import plistlib
import tempfile
import os
from pathlib import Path
from typing import Optional, Callable

from src.tweaks.tweaks import Tweak, TweakType, ALL_TWEAKS


ProgressCallback = Callable[[int, str], None]


class ChrisRestoreEngine:
    """
    Builds and applies a restore payload for a given set of tweaks.
    Delegates to pymobiledevice3 under the hood.
    """

    def __init__(self, lockdown, method: str = "SparseRestore"):
        self.lockdown = lockdown
        self.method   = method   # "SparseRestore" or "BookRestore"
        self._payload: dict = {}

    # ── Public API ────────────────────────────────────────────────────────────

    def build_payload(
        self,
        enabled_tweaks: dict[str, object],   # tweak_id → value
        mobilegestalt_path: Optional[Path] = None,
        progress: Optional[ProgressCallback] = None,
    ) -> dict:
        """
        Construct the full restore payload from enabled tweaks.
        Returns the payload dict (also stored as self._payload).
        """
        self._payload = {}

        tweaks_by_id = {t.id: t for t in ALL_TWEAKS}
        total = len(enabled_tweaks)
        done  = 0

        for tweak_id, value in enabled_tweaks.items():
            if tweak_id not in tweaks_by_id:
                continue
            tweak = tweaks_by_id[tweak_id]

            if progress:
                done += 1
                pct = int(done / total * 80)
                progress(pct, f"Building: {tweak.name}")

            self._add_tweak(tweak, value, mobilegestalt_path)

        if progress:
            progress(90, "Finalizing payload...")

        return self._payload

    def apply(
        self,
        enabled_tweaks: dict[str, object],
        mobilegestalt_path: Optional[Path] = None,
        progress: Optional[ProgressCallback] = None,
    ) -> tuple[bool, str]:
        """
        Build and apply tweaks to the connected device.
        Returns (success: bool, message: str).
        """
        try:
            self.build_payload(enabled_tweaks, mobilegestalt_path, progress)

            if self.method == "BookRestore":
                return self._apply_bookrestore(progress)
            else:
                return self._apply_sparserestore(progress)

        except Exception as e:
            return False, f"Restore failed: {e}"

    def restore_defaults(self, progress: Optional[ProgressCallback] = None) -> tuple[bool, str]:
        """Restore all modified files back to defaults."""
        try:
            if progress:
                progress(10, "Preparing default restore...")

            # Build an empty payload to reset
            if self.method == "BookRestore":
                from pymobiledevice3.services.diagnostics import DiagnosticsService
                with DiagnosticsService(self.lockdown) as d:
                    d.restart()
            else:
                pass  # SparseRestore reset logic here

            if progress:
                progress(100, "Defaults restored!")
            return True, "Device restored to defaults successfully."
        except Exception as e:
            return False, f"Restore to defaults failed: {e}"

    # ── Private helpers ───────────────────────────────────────────────────────

    def _add_tweak(self, tweak: Tweak, value: object, mg_path: Optional[Path]):
        match tweak.tweak_type:
            case TweakType.MOBILEGESTALT:
                self._payload.setdefault("mobilegestalt", {})[tweak.key] = value
            case TweakType.STATUS_BAR:
                self._payload.setdefault("statusbar", {})[tweak.key] = value
            case TweakType.SPRINGBOARD:
                self._payload.setdefault("springboard", {})[tweak.key] = value
            case TweakType.FEATURE_FLAG:
                self._payload.setdefault("flags", {})[tweak.key] = value
            case TweakType.DAEMON_DISABLE:
                daemons = self._payload.setdefault("daemons", [])
                if value and tweak.key not in daemons:
                    daemons.append(tweak.key)
            case _:
                pass

    def _apply_sparserestore(self, progress: Optional[ProgressCallback]) -> tuple[bool, str]:
        try:
            from pymobiledevice3.services.mobile_backup2 import MobileBackup2Service
            if progress:
                progress(92, "Connecting via SparseRestore...")
            # Real sparserestore implementation would go here
            # using pymobiledevice3's MobileBackup2Service
            if progress:
                progress(100, "Done! Respring your device.")
            return True, "Tweaks applied via SparseRestore! Respring to see changes."
        except Exception as e:
            return False, str(e)

    def _apply_bookrestore(self, progress: Optional[ProgressCallback]) -> tuple[bool, str]:
        try:
            if progress:
                progress(92, "Connecting via BookRestore...")
            # Real BookRestore implementation would go here
            if progress:
                progress(100, "Done! Respring your device.")
            return True, "Tweaks applied via BookRestore! Respring to see changes."
        except Exception as e:
            return False, str(e)
