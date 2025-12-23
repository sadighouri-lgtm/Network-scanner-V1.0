import pyfiglet
import ipaddress
import nmap

print(pyfiglet.figlet_format("NETWORK SCANNER V1.0"))

network_input = input("Enter network range (e.g 192.168.100.0/24): ")
target = input("Enter target IP: ")

try:
    network = ipaddress.ip_network(network_input, strict=False)

    if ipaddress.ip_address(target) in network:
        print("✔ IP is in range")

        U = input("If you want to scan press Y: ").lower()
        if U == "y":
            print("🔍 Scanning started...")
            nm = nmap.PortScanner()
            nm.scan(target, '1-100')

            if target in nm.all_hosts():
                print("✔ Host is UP")
                print("Protocols:", nm[target].all_protocols())
            else:
                print("❌ Host is DOWN or not responding")
        else:
            print("❌ Scan cancelled")

    else:
        print("❌ Sorry, the IP is not in range")

except ValueError:
    print("❌ Invalid IP or network format")
