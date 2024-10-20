# About this project 🚀
This is Adwance and simple SNI finding tool.This tool automates and simplifies the process of finding subdomains and scanning them for vulnerabilities. With a focus on ease of use, performance, and flexibility, it leverages powerful tools like subfinder and bugscanner-go, making it highly effective for security researchers and penetration testers. The addition of real-time progress tracking and concurrency ensures that it operates efficiently, even when processing multiple domains.

## Disclaimer⚠️
This tool is developed for educational and ethical purposes only. Users are responsible for ensuring they have explicit permission to perform any subdomain enumeration or vulnerability scanning on the target domain. Unauthorized use of this tool on systems, networks, or websites without proper authorization is illegal and may lead to legal consequences. The developer and contributors are not liable for any misuse, damage, or legal issues resulting from the improper use of this tool. By using this tool, you agree to abide by all applicable laws and take full responsibility for your actions.

## Installation commands 🔗
```shell
pkg update && pkg upgrade -y && pkg install golang -y && pkg install python-pip -y && pip install aiofiles rich && echo 'PATH="$PATH:$HOME/go/bin"' >> $HOME/.bashrc && source $HOME/.bashrc && go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && go install -v github.com/aztecrabbit/bugscanner-go@latest && pkg install git
```

## Usage 📌
<b>1</b> Download the python file
<p>
  (ignore if you see any "Display over apps" Pop up while opening the python file)
  <p>
 <b>2</b> Open the python file with termux
  <p>
  <b>3</b>  open your Domain (.txt) file with termux
    <p>
    <b>4</b>  enter 
      
      python AdwanceSNI.py ```
Select 1 if you want to find subdomains
<p>
Select 2 if you want to scan subdomains
