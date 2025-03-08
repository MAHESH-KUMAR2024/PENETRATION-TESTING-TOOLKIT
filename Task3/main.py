import modules.port_scanner as port_scanner
import modules.brute_forcer as brute_forcer
import modules.web_scanner as web_scanner
import modules.network_sniffer as network_sniffer

def main():
    print("\n=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute-Force Attack")
    print("3. Web Vulnerability Scanner")
    print("4. Network Sniffer")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        target = input("Enter target IP or domain: ")
        port_scanner.scan(target)
    elif choice == "2":
        brute_forcer.run_brute_force()
    elif choice == "3":
        url = input("Enter target URL: ")
        web_scanner.scan_web(url)
    elif choice == "4":
        network_sniffer.sniff_packets()
    elif choice == "5":
        print("Exiting...")
    else:
        print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
