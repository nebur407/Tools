print("""
     4    000   77777
    44   0   0     77
   4 4   0   0    77
  44444  0   0   77
     4   0   0  77
     4    000  77

******************************
*  realizado por nebur407    *
******************************

""")
import subprocess
import argparse
import re
import random
import time
import platform
def detect_system(interface):
    system = platform.system()
    try:
        if system == "Linux" or system == "Darwin":
            subprocess.check_output(["ifconfig", interface])
        elif system == "Windows":
            print("[-] This script is not supported on Windows.")
            exit()
        else:
            print(f"[-] Unsupported system: {system}")
            exit()
    except Exception as e:
        print(f"[-] Could not check interface: {e}")
        exit()

def get_arguments():
    parser = argparse.ArgumentParser(description="Tool to change MAC address")

    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change the MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address (optional)")
    parser.add_argument("-b", "--infinite", dest="infinite", action="store_true", help="Change MAC in infinite loop press Crtl + C to end.")
    parser.add_argument("-t", "--time", dest="loop_time", type=int, help="Interval time (in seconds) for infinite MAC changes press Crtl + C to end.")

    return parser.parse_args()

def set_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(f"ifconfig {interface} down", shell=True)
    subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
    subprocess.call(f"ifconfig {interface} up", shell=True)

def get_mac(interface):
    try:
        output = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
        mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
        if mac_search:
            return mac_search.group(0)
        else:
            print("[-] MAC address not found or invalid format.")
            return None
    except Exception as e:
        print(f"[-] Error getting MAC address: {e}")
        return None

def generate_random_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ":".join(f"{x:02x}" for x in mac)

def change_mac_loop(interface, delay):
    try:    
        while True:
            mac = generate_random_mac()
            print(f"[+] New random MAC: {mac}")
            set_mac(interface, mac)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("[!] Infinite loop ended")

def change_mac_infinite(interface):
    try:    
        while True:
            mac = generate_random_mac()
            print(f"[+] New random MAC: {mac}")
            set_mac(interface, mac)
    except KeyboardInterrupt:
        print("[!] Infinite loop ended")
    

options = get_arguments()

detect_system(options.interface)

original_mac = get_mac(options.interface)
print(f"[+] Current MAC: {original_mac}")

if options.infinite and options.loop_time:
    change_mac_loop(options.interface, options.loop_time)
elif options.infinite:
    change_mac_infinite(options.interface)
elif options.new_mac:
    set_mac(options.interface, options.new_mac)

updated_mac = get_mac(options.interface)
if updated_mac == options.new_mac:
    print(f"[+] MAC successfully changed to {updated_mac}")
else:
    print(f"[!] Final MAC: {updated_mac}")
