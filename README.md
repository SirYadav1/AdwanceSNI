## Overview

The Subdomain Finder & Scanner Tool is a command-line utility designed to discover and scan subdomains of specified domains. It utilizes asynchronous programming to efficiently handle multiple requests and integrates various tools to fetch and analyze subdomains.

## Features

- Fetches subdomains using the **subfinder** tool.
- Scans subdomains for vulnerabilities using the **bugscanner-go** tool.
- Displays user information and system details.
- Provides a clean and colorful command-line interface with progress indicators.
- Supports batch processing of domains for improved performance.

## Disclaimer⚠️
This tool is developed for educational and ethical purposes only. Users are responsible for ensuring they have explicit permission to perform any subdomain enumeration or vulnerability scanning on the target domain. Unauthorized use of this tool on systems, networks, or websites without proper authorization is illegal and may lead to legal consequences. The developer and contributors are not liable for any misuse, damage, or legal issues resulting from the improper use of this tool. By using this tool, you agree to abide by all applicable laws and take full responsibility for your actions.

## Installation commands 🔗
```shell
termux-setup-storage && pkg update && pkg upgrade -y && pkg install golang -y && pkg install python-pip -y && pkg install zlib && pip install aiofiles rich aiohttp pytz bs4 && echo 'PATH="$PATH:$HOME/go/bin"' >> $HOME/.bashrc && source $HOME/.bashrc && go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && go install -v github.com/aztecrabbit/bugscanner-go@latest
&& git clone https://github.com/SirYadav4601/AdwanceSNI
```

## Usage 📌
 ```shell
cd AdwanceSNI
```

```shell
python AdwanceSNI.py
```
<b> Save your domain file to main storage and then give the path for your TXT file
</b><br>
example: /storage/emulated/0/domain.txt<br>
(domain.txt की जगह अपनी फाइल का नाम डाले)


## Author Information

**Author**: YADAV  
**Coded by**: YADAV  
**Design by**: SONU<br>
**Contact**: siryadav025@gamil.com<br>
**Telegram**: [@SirYadav](https://t.me/SirYadav)  
**Version**: 0.6