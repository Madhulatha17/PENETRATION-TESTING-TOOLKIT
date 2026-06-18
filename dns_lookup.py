import dns.resolver

def dns_lookup(domain):
    print("\nDNS Records\n")

    try:
        result = dns.resolver.resolve(domain, 'A')

        for ip in result:
            print(ip)
    except Exception as e:
        print("Error:", e)
