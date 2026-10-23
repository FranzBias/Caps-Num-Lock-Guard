#!/usr/bin/env python3
##########################################################
##                Caps & Num Lock Guard                 ##
##  Switches Caps Lock off, keeps Num Lock the way you  ##
##                         want                         ##
##                 written in Python 3                  ##
##                          🍅                          ##
##       by FranzBias 2026 · github.com/FranzBias       ##
##            Licensed under the MIT License            ##
##          See LICENSE file for full license.          ##
##########################################################
# SPDX-License-Identifier: MIT
"""
Caps & Num Lock Guard — keeps an eye on the two lock keys.

WHY this script exists:
  * CAPS LOCK left on by mistake turns a friendly message into SHOUTING.
    The guard switches it off after a few seconds, or as soon as you move
    to another window — whichever comes first.
  * NUM LOCK on a desktop keyboard is almost always wanted ON (numbers on
    the keypad). If you switch it off on purpose (keypad arrows), the guard
    waits until you stop typing and then switches it back on. It can also
    keep it always OFF, or leave it alone.

All settings live in ~/.config/caps-num-lock-guard/config.ini, created with
defaults on first run and re-read automatically when you save it: no restart.

Requires (X11): xset, xdotool, xinput. Optional: numlockx (more reliable).

Usage:
    caps-num-lock-guard.py                 run the guard
    caps-num-lock-guard.py --write-config  create the default config and exit
    caps-num-lock-guard.py --show-config   print the settings in use and exit
"""

import argparse
import configparser
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "caps-num-lock-guard"
CONFIG_FILE = CONFIG_DIR / "config.ini"

DEFAULT_CONFIG = """\
# Caps & Num Lock Guard — settings
# Save this file and the guard picks up the changes within a second.

[caps_lock]
# true = switch Caps Lock off automatically, false = never touch it
enabled = true
# seconds Caps Lock may stay on
timeout_seconds = 10
# also switch it off as soon as the active window changes
off_on_window_change = true

[num_lock]
# always_on  = keep Num Lock on (switched back on when you stop typing)
# always_off = keep Num Lock off
# ignore     = never touch Num Lock
mode = always_on
# seconds without keyboard activity before Num Lock is restored
idle_seconds = 5

[general]
# how often the lock state is checked, in seconds
poll_interval = 0.5
"""

NUM_MODES = ("always_on", "always_off", "ignore")


class Settings:
    """Settings read from config.ini, with safe fallbacks for bad values."""

    def __init__(self) -> None:
        self.caps_enabled = True
        self.caps_timeout = 10.0
        self.caps_off_on_window_change = True
        self.num_mode = "always_on"
        self.num_idle = 5.0
        self.poll_interval = 0.5

    @classmethod
    def load(cls, path: Path) -> "Settings":
        s = cls()
        cp = configparser.ConfigParser(inline_comment_prefixes=("#", ";"))
        try:
            cp.read(path, encoding="utf-8")
            s.caps_enabled = cp.getboolean("caps_lock", "enabled", fallback=s.caps_enabled)
            s.caps_timeout = max(1.0, cp.getfloat("caps_lock", "timeout_seconds", fallback=s.caps_timeout))
            s.caps_off_on_window_change = cp.getboolean(
                "caps_lock", "off_on_window_change", fallback=s.caps_off_on_window_change)
            mode = cp.get("num_lock", "mode", fallback=s.num_mode).strip().lower()
            s.num_mode = mode if mode in NUM_MODES else "always_on"
            s.num_idle = max(0.5, cp.getfloat("num_lock", "idle_seconds", fallback=s.num_idle))
            s.poll_interval = min(5.0, max(0.1, cp.getfloat("general", "poll_interval", fallback=s.poll_interval)))
        except (configparser.Error, ValueError) as exc:
            print(f"[guard] config has an error, using defaults: {exc}", file=sys.stderr)
            return cls()
        return s

    def describe(self) -> str:
        return (f"caps: enabled={self.caps_enabled} timeout={self.caps_timeout}s "
                f"window_change={self.caps_off_on_window_change} | "
                f"num: mode={self.num_mode} idle={self.num_idle}s | poll={self.poll_interval}s")


def ensure_config() -> None:
    """Create the config file with defaults if it does not exist yet."""
    if not CONFIG_FILE.exists():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        CONFIG_FILE.write_text(DEFAULT_CONFIG, encoding="utf-8")


# ---------- keyboard LEDs and keys ----------

_own_press = 0.0  # last time the guard itself pressed a key

def led_state(name: str) -> bool:
    """Read an LED state ("Caps Lock" or "Num Lock") from `xset q`."""
    out = subprocess.run(["xset", "q"], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if name + ":" in line:
            return line.split(name + ":")[1].split()[0].lower() == "on"
    return False


def active_window() -> str | None:
    r = subprocess.run(["xdotool", "getactivewindow"], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def press(key: str) -> None:
    """Press a key on the user's behalf; remember when, so it is not taken for typing."""
    global _own_press
    _own_press = time.time()
    subprocess.run(["xdotool", "key", key])
    _own_press = time.time()


def set_numlock(on: bool) -> None:
    """Set Num Lock to a given state, deterministically (never a blind toggle)."""
    if shutil.which("numlockx"):
        subprocess.run(["numlockx", "on" if on else "off"])
        return
    for _ in range(2):  # Num_Lock is a toggle: press only if needed, then re-check
        if led_state("Num Lock") == on:
            return
        press("Num_Lock")
        time.sleep(0.15)


# ---------- keyboard activity monitor ----------

_last_key = time.time()


def keyboard_monitor() -> None:
    """Track the last key press (keyboard only, the mouse does not count).

    Restarts xinput by itself if it dies, e.g. after an X server restart.
    """
    global _last_key
    while True:
        try:
            proc = subprocess.Popen(["xinput", "test-xi2", "--root"],
                                    stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
            assert proc.stdout is not None
            for line in proc.stdout:
                # ignore the key presses made by the guard itself (xdotool)
                if "RawKeyPress" in line and time.time() - _own_press > 0.5:
                    _last_key = time.time()
        except Exception:
            pass
        time.sleep(5)


# ---------- main loop ----------

def run() -> None:
    ensure_config()
    settings = Settings.load(CONFIG_FILE)
    config_mtime = CONFIG_FILE.stat().st_mtime
    print(f"[guard] started — {settings.describe()}", flush=True)

    threading.Thread(target=keyboard_monitor, daemon=True).start()

    caps_since: float | None = None
    caps_window: str | None = None

    while True:
        # reload the settings when config.ini is saved
        try:
            mtime = CONFIG_FILE.stat().st_mtime
        except FileNotFoundError:
            ensure_config()
            mtime = CONFIG_FILE.stat().st_mtime
        if mtime != config_mtime:
            config_mtime = mtime
            settings = Settings.load(CONFIG_FILE)
            print(f"[guard] settings reloaded — {settings.describe()}", flush=True)

        # CAPS LOCK: off after the timeout or on window change
        if settings.caps_enabled and led_state("Caps Lock"):
            window = active_window()
            if caps_since is None:
                caps_since, caps_window = time.time(), window
            elif (time.time() - caps_since >= settings.caps_timeout
                  or (settings.caps_off_on_window_change and window != caps_window)):
                press("Caps_Lock")
                caps_since = caps_window = None
        else:
            caps_since = caps_window = None

        # NUM LOCK: restore the wanted state once the keyboard is idle
        if settings.num_mode != "ignore":
            wanted = settings.num_mode == "always_on"
            if led_state("Num Lock") != wanted and time.time() - _last_key >= settings.num_idle:
                set_numlock(wanted)

        time.sleep(settings.poll_interval)


def main() -> None:
    ap = argparse.ArgumentParser(description="Caps & Num Lock Guard")
    ap.add_argument("--write-config", action="store_true", help="create the default config and exit")
    ap.add_argument("--show-config", action="store_true", help="print the settings in use and exit")
    args = ap.parse_args()
    if args.write_config:
        ensure_config()
        print(CONFIG_FILE)
        return
    if args.show_config:
        ensure_config()
        print(f"{CONFIG_FILE}\n{Settings.load(CONFIG_FILE).describe()}")
        return
    try:
        run()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
