#!/usr/bin/python3

import requests
import zipfile
import io
import whois
import dns.resolver
import dns.exception

def get_ns_records(domain):
    """Retrieve NS records using whois for a given domain."""
    try:
        w = whois.whois(domain)
        name_servers = [ns.lower() for ns in w.name_servers]
        name_servers = list(set(name_servers))
        return name_servers
    except Exception as e:
        return []

def resolve_ns_to_ip(ns):
    """Resolve nameserver names to IP addresses."""
    try:
        return dns.resolver.resolve(ns, 'A')[0].address
    except Exception as e:
        return None

def check_ns_configuration(domain, ns_list):
    """Check if a domain is correctly configured in its NS servers."""
    grabbable = False
    for ns in ns_list:
        ns_ip = resolve_ns_to_ip(ns)
        if ns_ip:
            try:
                resolver = dns.resolver.Resolver()
                resolver.nameservers = [ns_ip]
                resolver.resolve(domain, 'A')
            except dns.resolver.NoNameservers:
                print(f"Domain {domain} does not exist on {ns}")
                grabbable = True
            except Exception as e:
                grabbable = False
        else:
            grabbable = False

    return grabbable

def load_domains_from_file(filename):
    """Load a list of domains from a file."""
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return []

def grabscan(filename):
    """Check NS servers and their configuration for a list of domains."""
    domains = load_domains_from_file(filename)
    if not domains:
        print("No valid domains found to check.")
        return

    for domain in domains:
        print(f"Checking domain: {domain}")
        ns_list = get_ns_records(domain)
        if ns_list:
            if check_ns_configuration(domain, ns_list):
                print(f"{domain} is grabbable!\n")
                with open("grabbable.txt", "a") as f:
                    f.write(F"{domain}\n")

if __name__ == "__main__":
    # URL of the newly registered domain names file
    url = "https://raw.githubusercontent.com/shreshta-labs/newly-registered-domains/main/nrd-1w.csv"
    
    # Download the file and process it
    response = requests.get(url)
    if response.status_code == 200:
        with open('domains.txt', 'wb') as f:
            f.write(response.content)

        grabscan('domains.txt')
    else:
        print('Failed to download file.')
