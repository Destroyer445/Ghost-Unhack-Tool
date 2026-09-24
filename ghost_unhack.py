#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GHOST UNHACK TOOL 👻
By @destroyer445.root | Ghost Lab
Educational Purpose Only
"""

import time
import os

# Colors
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
C = "\033[96m"
W = "\033[0m"

BANNER = f"""
{R}   _____ _               _   _       _            _    
  / ____| |             | | | |     | |          | |   
 | |  __| |__   ___  ___| |_| |_   _| |__   __ _| | __
 | | |_ | '_ \ / _ \/ __| __| | | | | '_ \ / _` | |/ /
 | |__| | | | | (_) \__ \ |_| | |_| | | | | (_| |   < 
  \_____|_| |_|\___/|___/\__|_|\__,_|_| |_|\__,_|_|\_\\
{W}
{G}           PHONE SECURITY SCANNER v1.0 👻{W}
           Creator: @destroyer445.root
           Support The Ghost Lab

"""

def print_slow(text, delay=0.02):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    os.system("clear")
    print(BANNER)
    
    print_slow(f"{Y}[*] Starting Ghost Security Scan...{W}")
    time.sleep(1)

    print(f"\n{C}[01] DEVICE ADMIN CHECK (Spy App){W}")
    print("  -> Settings > Security > Device Admin Apps")
    print("  -> Unknown app like 'System Service' kandal -> Deactivate + Uninstall")
    print(f"  {Y}Command (PC): adb shell dumpsys device_policy{W}")

    print(f"\n{C}[02] CALL FORWARDING HACK CHECK{W}")
    print("  -> Dial: *#21#  (Forwarding Status)")
    print("  -> Dial: *#62#  (When unreachable)")
    print("  -> If any number shown, you are tracked!")
    print(f"  {G} FIX: Dial ##002# to remove all forwarding{W}")

    print(f"\n{C}[03] APP PERMISSION CHECK{W}")
    print("  -> Settings > Apps > Permission Manager")
    print("  -> Check SMS, CALL LOGS, ACCESSIBILITY permission")
    print("  -> Flashlight app SMS read cheyyunnundenkil = FAKE APP")

    print(f"\n{C}[04] NETWORK & VPN CHECK{W}")
    print("  -> Settings > Network > VPN - Unknown VPN OFF")
    print("  -> Dial *#06# - IMEI check")

    print(f"\n{R}--- QUICK UNHACK STEPS ---{W}")
    print("  1. ##002# Dial")
    print("  2. Remove Device Admin Apps")
    print("  3. Uninstall Unknown Apps")
    print("  4. Change Gmail Password + Enable 2FA")
    print("  5. Restart Phone")

    print(f"\n{G}[✓] Scan Complete{W}")
    print(f"{W}If you found forwarding, your phone WAS hacked.")
    print(f"Support: Instagram @destroyer445.root")
    print("root@kali:~# ./ghost_unhack --clean")

if __name__ == "__main__":
    main()
