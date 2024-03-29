import os
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored
from tqdm import tqdm

def check_ip(ip):
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    status = colored("Attivo", "green") if response == 0 else colored("Non attivo", "red")
    return (ip, status)

def welcome_message():
    welcome = colored("Benvenuto da Viking t.me/rapid85", "blue", attrs=["bold"])
    print(welcome)

def main():
    welcome_message()

    network = "192.168.1."
    start_ip = 1
    end_ip = 255
    ip_range = [f"{network}{i}" for i in range(start_ip, end_ip + 1)]

    print(colored("Scansione in corso...", "red"))

    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(tqdm(executor.map(check_ip, ip_range), total=len(ip_range), desc="Progresso"))

    print("\nDispositivi connessi:")
    for ip, status in results:
        if status == colored("Attivo", "green"):
            print(f"IP: {colored(ip, 'cyan'):<15} Stato: {status}")

if __name__ == "__main__":
    main()
