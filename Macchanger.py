import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptParseError

    parser.add_option("-i", "--interface", dest="interface", help="Interface para cambiar Dirrecion MAC")
    parser.add_option("-m", "--mac", dest="interface", help="Nueva dirrecion MAC")
    parser.add_option("-b", "--interface", dest="interface", help="Cambio infinito de MAC")
    (options, arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[-] Por favor indica una Interfaz, usa --help para mas informacion")
    elif not options.new_mac:
        parser.error("[-] Por favor indica una Nueva dirrecion MAC, usa --help para mas informacion")
    return options

def cambiar_MAC(interface, new_mac):
    print(f"[+] Cambiar dirrecion MAC para  {interface}  a  {new_mac}")

    subprocess.call(f"ifconfig {interface} down " , shell=True)
    subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
    subprocess.call(f"ifconfig {interface} up ", shell=True)
def get_MAC(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    print(ifconfig_result)
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        print(mac_address_search_result.group(0))
    else:
        print("[-] La dirrecion no sigue los estandares de una MAC")

options = get_arguments()
current_MAC = get_MAC(options.interface)
print(f"Current MAC = {current_MAC}")

cambiar_MAC(options.interface, options.new_mac)

current_MAC = get_MAC(options.interface)
if current_MAC == options.new_mac:
    print("[+] MAC cambio correctamente a {current_MAC}")
else:
    print("[-] MAC no ha sido cambiada")
