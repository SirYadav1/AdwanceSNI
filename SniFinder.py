import subprocess
import os
import threading
import asyncio
import random
from concurrent.futures import ProcessPoolExecutor
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
import aiofiles

# ANSI कोड्स
RESET = "\033[0m"
BOLD = "\033[1m"
LIGHT_GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
GREEN = "\033[32m"
COLORS = [LIGHT_GREEN, RED, BLUE, YELLOW, GREEN]

write_lock = threading.Lock()

def show_banner():
    banner = """
    ##::: ##:'########:'##::::'##:'########::'######:::'########:'##::: ##:
     ###:: ##: ##.....::. ##::'##::... ##..::'##... ##:: ##.....:: ###:: ##:
     ####: ##: ##::::::::. ##'##:::::: ##:::: ##:::..::: ##::::::: ####: ##:
     ## ## ##: ######:::::. ###::::::: ##:::: ##::'####: ######::: ## ## ##:
     ##. ####: ##...:::::: ## ##:::::: ##:::: ##::: ##:: ##...:::: ##. ####:
     ##:. ###: ##:::::::: ##:. ##::::: ##:::: ##::: ##:: ##::::::: ##:. ###:
     ##::. ##: ########: ##:::. ##:::: ##::::. ######::: ########: ##::. ##:
    ..::::..::........::..:::::..:::::..::::::......::::........::..::::..::
    +-+-+-+-+-+-+-+-+
    |N|e|t|w|o|r|k|
    +-+-+-+-+-+-+-+-+
    Created by t.me/SirYadav
    Send feedback and Suggestions 
    """
    color = random.choice(COLORS)
    print(f"{BOLD}{color}{banner}{RESET}")

def clear_terminal():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_banner() 
    except Exception as e:
        print(f"Warning: Unable to clear terminal. {e}")

async def read_domains(file_name):
    async with aiofiles.open(file_name, 'r') as file:
        domains = await file.readlines()
    return [domain.strip() for domain in domains]

async def get_subdomains_subfinder(domain, output_file):
    try:
        print(f"{BOLD}{YELLOW}Fetching subdomains for: {BLUE}{domain}{RESET}")
        process = await asyncio.create_subprocess_exec(
            'subfinder', '-d', domain, '-silent',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            print(f"{BOLD}{RED}Error fetching subdomains for {domain}: {stderr.decode()}{RESET}")
            return 0
        else:
            subdomains = stdout.decode().splitlines()
            clean_subdomains = [line.strip() for line in subdomains if line.strip()]
            with write_lock:
                with open(output_file, 'a') as out_file:
                    for subdomain in clean_subdomains:
                        out_file.write(f"{subdomain}\n")
            print(f"{BOLD}{GREEN}Subdomains saved for: {domain}{RESET}")
            return len(clean_subdomains)
    except Exception as e:
        print(f"{BOLD}{RED}Error fetching subdomains for {BLUE}{domain}: {e}{RESET}")
        return 0

def scan_subdomains_with_bugscanner(input_file, output_file):
    try:
        print(f"{BOLD}{YELLOW}Scanning subdomains from: {BLUE}{input_file}{RESET}")
        subprocess.run(['bugscanner-go', 'scan', 'direct', '-f', input_file, '-o', output_file], check=True)
        print(f"{BOLD}{GREEN}Bug scanning completed! Results saved to {output_file}.{RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{BOLD}{RED}Error during bug scanning: {e}{RESET}")

def batch_domains(domains, batch_size=5):
    total_domains = len(domains)
    for i in range(0, total_domains, batch_size):
        yield domains[i:i + batch_size]

def show_menu():
    menu = f"""
    {BOLD}{LIGHT_GREEN}===== मुख्य मेनू ====={RESET}
    1. Subdomain ढूंढना
    2. Subdomain स्कैन करना
    3. बाहर निकलना
    """
    print(menu)

async def main():
    clear_terminal()
    while True:
        show_menu()
        choice = input(f"{BOLD}{YELLOW}अपना विकल्प चुनें (1/2/3): {RESET}").strip()
        if choice == "1":
            input_file = get_valid_file(prompt="अपने डोमेन की फ़ाइल दर्ज करें: ")
            domains = await read_domains(input_file)
            output_file = input(f"{BOLD}{LIGHT_GREEN}Subdomains सेव करने के लिए आउटपुट फ़ाइल का नाम दर्ज करें: {RESET}")
            with open(output_file, 'w') as f:
                pass
            total_domains = len(domains)
            total_subdomains = 0
            with Progress(
                SpinnerColumn(),
                BarColumn(),
                TextColumn("[progress.description]{task.description}"),
                TextColumn("[progress.percentage]{task.completed}/{task.total}"),
            ) as progress:
                task = progress.add_task("[cyan]Processing Domains...", total=total_domains)
                with ProcessPoolExecutor(max_workers=5) as executor:
                    for domain_batch in batch_domains(domains, batch_size=5):
                        tasks = [get_subdomains_subfinder(domain, output_file) for domain in domain_batch]
                        results = await asyncio.gather(*tasks)
                        total_subdomains += sum(results)
                        progress.update(task, advance=len(domain_batch))
            print(f"{BOLD}{LIGHT_GREEN}Subdomains have been saved in {output_file}.{RESET}")
            print(f"{BOLD}{GREEN}Total Subdomains Found: {total_subdomains}{RESET}")
        elif choice == "2":
            scan_file = get_valid_file(prompt="स्कैन करने के लिए अपनी Subdomain फ़ाइल दर्ज करें: ")
            output_file = input(f"{BOLD}{LIGHT_GREEN}Bugscan के परिणामों को सेव करने के लिए आउटपुट फ़ाइल का नाम दर्ज करें: {RESET}")
            scan_subdomains_with_bugscanner(scan_file, output_file)
        elif choice == "3":
            print(f"{BOLD}{GREEN}प्रोग्राम से बाहर निकल रहे हैं। धन्यवाद!{RESET}")
            break
        else:
            print(f"{BOLD}{RED}गलत विकल्प। कृपया 1, 2 या 3 में से चुनें।{RESET}")

def get_valid_file(prompt="अपनी फ़ाइल दर्ज करें: "):
    while True:
        input_file = input(f"{BOLD}{LIGHT_GREEN}{prompt}{RESET}").strip()
        if os.path.isfile(input_file):
            return input_file
        else:
            print(f"{BOLD}{RED}Error: The file '{input_file}' was not found.{RESET}")

# Run
if __name__ == "__main__":
    asyncio.run(main())
  
