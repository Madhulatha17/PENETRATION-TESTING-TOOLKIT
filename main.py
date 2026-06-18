from port_scanner import scan_ports
from header_analyzer import analyze_headers
from dns_lookup import dns_lookup

while True:
    print("\n=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. HTTP Header Analyzer")
    print("3. DNS Lookup")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        host = input("Enter host: ")
        scan_ports(host)

    elif choice == "2":
        url = input("Enter URL: ")
        analyze_headers(url)

    elif choice == "3":
        domain = input("Enter domain: ")
        dns_lookup(domain)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
