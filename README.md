## nrd_grabscan.py

This script scans a list of domains retrieved from a specified URL to identify "grabbable" domain names. A domain is considered grabbable if it has been registered, its DNS is pointed to a free service like Cloudflare or DigitalOcean, but the domain itself has not been configured on those DNS servers. This situation could potentially allow an attacker to take control of the domain by adding it to their own account on such services.

### Usage

1. **Requirements:**
   - Python 3.x
   - `requests`, `python-whois`, and `dnspython` Python libraries (install using `pip3 install requests python-whois dnspython`)

2. **Setup:**
   - Clone the script.
    ```
    git clone https://github.com/dimme/nrd_grabscan.git
    cd nrd_grabscan
    chmod +x nrd_grabscan.py
    ```

3. **Execution:**
   - Run the script:
     ```
     ./nrd_grabscan.py
     ```

4. **Output:**
   - The script will output domains that are identified as grabbable to `grabbable.txt`.

### How It Works

1. **Domain List Retrieval:**
   - The script retrieves a list of domains from a predefined URL (`https://raw.githubusercontent.com/shreshta-labs/newly-registered-domains/main/nrd-1w.csv`). This list is automatically downloaded and processed.

2. **Checking NS Records:**
   - Retrieves the nameservers (NS records) for each domain using WHOIS.

3. **Resolving NS IPs:**
   - Resolves nameserver names to IP addresses to prepare for DNS resolution.

4. **DNS Resolution Check:**
   - Checks if the domain resolves to an IP address on its nameservers. If the domain does not exist on the nameserver, it is marked as grabbable.

5. **Output:**
   - Domains identified as grabbable are logged in `grabbable.txt` for further investigation.

### Disclaimer

**DISCLAIMER:** This tool is provided for educational and informational purposes only. The author does not bear any responsibility for its misuse. **No one is allowed to use this tool for malicious purposes.**

### License

Copyright (C) 2024 Dimitrios Vlastaras. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
