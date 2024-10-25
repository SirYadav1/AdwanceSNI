# About this project 🚀
This is Adwance and simple SNI finding tool.This tool automates and simplifies the process of finding subdomains and scanning them for vulnerabilities. With a focus on ease of use, performance, and flexibility, it leverages powerful tools like subfinder and bugscanner-go, making it highly effective for security researchers and penetration testers. The addition of real-time progress tracking and concurrency ensures that it operates efficiently, even when processing multiple domains.

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
</b>
example: /storage/emulated/0/domain.txt
(domain.txt की जगह अपनी फाइल का नाम डाले)